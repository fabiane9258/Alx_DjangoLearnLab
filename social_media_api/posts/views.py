from django.http import HttpResponse

def index(request):
    return HttpResponse("Posts app is working!")
