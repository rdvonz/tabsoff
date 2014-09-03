from django.shortcuts import render
from mixtape.models import MixTape
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

def index(request):
    mixtapes = MixTape.objects.all()
    context = {'mixtapes': mixtapes,
            }

    return render(request, 'mixtape/mixtape.html', context, context_instance=RequestContext(request))
@login_required
def mixtape(request, pk):
    mixtape = MixTape.objects.get(pk=pk)

    context = {'mixtape': mixtape}

    return render(request, 'mixtape/mixtape-detail.html', context)

