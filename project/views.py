from django.http import HttpResponse


def homePageView(request):
    return HttpResponse('Hello, World!')

def greetingsView(request):
    return HttpResponse('Greetings!')

def hari(request):
    return HttpResponse('hari!')