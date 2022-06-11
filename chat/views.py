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

    messages_list = MessageModel.objects.all().order_by('-date')[:15]

    return render(request, 'main.html', {'chat_messages' : messages_list})


@login_required(login_url='/user/login')
def delete_message(request):
    if request.method == 'POST':
        try:
            message_id = request.POST['id']
            message = MessageModel.objects.get(id = message_id)
            if request.user.is_authenticated or message.author == request.user:
                message.delete()
        except:
            return HttpResponseNotFound('404')
    
    return HttpResponseRedirect('/')


@login_required(login_url='/user/login')
def history(request):
    messages_list = MessageModel.objects.all().order_by('-date')

    p = Paginator(messages_list, 10)
    page = request.GET.get('page')
    messages = p.get_page(page)
    nums = "a" * messages.paginator.num_pages

    return render(request, 'history.html', {'chat_messages' : messages, 'number_of_pages' : nums})


@login_required(login_url='/user/login')
def search_message(request):
    if request.method == 'POST':
        query_phrase = request.POST.get('content', None)
        if query_phrase:
            results = MessageModel.objects.filter(content__contains=query_phrase)
            return render(request, 'history.html', {'chat_messages' : results})

    return HttpResponseRedirect('/history')
