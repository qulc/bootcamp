from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from bootcamp.decorators import ajax_required
from .models import Notification


@login_required
def notifications(request):
    user = request.user
    notifications = Notification.objects.filter(to_user=user)
    unread = Notification.objects.filter(to_user=user, is_read=False)

    for notification in unread:
        notification.is_read = True
        notification.save()

    context = {'notifications': notifications}
    return render(request, 'activities/notifications.html', context)


@login_required
@ajax_required
def last_notifications(request):
    user = request.user
    notifications = Notification.objects.filter(
        to_user=user, is_read=False)[:5]

    for notification in notifications:
        notification.is_read = True
        notification.save()

    context = {'notifications': notifications}
    return render(request, 'activities/last_notifications.html', context)


@login_required
@ajax_required
def check_notifications(request):
    user = request.user
    notifications_count = Notification.objects.filter(
        to_user=user, is_read=False).count()
    return HttpResponse(notifications_count)
