from wagtail.documents.models import Document
from wagtail.images.models import Image

from rest_framework import serializers

from showcase.models import (
    Player,
    Showcase,
    Club,
    Team,
    Coach,
    Director,
    PlayerScorecard,
    Station,
    FieldLayout,
    ScoringCriteria
)
from users.models import User


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = (
            'id',
            'first_name',
            'last_name',
            'user',
            'photo',
            'trading_card',
            'birth_year',
            'team',
            'gender',
            'city',
            'state',
            'region',
            'country'
        )


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'user_type', 'username', 'email')


class CoachSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coach
        fields = ('id', 'first_name', 'last_name', 'user')


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ('id', 'first_name', 'last_name', 'user')


class DocumentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Document
        fields = ('title', 'file')


class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = ('title', 'file')


class ScoringCriteriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScoringCriteria
        fields = '__all__'


class StationSerializer(serializers.ModelSerializer):
    '''
    Station Serializer
    '''
    class Meta:
        model = Station
        depth = 1
        fields = (
            'name',
            'attempts',
            'index',
            'description',
            'scoring_criteria',
            'weight',
            'group',
            'image',
            'diagram',
            'scorecard_diagram',
            'animation',
            'webm_animation'
        )


class ShowcaseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Showcase
        fields = '__all__'


class FieldLayoutSerializer(serializers.ModelSerializer):
    '''
    Field Layout Serializer
    '''
    class Meta:
        model = FieldLayout
        fields = ('id', 'name', 'image', 'diagram')


class PlayerScorecardCreateSerializer(serializers.ModelSerializer):
    '''
    Used to create scorecards via Post requests
    '''
    class Meta:
        model = PlayerScorecard
        fields = '__all__'


class PlayerScorecardSerializer(serializers.ModelSerializer):
    player = PlayerSerializer(read_only=True)
    showcase = ShowcaseSerializer(read_only=True)

    class Meta:
        model = PlayerScorecard
        fields = (
            'id',
            'player',
            'showcase',
            'height',
            'muscle',
            'body_fat',
            'pulse',
            'oxygen',
            'player_number',
            'control_thigh',
            'control_foot',
            'foot_tap',
            'speed_dribble',
            'dribble_r',
            'dribble_l',
            'dribble_3_cone',
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
            'throw_between_2',
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
            'finisher_l_3',
            'total_control',
            'total_dribbling',
            'total_passing',
            'total_shooting',
            'grand_total',
        )


class ClubSerializer(serializers.ModelSerializer):
    '''
    consider making a detail serializer that will allow users to see
    averages etc
    '''
    class Meta:
        model = Club
        fields = (
            'id',
            'club_name',
            'director',
            'photo',
            'registration_code',
        )


class TeamSerializer(serializers.ModelSerializer):
    '''
    consider making a detail serializer that will allow users to see
    averages etc
    '''
    class Meta:
        model = Team
        fields = (
            'id',
            'team_name',
            'coach',
            'city',
            'state',
            'club',
        )
