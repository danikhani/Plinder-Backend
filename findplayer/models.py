
from django.db import models
from django.conf import settings


SEX_CHOICES = (
    ('F', 'Female',),
    ('M', 'Male',),
    ('N', 'Other')
)


class FindPlayer(models.Model):
    class Meta:
        db_table = 'findplayer_table'

    game = models.TextField(max_length=100, null=False, blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    last_location = models.PointField(max_length=40, null=True)
    preferred_radius = models.IntegerField(default=5,
                                          help_text="in kilometers")
    sex = models.CharField(max_length=1, choices=SEX_CHOICES, db_index=True)
    preferred_sex = models.CharField(max_length=1, choices=SEX_CHOICES)

    def __str__(self):
        return self.game



