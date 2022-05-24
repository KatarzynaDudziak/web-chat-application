from django.utils import timezone
from django.http import HttpResponseNotFound
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from .models import *
from .forms import *


def chat_view(request):
    print(request.user)
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


def admin_view(request):
    message = MessageModel.objects.all().order_by('-date')

    return render(request, 'admin_view.html', {'message' : message})


def delete_message(request):
    if request.method == 'POST':
        try:
            MessageModel.objects.filter(id = request.POST['id']).delete()
        except:
            return HttpResponseNotFound('...')
    
    return HttpResponseRedirect('/main/')
