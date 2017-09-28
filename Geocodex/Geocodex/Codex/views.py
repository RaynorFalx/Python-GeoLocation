from django.http import Http404, HttpResponse
from django.shortcuts import render
from .models import *



# LISTAGEM DE ALVOS INDEX


def list_target(request, template_name='index.html'):
    target = Target.objects.all()
    return render(request, template_name, {'targets': target})

# LOCALIZAÇÃO DETAILS


def target_details(request, target_id):
    target = Target.objects.filter(pk=target_id)
    target = {'targets': target}
    return render(request, 'detail.html', target)




