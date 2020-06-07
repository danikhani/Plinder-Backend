from django.shortcuts import render

# posts/views.py
from rest_framework import generics

from .models import Post
from .serializers import PostSerializer


class PostList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


# for Implementing CRUD ( it has every request from start)
#class PostDetail(generics.RetrieveUpdateDestroyAPIView):
#    queryset = Post.objects.all()
#    serializer_class = PostSerializer
