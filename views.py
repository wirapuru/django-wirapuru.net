__author__ = 'Eduardo Vaz de Mello'


from django.http import HttpResponse

def woah(request):
    return HttpResponse("<h1>Woah, it works even without restarting the server!</h1>") 