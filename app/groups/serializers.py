from rest_framework import serializers

from .models import Group, CustomUser

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CustomUser
        fields = ("id", "email", "username")
        read_only_fields = ('id')

class GroupSerializer(serializers.ModelSerializer):
    
    # members = serializers.PrimaryKeyRelatedField(many=True, queryset=CustomUser.objects.all())
    # members = UserSerializer(many=True)
    # owner = UserSerializer()
    
    class Meta:
        model = Group
        fields = '__all__'
        read_only_fields = ('id', 'created_at')
    