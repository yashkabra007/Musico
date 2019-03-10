from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Album, Song
from django.contrib.auth.decorators import login_required


def index(request):
    all_albums = Album.objects.all()
    return render(request, 'music/index.html', {'all_albums': all_albums})


@login_required
def details(request, album_id):
    # album = get_object_or_404(Album, pk=album_id)
    try:
        album = Album.objects.get(pk=album_id)
    except Album.DoesNotExist:
        raise Http404('Album does not exist')
    return render(request, 'music/details.html', {'album': album})


@login_required
def favorite(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    try:
        selected_song = album.song_set.get(pk=request.POST['song'])
    except (KeyError, Song.DoesNotExist):
        return render(request, 'music/details.html', {'album': album,
                                                      'error_message': "you did not select a valid song"})
    else:
        selected_song.is_favorite = True
        selected_song.save()
        return render(request, 'music/details.html', {'album': album})


