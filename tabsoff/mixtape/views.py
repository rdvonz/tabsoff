from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from mixtape.models import MixTape

def index(request):
    mixtapes = MixTape.objects.all()
    context = {'mixtapes': mixtapes}
    return render(request, 'mixtape/mixtape.html', context)

def mixtape(request, pk):
    mixtape = MixTape.objects.get(pk=pk)

    context = {'mixtape': mixtape}

    return render(request, 'mixtape/mixtape-detail.html', context)
