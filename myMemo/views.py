from django.shortcuts import render
from django.views.generic import View
from django.utils import timezone
from .models import MyUser
from .models import PublicMemo
from .models import PrivateMemo
from django.contrib.auth import authenticate, login, logout as _logout


class SignForm(View):
	def get(self, request, *args, **kwargs):
		response = render(request, 'myMemo/signForm.html')
		return response
	
	def post(self, request, *args, **kwargs):
		user_id = request.POST['user_id']
		user_pw = request.POST['user_pw']
		user_email = request.POST['user_email']

		try:
			user_model = MyUser.objects.create(username = user_id, email = user_email)
			user_model.set_password(user_pw)
			user_model.save()
		except:
			error = "This is already a registered ID."
			return render(request, 'myMemo/signForm.html', {'error':error})

		return render(request, 'myMemo/loginForm.html')

class LoginForm(View):
	def get(self, request, *args, **kwargs):
		response = render(request, 'myMemo/loginForm.html')
		return response

	def post(self, request, *args, **kwargs):
		user_id = request.POST['user_id']
		user_pw = request.POST['user_pw']
		user = authenticate(username=user_id, password=user_pw)
		try:
			publicMemos = PublicMemo.objects.filter(owner=user)
			privateMemos = PrivateMemo.objects.filter(owner=user)
		except:
			publicMemos = None
			privateMemos = None

		if user is not None:
			login(request, user)
			return render(request, 'myMemo/index.html', {'user':user, 'publicMemos':publicMemos, 'privateMemos':privateMemos})
		else:	
			error = "Invalid ID or PW."
			return render(request, 'myMemo/loginForm.html', {'error':error})


def publicMemo(request):
	title = request.POST['title']
	text = request.POST['text']
	user = request.user

	privateMemo = PrivateMemo(title=title, text=text, time=timezone.now(), owner=user)
	privateMemo.save()
	return render(request, 'myMemo/index.html')

def privateMemo(request):
	title = request.POST['title']
	text = request.POST['text']
	user = request.user

	privateMemo = PrivateMemo(title=title, text=text, time=timezone.now(), owner=user)
	privateMemo.save()
	return render(request, 'myMemo/index.html')

