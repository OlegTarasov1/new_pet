from datetime import date
from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password


class UserBaseSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    age = serializers.SerializerMethodField(read_only = True)
    birth_date = serializers.DateField(required = False)
    last_name = serializers.CharField(required = False)

    def get_age(self, obj):
        today = date.today()
        return today.year - obj.birth_date.year - int((today.month, today.day) < (obj.birth_date.month, obj.birth_date.day)) if obj.birth_date else None

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        user = get_user_model().objects.create(**validated_data)
        return user
    

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password', 'first_name', 'last_name', 'birth_date', 'age']
