from django.shortcuts import render
from .models import Movie
from watchlist_app.serializers import MovieSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view


# Create your views here.
@api_view(['GET', 'POST'])
def movie_list(request):
   if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)

   

def movie_detail(request,pk):
   movie=Movie.Object.get(pk=pk)
   serializer=MovieSerializer(movie)
   return Response (serializer.data)