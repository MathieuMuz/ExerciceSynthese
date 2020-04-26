from disks.models import *
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .forms import ResearchForm


# Create your views here.

def read(request, id_album):
    albums = Album.objects.all()
    album = get_object_or_404(Album, id=id_album)
    tracks = Track.objects.filter(album=id_album)
    return render(request, 'site_albums/album.html', locals())


def home(request):
    albums = Album.objects.all()
    return render(request, 'site_albums/home.html', locals())


def research(request):
    form = ResearchForm(request.GET)
    if form.is_valid():
        titre = form.cleaned_data['album']
        albums = Album.objects.filter(Title__contains=titre)
    else:
        return HttpResponse('Erreur dans le formulaire...')

    return render(request, 'site_albums/research.html', locals())
