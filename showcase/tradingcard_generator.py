import os
import time
import requests
import base64
import bs4
import datetime
from subprocess import run

from django.conf import settings
from django.db.models import Avg

from showcase.models import PlayerScorecard

file_read = os.path.join(settings.BASE_DIR, 'player.svg')
file_write = os.path.join(settings.BASE_DIR, 'player_latest.svg')


def getImageBase64(link):
    '''
    Given link to photo, returns base64 encoded bytes
    for injecting into inkscape SVG image tags
    '''
    r = requests.get(link, stream=True, timeout=3)
    photo = b''
    for chunk in r:
        photo += chunk
    base64_photo = base64.b64encode(photo)
    return 'data:image/png;base64,{}'.format(base64_photo.decode('ascii'))


def svgGenerator(player_data):
    player_name = '{} {}'.format(player_data.first_name, player_data.last_name[0])
    scorecards = PlayerScorecard.objects.filter(player=player_data.id).order_by('-id')
    averages = scorecards.aggregate(
        Avg('total_shooting'),
        Avg('total_passing'),
        Avg('total_dribbling'),
        Avg('total_control'),
        Avg('grand_total'),
        )

    with open(file_read, 'r') as f:
        with open(file_write, 'w') as w:
            svg_read = f.read()
            soup = bs4.BeautifulSoup(svg_read, 'xml')
            f.close()

            if player_data.photo:
                soup.find(id='player_headshot').attrs['xlink:href'] = getImageBase64(player_data.photo.url)

            for scorecard in scorecards:
                print(scorecard.showcase.showcase_date)
                print(scorecard.total_shooting)

            soup.find(id='skill_iq_latest').string = '{:.0f}'.format(averages['grand_total__avg'])
            soup.find(id='player_name').string = player_name
            soup.find(id='player_birth_year').string = '{}'.format(player_data.birth_year)
            soup.find(id='player_gender').string = player_data.gender
            soup.find(id='player_nation').string = player_data.country
            soup.find(id='player_city').string = player_data.city

            soup.find(id='ch1_month').string = scorecards[4].showcase.showcase_date.strftime('%b')
            soup.find(id='ch1_year').string = scorecards[4].showcase.showcase_date.strftime('%Y')
            soup.find(id='ch2_month').string = scorecards[3].showcase.showcase_date.strftime('%b')
            soup.find(id='ch2_year').string = scorecards[3].showcase.showcase_date.strftime('%Y')
            soup.find(id='ch3_month').string = scorecards[2].showcase.showcase_date.strftime('%b')
            soup.find(id='ch3_year').string = scorecards[2].showcase.showcase_date.strftime('%Y')
            soup.find(id='ch4_month').string = scorecards[1].showcase.showcase_date.strftime('%b')
            soup.find(id='ch4_year').string = scorecards[1].showcase.showcase_date.strftime('%Y')
            soup.find(id='ch5_month').string = scorecards[0].showcase.showcase_date.strftime('%b')
            soup.find(id='ch5_year').string = scorecards[0].showcase.showcase_date.strftime('%Y')

            soup.find(id='ch1_shooting_iq').string = '{:.0f}'.format(scorecards[4].total_shooting)
            soup.find(id='ch2_shooting_iq').string = '{:.0f}'.format(scorecards[3].total_shooting)
            soup.find(id='ch3_shooting_iq').string = '{:.0f}'.format(scorecards[2].total_shooting)
            soup.find(id='ch4_shooting_iq').string = '{:.0f}'.format(scorecards[1].total_shooting)
            soup.find(id='ch5_shooting_iq').string = '{:.0f}'.format(scorecards[0].total_shooting)
            soup.find(id='avg_shooting_iq').string = '{:.0f}'.format(averages['total_shooting__avg'])

            soup.find(id='ch1_passing_iq').string = '{:.0f}'.format(scorecards[4].total_passing)
            soup.find(id='ch2_passing_iq').string = '{:.0f}'.format(scorecards[3].total_passing)
            soup.find(id='ch3_passing_iq').string = '{:.0f}'.format(scorecards[2].total_passing)
            soup.find(id='ch4_passing_iq').string = '{:.0f}'.format(scorecards[1].total_passing)
            soup.find(id='ch5_passing_iq').string = '{:.0f}'.format(scorecards[0].total_passing)
            soup.find(id='avg_passing_iq').string = '{:.0f}'.format(averages['total_passing__avg'])

            soup.find(id='ch1_dribbling_iq').string = '{:.0f}'.format(scorecards[4].total_dribbling)
            soup.find(id='ch2_dribbling_iq').string = '{:.0f}'.format(scorecards[3].total_dribbling)
            soup.find(id='ch3_dribbling_iq').string = '{:.0f}'.format(scorecards[2].total_dribbling)
            soup.find(id='ch4_dribbling_iq').string = '{:.0f}'.format(scorecards[1].total_dribbling)
            soup.find(id='ch5_dribbling_iq').string = '{:.0f}'.format(scorecards[0].total_dribbling)
            soup.find(id='avg_dribbling_iq').string = '{:.0f}'.format(averages['total_dribbling__avg'])

            soup.find(id='ch1_control_iq').string = '{:.0f}'.format(scorecards[4].total_control)
            soup.find(id='ch2_control_iq').string = '{:.0f}'.format(scorecards[3].total_control)
            soup.find(id='ch3_control_iq').string = '{:.0f}'.format(scorecards[2].total_control)
            soup.find(id='ch4_control_iq').string = '{:.0f}'.format(scorecards[1].total_control)
            soup.find(id='ch5_control_iq').string = '{:.0f}'.format(scorecards[0].total_control)
            soup.find(id='avg_control_iq').string = '{:.0f}'.format(averages['total_control__avg'])

            soup.find(id='ch1_skill_iq').string = '{:.0f}'.format(scorecards[4].grand_total)
            soup.find(id='ch2_skill_iq').string = '{:.0f}'.format(scorecards[3].grand_total)
            soup.find(id='ch3_skill_iq').string = '{:.0f}'.format(scorecards[2].grand_total)
            soup.find(id='ch4_skill_iq').string = '{:.0f}'.format(scorecards[1].grand_total)
            soup.find(id='ch5_skill_iq').string = '{:.0f}'.format(scorecards[0].grand_total)
            soup.find(id='avg_skill_iq').string = '{:.0f}'.format(averages['grand_total__avg'])

            now = datetime.datetime.now()
            soup.find(id='copyright_year').string = str(now.year)

            w.write(str(soup))
            w.close()

    timestamp = int(time.time())
    png_file = '{}_{}_{}.png'.format(player_data.first_name, player_data.last_name, timestamp)
    file_location = os.path.join(settings.BASE_DIR, png_file)
    run(['inkscape', '-z', '-f', file_write, '--export-dpi=190', '-e', file_location])

    return file_location, png_file
