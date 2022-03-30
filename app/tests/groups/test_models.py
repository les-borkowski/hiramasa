import pytest
from django.utils import timezone
from groups.models import Group, CustomUser, Event, Post


@pytest.mark.django_db
def test_group_model():
    # try moving this bit to fixtures - group must be in fixtures too to be in the same db
    user1 = CustomUser(username="Rudy", email="rudy@kittens.com")
    user1.save()
    user2 = CustomUser(username="Lulu", email="lulu@kittens.com")
    user2.save()
    
    group = Group(id=999, name="Kittens", description="", owner=user1)
    group.save()
    group.members.add(user1, user2)
    group.save()
    assert group.name == "Kittens"
    assert group.description == ""
    assert group.owner == user1
    # research testing m2m relationships
    assert group.members.count() == 2
    assert group.created_at
    assert str(group) == group.name

@pytest.mark.django_db 
def test_user_model(mock_data):
    user = mock_data[0][1]
    assert user.username == "Lulu"
    assert user.email == "lulu@kittens.com"

@pytest.mark.django_db
def test_event_model():
    user1 = CustomUser(username="Rudy", email="rudy@kittens.com")
    user1.save()
    group1 = Group(id=999, name="Kittens", description="", owner=user1)
    group1.save()
    group1.members.add(user1)
    group1.save()
    event = Event(
        name="Dinner", 
        description="Food and Fun", 
        owner=user1, 
        location="Garden",
        time=timezone.now(),
        group=group1
        )
    event.save()
    event.attendees.add(user1)
    event.save()
    
    assert event.name == "Dinner"
    assert event.description == "Food and Fun"
    assert event.owner == user1
    assert event.group == group1
    assert event.location == "Garden"
    # research testing m2m relationships
    assert event.attendees.count() == 1
    assert event.created_at
    assert str(event) == event.name
 
@pytest.mark.django_db    
def test_post_model():
    # data setup
    user1 = CustomUser(username="Rudy", email="rudy@kittens.com")
    user1.save()
    group1 = Group(id=999, name="Kittens", description="", owner=user1)
    group1.save()
    group1.members.add(user1)
    group1.save()
    event1 = Event(
        name="Dinner", 
        description="Food and Fun", 
        owner=user1, 
        location="Garden",
        time=timezone.now(),
        group=group1
        )
    event1.save()
    event1.attendees.add(user1)
    event1.save()
    
    post1 = Post(
        title="Test", 
        content="Some text", 
        created_by=user1,
        event=event1
        )
    post1.save()