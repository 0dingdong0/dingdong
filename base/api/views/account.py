from rest_framework import status
from base.models import Account
from base.api.serializers import AccountSerializer
from rest_framework.decorators import action
from rest_framework import viewsets
from rest_framework.response import Response
from django.db.utils import IntegrityError

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

        # @TODO: add object level permission checking
        if request.user.id == user.id:
            if not user.check_password(request.data['password']):
                return Response({
                    'password': ['密码不正确']
                }, status.HTTP_405_METHOD_NOT_ALLOWED)

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

    @action(detail=True, methods=['patch'])
    def set_login_name(self, request, pk=None):
        user = self.get_object()

        # @TODO: add object level permission checking
        if request.user.id == user.id:
            if not user.check_password(request.data['password']):
                return Response({
                    'password': ['密码不正确']
                }, status.HTTP_405_METHOD_NOT_ALLOWED)

        user.username = request.data['username']

        try:
            user.save()
            return Response(
                {'username': user.username},
                status=status.HTTP_200_OK)
        except IntegrityError:
            return Response(
                {'username': request.data['username']},
                status=status.HTTP_409_CONFLICT)



