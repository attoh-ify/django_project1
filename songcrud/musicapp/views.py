from django.shortcuts import render
from django.http import JsonResponse
from .models import Artiste, Song, Lyric
from .serializers import ArtisteSerializer, SongSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


@api_view(['GET', 'POST'])
def artiste_list(request, format=None):

    if request.method == "GET":
        # get all artistes
        artiste = Artiste.objects.all()
        # serialize them
        serializer = ArtisteSerializer(artiste, many=True)
        # retuen json
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = ArtisteSerializer(data=request.data)
        # check if data is valid
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def artiste_detail(request, id, format=None):
    try:
        artiste = Artiste.objects.get(pk=id)
    except Artiste.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ArtisteSerializer(artiste)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ArtisteSerializer(artiste, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        artiste.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def song_list(request, format=None):

    if request.method == "GET":
        # get all songs
        song = Song.objects.all()
        # serialize them
        serializer = SongSerializer(song, many=True)
        # retuen json
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = SongSerializer(data=request.data)
        # check if data is valid
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def song_detail(request, id, format=None):
    try:
        song = Song.objects.get(pk=id)
    except Song.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SongSerializer(song)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SongSerializer(song, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        song.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
