from rest_framework import serializers
from polls.models import TodoEven, User
class TodoEvenSerializer(serializers.ModelSerializer):
    class Meta:
        model=TodoEven
        field='__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        field='__all__'