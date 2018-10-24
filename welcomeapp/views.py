from django.http import HttpResponse
def welcome(request):
    return HttpResponse("<html><body bgcolor=cyan><h1><center>welcome to lokesh it</center></h1></body></html>")
