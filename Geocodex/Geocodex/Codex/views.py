from django.shortcuts import render, HttpResponse
from .models import *
from .forms import *

# Create your views here.

# LISTAGEM DE ALVOS
def list_target(request, template_name='index.html'):
    target = Target.objects.all()
    return render(request, template_name, {'dataTarget' : target})

# LOCALIZAÇÃO


def target_details(request, target_id, template_name='index.html'):
    if request.method == 'POST':
        target_id = request.POST['user-id']

    localization = Localization.objects.all(pk=target_id)
    return render(request, template_name, {'dataLocalization' : localization})

