import uuid
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.cache import cache
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import UuidPermission
from .models import Notes
from .serializers import NotesSerializer


class NoteMeneger(ModelViewSet):
    queryset = Notes.objects.all()
    serializer_class = NotesSerializer
    authentication_classes = [JWTAuthentication]

    def list(self, request, *args, **kwargs):
        user = request.user
        to_serialize = self.get_queryset().filter(creator = user)
        serialized = self.get_serializer(to_serialize, many = True)
        return Response(serialized.data)


class CreateUuid(APIView):
    permission_classes = (UuidPermission, )
    authentication_classes = [JWTAuthentication]
    
    def post(self, request, *args, **kwargs):
        unique_href = uuid.uuid4()
        time = request.data.get('time')
        if time > 24*60:
            return Response({'error': 'maximum time the href could be stored is one day'})
        cache.set(unique_href, request.data.get('note_id'), time)
        return Response({"access_href": unique_href})

    def delete(self, request, *args, **kwargs):
        unique_href = request.data.get('unique_href')
        if cache.get(unique_href):
            cache.delete(unique_href)
            return Response({"success": f'key: {unique_href} has been deleted successfully!'})
        else:
            return Response({'error': 'there\'s no such value stored'})

    def get(self, request, *args, **kwargs):
        unique_href = request.GET.get('unique_href')
        required_id = cache.get(unique_href)
        if required_id:
            try:
                to_serialize = Notes.objects.get(id = required_id)
            except:
                return Response({"error": 'no such key-value pair is stored on the server'})
            serialized = NotesSerializer(to_serialize)
            return Response(serialized.data)
        else:
            return Response({'error': 'no such key-value pair is stored on the server'})
