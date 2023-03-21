from .models import Author,Blog
from rest_framework import serializers
from django.contrib.auth.models import User

class BlogSerializers(serializers.ModelSerializer):
    author = serializers.StringRelatedField(many=False)
    author = serializers.PrimaryKeyRelatedField(
        many = False, queryset=Author.objects.all()
        )
    
    class Meta:
        model = Blog
        fields = ['title','blog_content','author']


class AuthorSerializer(serializers.ModelSerializer):
    blogs = BlogSerializers(many=True, read_only=True)
    class Meta:
        model = Author
        fields = ['name','about_author' ,'blogs']


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}


class LoginSerializer(serializers.ModelSerializer):
     class Meta:
         model = User
         fields = ('username','password') 