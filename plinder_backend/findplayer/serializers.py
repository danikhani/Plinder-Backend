from rest_framework import serializers
from .models import FindPlayer,SEX_CHOICES
from django.contrib.gis.geos import fromstr

import os
from django.conf import settings


class ListNearbyPlayer(serializers.ModelSerializer):
    preferred_sex = serializers.ChoiceField(choices=SEX_CHOICES, default='male')
    sex = serializers.ChoiceField(choices=SEX_CHOICES, default='male')
    distance = serializers.SerializerMethodField(read_only=True)
    smaller_radius = serializers.IntegerField(read_only=True)

    class Meta:
        model = FindPlayer
        fields = "__all__"

    def get_distance(self, obj):
        if hasattr(obj, 'distance'):
            return round(obj.distance.m, 1)
        else:
            return None

    def to_representation(self, instance):
        ret = super(ListNearbyPlayer, self).to_representation(instance)
        pnt = fromstr(ret['last_location'])
        ret['last_location'] = {'longitude': pnt.coords[0], 'latitude': pnt.coords[1]}
        return ret