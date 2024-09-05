from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.db.models import Q
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from . import serializers
# from .permissions import UserPermissions

class UserBase(ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = serializers.UserBaseSerializer
    # permission_classes = (UserPermissions, )

    def list(self, request, *args, **kwargs):
        additional_filter = request.query_params.get('search', None)
        try:
            if additional_filter:
                to_serialize = get_user_model().notprivate.filter(Q(first_name__contains = additional_filter) | Q(last_name__contains = additional_filter) | Q(username__contains = additional_filter))
            else:
                to_serialize = get_user_model().notprivate.all()

            serializer = self.get_serializer(to_serialize, many=True)
            return Response(serializer.data)
        except:
            return Response({'error': 'something went wrong'})