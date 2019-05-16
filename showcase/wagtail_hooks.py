from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register)
from .models import Player, Station, FieldLayout


class PlayerModelAdmin(ModelAdmin):
    model = Player
