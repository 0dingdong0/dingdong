from rest_framework import status
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

        account = AccountSerializer(user, context={'request': request})

        return Response({'account': account.data, 'permissions': perms})

    @action(detail=True, methods=['patch'])
    def set_password(self, request, pk=None):
        user = self.get_object()
        print('-----------------------------')
        print(request.user.id, user.id)
        if (not request.user.is_superuser) or (request.user.id == user.id):
            if not user.check_password(request.data['password']):
                return Response({
                    'password': ['密码不正确']
                }, status.HTTP_400_BAD_REQUEST)

        new_password = request.data['new_password']
        confirm_password = request.data['confirm_password']
        if new_password != confirm_password:
            return Response({
                'new_password': ['两个新密码不一致'],
                'confirm_password': ['两个新密码不一致']
            }, status.HTTP_400_BAD_REQUEST)

        user.set_password(new_password)
        user.save()
        return Response(None, status=status.HTTP_200_OK)

