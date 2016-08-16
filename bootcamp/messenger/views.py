from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse

from bootcamp.decorators import ajax_required
from .models import Message


@login_required
def inbox(request):
    conversations = Message.get_conversations(user=request.user)
    messages = None
    active_conversation = None

    if conversations:
        conversation = conversations[0]
        active_conversation = conversation['user'].username

        messages = Message.objects.filter(user=request.user,
                                          conversation=conversation['user'])
        messages.update(is_read=True)

        for conversation in conversations:
            if conversation['user'].username == active_conversation:
                conversation['unread'] = 0
    content = {
        'messages': messages,
        'active': active_conversation,
        'conversations': conversations
    }
    return render(request, 'messages/inbox.html', content)


@login_required
def messages(request, username):
    active_conversation = username
    conversations = Message.get_conversations(user=request.user)
    messages = Message.objects.filter(user=request.user,
                                      conversation__username=username)
    messages.update(is_read=True)
    for conversation in conversations:
        if conversation['user'].username == username:
            conversation['unread'] = 0

    content = {
        'messages': messages,
        'conversations': conversations,
        'active': active_conversation
    }
    return render(request, 'messages/inbox.html', content)


@login_required
def new(request):
    if request.method == 'POST':
        to_user_username = request.POST.get('to')
        message = request.POST.get('message')

        to_user = User.objects.filter(username=to_user_username).first()

        if not to_user:
            start = to_user_username.rfind('(') + 1
            end = len(to_user_username) - 1

            to_user_username = to_user_username[start:end]
            to_user = User.objects.get(username=to_user_username)

        if len(message.strip()) == 0:
            return redirect('/messages/new/')

        from_user = request.user
        if from_user != to_user:
            Message.send_message(from_user, to_user, message)

        return redirect('/messages/{0}/'.format(to_user_username))

    conversations = Message.get_conversations(user=request.user)
    content = {'conversations': conversations}
    return render(request, 'messages/new.html', content)


@login_required
@ajax_required
def delete(request):
    return HttpResponse()


@login_required
@ajax_required
def send(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        to_user_username = request.POST.get('to')

        to_user = User.objects.get(username=to_user_username)

        if len(message.strip()) == 0:
            return HttpResponse()

        from_user = request.user
        if from_user != to_user:
            msg = Message.send_message(from_user, to_user, message)
            return render(request, 'messages/includes/partial_message.html',
                          {'message': msg})
        return HttpResponse()

    return HttpResponseBadRequest()


@login_required
@ajax_required
def users(request):
    users = User.objects.filter(is_active=True)

    dump = []
    template = '{0} ({1})'

    for user in users:
        if user.profile.get_screen_name() != user.username:
            screen_name = user.profile.get_screen_name()
            dump.append(template.format(screen_name, user.username))
        else:
            dump.append(user.username)

    return JsonResponse(dump)


@login_required
@ajax_required
def check(request):
    count = Message.objects.filter(user=request.user, is_read=False).count()
    return HttpResponse(count)
