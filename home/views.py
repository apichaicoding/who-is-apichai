from django.shortcuts import render
from django.http import HttpResponse
from .models import ContactMessage

def Home(request):
	return render(request, 'home/home.html')

def Services(request):
	return render(request, 'home/service.html')

def Contact(request):

	context = {}

	if request.method == 'POST':
		data = request.POST.copy()
		title = data.get('title')
		email = data.get('email')
		detail = data.get('detail')
		print(title,email,detail)

		if title == '' or email == '':
			context['status'] = 'alert'
			return render(request,'home/contact.html',context)

		new = ContactMessage()
		new.title = title
		new.email = email
		new.detail = detail
		new.save()
		context['status'] = 'success'

	return render(request, 'home/contact.html',context)