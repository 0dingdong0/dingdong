from base.models import Account
from rest_framework import serializers


class AccountSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Account
        fields = ['url'] + [field.name for field in Account._meta.get_fields() if not (field.is_relation or field.name == "password")]
