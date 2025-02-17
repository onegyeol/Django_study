from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm

def todo_list(request):
    todos = Todo.objects.filter(complete=False)
    return render(request, 'todo/todo_list.html', {'todos':todos})

def todo_detail(request,pk):
    todo = Todo.objects.get(id=pk)
    return render(request, 'todo/todo_detail.html', {'todo':todo})

def todo_post(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid(): # 유효성 검증
            todo = form.save(commit=False)
            todo.save() # 작성한 목록 저장
            return redirect('todo_list') # 목록 페이지로 리다이렉트
    else: # GET 요청 시
        form = TodoForm()
    return render(request, 'todo/todo_post.html', {'form':form})

def todo_edit(request):
    todo = Todo.objects.get(id=pk)
    if request.method == "POST":
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.save()
            return redirect('todo_list')
    else:
        form = TodoForm(instance=todo)

    return render(request, 'todo/todo_post.html', {'form': form})

def done_list(request):
    dones = Todo.objects.filter(complete=False)
    return render(request, 'todo/done_list.html', {'dones':dones})

def todo_done(request, pk):
    todo = Todo.objects.get(id=pk)
    todo.complete = True
    todo.save()
    return redirect('todo_list')