# Anchovy API (DRF)

## TODO

### SETUP
**Initial**
- [x] django
- [x] django rest framework
- [x] postgres
- [x] docker
    - [x] drf dockerfile
    - [x] postgres
    - [] (pgadmin)
- [x] pytest
    - [] fixtures
    - [] refactor tests

### MODELS/SERIALIZERS/TESTS
- [x][x][x] custom user
- [x][x][x] group
    - [x] add related fields (user, events)
    - [x] fix test to show related fields
    - [x] fix serializers tests
    - [x] fix views test
- [][][] event
- [][][] post

- Join tables
- [x] members
- [] event attendees

### AUTH
- [x] setup
    - [] use django auth with drf?

### Endpoints
- [x] group list
    - [x] group detail
- [x] user list
    - [x] user detail
- [] event list
    - [] event detail
- [] event_post list
    - [] event_post detail

### jobs for tomorrow
    - [] add group events
        - [] models
        - [] serializers
        - [] endpoints
    - [] add auth
    - [x] git repo
    - [] add readme file