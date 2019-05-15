from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.core.mail import EmailMessage
from datetime import datetime
from mysite import models, forms
import json

# Create your views here.
def userinfo(request):
	if 'username' in request.session:
		username = request.session['username']
	else:
		return redirect('/login/')
	try:
		userinfo = models.User.objects.get(name = username)
	except:
		pass
	return render(request, 'userinfo.html', locals())

def logout(request):
	if 'username' in request.session:
		#Session.objects.all().delete()
		request.session['username'] = None
		request.session['useremail'] = None
		request.session['password'] = None
		return redirect('/login/')

	return redirect('/')



def login(request):
	message = "haha"
	if request.method == 'POST':
		login_form = forms.LoginForm(request.POST)
		if login_form.is_valid():
			login_name = request.POST['username'].strip()
			login_password = request.POST['password']
			#message = "(" + username + ") 登入成功"
			try:
				user = models.User.objects.get(name = login_name)
				if user.password == login_password:
					request.session['username'] = user.name
					request.session['useremail'] = user.email
					return redirect('/')
				else:
					message = "密碼錯誤，請再檢查一次"
			except:
				message = "找不此使用者"
		else:
			message = "請檢查輸入的欄位內容"
	else:
		login_form = forms.LoginForm()

	data={
		'state':True,
		'message':message,
	}
	#returnValue = magicNum, message
	return HttpResponse(json.dumps(data))
	#return render(request, 'login.html', locals())

def contact(request):
	message = "盡情的寫吧"
	if request.method == 'POST':
		form = forms.ContactForm(request.POST)
		if form.is_valid():
			message = "感謝您的來信"
			user_name = form.cleaned_data['user_name']
			user_city = form.cleaned_data['user_city']
			user_school = form.cleaned_data['user_school']
			user_email = form.cleaned_data['user_email']
			user_message = form.cleaned_data['user_message']
			mail_body = u'''
				網友姓名：{}
				居住城市：{}
				是否在學：{}
				反應意見：如下{}
				'''.format(user_name, user_city, user_school, user_message)
			email = EmailMessage('來自【不吐不快】網站的網友意見', mail_body, user_email, ['suepr57033@gmail.com'])
			email.send()
		else:
			message = "請檢查您輸入資料是否正確"
	else:
		form = forms.ContactForm()
	return render(request, 'contact.html', locals())

def listing(request):
	posts = models.Post.objects.filter(enabled=True).order_by('-pub_time')[:30]
	moods = models.Mood.objects.all()

	return render(request, 'listing.html', locals()) 

def posting(request):
	moods = models.Mood.objects.all()
	try:
		user_id = request.GET['user_id']
		user_pass = request.GET['user_pass']
		user_post = request.GET['user_post']
		user_mood = request.GET['mood']
	except:
		user_id = None
		message = '如要張貼訊息，則每一個欄位都要填'

	if user_id != None:
		mood = models.Mood.objects.get(status=user_mood)
		post = models.Post.objects.create(mood=mood, nickname=user_id, enabled=True, del_pass=user_pass, message=user_post)
		post.save()
		message="成功儲存！"

	return render(request, 'posting.html', locals()) 

def index(request, pid=None, del_pass=None):
	if 'username' in request.session:
		username = request.session['username']
		useremail = request.session['useremail']
	return render(request, 'index.html', locals()) 





