from attr import fields
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin

from .models import Group, CustomUser, Event

@admin.register(CustomUser)
class UserAdmin(DefaultUserAdmin):
    pass

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    fields = (
        "name", "description", "owner", "members", "created_at"
    )
    list_display = (
        "name", "description", "owner", "created_at"
    )
    readonly_fields = (
        "created_at",
    )

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    fields = (
        "name", "description", "owner", "group", "attendees", "location", "time", "created_at"
    )
    list_display = (
        "name", "description", "owner", "group", "location", "time", "created_at"
    )
    readonly_fields = (
        "created_at",
    )