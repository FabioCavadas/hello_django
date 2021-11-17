from django.shortcuts import render, HttpResponse

# Create your views here.
def hello(request, nome, ano):
    return HttpResponse('<h1>Hello {}, como estamos em {} ?<h1>'.format(nome, ano))