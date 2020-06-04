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
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # get details of a single Post
    if request.method == 'GET':
        serializer = PostSerializer(post)
        return Response(serializer.data)
    # delete a single Post
    elif request.method == 'DELETE':
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    # update details of a single Post
    # similar to an insert, we serialize and validate the request data and then respond appropriately.
    elif request.method == 'PUT':
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def get_post_post(request):
    # get all post
    if request.method == 'GET':
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    # insert a new record for a post
    # Here, we inserted a new record by serializing and validating the request data before inserting to the database.
    elif request.method == 'POST':
        data = {
            'name': request.data.get('name'),
            'title': request.data.get('title'),
            'content': request.data.get('content'),
            'time_created': request.data.get('time_created'),
            'time_updated' : request.data.get('time_updated'),
        }
        serializer = PostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
