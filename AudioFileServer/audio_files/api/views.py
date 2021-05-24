
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.parsers import JSONParser
from rest_framework import permissions
from rest_framework import status
from audio_files.models import *
from .serializers import *

@permission_classes((permissions.AllowAny,))
class AudioFilesListView(APIView):
    def get(self, request, audioFileType):
        if audioFileType not in ['song', 'podcast', 'audiobook']:
            return Response("File type is invalid, must be one from 'song', 'podcast', 'audiobook'", status=400)
        if audioFileType =='song':
            obj = Song.objects.all()
            serialized_obj = SongSerializer(obj, many=True)
        elif audioFileType =='podcast':
            obj = Podcast.objects.all()
            serialized_obj = PodcastSerializer(obj, many=True)
        elif audioFileType =='audiobook':
            obj = AudioBook.objects.all()
            serialized_obj = AudioBookSerializer(obj, many=True)
        return Response(serialized_obj.data)

    def post(self, request, audioFileType):
        if audioFileType not in ['song', 'podcast', 'audiobook']:
            return Response("File type is invalid, must be one from 'song', 'podcast', 'audiobook'", status=400)
        data = request.data  #JSONParser().parse(request)
        if audioFileType =='song':
            serializer = SongSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=200)
            return JsonResponse(serializer.errors, status=400)
        elif audioFileType =='podcast':
            serializer = PodcastSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=200)
            return JsonResponse(serializer.errors, status=400)
        elif audioFileType =='audiobook':
            serializer = AudioBookSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=200)
            return JsonResponse(serializer.errors, status=400)

@permission_classes((permissions.AllowAny,))
class AudioFilesView(APIView):
    def get(self, request, audioFileType, audioFileID):
        if audioFileType not in ['song', 'podcast', 'audiobook']:
            return Response("File type is invalid, must be one from 'song', 'podcast', 'audiobook'", status=400)
        try:
            if audioFileType =='song':
                obj = Song.objects.get(pk=audioFileID)
                serialized_obj = SongSerializer(obj)
            elif audioFileType =='podcast':
                obj = Podcast.objects.get(pk=audioFileID)
                serialized_obj = PodcastSerializer(obj)
            elif audioFileType =='audioBook':
                obj = AudioBook.objects.get(pk=audioFileID)
                serialized_obj = AudioBookSerializer(obj)
            return Response(serialized_obj.data)
        except (Song.DoesNotExist, Song.DoesNotExist, Song.DoesNotExist) as err:
            return Response(str(err), status=400)

    def put(self, request, audioFileType, audioFileID):
        if audioFileType not in ['song', 'podcast', 'audiobook']:
            return Response("File type is invalid, must be one from 'song', 'podcast', 'audiobook'", status=400)
        data = request.data  #JSONParser().parse(request)
        if audioFileType =='song':
            try:
                obj = Song.objects.get(pk=audioFileID)
            except Song.DoesNotExist as err:
                return Response(str(err), status=400)
            serializer = SongSerializer(obj, data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=200)
            return JsonResponse(serializer.errors, status=400)
        elif audioFileType =='podcast':
            try:
                obj = Podcast.objects.get(pk=audioFileID)
            except Podcast.DoesNotExist as err:
                return Response(str(err), status=400)
            serializer = PodcastSerializer(obj, data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=200)
            return JsonResponse(serializer.errors, status=400)
        elif audioFileType =='audiobook':
            try:
                obj = AudioBook.objects.get(pk=audioFileID)
            except AudioBook.DoesNotExist as err:
                return Response(str(err), status=400)
            serializer = AudioBookSerializer(obj, data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=200)
            return JsonResponse(serializer.errors, status=400)

    def delete(self, request, audioFileType, audioFileID):
        if audioFileType not in ['song', 'podcast', 'audiobook']:
            return Response("File type is invalid, must be one from 'song', 'podcast', 'audiobook'", status=400)
        try:
            if audioFileType =='song':
                obj = Song.objects.get(pk=audioFileID)
            elif audioFileType =='podcast':
                obj = Podcast.objects.get(pk=audioFileID)
            elif audioFileType =='audiobook':
                obj = AudioBook.objects.get(pk=audioFileID)
        except (Song.DoesNotExist, Song.DoesNotExist, Song.DoesNotExist) as err:
            return Response(str(err), status=400)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

