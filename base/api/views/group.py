from django.contrib.auth.models import Group
from base.api.serializers import GroupSerializer
from rest_framework import viewsets
from rest_framework import permissions


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
