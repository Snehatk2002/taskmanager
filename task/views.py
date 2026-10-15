from django.shortcuts import render,redirect,get_object_or_404
from .models import Task

# Get Tasks List
def task_list(request): # get request 
    tasks=Task.objects.all().order_by('-created_at') # Last task displayed first
    return render(request,'task_list.html',{'tasks':tasks})


# Add task
def add_task(request):
    if request.method=='POST':
        title=request.POST.get('title')
        description=request.POST.get('description')
        Task.objects.create(title=title,description=description)
        return redirect('task_list')
    
    return render(request,'add_task.html')


# Edit/Update task
def update_task(request,id):
    task=get_object_or_404(Task,id=id)
    if request.method=='POST':
        task.title=request.POST.get('title')
        task.description=request.POST.get('description')
        task.completed='completed' in request.POST
        task.save()
        return redirect('task_list')
    return render(request,'update_task.html',{'task':task})


# Delete task
def delete_task(request,id):
    task=get_object_or_404(Task,id=id)
    task.delete()
    return redirect('task_list')
    