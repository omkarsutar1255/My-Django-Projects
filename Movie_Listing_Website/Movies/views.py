from django.shortcuts import render
import requests
from .models import MoviesData
from rest_framework import viewsets
from .serializers import MoviesSerializer


class MovieModelViewSet(viewsets.ModelViewSet):
    queryset = MoviesData.objects.all()
    serializer_class = MoviesSerializer


# Create your views here.
def home(request):
    print("inside home")
    try:
        Url = "https://api.themoviedb.org/3/movie/550"
        resp = requests.get(url=Url, params={"api_key": "87402fb400c0ccbffe519e4fb110b891"},
                            ).json()
        print("data = ", resp)
    except Exception:
        raise ValueError
    genres = ''
    for t, l in enumerate(resp['genres']):
        if t < len(resp['genres']) - 1:
            genres += l['name'] + ', '
        else:
            genres += l['name']

    if not MoviesData.objects.filter(Name=resp['original_title']).exists():
        new_data = MoviesData.objects.create(Name=resp['original_title'],
                                             Budget=resp['budget'],
                                             Description=resp['overview'],
                                             Genres=genres,
                                             Popularity=resp['popularity'],
                                             Revenue=resp['revenue'],
                                             Duration=resp['runtime'],
                                             Language=resp['spoken_languages'][0]['english_name'],
                                             Status=resp['status'],
                                             Release_Date=resp['release_date'])
        new_data.save()
        print("data saved")
    else:
        print("Exsting Data")
    return render(request, 'index.html')
