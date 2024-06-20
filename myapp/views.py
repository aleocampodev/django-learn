from django.http import HttpResponse

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