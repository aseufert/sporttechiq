from django.shortcuts import render, redirect
from django.views import generic
from django.db.models import Avg
from django.contrib import messages

from showcase.models import Player, Club, PlayerScorecard, Showcase
from showcase import tradingcard_generator

from statistics import mean
from subprocess import run


class ScorecardListView(generic.ListView):
    model = Showcase

    def get_context_data(self, **kwargs):
        context = super(ScorecardListView, self).get_context_data(**kwargs)
        context['player_count'] = Player.objects.count()
        context['clubs'] = Club.objects.all().count()
        return context


def ShowcaseDetail(request, pk):
    showcase = Showcase.objects.filter(id=pk)
    player_in_scorecard = PlayerScorecard.objects.filter(showcase_name=pk)

    return render(request, 'showcase/showcase_detail.html', context={
        'showcase': showcase,
        'player_in_scorecard': player_in_scorecard
        })


def PlayerDetail(request, **kwargs):
    player_id = kwargs['pk']
    player = Player.objects.get(id=player_id)

    player_data = PlayerScorecard.objects.filter(player=player.id).order_by('id')
    scorecard = {
        'showcase_name': player_data[0].showcase,
        'height': player_data[0].height,
        'muscle': player_data[0].muscle,
        'body_fat': player_data[0].body_fat,
        'pulse': player_data[0].pulse,
        'oxygen': player_data[0].oxygen,
        'player_number': player_data[0].player_number,
        'pk': int(player_data[0].shoot_pk),
        'on_run_right': int(mean([player_data[0].shoot_run_r_1, player_data[0].shoot_run_r_2, player_data[0].shoot_run_r_3])),
        'on_run_left': int(mean([player_data[0].shoot_run_l_1, player_data[0].shoot_run_l_2, player_data[0].shoot_run_l_3])),
        'finish_r': int(mean([player_data[0].finisher_r_1, player_data[0].finisher_r_2, player_data[0].finisher_r_3])),
        'finish_l': int(mean([player_data[0].finisher_l_1, player_data[0].finisher_l_2, player_data[0].finisher_l_3])),
        'long_r': int(mean([player_data[0].long_r_1, player_data[0].long_r_2])),
        'long_l': int(mean([player_data[0].long_l_1, player_data[0].long_l_2])),
        'cross_r': int(mean([player_data[0].cross_r_1, player_data[0].cross_r_2])),
        'cross_l': int(mean([player_data[0].cross_l_1, player_data[0].cross_l_2])),
        'side_r': int(mean([player_data[0].side_pass_r_1, player_data[0].side_pass_r_2, player_data[0].side_pass_r_3])),
        'side_l': int(mean([player_data[0].side_pass_l_1, player_data[0].side_pass_l_2, player_data[0].side_pass_l_3])),
        'weigh_r': int(mean([player_data[0].weigh_pass_r_1, player_data[0].weigh_pass_r_2, player_data[0].weigh_pass_r_3])),
        'weigh_l': int(mean([player_data[0].weigh_pass_l_1, player_data[0].weigh_pass_l_2, player_data[0].weigh_pass_l_3])),
        'throw_inside': int(mean([player_data[0].throw_inside_1, player_data[0].throw_inside_2])),
        'throw_between': int(mean([player_data[0].throw_between_1, player_data[0].throw_between_2])),
        'speed_dribble': int(player_data[0].speed_dribble),
        'dribble_r': int(player_data[0].dribble_r),
        'dribble_l': int(player_data[0].dribble_l),
        'dribble_3_cone': int(player_data[0].dribble_3_cone),
        'foot': int(player_data[0].control_foot),
        'thigh': int(player_data[0].control_thigh),
        'taps': int(player_data[0].foot_tap),
        'total_control': player_data[0].total_control,
        'total_dribbling': player_data[0].total_dribbling,
        'total_passing': player_data[0].total_passing,
        'total_shooting': player_data[0].total_shooting,
        'grand_total': player_data[0].grand_total
    }
    player_comps = PlayerScorecard.objects.all().aggregate(
        Avg('total_shooting'),
        Avg('total_passing'),
        Avg('total_dribbling'),
        Avg('total_control'),
        Avg('grand_total'),
        )

    return render(request, 'player_detail.html', context={
            'player': player,
            'scorecard': scorecard,
            'showcases': player_data,
            'player_comps': player_comps
        })


# TODO: SET PERMISSION ON THIS TO ADMIN
def GenerateTradingCard(request, **kwargs):
    pk = kwargs['pk']
    prev_link = request.META.get('HTTP_REFERER')
    try:
        player_object = Player.objects.get(id=pk)
        png_file, file_name = tradingcard_generator.svgGenerator(player_object)
        upload_file = open(png_file, 'rb')
        player_object.trading_card.save(file_name, upload_file)
        msg = 'Trading Card Generated for {}'.format(player_object)
        messages.add_message(request, messages.INFO, msg)
        run(['rm', png_file])
    except IndexError:
        msg = 'Player does not currently have any data'
        messages.add_message(request, messages.ERROR, msg)
    except Exception as e:
        msg = e
        messages.add_message(request, messages.ERROR, msg)

    return redirect(prev_link)
