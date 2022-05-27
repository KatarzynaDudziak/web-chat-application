from django.utils import timezone
from django.http import HttpResponseNotFound
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

from .models import *
from .forms import *


@login_required(login_url='/user/login')
def chat_view(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)

        if form.is_valid():
            content = form.cleaned_data['content']
            message = MessageModel(content=content, date=timezone.now(), author=request.user)
            message.save()
            return HttpResponseRedirect('/')

    messages_list = MessageModel.objects.all().order_by('-date')

    return render(request, 'main.html', {'messages' : messages_list})


@login_required(login_url='/user/login')
def delete_message(request):
    if request.method == 'POST':
        try:
            MessageModel.objects.get(id = request.POST['id']).delete()
        except:
            return HttpResponseNotFound('404')
    
    return HttpResponseRedirect('/')


@login_required(login_url='/user/login')
def history(request):
    messages_list = MessageModel.objects.all().order_by('-date')

    p = Paginator(messages_list, 5)
    page = request.GET.get('page')
    messages = p.get_page(page)
    nums = "a" * messages.paginator.num_pages

    return render(request, 'history.html', {'messages' : messages, 'number_of_pages' : nums})
