from rest_framework import serializers
from .models import Post

'''we defined a ModelSerializer for our puppy model,
 validating all the mentioned fields. 
 In short, if you have a one-to-one relationship between your API endpoints and your models 
 - which you probably should if you’re creating a RESTful API - 
 then you can use a ModelSerializer to create a Serializer.'''

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('name', 'title', 'content', 'time_created', 'time_updated')
