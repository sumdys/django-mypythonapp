#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse



# Create your views here.
def index(request):
	return render(request, 'home.html')

def home(request):
	info_dict = {'site': u'自强学堂', 'content': u'各种IT技术教程'}
	List = map(str, range(100))
	return render(request, 'home.html',{'info_dict':info_dict,'hesheng':'何生','List':List,'vars':'65'})

def add(request):
	a = request.GET.get('a',0)
	b = request.GET.get('b',0)
	c = int(a)+int(b)
	return HttpResponse(str(c))


def add2(request, a, b):
	c = int(a)+int(b)
	return HttpResponse(str(c))

def old_add2_redirect(request, a, b):
	return HttpResponseRedirect(
		reverse('add2', args=(a, b))
	)