from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from .models import Album, Song
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm
from django.contrib.auth import login, authenticate


def index(request):
    all_albums = Album.objects.all()
    return render(request, 'music/index.html', {'all_albums': all_albums})


def my_albums(request):
    user = request.user
    albums = user.albums.all()
    return render(request, 'music/myalbums.html', {'albums': albums})


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


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.bio = form.cleaned_data.get('bio')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('/music/')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})




