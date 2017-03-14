from django.contrib.auth import get_user_model
from rest_framework import serializers
from blog.models import Post


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'username',]


class AuthorSerializer(serializers.HiddenField):
    def __init__(self, **kwargs):
        super(serializers.HiddenField, self).__init__(default=serializers.CurrentUserDefault, **kwargs)

    def to_internal_value(self, data):
        return data

    def get_value(self, dictionary):
        return self.context.get('request').user

    def to_representation(self, user):
        return UserSerializer(user).data


"""
viewset:
    def list:
        serializer = PS(user)
        return Response(serializer.data)

ModelSerializer:
    def data:
        result = {}
        for field in self.fields:
            result[field.name] = field.to_representation(getattr(obj, field.name))
Field
    def data:
        return str(self) + ">_<"
"""


class PostSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    class Meta:
        model = Post
        fields = ['id', 'author',  'title', 'content', 'created_at']

