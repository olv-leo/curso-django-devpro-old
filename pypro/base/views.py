from django.shortcuts import HttpResponse


def home(request):
    return HttpResponse('<html><body>Olá Django!</body></html>')
