from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import Avg
from showcase.models import PlayerScorecard, Team, Club


@receiver(post_save, sender=PlayerScorecard)
def calculateAvgs(sender, signal, instance, **kwargs):
    control_thigh_avg = PlayerScorecard.objects.filter(player__team=instance.player.team).aggregate(Avg('control_thigh'))['control_thigh__avg']
    control_foot_avg = PlayerScorecard.objects.filter(player__team=instance.player.team).aggregate(Avg('control_foot'))['control_foot__avg']
    foot_tap_avg = PlayerScorecard.objects.filter(player__team=instance.player.team).aggregate(Avg('foot_tap'))['foot_tap__avg']
    '''dribbling'''
    speed_dribble_avg = PlayerScorecard.objects.filter(player__team=instance.player.team).aggregate(Avg('speed_dribble'))['speed_dribble__avg']
    dribble_r_avg = PlayerScorecard.objects.filter(player__team=instance.player.team).aggregate(Avg('dribble_r'))['dribble_r__avg']
    dribble_l_avg = PlayerScorecard.objects.filter(player__team=instance.player.team).aggregate(Avg('dribble_l'))['dribble_l__avg']
    dribble_3_cone_avg = PlayerScorecard.objects.filter(player__team=instance.player.team).aggregate(Avg('dribble_3_cone'))['dribble_3_cone__avg']
    '''passing'''
    long_r_1_avg = PlayerScorecard.objects.filter(player__team=instance.player.team).aggregate(Avg('long_r_1'))['long_r_1__avg']
    long_r_2_avg = PlayerScorecard.objects.filter(player__team=instance.player.team).aggregate(Avg('long_r_2'))['long_r_2__avg']
    long_l_1_avg = PlayerScorecard.objects.filter(player__team=instance.player.team).aggregate(Avg('long_l_1'))['long_l_1__avg']
    long_l_2_avg = PlayerScorecard.objects.filter(player__team=instance.player.team).aggregate(Avg('long_l_2'))['long_l_2__avg']
    cross_r_1_avg = PlayerScorecard.objects.filter(player__team=instance.player.team).aggregate(Avg('cross_r_1'))['cross_r_1__avg']
    cross_r_2_avg = PlayerScorecard.objects.filter(player__team=instance.player.team).aggregate(Avg('cross_r_2'))['cross_r_2__avg']
    cross_l_1_avg = PlayerScorecard.objects.filter(player__team=instance.player.team).aggregate(Avg('cross_l_1'))['cross_l_1__avg']
    cross_l_2_avg = PlayerScorecard.objects.filter(player__team=instance.player.team).aggregate(Avg('cross_l_2'))['cross_l_2__avg']
    side_pass_r_1_avg = PlayerScorecard.objects.filter(player__team=instance.player.team).aggregate(Avg('side_pass_r_1'))['side_pass_r_1__avg']
    side_pass_r_2_avg = PlayerScorecard.objects.filter(player__team=instance.player.team).aggregate(Avg('side_pass_r_2'))['side_pass_r_2__avg']
    side_pass_r_3_avg = PlayerScorecard.objects.filter(player__team=instance.player.team).aggregate(Avg('side_pass_r_3'))['side_pass_r_3__avg']
    side_pass_l_1_avg = PlayerScorecard.objects.filter(player__team=instance.player.team).aggregate(Avg('side_pass_l_1'))['side_pass_l_1__avg']
    side_pass_l_2_avg = PlayerScorecard.objects.filter(player__team=instance.player.team).aggregate(Avg('side_pass_l_2'))['side_pass_l_2__avg']
    side_pass_l_3_avg = PlayerScorecard.objects.filter(player__team=instance.player.team).aggregate(Avg('side_pass_l_3'))['side_pass_l_3__avg']
    weigh_pass_r_1_avg = PlayerScorecard.objects.filter(player__team=instance.player.team).aggregate(Avg('weigh_pass_r_1'))['weigh_pass_r_1__avg']
    weigh_pass_r_2_avg = PlayerScorecard.objects.filter(player__team=instance.player.team).aggregate(Avg('weigh_pass_r_2'))['weigh_pass_r_2__avg']
    weigh_pass_r_3_avg = PlayerScorecard.objects.filter(player__team=instance.player.team).aggregate(Avg('weigh_pass_r_3'))['weigh_pass_r_3__avg']
    weigh_pass_l_1_avg = PlayerScorecard.objects.filter(player__team=instance.player.team).aggregate(Avg('weigh_pass_l_1'))['weigh_pass_l_1__avg']
    weigh_pass_l_2_avg = PlayerScorecard.objects.filter(player__team=instance.player.team).aggregate(Avg('weigh_pass_l_2'))['weigh_pass_l_2__avg']
    weigh_pass_l_3_avg = PlayerScorecard.objects.filter(player__team=instance.player.team).aggregate(Avg('weigh_pass_l_3'))['weigh_pass_l_3__avg']
    throw_inside_1_avg = PlayerScorecard.objects.filter(player__team=instance.player.team).aggregate(Avg('throw_inside_1'))['throw_inside_1__avg']
    throw_inside_2_avg = PlayerScorecard.objects.filter(player__team=instance.player.team).aggregate(Avg('throw_inside_2'))['throw_inside_2__avg']
    throw_between_1_avg = PlayerScorecard.objects.filter(player__team=instance.player.team).aggregate(Avg('throw_between_1'))['throw_between_1__avg']
    throw_between_2_avg = PlayerScorecard.objects.filter(player__team=instance.player.team).aggregate(Avg('throw_between_2'))['throw_between_2__avg']
    '''shooting'''
    shoot_pk_avg = PlayerScorecard.objects.filter(player__team=instance.player.team).aggregate(Avg('shoot_pk'))['shoot_pk__avg']
    shoot_run_r_1_avg = PlayerScorecard.objects.filter(player__team=instance.player.team).aggregate(Avg('shoot_run_r_1'))['shoot_run_r_1__avg']
    shoot_run_r_2_avg = PlayerScorecard.objects.filter(player__team=instance.player.team).aggregate(Avg('shoot_run_r_2'))['shoot_run_r_2__avg']
    shoot_run_r_3_avg = PlayerScorecard.objects.filter(player__team=instance.player.team).aggregate(Avg('shoot_run_r_3'))['shoot_run_r_3__avg']
    shoot_run_l_1_avg = PlayerScorecard.objects.filter(player__team=instance.player.team).aggregate(Avg('shoot_run_l_1'))['shoot_run_l_1__avg']
    shoot_run_l_2_avg = PlayerScorecard.objects.filter(player__team=instance.player.team).aggregate(Avg('shoot_run_l_2'))['shoot_run_l_2__avg']
    shoot_run_l_3_avg = PlayerScorecard.objects.filter(player__team=instance.player.team).aggregate(Avg('shoot_run_l_3'))['shoot_run_l_3__avg']
    finisher_r_1_avg = PlayerScorecard.objects.filter(player__team=instance.player.team).aggregate(Avg('finisher_r_1'))['finisher_r_1__avg']
    finisher_r_2_avg = PlayerScorecard.objects.filter(player__team=instance.player.team).aggregate(Avg('finisher_r_2'))['finisher_r_2__avg']
    finisher_r_3_avg = PlayerScorecard.objects.filter(player__team=instance.player.team).aggregate(Avg('finisher_r_3'))['finisher_r_3__avg']
    finisher_l_1_avg = PlayerScorecard.objects.filter(player__team=instance.player.team).aggregate(Avg('finisher_l_1'))['finisher_l_1__avg']
    finisher_l_2_avg = PlayerScorecard.objects.filter(player__team=instance.player.team).aggregate(Avg('finisher_l_2'))['finisher_l_2__avg']
    finisher_l_3_avg = PlayerScorecard.objects.filter(player__team=instance.player.team).aggregate(Avg('finisher_l_3'))['finisher_l_3__avg']
    '''aggregates'''
    total_control_avg = PlayerScorecard.objects.filter(player__team=instance.player.team).aggregate(Avg('total_control'))['total_control__avg']
    total_dribbling_avg = PlayerScorecard.objects.filter(player__team=instance.player.team).aggregate(Avg('total_dribbling'))['total_dribbling__avg']
    total_passing_avg = PlayerScorecard.objects.filter(player__team=instance.player.team).aggregate(Avg('total_passing'))['total_passing__avg']
    total_shooting_avg = PlayerScorecard.objects.filter(player__team=instance.player.team).aggregate(Avg('total_shooting'))['total_shooting__avg']
    grand_total_avg = PlayerScorecard.objects.filter(player__team=instance.player.team).aggregate(Avg('grand_total'))['grand_total__avg']

    # Update fields
    if instance.player.team:
        Team.objects.filter(id=instance.player.team.id).update(
            control_thigh_avg=control_thigh_avg,
            control_foot_avg=control_foot_avg,
            foot_tap_avg=foot_tap_avg,
            speed_dribble_avg=speed_dribble_avg,
            dribble_r_avg=dribble_r_avg,
            dribble_l_avg=dribble_l_avg,
            dribble_3_cone_avg=dribble_3_cone_avg,
            long_r_1_avg=long_r_1_avg,
            long_r_2_avg=long_r_2_avg,
            long_l_1_avg=long_l_1_avg,
            long_l_2_avg=long_l_2_avg,
            cross_r_1_avg=cross_r_1_avg,
            cross_r_2_avg=cross_r_2_avg,
            cross_l_1_avg=cross_l_1_avg,
            cross_l_2_avg=cross_l_2_avg,
            side_pass_r_1_avg=side_pass_r_1_avg,
            side_pass_r_2_avg=side_pass_r_2_avg,
            side_pass_r_3_avg=side_pass_r_3_avg,
            side_pass_l_1_avg=side_pass_l_1_avg,
            side_pass_l_2_avg=side_pass_l_2_avg,
            side_pass_l_3_avg=side_pass_l_3_avg,
            weigh_pass_r_1_avg=weigh_pass_r_1_avg,
            weigh_pass_r_2_avg=weigh_pass_r_2_avg,
            weigh_pass_r_3_avg=weigh_pass_r_3_avg,
            weigh_pass_l_1_avg=weigh_pass_l_1_avg,
            weigh_pass_l_2_avg=weigh_pass_l_2_avg,
            weigh_pass_l_3_avg=weigh_pass_l_3_avg,
            throw_inside_1_avg=throw_inside_1_avg,
            throw_inside_2_avg=throw_inside_2_avg,
            throw_between_1_avg=throw_between_1_avg,
            throw_between_2_avg=throw_between_2_avg,
            shoot_pk_avg=shoot_pk_avg,
            shoot_run_r_1_avg=shoot_run_r_1_avg,
            shoot_run_r_2_avg=shoot_run_r_2_avg,
            shoot_run_r_3_avg=shoot_run_r_3_avg,
            shoot_run_l_1_avg=shoot_run_l_1_avg,
            shoot_run_l_2_avg=shoot_run_l_2_avg,
            shoot_run_l_3_avg=shoot_run_l_3_avg,
            finisher_r_1_avg=finisher_r_1_avg,
            finisher_l_1_avg=finisher_l_1_avg,
            finisher_r_2_avg=finisher_r_2_avg,
            finisher_l_2_avg=finisher_l_2_avg,
            finisher_r_3_avg=finisher_r_3_avg,
            finisher_l_3_avg=finisher_l_3_avg,
            total_control_avg=total_control_avg,
            total_dribbling_avg=total_dribbling_avg,
            total_passing_avg=total_passing_avg,
            total_shooting_avg=total_shooting_avg,
            grand_total_avg=grand_total_avg
        )

    # update club records
    if instance.player.team:
        control_thigh_avg = Team.objects.filter(id=instance.player.team.id).aggregate(Avg('control_thigh_avg'))['control_thigh_avg__avg']
        control_foot_avg = Team.objects.filter(id=instance.player.team.id).aggregate(Avg('control_foot_avg'))['control_foot_avg__avg']
        foot_tap_avg = Team.objects.filter(id=instance.player.team.id).aggregate(Avg('foot_tap_avg'))['foot_tap_avg__avg']
        '''dribbling'''
        speed_dribble_avg = Team.objects.filter(id=instance.player.team.id).aggregate(Avg('speed_dribble_avg'))['speed_dribble_avg__avg']
        dribble_r_avg = Team.objects.filter(id=instance.player.team.id).aggregate(Avg('dribble_r_avg'))['dribble_r_avg__avg']
        dribble_l_avg = Team.objects.filter(id=instance.player.team.id).aggregate(Avg('dribble_l_avg'))['dribble_l_avg__avg']
        dribble_3_cone_avg = Team.objects.filter(id=instance.player.team.id).aggregate(Avg('dribble_3_cone_avg'))['dribble_3_cone_avg__avg']
        '''passing'''
        long_r_1_avg = Team.objects.filter(id=instance.player.team.id).aggregate(Avg('long_r_1_avg'))['long_r_1_avg__avg']
        long_r_2_avg = Team.objects.filter(id=instance.player.team.id).aggregate(Avg('long_r_2_avg'))['long_r_2_avg__avg']
        long_l_1_avg = Team.objects.filter(id=instance.player.team.id).aggregate(Avg('long_l_1_avg'))['long_l_1_avg__avg']
        long_l_2_avg = Team.objects.filter(id=instance.player.team.id).aggregate(Avg('long_l_2_avg'))['long_l_2_avg__avg']
        cross_r_1_avg = Team.objects.filter(id=instance.player.team.id).aggregate(Avg('cross_r_1_avg'))['cross_r_1_avg__avg']
        cross_r_2_avg = Team.objects.filter(id=instance.player.team.id).aggregate(Avg('cross_r_2_avg'))['cross_r_2_avg__avg']
        cross_l_1_avg = Team.objects.filter(id=instance.player.team.id).aggregate(Avg('cross_l_1_avg'))['cross_l_1_avg__avg']
        cross_l_2_avg = Team.objects.filter(id=instance.player.team.id).aggregate(Avg('cross_l_2_avg'))['cross_l_2_avg__avg']
        side_pass_r_1_avg = Team.objects.filter(id=instance.player.team.id).aggregate(Avg('side_pass_r_1_avg'))['side_pass_r_1_avg__avg']
        side_pass_r_2_avg = Team.objects.filter(id=instance.player.team.id).aggregate(Avg('side_pass_r_2_avg'))['side_pass_r_2_avg__avg']
        side_pass_r_3_avg = Team.objects.filter(id=instance.player.team.id).aggregate(Avg('side_pass_r_3_avg'))['side_pass_r_3_avg__avg']
        side_pass_l_1_avg = Team.objects.filter(id=instance.player.team.id).aggregate(Avg('side_pass_l_1_avg'))['side_pass_l_1_avg__avg']
        side_pass_l_2_avg = Team.objects.filter(id=instance.player.team.id).aggregate(Avg('side_pass_l_2_avg'))['side_pass_l_2_avg__avg']
        side_pass_l_3_avg = Team.objects.filter(id=instance.player.team.id).aggregate(Avg('side_pass_l_3_avg'))['side_pass_l_3_avg__avg']
        weigh_pass_r_1_avg = Team.objects.filter(id=instance.player.team.id).aggregate(Avg('weigh_pass_r_1_avg'))['weigh_pass_r_1_avg__avg']
        weigh_pass_r_2_avg = Team.objects.filter(id=instance.player.team.id).aggregate(Avg('weigh_pass_r_2_avg'))['weigh_pass_r_2_avg__avg']
        weigh_pass_r_3_avg = Team.objects.filter(id=instance.player.team.id).aggregate(Avg('weigh_pass_r_3_avg'))['weigh_pass_r_3_avg__avg']
        weigh_pass_l_1_avg = Team.objects.filter(id=instance.player.team.id).aggregate(Avg('weigh_pass_l_1_avg'))['weigh_pass_l_1_avg__avg']
        weigh_pass_l_2_avg = Team.objects.filter(id=instance.player.team.id).aggregate(Avg('weigh_pass_l_2_avg'))['weigh_pass_l_2_avg__avg']
        weigh_pass_l_3_avg = Team.objects.filter(id=instance.player.team.id).aggregate(Avg('weigh_pass_l_3_avg'))['weigh_pass_l_3_avg__avg']
        throw_inside_1_avg = Team.objects.filter(id=instance.player.team.id).aggregate(Avg('throw_inside_1_avg'))['throw_inside_1_avg__avg']
        throw_inside_2_avg = Team.objects.filter(id=instance.player.team.id).aggregate(Avg('throw_inside_2_avg'))['throw_inside_2_avg__avg']
        throw_between_1_avg = Team.objects.filter(id=instance.player.team.id).aggregate(Avg('throw_between_1_avg'))['throw_between_1_avg__avg']
        throw_between_2_avg = Team.objects.filter(id=instance.player.team.id).aggregate(Avg('throw_between_2_avg'))['throw_between_2_avg__avg']
        '''shooting'''
        shoot_pk_avg = Team.objects.filter(id=instance.player.team.id).aggregate(Avg('shoot_pk_avg'))['shoot_pk_avg__avg']
        shoot_run_r_1_avg = Team.objects.filter(id=instance.player.team.id).aggregate(Avg('shoot_run_r_1_avg'))['shoot_run_r_1_avg__avg']
        shoot_run_r_2_avg = Team.objects.filter(id=instance.player.team.id).aggregate(Avg('shoot_run_r_2_avg'))['shoot_run_r_2_avg__avg']
        shoot_run_r_3_avg = Team.objects.filter(id=instance.player.team.id).aggregate(Avg('shoot_run_r_3_avg'))['shoot_run_r_3_avg__avg']
        shoot_run_l_1_avg = Team.objects.filter(id=instance.player.team.id).aggregate(Avg('shoot_run_l_1_avg'))['shoot_run_l_1_avg__avg']
        shoot_run_l_2_avg = Team.objects.filter(id=instance.player.team.id).aggregate(Avg('shoot_run_l_2_avg'))['shoot_run_l_2_avg__avg']
        shoot_run_l_3_avg = Team.objects.filter(id=instance.player.team.id).aggregate(Avg('shoot_run_l_3_avg'))['shoot_run_l_3_avg__avg']
        finisher_r_1_avg = Team.objects.filter(id=instance.player.team.id).aggregate(Avg('finisher_r_1_avg'))['finisher_r_1_avg__avg']
        finisher_r_2_avg = Team.objects.filter(id=instance.player.team.id).aggregate(Avg('finisher_r_2_avg'))['finisher_r_2_avg__avg']
        finisher_r_3_avg = Team.objects.filter(id=instance.player.team.id).aggregate(Avg('finisher_r_3_avg'))['finisher_r_3_avg__avg']
        finisher_l_1_avg = Team.objects.filter(id=instance.player.team.id).aggregate(Avg('finisher_l_1_avg'))['finisher_l_1_avg__avg']
        finisher_l_2_avg = Team.objects.filter(id=instance.player.team.id).aggregate(Avg('finisher_l_2_avg'))['finisher_l_2_avg__avg']
        finisher_l_3_avg = Team.objects.filter(id=instance.player.team.id).aggregate(Avg('finisher_l_3_avg'))['finisher_l_3_avg__avg']
        '''aggregates'''
        total_control_avg = Team.objects.filter(id=instance.player.team.id).aggregate(Avg('total_control_avg'))['total_control_avg__avg']
        total_dribbling_avg = Team.objects.filter(id=instance.player.team.id).aggregate(Avg('total_dribbling_avg'))['total_dribbling_avg__avg']
        total_passing_avg = Team.objects.filter(id=instance.player.team.id).aggregate(Avg('total_passing_avg'))['total_passing_avg__avg']
        total_shooting_avg = Team.objects.filter(id=instance.player.team.id).aggregate(Avg('total_shooting_avg'))['total_shooting_avg__avg']
        grand_total_avg = Team.objects.filter(id=instance.player.team.id).aggregate(Avg('grand_total_avg'))['grand_total_avg__avg']

        if instance.player.team.club:
            Club.objects.filter(id=instance.player.team.club.id).update(
                control_thigh_avg=control_thigh_avg,
                control_foot_avg=control_foot_avg,
                foot_tap_avg=foot_tap_avg,
                speed_dribble_avg=speed_dribble_avg,
                dribble_r_avg=dribble_r_avg,
                dribble_l_avg=dribble_l_avg,
                dribble_3_cone_avg=dribble_3_cone_avg,
                long_r_1_avg=long_r_1_avg,
                long_r_2_avg=long_r_2_avg,
                long_l_1_avg=long_l_1_avg,
                long_l_2_avg=long_l_2_avg,
                cross_r_1_avg=cross_r_1_avg,
                cross_r_2_avg=cross_r_2_avg,
                cross_l_1_avg=cross_l_1_avg,
                cross_l_2_avg=cross_l_2_avg,
                side_pass_r_1_avg=side_pass_r_1_avg,
                side_pass_r_2_avg=side_pass_r_2_avg,
                side_pass_r_3_avg=side_pass_r_3_avg,
                side_pass_l_1_avg=side_pass_l_1_avg,
                side_pass_l_2_avg=side_pass_l_2_avg,
                side_pass_l_3_avg=side_pass_l_3_avg,
                weigh_pass_r_1_avg=weigh_pass_r_1_avg,
                weigh_pass_r_2_avg=weigh_pass_r_2_avg,
                weigh_pass_r_3_avg=weigh_pass_r_3_avg,
                weigh_pass_l_1_avg=weigh_pass_l_1_avg,
                weigh_pass_l_2_avg=weigh_pass_l_2_avg,
                weigh_pass_l_3_avg=weigh_pass_l_3_avg,
                throw_inside_1_avg=throw_inside_1_avg,
                throw_inside_2_avg=throw_inside_2_avg,
                throw_between_1_avg=throw_between_1_avg,
                throw_between_2_avg=throw_between_2_avg,
                shoot_pk_avg=shoot_pk_avg,
                shoot_run_r_1_avg=shoot_run_r_1_avg,
                shoot_run_r_2_avg=shoot_run_r_2_avg,
                shoot_run_r_3_avg=shoot_run_r_3_avg,
                shoot_run_l_1_avg=shoot_run_l_1_avg,
                shoot_run_l_2_avg=shoot_run_l_2_avg,
                shoot_run_l_3_avg=shoot_run_l_3_avg,
                finisher_r_1_avg=finisher_r_1_avg,
                finisher_l_1_avg=finisher_l_1_avg,
                finisher_r_2_avg=finisher_r_2_avg,
                finisher_l_2_avg=finisher_l_2_avg,
                finisher_r_3_avg=finisher_r_3_avg,
                finisher_l_3_avg=finisher_l_3_avg,
                total_control_avg=total_control_avg,
                total_dribbling_avg=total_dribbling_avg,
                total_passing_avg=total_passing_avg,
                total_shooting_avg=total_shooting_avg,
                grand_total_avg=grand_total_avg
            )
