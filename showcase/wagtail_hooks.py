from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register)
from .models import Player, Station, FieldLayout


class PlayerModelAdmin(ModelAdmin):
    model = Player

    # menu_label = 'Page Model'  # ditch this to use verbose_name_plural from model
    # menu_icon = 'date'  # change as required
    # menu_order = 200  # will put in 3rd place (000 being 1st, 100 2nd)
    # add_to_settings_menu = False  # or True to add your model to the Settings sub-menu
    # exclude_from_explorer = False # or True to exclude pages of this type from Wagtail's explorer view
    # list_display = ('title', 'example_field2', 'example_field3', 'live')
    # list_filter = ('live', 'example_field2', 'example_field3')
    # search_fields = ('title',)


# class StationModelAdmin(ModelAdmin):
#     model = Station


# class FieldLayoutModelAdmin(ModelAdmin):
#     model = FieldLayout


# Uncommented to show in Wagtail admin. No foreign relations
# makes it less than ideal for data entry. Need to figure out way

# modeladmin_register(PlayerModelAdmin)
# modeladmin_register(StationModelAdmin)
# modeladmin_register(FieldLayoutModelAdmin)