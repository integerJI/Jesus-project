from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.models import User
from django.utils import timezone
from .models import Save

def index(request):
    saves = Save.objects.all().filter(create_user=conn_user).order_by('-id')
    return render(request, 'index.html', {'saves':saves})

def save(request):
    save = Save()
    save.save_user = User.objects.get(username = request.user.get_username())
    save.save_date = timezone.datetime.now()
    save.save()
    return redirect(reverse('index'))
