from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from board.models import Board


def list(request):
    board_list = Board.objects.all().order_by('-regdate')
    context = {'board_list': board_list}

    return render(request, 'board/list.html', context)


# -------------------------------------------------------------------------------
def view(request):
    id = request.GET.get('id', False)

    board_list = Board.objects.filter(id=id).order_by('-regdate')

    context = {'board_list': board_list}
    board = board_list[0]
    hit_update(board)

    return render(request, 'board/view.html', context)


# -------------------------------------------------------------------------------
def write(request):
    id = request.GET.get('id', False)
    return render(request, 'board/write.html')


def add(request):
    board_txt = Board()
    board_txt.title = request.POST['title']
    board_txt.content = request.POST['content']
    board_txt.user_id = request.session['authuser']['id']
    board_txt.hit = 0
    board_txt.name = request.session['authuser']['name']

    board_txt.save()

    return HttpResponseRedirect('/board')


# -------------------------------------------------------------------------------
def modifyform(request):
    id = request.GET.get('id', False)
    board_list = Board.objects.filter(id=id)
    board = board_list[0]
    context = {'board': board}


    return render(request, 'board/modify.html', context)



def modify(request):

    id = request.POST.get('id')
    board_save = Board.objects.get(id=id)
    board_save.title = request.POST['title']
    board_save.content = request.POST['content']
    board_save.save()

    return HttpResponseRedirect('/board/view?id=' + id)


def hit_update(board):
    board.hit += 1
    board.save()


# -------------------------------------------------------------------------------
def delete(request):
    try:
        id = request.GET.get('id', False)

        board_list = Board.objects.filter(id=id)

        for i in board_list:
            board = i.user_id

        if board == request.session['authuser']['id']:
            count = Board.objects.filter(id=id).count()

            if count != 0:
                Board.objects.filter(id=id).delete()

        return HttpResponseRedirect('/board')
    except:
        return HttpResponseRedirect('/board')
