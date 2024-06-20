from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<p>Hello</p>")

def hello(request, username):
    print(username)
    return HttpResponse("<h2>Hello World</h2>")

def about(request):
    return HttpResponse("About")