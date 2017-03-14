from django.conf.urls import url
from . import views
from django.views.static import serve
from django.contrib.auth.decorators import login_required
from django.conf import settings

urlpatterns = [
	url(r'^sign/$', views.SignForm.as_view(), name='signForm'),
	url(r'^login/$', views.LoginForm.as_view(), name='loginForm'),
	url(r'^logout/$', views.logout, name='logout'),
	url(r'^auth/$', views.Auth.as_view(), name='auth'),
	url(r'^memo/$', views.myMemo, name='myMemo'),
	url(r'^random/$', views.randomMemo, name='randomMemo'),
]

