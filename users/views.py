from django.shortcuts import render, redirect, reverse
from django.db.models import Avg
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required

from showcase.models import Player, Team, PlayerScorecard, Club, Coach
from .forms import SignUpForm, RegistrationForm

from statistics import mean


def AccountProfile(request):
    profile_type = request.user.user_type
    if profile_type == 'Unregistered':
        # return render(request, 'signup.html')
        return redirect('/?account_type=unregistered')
    elif profile_type == 'Player':
        return redirect('player_profile')
    elif profile_type == 'Coach':
        return redirect('coach_profile')
    elif profile_type == 'Director':
        return redirect('/?account_type=agent')
    elif profile_type == 'Agent':
        return redirect('/?account_type=agent')
    elif profile_type == 'Referee':
        return redirect('/?account_type=referee')


def PlayerProfile(request):
    user_id = request.user.pk
    if Player.objects.filter(user=user_id).exists() or request.user.user_type != 2:
        player = Player.objects.get(user=user_id)
        return redirect(reverse('player_detail', kwargs={
                'pk': player.id,
                'slug': player.slug
            }))
    else:
        return redirect('/?message=player has no data')


def CoachProfile(request):
    if Coach.objects.filter(user=request.user.pk).exists():
        coach_data = Coach.objects.get(user=request.user.pk)
        team_data = Team.objects.get(coach=coach_data.id)
        team_averages = {
            'name': team_data,
            'city': team_data.city,
            'pk': int(team_data.shoot_pk_avg * 100),
            'on_run_right': int(mean([team_data.shoot_run_r_1_avg, team_data.shoot_run_r_2_avg, team_data.shoot_run_r_3_avg]) * 100),
            'on_run_left': int(mean([team_data.shoot_run_l_1_avg, team_data.shoot_run_l_2_avg, team_data.shoot_run_l_3_avg]) * 100),
            'finish_r': int(mean([team_data.finisher_r_1_avg, team_data.finisher_r_2_avg, team_data.finisher_r_3_avg]) * 100),
            'finish_l': int(mean([team_data.finisher_l_1_avg, team_data.finisher_l_2_avg, team_data.finisher_l_3_avg]) * 100),
            'long_r': int(mean([team_data.long_r_1_avg, team_data.long_r_2_avg]) * 100),
            'long_l': int(mean([team_data.long_l_1_avg, team_data.long_l_2_avg]) * 100),
            'cross_r': int(mean([team_data.cross_r_1_avg, team_data.cross_r_2_avg]) * 100),
            'cross_l': int(mean([team_data.cross_l_1_avg, team_data.cross_l_2_avg]) * 100),
            'side_r': int(mean([team_data.side_pass_r_1_avg, team_data.side_pass_r_2_avg, team_data.side_pass_r_3_avg]) * 100),
            'side_l': int(mean([team_data.side_pass_l_1_avg, team_data.side_pass_l_2_avg, team_data.side_pass_l_3_avg]) * 100),
            'weigh_r': int(mean([team_data.weigh_pass_r_1_avg, team_data.weigh_pass_r_2_avg, team_data.weigh_pass_r_3_avg]) * 100),
            'weigh_l': int(mean([team_data.weigh_pass_l_1_avg, team_data.weigh_pass_l_2_avg, team_data.weigh_pass_l_3_avg]) * 100),
            'throw_inside': int(mean([team_data.throw_inside_1_avg, team_data.throw_inside_2_avg]) * 100),
            'throw_between': int(mean([team_data.throw_between_1_avg, team_data.throw_between_2_avg]) * 100),
            'speed_dribble': int(team_data.speed_dribble_avg * 100),
            'dribble_r': int(team_data.dribble_r_avg * 100),
            'dribble_l': int(team_data.dribble_l_avg * 100),
            'dribble_3_cone': int(team_data.dribble_3_cone_avg * 100),
            'foot': int(team_data.control_foot_avg * 100),
            'thigh': int(team_data.control_thigh_avg * 100),
            'taps': int(team_data.foot_tap_avg * 100),
            'total_control': int(team_data.total_control_avg),
            'total_dribbling': int(team_data.total_dribbling_avg),
            'total_passing': int(team_data.total_passing_avg),
            'total_shooting': int(team_data.total_shooting_avg),
            'grand_total': int(team_data.grand_total_avg)
        }
        club_averages = {
            'name': team_data.club,
            'pk': int(team_data.club.shoot_pk_avg * 100),
            'on_run_right': int(mean([team_data.club.shoot_run_r_1_avg, team_data.club.shoot_run_r_2_avg, team_data.club.shoot_run_r_3_avg]) * 100),
            'on_run_left': int(mean([team_data.club.shoot_run_l_1_avg, team_data.club.shoot_run_l_2_avg, team_data.club.shoot_run_l_3_avg]) * 100),
            'finish_r': int(mean([team_data.club.finisher_r_1_avg, team_data.club.finisher_r_2_avg, team_data.club.finisher_r_3_avg]) * 100),
            'finish_l': int(mean([team_data.club.finisher_l_1_avg, team_data.club.finisher_l_2_avg, team_data.club.finisher_l_3_avg]) * 100),
            'long_r': int(mean([team_data.club.long_r_1_avg, team_data.club.long_r_2_avg]) * 100),
            'long_l': int(mean([team_data.club.long_l_1_avg, team_data.club.long_l_2_avg]) * 100),
            'cross_r': int(mean([team_data.club.cross_r_1_avg, team_data.club.cross_r_2_avg]) * 100),
            'cross_l': int(mean([team_data.club.cross_l_1_avg, team_data.club.cross_l_2_avg]) * 100),
            'side_r': int(mean([team_data.club.side_pass_r_1_avg, team_data.club.side_pass_r_2_avg, team_data.club.side_pass_r_3_avg]) * 100),
            'side_l': int(mean([team_data.club.side_pass_l_1_avg, team_data.club.side_pass_l_2_avg, team_data.club.side_pass_l_3_avg]) * 100),
            'weigh_r': int(mean([team_data.club.weigh_pass_r_1_avg, team_data.club.weigh_pass_r_2_avg, team_data.club.weigh_pass_r_3_avg]) * 100),
            'weigh_l': int(mean([team_data.club.weigh_pass_l_1_avg, team_data.club.weigh_pass_l_2_avg, team_data.club.weigh_pass_l_3_avg]) * 100),
            'throw_inside': int(mean([team_data.club.throw_inside_1_avg, team_data.club.throw_inside_2_avg]) * 100),
            'throw_between': int(mean([team_data.club.throw_between_1_avg, team_data.club.throw_between_2_avg]) * 100),
            'speed_dribble': int(team_data.club.speed_dribble_avg * 100),
            'dribble_r': int(team_data.club.dribble_r_avg * 100),
            'dribble_l': int(team_data.club.dribble_l_avg * 100),
            'dribble_3_cone': int(team_data.club.dribble_3_cone_avg * 100),
            'foot': int(team_data.club.control_foot_avg * 100),
            'thigh': int(team_data.club.control_thigh_avg * 100),
            'taps': int(team_data.club.foot_tap_avg * 100),
            'total_control': int(team_data.club.total_control_avg),
            'total_dribbling': int(team_data.club.total_dribbling_avg),
            'total_passing': int(team_data.club.total_passing_avg),
            'total_shooting': int(team_data.club.total_shooting_avg),
            'grand_total': int(team_data.club.grand_total_avg)
        }

        player_info = PlayerScorecard.objects.filter(player__team=team_data)
        player_count = Player.objects.filter(team=team_data).count()
        showcase_info = PlayerScorecard.objects.values('showcase', 'showcase__showcase_name', 'showcase__showcase_date').annotate(
            average_shooting=Avg('total_shooting'),
            average_passing=Avg('total_passing'),
            average_dribbling=Avg('total_dribbling'),
            average_control=Avg('total_control'),
            average_total=Avg('grand_total')
            )

        return render(request, 'profiles/coach_profile.html', context={
            'players': player_info,
            'team': team_averages,
            'club': club_averages,
            'count': player_count,
            'showcase_info': showcase_info
            })
    else:
        return redirect('/')


def Signup(request):
    if request.method =='POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)

            form_user_type = form.cleaned_data['user_type']

            if form_user_type == '2':
                return redirect('player_registration')
            else:
                return redirect('/?type={}'.format(form_user_type)) # query string is just a test
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


@login_required()
def Registration(request):
    '''
    ADD: user must be logged in because I'll likely snag request.user data
    '''

    if request.method =='POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            code = form.cleaned_data['registration_code']
            instance = form.save(commit=False)
            instance.user = request.user
            instance.club = Club.objects.get(registration_code=code)
            instance.save()

            return redirect('/')

    else:
        form = RegistrationForm()

    return render(request, 'registration.html', {'form': form})