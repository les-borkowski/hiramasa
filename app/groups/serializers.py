from rest_framework import serializers

from .models import Group, CustomUser, Event, Post

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CustomUser
        fields = ("email", "username")
        # read_only_fields = ('id')

class GroupSerializer(serializers.ModelSerializer):
    
    members = serializers.PrimaryKeyRelatedField(many=True, queryset=CustomUser.objects.all())
    owner = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all())
    
    class Meta:
        model = Group
        fields = ("name", "description", "owner", "created_at", "members")
        read_only_fields = ('id', 'created_at')

class EventSerializer(serializers.ModelSerializer):
    attendees = serializers.PrimaryKeyRelatedField(many=True, queryset=CustomUser.objects.all())
    owner = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all())
    group = serializers.PrimaryKeyRelatedField(queryset=Group.objects.all())
    
    class Meta:
        model = Event
        fields = ("name", "description", "owner", "group", "location", "time", "attendees", "created_at")
        read_only_fields = ('id', 'created_at')
        
class PostSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Post
        fields = ("title", "content", "created_by", "created_at", "event")
        read_only_fields = ('id', 'created_at')    