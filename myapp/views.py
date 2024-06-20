from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404
# Create your views here.
def index(request):
    return HttpResponse("<p>Hello</p>")

def hello(request, id):
    print(type(id))
    #print(username)
    # return HttpResponse("<h2>Hello %s</h2>" % username)
    return HttpResponse("<h2>Hello %s</h2>" % id)


def about(request):
    return HttpResponse("About")

def projects(request):
    projects = list(Project.objects.values())
    return JsonResponse(projects, safe=False)

def tasks(request, id):
    task = get_object_or_404(Task, id=id)
    return HttpResponse('task: %s' % task.title)