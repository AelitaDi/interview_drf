from django.contrib import admin

from forest.models import Tree


@admin.register(Tree)
class TreeAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "owner",
        "type_of_tree",
        "created_at",
    )
