from django.conf.urls import url
from . import views
from django.views.static import serve
from django.contrib.auth.decorators import login_required
from django.conf import settings

urlpatterns = [
	url(r'^sign/$', views.SignForm.as_view(), name='signForm'),
	url(r'^login/$', views.LoginForm.as_view(), name='loginForm'),
	url(r'^privateMemo/$', views.privateMemo, name='privateMemo'),
]

