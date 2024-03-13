from rest_framework import serializers
from .models import Post
from accounts.serializers import UserSerializer



class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    #author = UserSerializer()
    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'author', 'created_at', 'updated_at')
