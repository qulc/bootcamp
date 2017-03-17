from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from bootcamp.decorators import ajax_required
from .models import Notification


@login_required
def notifications(request):
    user = request.user
    all_notifications = Notification.objects.filter(to_user=user)
    all_notifications.update(is_read=True)

    context = {'notifications': all_notifications}
    return render(request, 'activities/notifications.html', context)


@login_required
@ajax_required
def last_notifications(request):
    user = request.user
    last_unread_notifications = Notification.objects.filter(
        to_user=user, is_read=False)[:5]

    for unread_notification in last_unread_notifications:
        unread_notification.is_read = True
        unread_notification.save()

    context = {'notifications': last_unread_notifications}
    return render(request, 'activities/last_notifications.html', context)


@login_required
@ajax_required
def check_notifications(request):
    user = request.user
    notifications_count = Notification.objects.filter(
        to_user=user, is_read=False).count()
    return HttpResponse(notifications_count)
