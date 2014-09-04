from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

from mixtape.models import MixTape
from mixtape.forms import MixTapeUploadForm

def index(request):
    '''
    The mixtape site index.
    '''
    #We want to show all the mixtapes on the main page. Maybe add an ordering later?
    mixtapes = MixTape.objects.all()

    #The template context, gives us a 'mixtapes' variable to work with
    context = {'mixtapes': mixtapes,
               }

    return render(request, 'mixtape/mixtape.html', context)


def mixtape(request, pk):
    '''
    the mixtape page
    '''
    #we're only displaying a single mixtape here, and we're building the url based off the mixtape id (the primary key)
    mixtape = MixTape.objects.get(pk=pk)
    users_favorited = []

    context = {'mixtape': mixtape,
               'favorites': users_favorited,
               }

    return render(request, 'mixtape/mixtape-detail.html', context)


@login_required(login_url='/mixtapes/')
def upload(request):
    '''
    The mixtape upload form
    '''

    #if the form is being sent to the server we're going to want to hand the upload of the album artwork
    if request.method == 'POST':
        #passing the necessary post data to the upload form
        upload_form = MixTapeUploadForm(request.POST, request.FILES)
        if upload_form.is_valid():
            #when we know we're dealing with a bound form, create a new model based on the form data
            new_mix = MixTape(title=request.POST['mix_name'], album_art=request.FILES['album_art'], created_by=request.user)
            #and save the model to the database
            new_mix.save()
            #redirect to the user to the mixtape page in order to add music
            return HttpResponseRedirect(reverse('mixtapes:mixtape', args=(new_mix.id,)))
        else:
            #an unbound form (that is, no data was added to this form)
            upload_form = MixTapeUploadForm()

    return render(request, 'mixtape/upload.html', {'upload_form': upload_form})

@login_required(login_url='/mixtapes/')
def user_mixes(request):
    '''
    This is very similar to the default mixtape index
    The only difference is we find all the mixes the user
    has created in the database
    Is there a way to do this without repeating myself?
    '''
    mixtapes= MixTape.objects.filter(created_by=request.user)

    return render(request, 'mixtape/mixtape.html', {'mixtapes': mixtapes,})

@login_required(login_url='/mixtapes')
def add_favorite(request, pk):
    mixtape = MixTape.objects.get(pk=pk)
    mixtape.favorited_by.add(request.user)
    return HttpResponseRedirect(reverse('mixtapes:mixtape', args=(pk,)))

