from django.contrib.auth.models import Group
from rest_framework import serializers
from base.models import Account


class GroupSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Group
        fields = ('url', 'name')
