from groups.serializers import GroupSerializer, UserSerializer
# from events.serializers import EventSerializer
import pytest

@pytest.mark.django_db 
def test_valid_group_serializer():
    valid_serializer_data = {
        "name": "Cheeses",
        "description": "oh so tasty!",
        "owner": 1,
        "members": [1, 2],    
    }
    serializer = GroupSerializer(data=valid_serializer_data)

    assert serializer.is_valid()
    assert serializer.validated_data == valid_serializer_data
    assert serializer.data == valid_serializer_data
    assert serializer.errors == {}
    
@pytest.mark.django_db 
def test_invalid_group_serializer():
    invalid_serializer_data = {
        "description": "lorem ipsum",
    }
    serializer = GroupSerializer(data=invalid_serializer_data)
    assert not serializer.is_valid()
    assert serializer.validated_data == {}
    assert serializer.data == invalid_serializer_data
    assert serializer.errors == {
        "name": ["This field is required."], 
        "members": ["This field is required."], 
        "owner": ["This field is required."]
        }    

@pytest.mark.django_db 
def test_user_serializer():
    valid_serializer_data = {
        "username": "Rudy",
        "email": "rudy@kittens.net"
    }
    serializer = UserSerializer(data=valid_serializer_data)
    assert serializer.is_valid()
    assert serializer.validated_data == valid_serializer_data
    assert serializer.data == valid_serializer_data
    assert serializer.errors == {}

@pytest.mark.django_db     
def test_valid_event_serializer():
    valid_serializer_data = {
        "name": "Lunch",
        "description": "Lunch al fresco",
        "owner": 1,
        "location": "garden",
        "time": "22:03:27 14:00:00",
        "attendees": [1, 2],    
    }
    serializer = GroupSerializer(data=valid_serializer_data)

    assert serializer.is_valid()
    assert serializer.validated_data == valid_serializer_data
    assert serializer.data == valid_serializer_data
    assert serializer.errors == {}
