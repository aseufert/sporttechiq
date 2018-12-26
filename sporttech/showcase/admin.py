from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse

from .models import Player, PlayerScorecard, Showcase, Club, Team, Director, Coach


admin.site.register(Showcase)
admin.site.register(Director)
admin.site.register(Coach)


@admin.register(PlayerScorecard)
class ShowcaseScorecardAdmin(admin.ModelAdmin):
    list_display = ('player', 'showcase')
    list_filter = ('player', 'showcase')

    fieldsets = (
            (None, {
                'fields': ('player', 'showcase')
                }),
            ('Physical Stats', {
                'fields': (
                    'height',
                    'muscle',
                    'body_fat',
                    'pulse',
                    'oxygen',
                    'player_number'
                    )
                }),
            ('Control', {
                'fields' : (
                    'control_thigh',
                    'control_foot',
                    'foot_tap'
                    )
                }),
            ('Dribbling', {
                'fields' : (
                    'speed_dribble',
                    'dribble_r',
                    'dribble_l',
                    'dribble_3_cone'
                    )
                }),
            ('Passing', {
                'fields' : (
                    'long_r_1',
                    'long_r_2',
                    'long_l_1',
                    'long_l_2',
                    'cross_r_1',
                    'cross_r_2',
                    'cross_l_1',
                    'cross_l_2',
                    'side_pass_r_1',
                    'side_pass_r_2',
                    'side_pass_r_3',
                    'side_pass_l_1',
                    'side_pass_l_2',
                    'side_pass_l_3',
                    'weigh_pass_r_1',
                    'weigh_pass_r_2',
                    'weigh_pass_r_3',
                    'weigh_pass_l_1',
                    'weigh_pass_l_2',
                    'weigh_pass_l_3',
                    'throw_inside_1',
                    'throw_inside_2',
                    'throw_between_1',
                    'throw_between_2'
                    )      
                }),
            ('Shooting', {
                'fields' : (
                    'shoot_pk',
                    'shoot_run_r_1',
                    'shoot_run_r_2',
                    'shoot_run_r_3',
                    'shoot_run_l_1',
                    'shoot_run_l_2',
                    'shoot_run_l_3',
                    'finisher_r_1',
                    'finisher_r_2',
                    'finisher_r_3',
                    'finisher_l_1',
                    'finisher_l_2',
                    'finisher_l_3'
                    )
                })
        )


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'team', 'trading_card', 'ScorecardActions')
    list_filter = ('team', 'region', 'country', 'state')
    readonly_fields = ('slug',)

    def ScorecardActions(self, obj):
        return format_html(
                '<a class="button" href="{}">Generate Scorecard</a>',
                reverse('generate_trading_card', kwargs={'pk': obj.pk, 'first': obj.first_name, 'last': obj.last_name})
            )

    ScorecardActions.short_description = 'Trading Card Generator'

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('team_name', 'coach', 'city', 'state')

    exclude = (
        'control_thigh_avg',
        'control_foot_avg',
        'foot_tap_avg',
        'speed_dribble_avg',
        'dribble_r_avg',
        'dribble_l_avg',
        'dribble_3_cone_avg',
        'long_r_1_avg',
        'long_r_2_avg',
        'long_l_1_avg',
        'long_l_2_avg',
        'cross_r_1_avg',
        'cross_r_2_avg',
        'cross_l_1_avg',
        'cross_l_2_avg',
        'side_pass_r_1_avg',
        'side_pass_r_2_avg',
        'side_pass_r_3_avg',
        'side_pass_l_1_avg',
        'side_pass_l_2_avg',
        'side_pass_l_3_avg',
        'weigh_pass_r_1_avg',
        'weigh_pass_r_2_avg',
        'weigh_pass_r_3_avg',
        'weigh_pass_l_1_avg',
        'weigh_pass_l_2_avg',
        'weigh_pass_l_3_avg',
        'throw_inside_1_avg',
        'throw_inside_2_avg',
        'throw_between_1_avg',
        'throw_between_2_avg',
        'shoot_pk_avg',
        'shoot_run_r_1_avg',
        'shoot_run_r_2_avg',
        'shoot_run_r_3_avg',
        'shoot_run_l_1_avg',
        'shoot_run_l_2_avg',
        'shoot_run_l_3_avg',
        'finisher_r_1_avg',
        'finisher_r_2_avg',
        'finisher_r_3_avg',
        'finisher_l_1_avg',
        'finisher_l_2_avg',
        'finisher_l_3_avg',
        'total_control_avg',
        'total_dribbling_avg',
        'total_passing_avg',
        'total_shooting_avg',
        'grand_total_avg'
    )

# admin.site.register(Club)
@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
    list_display = ('club_name', 'registration_code','director')
    readonly_fields = ('registration_code',)
    exclude = (
        'control_thigh_avg',
        'control_foot_avg',
        'foot_tap_avg',
        'speed_dribble_avg',
        'dribble_r_avg',
        'dribble_l_avg',
        'dribble_3_cone_avg',
        'long_r_1_avg',
        'long_r_2_avg',
        'long_l_1_avg',
        'long_l_2_avg',
        'cross_r_1_avg',
        'cross_r_2_avg',
        'cross_l_1_avg',
        'cross_l_2_avg',
        'side_pass_r_1_avg',
        'side_pass_r_2_avg',
        'side_pass_r_3_avg',
        'side_pass_l_1_avg',
        'side_pass_l_2_avg',
        'side_pass_l_3_avg',
        'weigh_pass_r_1_avg',
        'weigh_pass_r_2_avg',
        'weigh_pass_r_3_avg',
        'weigh_pass_l_1_avg',
        'weigh_pass_l_2_avg',
        'weigh_pass_l_3_avg',
        'throw_inside_1_avg',
        'throw_inside_2_avg',
        'throw_between_1_avg',
        'throw_between_2_avg',
        'shoot_pk_avg',
        'shoot_run_r_1_avg',
        'shoot_run_r_2_avg',
        'shoot_run_r_3_avg',
        'shoot_run_l_1_avg',
        'shoot_run_l_2_avg',
        'shoot_run_l_3_avg',
        'finisher_r_1_avg',
        'finisher_r_2_avg',
        'finisher_r_3_avg',
        'finisher_l_1_avg',
        'finisher_l_2_avg',
        'finisher_l_3_avg',
        'total_control_avg',
        'total_dribbling_avg',
        'total_passing_avg',
        'total_shooting_avg',
        'grand_total_avg'
    )

