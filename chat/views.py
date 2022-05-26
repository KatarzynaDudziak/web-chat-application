from django.utils import timezone
from django.http import HttpResponseNotFound
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from .models import *
from .forms import *


def chat_view(request):
    if not request.user.id:
        return HttpResponseRedirect('user/login')

    if request.method == 'POST':
        form = MessageForm(request.POST)

        if form.is_valid():
            content = form.cleaned_data['content']
            message = MessageModel(content=content, date=timezone.now(), author=request.user)
            message.save()
            return HttpResponseRedirect('/')

    message = MessageModel.objects.all().order_by('-date')

    return render(request, 'main.html', {'messages' : message})


def delete_message(request):
    if request.method == 'POST':
        try:
            MessageModel.objects.get(id = request.POST['id']).delete()
        except:
            return HttpResponseNotFound('404')
    
    return HttpResponseRedirect('/')


def history(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)

        if form.is_valid():
            content = form.cleaned_data['content']
            message = MessageModel(content=content, date=timezone.now(), author=request.user)
            message.save()
            return HttpResponseRedirect('/')

    message = MessageModel.objects.all().order_by('-date')

    
    return render(request, 'history.html', {'messages' : message})
