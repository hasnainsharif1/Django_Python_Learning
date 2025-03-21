from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello word, I'm currently in home page.")

def about(request):
    return HttpResponse("Hello word, I'm currently in about page.")

def contact(request):
    return HttpResponse("Hello word, I'm currently in contac page.")