from django.contrib import admin
from . import models


@admin.register(models.Version)
class VersionAdmin(admin.ModelAdmin):
    list_display  = ("v_number", "v_title",)
    list_filter   = ("v_number", "v_title",)
    search_fields = ("v_number", "v_title",)


# @admin.register(models.Music)
# class MusicAdmin(admin.ModelAdmin):
#     list_display  = ("v_number", "v_title",)
#     list_filter   = ("v_number", "v_title",)
#     search_fields = ("v_number", "v_title",)

admin.site.register(models.Music)
# admin.site.register(Version)
