from django.shortcuts import render
from django.contrib.auth import authenticate, login
from mixtape.models import MixTape

def index(request):
    mixtapes = MixTape.objects.all()
    context = {'mixtapes': mixtapes}
    return render(request, 'mixtape/mixtape.html', context)

def mixtape(request, pk):
    mixtape = MixTape.objects.get(pk=pk)

    context = {'mixtape': mixtape}

    return render(request, 'mixtape/mixtape-detail.html', context)

def user_profile(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            #redirect to a success page
        else:
            #return a 'disabled account' error message
            pass
    else:
        #return an 'invalid login' messageS
        pass
