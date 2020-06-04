import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from ..models import Post
from ..serializers import PostSerializer
from datetime import datetime

# initialize the APIClient app
client = Client()

class GetAllPostsTest(TestCase):
    """ Test module for GET all posts API """

    def setUp(self):
        Post.objects.create(
            name='mw', title='kd', content='we are beasts', time_created=datetime.utcnow(), time_updated=datetime.utcnow())
        Post.objects.create(
            name='bf5', title='win/lose', content='we are noobs', time_created=datetime.utcnow(),
            time_updated=datetime.utcnow())

    def test_get_all_puppies(self):
        # get API response
        response = client.get(reverse('get_post_post'))
        # get data from db
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)