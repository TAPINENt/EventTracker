from multiprocessing import Event
from rest_framework import serializers
from .models import Todo
from .models import Event

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id' ,'title', 'description', 'completed')

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event

        fields = ('event_id','event_code','event_code_short','event_name','event_location','event_org','host','event_start_date','event_end_date','event_image','about_event',)