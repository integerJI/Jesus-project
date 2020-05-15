# myProject/myProject/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import myMember.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', myMember.views.signin, name="signin"),
    path('myApp/', include('myApp.urls')),
    path('myMember/', include('myMember.urls')),
]
