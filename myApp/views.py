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
