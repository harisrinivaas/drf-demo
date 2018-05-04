from django.http import HttpResponse


def homePageView(request):
    return HttpResponse('Hello, World!')

def welcome(request):
    return HttpResponse('welcome!')
