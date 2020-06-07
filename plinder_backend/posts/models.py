from django.db import models

# posts/models.py
from django.db import models


class Post(models.Model):
    class Meta:
       db_table = 'posts_table'
       # db_table = 'public\".\"posts_table'

    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title