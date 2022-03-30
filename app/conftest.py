import os
from django.conf import settings

import pytest
from groups.models import CustomUser, Group

DEFAULT_ENGINE = "django.db.backends.postgresql_psycopg2"

# example how to set up separate db for testing only
# @pytest.fixture(scope="session")
# def django_db_setup():
#     settings.DATABASES["default"] = {
#         "ENGINE": os.environ.get("DB_TEST_ENGINE", DEFAULT_ENGINE),
#         "HOST": os.environ["DB_TEST_HOST"],
#         "NAME": os.environ["DB_TEST_NAME"],
#         "PORT": os.environ["DB_TEST_PORT"],
#         "USER": os.environ["DB_TEST_USER"],
#         "PASSWORD": os.environ["DB_TEST_PASSWORD"],
#     }
   
@pytest.fixture(scope="session")
def mock_data():
    user1 = CustomUser(username="Rudy", email="rudy@kittens.com")
    user2 = CustomUser(username="Lulu", email="lulu@kittens.com")
    
    users = [user1, user2]
   
    test_data = [users]
    return test_data