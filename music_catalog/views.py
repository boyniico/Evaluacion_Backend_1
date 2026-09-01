from django.shortcuts import render
from django.http import Http404
from utils import load_json_app

def catalog(request):
    albums = load_json_app("music.json")
    for album in albums:
        album['creator'] = album['artist']
    return render(request, 'music/catalog.html', {'albums': albums})

def music_detail(request, album_id):
    albums = load_json_app("music.json")
    for album in albums:
        album['creator'] = album['artist']

    album = next((item for item in albums if item['id'] == album_id), None)
    
    if album is None:
        raise Http404("Album not found")
        
    return render(request, 'music/music_detail.html', {'album': album})