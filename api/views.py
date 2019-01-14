from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import get_object_or_404, get_list_or_404
from django.http import Http404

from api import serializers
from api import permissions as api_permissions
from showcase.models import (
    Player,
    Club,
    Team,
    Coach,
    Director,
    Showcase,
    PlayerScorecard,
    Station,
    FieldLayout
    )
from users.models import User

class PlayerList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, api_permissions.IsCoachDirectorOrReadOnly)
    serializer_class = serializers.PlayerSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('id', 'first_name', 'last_name', 'birth_year', 'team', 'gender', 'city', 'state', 'region', 'country')

    def get_queryset(self):
        user_type = self.request.user.user_type
        queryset = Player.objects.all()

        if user_type == 2:
            # player
            queryset = Player.objects.filter(user=self.request.user.id)
        elif user_type == 3:
            # coach
            queryset = Player.objects.filter(team__coach__user=self.request.user.id)
        elif user_type == 4:
            # director
            queryset = Player.objects.filter(club__director__user=self.request.user.id)
        elif self.request.user.is_staff:
            queryset = Player.objects.all()

        if queryset.exists():
            return queryset
        else:
            raise Http404


class PlayerDetail(generics.RetrieveUpdateDestroyAPIView):
    # TODO: player, read only. if coach, request.user == coach's team, If Director, request.user == director's club > team
    permission_classes = (IsAuthenticated, api_permissions.IsAppropriateUser)
    queryset = Player.objects.all()
    serializer_class = serializers.PlayerSerializer


class ShowcaseList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, api_permissions.IsAdminOrReadOnly)
    queryset = Showcase.objects.all()
    serializer_class = serializers.ShowcaseSerializer


class ShowcaseDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, api_permissions.IsAdminOrReadOnly)
    queryset = Showcase.objects.all()
    serializer_class = serializers.ShowcaseSerializer


class PlayerScorecardList(generics.ListCreateAPIView):
    # TODO: Add more advanced filtering options. e.g. height__gt=65
    permission_classes = (IsAuthenticated, api_permissions.IsCoachDirectorOrReadOnly)
    serializer_class = serializers.PlayerScorecardSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = (
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

    def get_queryset(self):
        queryset = PlayerScorecard.objects.all().select_related('player').select_related('showcase')
        gender = self.request.query_params.get('gender', None)
        user_type = self.request.user.user_type

        if gender is not None:
            # additional gender filter not included in others
            queryset = queryset.filter(player__gender=gender)

        if user_type == 'Player':
            # player
            queryset = queryset.filter(player=self.request.user.id)
        elif user_type == 'Coach':
            # coach
            queryset = queryset.filter(player__team__coach__user=self.request.user.id)
        elif user_type == 'Director':
            # director
            queryset = queryset.filter(player__club__director__user=self.request.user.id)
        elif self.request.user.is_staff:
            # Admin - no filters applied
            pass
        else:
            # TODO: setup permissions to reject if not player
            pass

        if queryset.exists():
            return queryset
        else:
            raise Http404

class PlayerScorecardDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, api_permissions.IsCoachDirectorOrReadOnly)
    serializer_class = serializers.PlayerScorecardSerializer
    queryset = PlayerScorecard.objects.all()


class TeamList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, api_permissions.IsCoachDirectorOrReadOnly)
    serializer_class = serializers.TeamSerializer

    def get_queryset(self, *args, **kwargs):
        user_type = self.request.user.user_type

        if self.request.user.is_staff:
            # Admin list all
            return Team.objects.all()
        elif user_type == 3:
            # coach list appropriate teams
            return get_list_or_404(Team, coach__user=self.request.user.id)
        elif user_type == 4:
            # director list appropriate teams
            return get_list_or_404(Team, club__director__user=self.request.user.id)


class TeamDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, api_permissions.IsCoachDirectorOrReadOnly)
    queryset = Team.objects.all()
    serializer_class = serializers.TeamSerializer


class ClubList(generics.ListCreateAPIView):
    # Admin see all. Directors only see their own clubs
    serializer_class = serializers.ClubSerializer

    def get_queryset(self, *args, **kwargs):
        if self.request.user.is_staff:
            return Club.objects.all()
        else:
            return get_object_or_404(Club, director=self.request.user.id)


class ClubDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, api_permissions.IsCoachDirectorOrReadOnly)
    queryset = Club.objects.all()
    serializer_class = serializers.ClubSerializer


class CoachList(generics.ListCreateAPIView):
    # TODO: If coach, coach == user. If Director, team.club.director == user
    permission_classes = (IsAuthenticated, api_permissions.IsCoachDirectorOrReadOnly)
    queryset = Coach.objects.all()
    serializer_class = serializers.CoachSerializer


class CoachDetail(generics.RetrieveUpdateDestroyAPIView):
    # TODO: Only allow if coach == user or director == team.club.director
    permission_classes = (IsAuthenticated, api_permissions.IsCoachDirectorOrReadOnly)
    queryset = Coach.objects.all()
    serializer_class = serializers.CoachSerializer


class DirectorDetail(generics.RetrieveUpdateDestroyAPIView):
    # TODO: Only allow if director == user
    permission_classes = (IsAuthenticated, api_permissions.IsDirectorOrAdmin)
    queryset = Director.objects.all()
    serializer_class = serializers.DirectorSerializer


class UserList(generics.ListCreateAPIView):
    # Admin ONLY
    permission_classes = (IsAuthenticated, IsAdminUser)
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    # Admin ONLY
    permission_classes = (IsAuthenticated, IsAdminUser)
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class UserProfile(APIView):
    """
    Retrieve, update or delete a user instance.
    """
    permission_classes = (api_permissions.IsUser,)
    def get_object(self, pk):
        try:
            return User.objects.get(id=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, format=None):
        user = self.get_object(request.user.id)
        serializer = serializers.UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, format=None):
        user = self.get_object(request.user.id)
        serializer = serializers.UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, format=None):
        user = self.get_object(request.user.id)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class StationList(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Station.objects.all().order_by('index')
    serializer_class = serializers.StationSerializer


class FieldLayoutList(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = FieldLayout.objects.all()
    serializer_class = serializers.FieldLayoutSerializer
