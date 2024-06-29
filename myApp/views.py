from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404

# Create your views here.

def index(request):
    return HttpResponse('Index Page')

def hello(request, username):
    return HttpResponse('<h2> Hello World %s </h2>' % username)

def about(request):
    return HttpResponse('About')

def projects(request):
    projects = list(Project.objects.values())
    return JsonResponse(projects, safe=False)

def tasks(request, title):
    task = Task.objects.get(title=title)
    return HttpResponse('task: %s' % task.title)