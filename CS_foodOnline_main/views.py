from django.http.response import HttpResponse
def home(req):
    return HttpResponse("H")