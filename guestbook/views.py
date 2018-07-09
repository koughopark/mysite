from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from guestbook.models import Guestbook1


def list(request):
    guestbook_list = Guestbook1.objects.all().order_by('-regdate')
    context = {'guestbook_list': guestbook_list}
    return render(request, 'guestbook/list.html', context)


def add(request):
    guestbook = Guestbook1()
    guestbook.name = request.POST['name']
    guestbook.password = request.POST['password']
    guestbook.message = request.POST['message']

    guestbook.save()

    return HttpResponseRedirect('/guestbook')


def deleteform(request):
    id = request.GET.get('id', False)
    context = {'id': id}
    return render(request, 'guestbook/deleteform.html', context)


def delete(request):
    count = Guestbook1.objects.filter(id=request.POST['id']).filter(password=request.POST['password']).count()

    if count != 0:
        Guestbook1.objects.filter(id=request.POST['id']).filter(password=request.POST['password']).delete()
    # Guestbook.save()
    return HttpResponseRedirect('/guestbook')


