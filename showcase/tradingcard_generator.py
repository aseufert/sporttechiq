import time
import requests

from django.conf import settings
from subprocess import run
from showcase import player_template

from showcase.models import PlayerScorecard, Player
from django.db.models import Avg


def svgGenerator(pk):
    player_data = Player.objects.get(id=pk)
    showcases = PlayerScorecard.objects.filter(player=pk).order_by('-id')
    averages = showcases.aggregate(
        Avg('total_shooting'),
        Avg('total_passing'),
        Avg('total_dribbling'),
        Avg('total_control'),
        Avg('grand_total'),
        )

    if player_data.photo:
        # photos must be written to local directory to be rasterized properly
        r = requests.get(player_data.photo.url)
        local_file = '{}/showcase/static/img/player_photo.png'.format(settings.BASE_DIR)
        open(local_file, 'wb').write(r.content)
        player_photo = local_file
    else:
        player_photo = '{}/showcase/static/img/default_profile.png'.format(settings.BASE_DIR)

    if player_data.team.club.photo:
        # photos must be written to local directory to be rasterized properly
        r = requests.get(player_data.team.club.photo.url)
        local_file = '{}/showcase/static/img/club_photo.png'.format(settings.BASE_DIR)
        open(local_file, 'wb').write(r.content)
        club_photo = local_file
    else:
        club_photo = '{}/showcase/static/img/club.png'.format(settings.BASE_DIR)

    tradingcard_data = {
        'first_name': player_data.first_name,
        'last_name': player_data.last_name[0],
        'birth_year': player_data.birth_year,
        'height': showcases[0].height,
        'country': player_data.country,
        'city': player_data.city,
        'state': player_data.state,
        'club_icon': club_photo,
        'photo': player_photo,
        'no_scorecards': len(showcases),
        'scorecards': [],
        'grass_tile': '{}/showcase/static/img/grass_tile.png'.format(settings.BASE_DIR),
        'avg': {k: int(v) for k, v in averages.items()},
    }
    for showcase in showcases[:5]:
        showcase_date = showcase.showcase_name.showcase_date
        scorecard_data = {
            'month': showcase_date.strftime('%b'),
            'year': showcase_date.strftime('%Y'),
            'shooting': int(showcase.total_shooting),
            'passing': int(showcase.total_passing),
            'dribbling': int(showcase.total_dribbling),
            'control': int(showcase.total_control),
            'skill': int(showcase.grand_total)
        }
        tradingcard_data['scorecards'].append(scorecard_data)

    svg_file = player_template.svg_lines.format(
      second_block=player_template.block_2.format(**tradingcard_data) if tradingcard_data['no_scorecards'] >= 2 else '',
      third_block=player_template.block_3.format(**tradingcard_data) if tradingcard_data['no_scorecards'] >= 3 else '',
      fourth_block=player_template.block_4.format(**tradingcard_data) if tradingcard_data['no_scorecards'] >= 4 else '',
      fifth_block=player_template.block_5.format(**tradingcard_data) if tradingcard_data['no_scorecards'] >= 5 else '',
      **tradingcard_data
    )
    timestamp = int(time.time())
    file_name = '{}_{}_{}.png'.format(tradingcard_data['first_name'], tradingcard_data['last_name'], timestamp)
    file_location = '{}/showcase/static/img/{}'.format(settings.BASE_DIR, file_name)
    local_svg = '{}/showcase/static/img/player.svg'.format(settings.BASE_DIR)
    outF = open(local_svg, 'w', encoding='utf-8')
    outF.write(svg_file)
    outF.close()
    run(['inkscape', '-z', '-f', local_svg, '--export-dpi=110', '-e', file_location])

    return file_location, file_name
