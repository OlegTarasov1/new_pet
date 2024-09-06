from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.db.models import Q
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from . import serializers
from .permissions import UserPermissions

class UserBase(ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = serializers.UserBaseSerializer
    permission_classes = (UserPermissions, )
    authentication_classes = [JWTAuthentication]

    def list(self, request, *args, **kwargs):
        additional_filter = request.query_params.get('search', None)
        try:
            if additional_filter:
                to_serialize = get_user_model().objects.filter(Q(Q(first_name__contains = additional_filter) | Q(last_name__contains = additional_filter) | Q(username__contains = additional_filter)) & Q(private = False))
            else:
                to_serialize = get_user_model().objects.filter(private = False)

            serializer = self.get_serializer(to_serialize, many=True)
            return Response(serializer.data)
        except:
            return Response({'error': 'something went wrong'})