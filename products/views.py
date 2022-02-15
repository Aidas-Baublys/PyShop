from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("Hi lop")


def new(request):
    return HttpResponse("So new")
