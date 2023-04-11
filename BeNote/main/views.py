from django.shortcuts import render
from django.http import HttpResponse



def main(request):
    return render(request, 'main/base.html')


def new_note(request):
    return HttpResponse("Новая записка")