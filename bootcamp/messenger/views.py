from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse

from bootcamp.decorators import ajax_required
from .models import Message


@login_required
def inbox(request):
    messages = None
    active_conversation = None

    conversations = Message.get_conversations(user=request.user)

    if conversations:
        conversation = conversations[0]
        active_conversation = conversation['user'].username

        messages = Message.objects.filter(user=request.user,
                                          conversation=conversation['user'])
        messages.update(is_read=True)

        for conversation in conversations:
            if conversation['user'].username == active_conversation:
                conversation['unread'] = 0
    context = {
        'messages': messages,
        'active': active_conversation,
        'conversations': conversations
    }
    return render(request, 'messages/inbox.html', context)


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

    context = {
        'messages': messages,
        'conversations': conversations,
        'active': active_conversation
    }
    return render(request, 'messages/inbox.html', context)


@login_required
def new(request):
    if request.method == 'POST':
        to_user_username = request.POST.get('to')
        message = request.POST.get('message')

        to_user = User.objects.filter(username=to_user_username).first()

        if not to_user:
            return redirect('/messages/new/')

        if len(message.strip()) == 0:
            return redirect('/messages/new/')

        from_user = request.user
        if from_user != to_user:
            Message.send_message(from_user, to_user, message)

        return redirect(f'/messages/{to_user_username}/')

    conversations = Message.get_conversations(user=request.user)
    context = {'conversations': conversations}
    return render(request, 'messages/new.html', context)


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

    return JsonResponse(dump, safe=False)


@login_required
@ajax_required
def check(request):
    count = Message.objects.filter(user=request.user, is_read=False).count()
    return HttpResponse(count)
