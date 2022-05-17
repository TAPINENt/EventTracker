from multiprocessing import Event
from rest_framework import serializers
from .models import Todo
from .models import Event

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id' ,'title', 'description', 'completed')

class CreateRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event