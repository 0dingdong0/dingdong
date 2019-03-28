from base.models import Account
from base.api.serializers import AccountSerializer
from rest_framework import permissions
from rest_framework import viewsets


class AccountViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Account.objects.all().order_by('-date_joined')
    serializer_class = AccountSerializer
