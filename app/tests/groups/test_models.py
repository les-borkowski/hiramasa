import pytest

from groups.models import Group, CustomUser

@pytest.mark.django_db
def test_group_model():
    # try moving this bit to fixtures
    user1 = CustomUser(username="Rudy", email="rudy@kittens.com")
    user1.save()
    user2 = CustomUser(username="Lulu", email="lulu@kittens.com")
    user2.save()
    
    group = Group(id=999, name="Kittens", description="", owner=user2)
    group.members.add(user2, user1)
    group.save()
    assert group.name == "Kittens"
    assert group.description == ""
    assert group.owner == user2
    # research testing m2m relationships
    assert group.members.count() == 2
    assert group.created_at
    assert str(group) == group.name

@pytest.mark.django_db 
def test_user_model():
    # try moving this bit to fixtures
    user = CustomUser(username="Lulu", email="lulu@kittens.com")
    user.save()
    
    assert user.username == "Lulu"
    assert user.email == "lulu@kittens.com"