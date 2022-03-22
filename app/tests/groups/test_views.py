import json
import pytest

from groups.models import Group, CustomUser

# why is this test not working -- user needs to be created before it can be added to the group
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


def test_get_single_movie_incorrect_id(client):
    resp = client.get(f"/groups/foo/")
    assert resp.status_code == 404