'''
@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def CreateView(request, audioFileType):
    pass

@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def ListCreateView(request, audioFileType):
    if request.method == 'GET':
        if audioFileType =='song':
            obj = Song.objects.all()
            serialized_obj = SongSerializer(obj, many=True)
        elif audioFileType =='podcast':
            obj = Podcast.objects.all()
            serialized_obj = PodcastSerializer(obj, many=True)
        elif audioFileType =='audiobook':
            obj = AudioBook.objects.all()
            serialized_obj = AudioBookSerializer(obj, many=True)
        return Response(serialized_obj.data)

    if request.method == 'POST':
        data = request.data  #JSONParser().parse(request)
        if audioFileType =='song':
            serializer = SongSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=200)
            return JsonResponse(serializer.errors, status=400)
        elif audioFileType =='podcast':
            serializer = PodcastSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=200)
            return JsonResponse(serializer.errors, status=400)
        elif audioFileType =='audiobook':
            serializer = AudioBookSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=200)
            return JsonResponse(serializer.errors, status=400)




@api_view(['GET', 'DELETE', 'PUT'])
@permission_classes((permissions.AllowAny,))
def DetailDeleteUpdateView(request, audioFileType, audioFileID):
    if request.method == 'GET':
        if audioFileType =='song':
            obj = Song.objects.get(pk=audioFileID)
            serialized_obj = SongSerializer(obj)
        elif audioFileType =='podcast':
            obj = Podcast.objects.get(pk=audioFileID)
            serialized_obj = PodcastSerializer(obj)
        elif audioFileType =='audiobook':
            obj = AudioBook.objects.get(pk=audioFileID)
            serialized_obj = AudioBookSerializer(obj)
        return Response(serialized_obj.data)
    elif request.method == 'DELETE':
        if audioFileType =='song':
            obj = Song.objects.get(pk=audioFileID)
        elif audioFileType =='podcast':
            obj = Podcast.objects.get(pk=audioFileID)
        elif audioFileType =='audiobook':
            obj = AudioBook.objects.get(pk=audioFileID)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        data = request.data  #JSONParser().parse(request)
        if audioFileType =='song':
            obj = Song.objects.get(pk=audioFileID)
            serializer = SongSerializer(obj, data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=200)
            return JsonResponse(serializer.errors, status=400)
        elif audioFileType =='podcast':
            obj = Podcast.objects.get(pk=audioFileID)
            serializer = PodcastSerializer(obj, data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=200)
            return JsonResponse(serializer.errors, status=400)
        elif audioFileType =='audiobook':
            obj = AudioBook.objects.get(pk=audioFileID)
            serializer = AudioBookSerializer(obj, data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=200)
            return JsonResponse(serializer.errors, status=400)


@api_view(['DELETE'])
@permission_classes((permissions.AllowAny,))
def DeleteView(request, audioFileType, audioFileID):
    if audioFileType =='song':
        obj = Song.objects.get(pk=audioFileID)
    elif audioFileType =='podcast':
        obj = Podcast.objects.get(pk=audioFileID)
    elif audioFileType =='audiobook':
        obj = AudioBook.objects.get(pk=audioFileID)
    obj.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['PUT'])
@permission_classes((permissions.AllowAny,))
def UpdateView(request, audioFileType, audioFileID):
    data = request.data  #JSONParser().parse(request)
    if audioFileType =='song':
        obj = Song.objects.get(pk=audioFileID)
        serializer = SongSerializer(obj, data=data, many=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)
    elif audioFileType =='podcast':
        obj = Podcast.objects.get(pk=audioFileID)
        serializer = PodcastSerializer(obj, data=data, many=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)
    elif audioFileType =='audiobook':
        obj = AudioBook.objects.get(pk=audioFileID)
        serializer = AudioBookSerializer(obj, data=data, many=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)
'''
