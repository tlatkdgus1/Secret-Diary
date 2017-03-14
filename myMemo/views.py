from django.shortcuts import render
from django.views.generic import View
from django.utils import timezone
from .models import MyUser
from .models import PublicMemo
from .models import PrivateMemo
from django.views.generic.base import TemplateView
from django.contrib.auth import authenticate, login, logout as _logout

class Auth(TemplateView):
	template_name='myMemo/auth.html'

class SignForm(View):
	def get(self, request, *args, **kwargs):
		response = render(request, 'myMemo/signForm.html')
		return response
	
	def post(self, request, *args, **kwargs):
		user_id = request.POST.get('user_id')
		user_pw = request.POST.get('user_pw')
		user_pwagain = request.POST.get('user_pwagain')
		user_email = request.POST.get('user_email')

		if user_pw is not user_pwagain:
			msg = "Password and Password Again is Incorrect"
			return render(request, 'myMemo/auth.html' , {'msg':msg})

		try:
			user_model = MyUser.objects.create(username=user_id, email=user_email)
			user_model.set_password(user_pw)
			user_model.save()
			msg = "Succese to Make Account"
		except:
			msg = "This is already a registered ID."
			return render(request, 'myMemo/auth.html', {'msg':msg} )

		return render(request, 'myMemo/auth.html' , {'msg':msg})

class LoginForm(View):
	def get(self, request, *args, **kwargs):
		response = render(request, 'myMemo/loginForm.html')
		return response

	def post(self, request, *args, **kwargs):
		user_id = request.POST.get('user_id')
		user_pw = request.POST.get('user_pw')
		user = authenticate(username=user_id, password=user_pw)

		if user is not None:
			login(request, user)
			return render(request, 'myMemo/memo.html')
		else:	
			msg = "Invalid ID or PW."
			return render(request, 'myMemo/auth.html', {'msg':msg})

def logout(request):
	_logout(request)
	return render(request, 'myMemo/auth.html')

def registerMemo(request):
	private = request.POST['private']
	title = request.POST['title']
	text = request.POST['text']
	user = request.user

	if private is "private":	
		privateMemo = PrivateMemo(title=title, text=text, time=timezone.now(), owner=user)
		privateMemo.save()
		return render(request, 'myMemo/index.html')

	else:
		publicMemo = PublicMemo(title=title, text=text, time=timezone.now(), owner=user)
		publicMemo.save()
		return render(request, 'myMemo/index.html')
	


def myMemo(request):
	user = request.user
	try:
		publicMemos = PublicMemo.objects.filter(owner=user)
		privateMemos = PrivateMemo.objects.filter(owner=user)
	except:
		publicMemos = None
		privateMemos = None

	return render(request, 'myMemo/memo.html',{'publicMemos':publicMemos, 'privateMemos':privateMemos})

def randomMemo(request):
	randomMemo = PublicMemo.objects.order_by('?').first()
	return render(request, 'myMemo/random.html', {'randomMemo':randomMemo})


