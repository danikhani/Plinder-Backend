from django.db import models


# Create your models here.
class Post(models.Model):
    class Meta:
        db_table = 'user_profile_data'

    name = models.CharField(max_length=255)
    title = models.CharField(max_length=60)
    content = models.TextField(max_length=1024)
    time_created = models.DateTimeField(auto_now=True, auto_now_add=False)
    time_updated = models.DateTimeField(auto_now=False, auto_now_add=True)

    def get_content(self):
        return self.content + ' belongs to this post: ' + self.name

    def __repr__(self):
        return self.name + ' is added.'
