from django.test import TestCase
from ..models import Post
from datetime import datetime


class PostsTest(TestCase):
    """ Test module for Post model """

    def setUp(self):
        Post.objects.create(
            name='mw', title='kd', content='we are beasts', time_created=datetime.utcnow(),time_updated=datetime.utcnow())
        Post.objects.create(
            name='bf5', title='win/lose', content='we are noobs', time_created=datetime.utcnow(),time_updated=datetime.utcnow())

    def test_posts(self):
        mw_post = Post.objects.get(name='mw')
        bf5_post = Post.objects.get(name='bf5')
        self.assertEqual(
            mw_post.get_content(), "we are beasts belongs to this post: mw")
        self.assertEqual(
            bf5_post.get_content(), "we are noobs belongs to this post: bf5")