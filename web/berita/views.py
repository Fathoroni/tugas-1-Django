from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def tugas (request):
    template = loader.get_template('tugas.html')
    return HttpResponse(template.render())

def aboutme (request):
    template = loader.get_template('aboutme.html')
    return HttpResponse(template.render())

def contentme (request):
    template = loader.get_template('contentme.html')
    return HttpResponse(template.render())

