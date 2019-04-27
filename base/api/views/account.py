from base.models import Account
from base.api.serializers import AccountSerializer
from rest_framework.decorators import action
from rest_framework import viewsets
from rest_framework.response import Response


class AccountViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Account.objects.all().order_by('-date_joined')
    serializer_class = AccountSerializer

    @action(detail=True, name='get all permissions')
    def permissions(self, request, pk=None):
        perms = self.get_object().get_all_permissions()
        return Response(perms)
