from django.contrib.auth.forms import AuthenticationForm

def login_context_processor(request):
    if request.method == 'POST':
        login_form = AuthenticationForm(request, request.POST)
        print 'hello'
    else:
        login_form = AuthenticationForm()

    return {
        'login_form': login_form,
        }
