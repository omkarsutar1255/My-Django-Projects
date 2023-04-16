from django.shortcuts import render, HttpResponse
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
    movies = MoviesData.objects.all()
    data = {'movies': movies}
    return render(request, 'index.html', context=data)


def fetch(request):
    url_main = "https://api.themoviedb.org/3/movie/"
    for i in range(1, 1000):
        URL = url_main + f'{i}'
        print('urls = ', URL)
        resp = requests.get(url=URL, params={"api_key": "87402fb400c0ccbffe519e4fb110b891"},
                            ).json()
        try:
            if not resp['success']:
                print("Data not present")
        except:
            if not MoviesData.objects.filter(Name=resp['original_title']).exists():
                genres = ''
                for t, l in enumerate(resp['genres']):
                    if t < len(resp['genres']) - 1:
                        genres += l['name'] + ', '
                    else:
                        genres += l['name']
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
        # except:
        #     print("except = ", URL)
        #     return HttpResponse("in except")
    print("for loop ends")
    return render(request, 'index.html')


def getdetails(request):
    print('method = ', request.method)
    print('data = ', request.GET)
    if request.method == 'GET':
        print('get method', request.GET.get('dropdown'))
        movie = MoviesData.objects.get(id=request.GET.get('dropdown'))
        print(movie.Release_Date)
        return render(request, 'getdetails.html', context={"moviedata": movie})
    else:
        print('not get method')