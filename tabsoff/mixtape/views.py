import zipfile, os
from mutagen.mp3 import EasyMP3 as MP3
from mutagen.mp3 import HeaderNotFoundError
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.core.files import File
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView
from mixtape.models import MixTape, Track
from mixtape.forms import MixTapeUploadForm

class MixTapeList(ListView):
    '''
    The mixtape site index.
    '''
    #We want to show all the mixtapes on the main page. Maybe add an ordering later?
    context_object_name = 'mixtapes'
    template_name = 'mixtape/mixtape.html'
    model = MixTape

class FavoriteMixTapeList(ListView):
        context_object_name = 'mixtapes'
        template_name = 'mixtape/mixtape.html'
        def get_queryset(self):
            return MixTape.objects.filter(favorited_by=self.request.user)
class UserMixTapeList(ListView):
    context_object_name = 'mixtapes'
    template_name = 'mixtape/mixtape.html'

    def get_queryset(self):
        return MixTape.objects.filter(created_by=self.request.user)

class MixTapeDetail(DetailView):
    '''
    'registration',
    the mixtape page
    '''
    template_name = 'mixtape/mixtape-detail.html'
    #we're only displaying a single mixtape here, and we're building the url based off the mixtape id (the primary key)
    model = MixTape

def not_logged_in(request):
    mixtape = MixTape.objects.all()

    return render(request, 'mixtape/mixtape.html', {'mixtapes': mixtape, 'no_entry': True})

def upload(request):
    '''
            except zipfile.BadZipFile:
                return render(request, 'mixtape/upload.html', {'upload_form': upload_form, 'error':True})
    The mixtape upload form
    '''

    #if the form is being sent to the server we're going to want to hand the upload of the album artwork

    upload_form = MixTapeUploadForm()
    if request.method == 'POST':

        #passing the necessary post data to the upload form
        upload_form = MixTapeUploadForm(request.POST, request.FILES)
        if upload_form.is_valid():
            #when we know we're dealing with a bound form, create a new model based on the form data

            #The easiest thing to do is to create the new MixTape object, we need it to create each track
            new_mix = MixTape(title=request.POST['mix_name'], album_art=request.FILES['album_art'], created_by=request.user)
            new_mix.save()

            #Next we check if we're really dealing with a zipfile, else we give the user an error message
            mix_zipfile = request.FILES['mixtape']
            try:
                mixtape_files = zipfile.ZipFile(mix_zipfile)
                mixtape_files.extractall()
            except zipfile.BadZipfile:

                return render(request, 'mixtape/upload.html', {'upload_form': upload_form, 'error_zip':True})

            for filename in mixtape_files.namelist():
                    current_file = os.path.join(os.getcwd(), filename)
                    try:
                        f = open(current_file)
                    except IOError:
                        return render(request, 'mixtape/upload.html', {'upload_form': upload_form, 'error_dir':True, 'song_error': filename})
                        os.remove(current_file)
                    try:
                        mixtape_files.extractall()
                        music_tags = MP3(os.path.join(os.getcwd(), filename))
                        track = Track(
                        title=music_tags['title'][0],
                        artist = music_tags['artist'][0],
                        album = music_tags['album'][0],
                        song_file = File(f),
                        mixtape = new_mix,
                        )
                        track.save()
                        f.close()
                        os.remove(current_file)

                    #A header not found error means we don't have an mp3 file
                    except HeaderNotFoundError:
                        return render(request, 'mixtape/upload.html', {'upload_form': upload_form, 'error_mp3':True, 'song_error': filename})

                    #this is indicative of a missing tag
                    except KeyError:
                        return render(request, 'mixtape/upload.html', {'upload_form': upload_form, 'error_tag':True, 'song_error': filename})

            return HttpResponseRedirect(reverse('mixtapes:mixtape', args=(new_mix.id,)))

    return render(request, 'mixtape/upload.html', {'upload_form': upload_form, 'error': False}, )

@login_required()
def add_favorite(request, pk):
    mixtape = MixTape.objects.get(pk=pk)
    mixtape.favorited_by.add(request.user)
    return HttpResponseRedirect(reverse('mixtapes:mixtape', args=(pk,)))

def anywhere_login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            print request.path
            return HttpResponseRedirect(reverse('mixtapes:index'))
        else:
            pass
    else:
        return HttpResponseRedirect(reverse('mixtapes:index'))

def anywhere_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('mixtapes:index'))
