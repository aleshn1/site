from django.http import HttpResponse

def index(request):
    return HttpResponse("Olá, seja bem vindo ao site d pesquisa!")

# Create your views here.
