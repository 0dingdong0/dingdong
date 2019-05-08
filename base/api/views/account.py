from collections import OrderedDict
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

    @action(detail=False, name='get current_user')
    def current_account(self, request, pk=None):
        user = request.user
        if user.is_superuser:
            perms = []
        else:
            perms = user.get_all_permissions()

        user_dict = OrderedDict([
            (field.name, getattr(user, field.name))
            for field in type(user)._meta.get_fields()
            if not field.is_relation and field.name != 'password'
        ])

        return Response({'account': user_dict, 'permissions': perms})
