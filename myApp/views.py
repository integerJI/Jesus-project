from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.models import User
from django.utils import timezone
from .models import Save
from myMember.models import Profile

def index(request):
    request_user = request.user
    saves = Save.objects.all().filter(save_user_id=request_user).order_by('-id')
    return render(request, 'index.html', {'saves':saves})

def save(request):
    save = Save()
    save.save_user = User.objects.get(username = request.user.get_username())
    save.save_date = timezone.datetime.now()
    save.save()
    return redirect(reverse('index'))

def calender(request):
    return render(request, 'calender.html')


# 정수 전용 페이지
def dev(request):
    # request_user = request.user
    # saves = Save.objects.all().filter(save_user_id=request_user).order_by('-id')
    # request_profile = Profile.objects.get(user=request_user)

    # context = {
    #    'id' : request_user.username,
    #    'nick' : request_profile.nick,
    #    'intro' : request_profile.intro,
    #    'saves' : saves,
    # }
    return render(request, 'dev.html')
    # return render(request, 'dev.html', context=context)