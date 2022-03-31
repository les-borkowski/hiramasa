import json
import pytest
from django.utils import timezone

from groups.models import Group, CustomUser, Event, Post

# I need to refactor these tests, remove repeated code
@pytest.mark.django_db
def test_add_group(client):
    user1 = CustomUser.objects.create(username="Rudy", email="rudy@kittens.com")
    groups = Group.objects.all()
    assert len(groups) == 0

    resp = client.post(
        "/groups/",
        {
            "name": "Cheddar",
            "description": "cheese",
            "owner": 1,
            "members": [1],
        },
        content_type="application/json"
    )
    assert resp.status_code == 201
    assert resp.data["name"] == "Cheddar"

    groups = Group.objects.all()
    assert len(groups) == 1
    
@pytest.mark.django_db
def test_add_group_invalid_json_keys(client):
    groups = Group.objects.all()
    assert len(groups) == 0

    resp = client.post(
        "/groups/",
        {
            "title": "Cheddar",
            "description": "cheese",
            "owner": 1,
            "members": [1, 2],
        },
        content_type="application/json"
    )
    assert resp.status_code == 400

    groups = Group.objects.all()
    assert len(groups) == 0
    
@pytest.mark.django_db
def test_add_group_invalid_json(client):
    groups = Group.objects.all()
    assert len(groups) == 0

    resp = client.post(
        "/groups/",
        {
        },
        content_type="application/json"
    )
    assert resp.status_code == 400

    groups = Group.objects.all()
    assert len(groups) == 0
    
# Single group view
@pytest.mark.django_db
def test_get_single_group(client):
    user1 = CustomUser.objects.create(username="Rudy", email="rudy@kittens.com")
    
    group = Group.objects.create(name="Pets", description="my animals", owner=user1)
    group.members.add(user1)
    
    resp = client.get(f"/groups/{group.id}/")
    assert resp.status_code == 200
    assert resp.data["name"] == "Pets"


def test_get_single_group_incorrect_id(client):
    resp = client.get(f"/groups/foo/")
    assert resp.status_code == 404

# GROUP views tests

@pytest.mark.django_db    
def test_add_event(client):
    # test setup
    user1 = CustomUser.objects.create(username="Rudy", email="rudy@kittens.com")
    group1 = Group.objects.create(name="Pets", description="my animals", owner=user1)
    group1.members.add(user1)
    
    events = Event.objects.all()
    assert len(events) == 0
    # created_time = timezone.now()
    
    resp = client.post(
        "/events/",
        {
            "name": "Dinner",
            "description": "Food",
            "owner": 1,
            "group": 1,
            "location": "Pub",
            "time": timezone.now(),
            "attendees": [1],    
        },
        content_type="application/json"
    )
    assert resp.status_code == 201
    assert resp.data["name"] == "Dinner"

    events = Event.objects.all()
    assert len(events) == 1
    
@pytest.mark.django_db
def test_add_event_ivalid_json_keys(client):
    # test setup
    user1 = CustomUser.objects.create(username="Rudy", email="rudy@kittens.com")
    group = Group.objects.create(name="Pets", description="my animals", owner=user1)
    group.members.add(user1)
    
    events = Event.objects.all()
    assert len(events) == 0
    # created_time = timezone.now()
    
    resp = client.post(
        "/events/",
        {
            "random key": "Dinner",
            "description": "Food",
            "owner": 1,
            "location": "Pub",
            "time": timezone.now(),
        },
        content_type="application/json"
    )
    assert resp.status_code == 400

    groups = Event.objects.all()
    assert len(groups) == 0
    
@pytest.mark.django_db
def test_add_event_ivalid_json(client):
    # test setup
    user1 = CustomUser.objects.create(username="Rudy", email="rudy@kittens.com")
    group = Group.objects.create(name="Pets", description="my animals", owner=user1)
    group.members.add(user1)
    
    events = Event.objects.all()
    assert len(events) == 0
    # created_time = timezone.now()
    
    resp = client.post(
        "/events/",
        {
        },
        content_type="application/json"
    )
    assert resp.status_code == 400

    groups = Event.objects.all()
    assert len(groups) == 0
    
# Single event view
@pytest.mark.django_db
def test_get_single_event(client):
    user1 = CustomUser.objects.create(username="Rudy", email="rudy@kittens.com")
    
    group1 = Group.objects.create(name="Pets", description="my animals", owner=user1)
    group1.members.add(user1)
    
    event1 = Event.objects.create(
        name="Party", 
        description="Kittys party", 
        owner=user1, 
        group=group1,
        location="Garden",
        )
    event1.attendees.add(user1)
    
    resp = client.get(f"/events/{event1.id}/")
    assert resp.status_code == 200
    assert resp.data["name"] == "Party"


def test_get_single_group_incorrect_id(client):
    resp = client.get(f"/events/foo/")
    assert resp.status_code == 404
 
# POST views tests
    
@pytest.mark.django_db    
def test_add_post(client):
    # test setup
    user1 = CustomUser.objects.create(username="Rudy", email="rudy@kittens.com")
    group1 = Group.objects.create(name="Pets", description="my animals", owner=user1)
    group1.members.add(user1)
    event1 = Event.objects.create(
        name="Dinner", 
        description="test test test", 
        owner=user1, 
        group=group1, 
        location="Here",
        time=timezone.now()
        )
    event1.attendees.add(user1)
    
    posts = Post.objects.all()
    assert len(posts) == 0
    
    resp = client.post(
        "/posts/",
        {
            "title": "test",
            "content": "test test test",
            "created_by": 1,
            "event": 1,    
        },
        content_type="application/json"
    )
    assert resp.status_code == 201
    assert resp.data["title"] == "test"

    posts = Post.objects.all()
    assert len(posts) == 1
    
@pytest.mark.django_db    
def test_add_post_invalid_json_keys(client):
    # test setup
    user1 = CustomUser.objects.create(username="Rudy", email="rudy@kittens.com")
    group1 = Group.objects.create(name="Pets", description="my animals", owner=user1)
    group1.members.add(user1)
    event1 = Event.objects.create(
        name="Dinner", 
        description="test test test", 
        owner=user1, 
        group=group1, 
        location="Here",
        time=timezone.now()
        )
    event1.attendees.add(user1)
    
    posts = Post.objects.all()
    assert len(posts) == 0
    
    resp = client.post(
        "/posts/",
        {
            "name": "test",
            "content": "test test test",
            "created_by": 1,
            "event": 1,    
        },
        content_type="application/json"
    )
    assert resp.status_code == 400

    posts = Post.objects.all()
    assert len(posts) == 0

@pytest.mark.django_db    
def test_add_post_invalid_json(client):
    # test setup
    user1 = CustomUser.objects.create(username="Rudy", email="rudy@kittens.com")
    group1 = Group.objects.create(name="Pets", description="my animals", owner=user1)
    group1.members.add(user1)
    event1 = Event.objects.create(
        name="Dinner", 
        description="test test test", 
        owner=user1, 
        group=group1, 
        location="Here",
        time=timezone.now()
        )
    event1.attendees.add(user1)
    
    posts = Post.objects.all()
    assert len(posts) == 0
    
    resp = client.post(
        "/posts/",
        {   
        },
        content_type="application/json"
    )
    assert resp.status_code == 400

    posts = Post.objects.all()
    assert len(posts) == 0