from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.views import generic, View
from django.contrib.auth.decorators import login_required
from .forms import UserCreationMultiForm, ProfileForm, ProfileUpdateForm
from .models import Profile
from myApp.models import Save

def signup(request):
    if request.method == 'POST':
        if request.POST['user-password1'] == request.POST['user-password2']:
            form = UserCreationMultiForm(request.POST, request.FILES)
            if form.is_valid(): 
                user = form['user'].save()
                profile = form['profile'].save(commit=False)
                profile.user = user
                profile.nick = user
                profile.save()
                return redirect('signin')
            else:
                user = request.POST['user-username']
                user = User.objects.get(username=user)
                messages.info(request, '아이디가 중복됩니다.')
                return render(request, 'signup.html')
        else:
            messages.info(request, '비밀번호가 다릅니다.')
            return render(request, 'signup.html')
    return render(request, 'signup.html')


class Loginviews(LoginView):
    template_name = 'signin.html'

    def form_invalid(self, form):
        messages.error(self.request, '로그인에 실패하였습니다. Id 혹은 Password를 확인해 주세요.', extra_tags='danger')
        return super().form_invalid(form)

signin = Loginviews.as_view()


class LogoutViews(LogoutView):
    # setting.py에 설정해준 값
    next_page = settings.LOGOUT_REDIRECT_URL
signout = LogoutViews.as_view()


@login_required
def userinfo(request):
    request_user = request.user
    request_profile = Profile.objects.get(user=request_user)

    context = {
        'id' : request_user.username,
        'nick' : request_profile.nick,
        'intro' : request_profile.intro,
    }

    return render(request, 'mypage.html', context=context)

#   유저페이지에서 자기글 조회 여기선 Save
#   posts = Post.objects.all().filter(create_user=conn_user).order_by('-id')
#   자기글 객체
#   'posts' : posts,


# user page 인데... 이건 나중에 살릴듯
# @login_required
# def user_select_info(request, writer):
#     select_profile = Profile.objects.get(nick=writer)
#     select_user = select_profile.user
            
#     context = {
#         'id' : select_user.username,
#         'nick' : select_profile.nick,
#         'intro' : select_profile.intro,
#     }

#     return render(request, 'userpage.html', context=context)

#   유저페이지에서 자기글 조회 여기선 Save
#   posts = Post.objects.all().filter(create_user=conn_user).order_by('-id')
#   자기글 객체
#   'posts' : posts,

class ProfileUpdateView(View): 
    def get(self, request):
        user = get_object_or_404(User, pk=request.user.pk) 

        if hasattr(user, 'profile'):  
            profile = user.profile
            profile_form = ProfileUpdateForm(initial={
                'nick': profile.nick,
                'intro': profile.intro,
            })
        else:
            profile_form = ProfileUpdateForm()

        return render(request, 'profile_update.html', { "profile_form": profile_form, "profile": profile})

    def post(self, request):
        u = User.objects.get(id=request.user.pk)       

        if hasattr(u, 'profile'):
            profile = u.profile
            profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=profile) 
        else:
            profile_form = ProfileUpdateForm(request.POST, request.FILES)

        # Profile 폼
        if profile_form.is_valid():
            profile = profile_form.save(commit=False) 
            profile.user = u
            profile.save()

            context = {
                'id' : u.username,
                'nick' : profile.nick,
                'intro' : profile.intro,
            }

            return render(request, 'mypage.html', context=context)
            
        return redirect('mypage', pk=request.user.pk) 