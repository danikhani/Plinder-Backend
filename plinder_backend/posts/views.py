from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Post
from .serializers import PostSerializer

# Create your views here.
@api_view(['GET', 'DELETE', 'PUT'])
def get_delete_update_post(request, pk):
    try:
        puppy = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # get details of a single Post
    if request.method == 'GET':
        return Response({})
    # delete a single Post
    elif request.method == 'DELETE':
        return Response({})
    # update details of a single Post
    elif request.method == 'PUT':
        return Response({})


@api_view(['GET', 'POST'])
def get_post_post(request):
    # get all post
    if request.method == 'GET':
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    # insert a new record for a post
    elif request.method == 'POST':
        return Response({})
