from django.contrib.auth.forms import AuthenticationForm
from django.core.urlresolvers import reverse

def login_context_processor(request):
    if request.method== 'POST':
        login_form = AuthenticationForm(request.POST)
    else:
        login_form = AuthenticationForm()

    return {
        'login_form': login_form,
        'login_form_url': 'mixtapes:index',
        }
