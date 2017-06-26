from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse, HttpResponseRedirect
import datetime
from tasks.models import Task

def sort_tasks_recent(tasks_data):
    '''sorts list of tasks in order by date created'''
    task_tuples = [(single_task.date_created, single_task) for single_task in tasks_data] 
    sorted_tasks = [item[1] for item in sorted(task_tuples, key=lambda tup: tup[0], reverse=True)]
    return sorted_tasks

def homepage(request):
    now = datetime.datetime.now()
    tasks = sort_tasks_recent(Task.objects.all())
    return render(request, 'homepage.html', {'current_date': now, 'tasks': tasks})

def add_task(request):
    now = datetime.datetime.now()
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('Invalid task description. Try again.')
        else:
            Task.objects.create(
                description = q,
                date_created = now,
                #user = request.user,
                is_done = False
            )
            tasks = sort_tasks_recent(Task.objects.all())
            return redirect('/', {'current_date': now, 'tasks': tasks})
    return render(request, 'addtask.html', {'errors': errors})

