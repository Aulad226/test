from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
# Create your views here.
from Assignmentapp.models import Producer
from Assignmentapp.models import Artist
from Assignmentapp.models import Song
from Assignmentapp.forms import ProducerForm
from Assignmentapp.forms import ArtistForm
from Assignmentapp.forms import SongForm

def home(request):
    return render(request, 'index.html')

def song(request):
    results=Song.objects.all()
    page_data = { 'list_of_songs': results}
    return render(request, 'song.html', page_data)

def add_song(request):
    if request.method !='POST':
        page_data = {'my_form' : SongForm(),}
    else:
        form = SongForm(request.POST)
        if form.is_valid() !=True:
            page_data = {'my_form' : form,}
        else:
            form.save()
            return HttpResponseRedirect(reverse('song'))
    return render(request, 'add_song.html', page_data)

def edit_song(request, key):
     song = Song.objects.get(id=key)
     if request.method == 'POST':
         form = SongForm(request.POST, instance=song)
         if form.is_valid() != True:
             page_data = {'my_form' : form,}
         else:
             form.save()
             return HttpResponseRedirect(reverse('song'))
     else:
         form = SongForm(instance=song)
         page_data={'my_form': form,}
     return render(request, 'edit_song.html', page_data)

def delete_song(request, key):
    results=Song.objects.filter(id=key)
    results.delete()
    return HttpResponseRedirect(reverse('song'))

def artist(request):
    results=Artist.objects.all()
    page_data = { 'list_of_artist': results}
    return render(request, 'artist.html', page_data)

def add_artist(request):
    if request.method != 'POST':
        page_data={'my_form' : ArtistForm(),}
    else:
        form=ArtistForm(request.POST)
        if form.is_valid() != True:
            page_data = {'my_form' : form,}
        else:
            return HttpResponseRedirect(reverse('artist'))
    return render(request, 'add_artist.html', page_data)

def edit_artist(request, key):
     artist = Artist.objects.get(id=key)
     if request.method == 'POST':
         form = ArtistForm(request.POST, instance=artist)
         if form.is_valid() != True:
             page_data = {'my_form' : form,}
         else:
             form.save()
             return HttpResponseRedirect(reverse('artist'))
     else:
         form = SongForm(instance=artist)
         page_data={'my_form': form,}
     return render(request, 'edit_artist.html', page_data)

def delete_artist(request, key):
    results=Artist.objects.filter(id=key)
    results.delete()
    return HttpResponseRedirect(reverse('artist'))

def producer(request):
    results=Producer.objects.all()
    page_data = { 'list_of_producer': results}
    return render(request, 'producer.html', page_data)

def add_producer(request):
    if request.method != 'POST':
        page_data={'my_form' : ProducerForm(),}
    else:
        form=ProducerForm(request.POST)
        if form.is_valid() != True:
            page_data = {'my_form' : form,}
        else:
            return HttpResponseRedirect(reverse('producer'))
    return render(request, 'add_producer.html', page_data)

def edit_producer(request, key):
     producer = Producer.objects.get(id=key)
     if request.method == 'POST':
         form = ProducerForm(request.POST, instance=producer)
         if form.is_valid() != True:
             page_data = {'my_form' : form,}
         else:
             form.save()
             return HttpResponseRedirect(reverse('producer'))
     else:
         form = ProducerForm(instance=producer)
         page_data={'my_form': form,}
     return render(request, 'edit_producer.html', page_data)

def delete_producer(request, key):
    results=Producer.objects.filter(id=key)
    results.delete()
    return HttpResponseRedirect(reverse('producer'))
