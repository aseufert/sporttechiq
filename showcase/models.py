import uuid
from math import ceil

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import ArrayField

from users.models import User
from showcase import file_size_validator
import showcase.dropdowns as choices


class Player(models.Model):
    first_name = models.CharField(max_length=100, help_text='First Name')
    last_name = models.CharField(max_length=100, help_text='Last Name')
    player_number = models.SmallIntegerField(null=True, default=None)
    slug = models.SlugField(unique=True, max_length=255)
    user = models.OneToOneField(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        help_text='If you add a new user here, be sure to fill in email field.'
    )
    photo = models.ImageField(
        upload_to='players',
        null=True,
        blank=True,
        validators=[file_size_validator.file_size]
    )
    trading_card = models.ImageField(
        upload_to='cards',
        null=True,
        blank=True,
        help_text='Autogenerated. Do not load file unless necessary.'
    )
    birth_year = models.SmallIntegerField(choices=choices.years, null=True, blank=True)
    team = models.ForeignKey('Team', on_delete=models.CASCADE, null=True, blank=True)
    gender = models.CharField(max_length=1, choices=choices.genders)
    city = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(
        max_length=3,
        null=True,
        blank=True,
        choices=choices.states
    )
    region = models.CharField(
        max_length=10, null=True, blank=True, choices=choices.regions
    )
    country = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        choices=choices.countries
    )

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def get_unique_slug(self):
        slug = '{}-{}'.format(self.first_name, self.last_name).lower()
        unique_slug = slug
        num = 1
        while Player.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1

        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.get_unique_slug()

        super(Player, self).save(*args, **kwargs)


class Coach(models.Model):
    first_name = models.CharField(max_length=100, help_text='First Name')
    last_name = models.CharField(max_length=100, help_text='Last Name')
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)

    class Meta:
        verbose_name_plural = 'Coaches'


class Director(models.Model):
    first_name = models.CharField(max_length=100, help_text='First Name')
    last_name = models.CharField(max_length=100, help_text='Last Name')
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)


class PlayerScorecard(models.Model):
    '''
    model for inserting scorecard data from showcase
    '''
    five_star = ((1.0, '5 Star'), (0.75, '4 Star'), (0.5, '3 Star'), (0.25, '2 Star'), (0, '1 Star'))
    two_star = ((1.0, '5 Star'), (0, '1 Star'))

    player = models.ForeignKey(Player, related_name='player', on_delete=models.SET_NULL, null=True)
    showcase = models.ForeignKey('Showcase', on_delete=models.SET_NULL, null=True)
    height = models.SmallIntegerField(null=True, default=None, verbose_name='Height in inches')
    muscle = models.SmallIntegerField(null=True, default=None, verbose_name='Muscle Percentage')
    body_fat = models.SmallIntegerField(null=True, default=None, verbose_name='Body Fat Percentage')
    pulse = models.SmallIntegerField(null=True, default=None)
    oxygen = models.SmallIntegerField(null=True, default=None)
    '''control'''
    control_thigh = models.FloatField(choices=five_star, help_text='Select an option. Weight: 33.33', default=0.0, verbose_name='Thigh Control')
    control_foot = models.FloatField(choices=five_star, help_text='Select an option. Weight: 33.33', default=0.0, verbose_name='Foot Control')
    foot_tap = models.FloatField(choices=five_star, help_text='Select an option. Weight: 33.33', default=0.0, verbose_name='Taps')
    '''dribbling'''
    speed_dribble = models.FloatField(choices=five_star, help_text='Select an option. Weight: 25', default=0.0, verbose_name='Speed Dribble')
    dribble_r = models.FloatField(choices=five_star, help_text='Select an option. Weight: 25', default=0.0, verbose_name='Dribble Right Foot')
    dribble_l = models.FloatField(choices=five_star, help_text='Select an option. Weight: 25', default=0.0, verbose_name='Dribble Left Foot')
    dribble_3_cone = models.FloatField(choices=five_star, help_text='Select an option. Weight: 25', default=0.0, verbose_name='Dribble 3-Cone')
    '''passing'''
    long_r_1 = models.FloatField(choices=two_star, help_text='Select an option. Weight: 4.5', default=0.0, verbose_name='Long Pass Right Foot 1')
    long_r_2 = models.FloatField(choices=two_star, help_text='Select an option. Weight: 4.5', default=0.0, verbose_name='Long Pass Right Foot 2')
    long_l_1 = models.FloatField(choices=two_star, help_text='Select an option. Weight: 4.5', default=0.0, verbose_name='Long Pass Left Foot 1')
    long_l_2 = models.FloatField(choices=two_star, help_text='Select an option. Weight: 4.5', default=0.0, verbose_name='Long Pass Left Foot 2')
    cross_r_1 = models.FloatField(choices=two_star, help_text='Select an option. Weight: 4.5', default=0.0, verbose_name='Cross Right 1')
    cross_r_2 = models.FloatField(choices=two_star, help_text='Select an option. Weight: 4.5', default=0.0, verbose_name='Cross Right 2')
    cross_l_1 = models.FloatField(choices=two_star, help_text='Select an option. Weight: 4.5', default=0.0, verbose_name='Cross Left 1')
    cross_l_2 = models.FloatField(choices=two_star, help_text='Select an option. Weight: 4.5', default=0.0, verbose_name='Cross Left 2')
    side_pass_r_1 = models.FloatField(choices=two_star, help_text='Select an option. Weight: 4.5', default=0.0, verbose_name='Side Pass Right 1')
    side_pass_r_2 = models.FloatField(choices=two_star, help_text='Select an option. Weight: 4.5', default=0.0, verbose_name='Side Pass Right 2')
    side_pass_r_3 = models.FloatField(choices=two_star, help_text='Select an option. Weight: 4.5', default=0.0, verbose_name='Side Pass Right 3')
    side_pass_l_1 = models.FloatField(choices=two_star, help_text='Select an option. Weight: 4.5', default=0.0, verbose_name='Side Pass Left 1')
    side_pass_l_2 = models.FloatField(choices=two_star, help_text='Select an option. Weight: 4.5', default=0.0, verbose_name='Side Pass Left 2')
    side_pass_l_3 = models.FloatField(choices=two_star, help_text='Select an option. Weight: 4.5', default=0.0, verbose_name='Side Pass Left 3')
    weigh_pass_r_1 = models.FloatField(choices=two_star, help_text='Select an option. Weight: 4.5', default=0.0, verbose_name='Weighted Pass Right 1')
    weigh_pass_r_2 = models.FloatField(choices=two_star, help_text='Select an option. Weight: 4.5', default=0.0, verbose_name='Weighted Pass Right 2')
    weigh_pass_r_3 = models.FloatField(choices=two_star, help_text='Select an option. Weight: 4.5', default=0.0, verbose_name='Weighted Pass Right 3')
    weigh_pass_l_1 = models.FloatField(choices=two_star, help_text='Select an option. Weight: 4.5', default=0.0, verbose_name='Weighted Pass Left 1')
    weigh_pass_l_2 = models.FloatField(choices=two_star, help_text='Select an option. Weight: 4.5', default=0.0, verbose_name='Weighted Pass Left 2')
    weigh_pass_l_3 = models.FloatField(choices=two_star, help_text='Select an option. Weight: 4.5', default=0.0, verbose_name='Weighted Pass Left 3')
    throw_inside_1 = models.FloatField(choices=two_star, help_text='Select an option. Weight: 2.5', default=0.0, verbose_name='Throw Inside Box 1')
    throw_inside_2 = models.FloatField(choices=two_star, help_text='Select an option. Weight: 2.5', default=0.0, verbose_name='Throw Inside Box 2')
    throw_between_1 = models.FloatField(choices=two_star, help_text='Select an option. Weight: 2.5', default=0.0, verbose_name='Throw-in between far cones 1')
    throw_between_2 = models.FloatField(choices=two_star, help_text='Select an option. Weight: 2.5', default=0.0, verbose_name='Throw-in between far cones 2')
    '''shooting'''
    shoot_pk = models.FloatField(choices=two_star, help_text='Select an option. Weight: 10.0', default=0.0, verbose_name='Penalty Kick')
    shoot_run_r_1 = models.FloatField(choices=two_star, help_text='Select an option. Weight: 7.5', default=0.0, verbose_name='Shot Right Foot 1')
    shoot_run_r_2 = models.FloatField(choices=two_star, help_text='Select an option. Weight: 7.5', default=0.0, verbose_name='Shot Right Foot 2')
    shoot_run_r_3 = models.FloatField(choices=two_star, help_text='Select an option. Weight: 7.5', default=0.0, verbose_name='Shot Right Foot 3')
    shoot_run_l_1 = models.FloatField(choices=two_star, help_text='Select an option. Weight: 7.5', default=0.0, verbose_name='Shot Left Foot 1')
    shoot_run_l_2 = models.FloatField(choices=two_star, help_text='Select an option. Weight: 7.5', default=0.0, verbose_name='Shot Left Foot 2')
    shoot_run_l_3 = models.FloatField(choices=two_star, help_text='Select an option. Weight: 7.5', default=0.0, verbose_name='Shot Left Foot 3')
    finisher_r_1 = models.FloatField(choices=two_star, help_text='Select an option. Weight: 7.5', default=0.0, verbose_name='Finish Right Foot 1')
    finisher_r_2 = models.FloatField(choices=two_star, help_text='Select an option. Weight: 7.5', default=0.0, verbose_name='Finish Right Foot 2')
    finisher_r_3 = models.FloatField(choices=two_star, help_text='Select an option. Weight: 7.5', default=0.0, verbose_name='Finish Right Foot 3')
    finisher_l_1 = models.FloatField(choices=two_star, help_text='Select an option. Weight: 7.5', default=0.0, verbose_name='Finish Left Foot 1')
    finisher_l_2 = models.FloatField(choices=two_star, help_text='Select an option. Weight: 7.5', default=0.0, verbose_name='Finish Left Foot 2')
    finisher_l_3 = models.FloatField(choices=two_star, help_text='Select an option. Weight: 7.5', default=0.0, verbose_name='Finish Left Foot 3')
    '''aggregates'''
    total_control = models.FloatField(default=0.0)
    total_dribbling = models.FloatField(default=0.0)
    total_passing = models.FloatField(default=0.0)
    total_shooting = models.FloatField(default=0.0)
    grand_total = models.FloatField(default=0.0)

    '''calculated fields'''
    @property
    def calc_control(self):
        calc = (
            self.control_thigh * 33.33 +
            self.control_foot * 33.33 +
            self.foot_tap * 33.33
        )
        return ceil(calc)

    @property
    def calc_dribbling(self):
        calc = (
            self.speed_dribble * 25.0 +
            self.dribble_r * 25.0 +
            self.dribble_l * 25.0 +
            self.dribble_3_cone * 25.0
        )
        return ceil(calc)

    @property
    def calc_passing(self):
        calc = (
            self.long_r_1 * 4.5 +
            self.long_r_2 * 4.5 +
            self.long_l_1 * 4.5 +
            self.long_l_2 * 4.5 +
            self.cross_r_1 * 4.5 +
            self.cross_r_2 * 4.5 +
            self.cross_l_1 * 4.5 +
            self.cross_l_2 * 4.5 +
            self.side_pass_r_1 * 4.5 +
            self.side_pass_r_2 * 4.5 +
            self.side_pass_r_3 * 4.5 +
            self.side_pass_l_1 * 4.5 +
            self.side_pass_l_2 * 4.5 +
            self.side_pass_l_3 * 4.5 +
            self.weigh_pass_r_1 * 4.5 +
            self.weigh_pass_r_2 * 4.5 +
            self.weigh_pass_r_3 * 4.5 +
            self.weigh_pass_l_1 * 4.5 +
            self.weigh_pass_l_2 * 4.5 +
            self.weigh_pass_l_3 * 4.5 +
            self.throw_inside_1 * 2.5 +
            self.throw_inside_2 * 2.5 +
            self.throw_between_1 * 2.5 +
            self.throw_between_2 * 2.5
        )
        return ceil(calc)

    @property
    def calc_shooting(self):
        calc = (
            self.shoot_pk * 10.0 +
            self.shoot_run_r_1 * 7.5 +
            self.shoot_run_r_2 * 7.5 +
            self.shoot_run_r_3 * 7.5 +
            self.shoot_run_l_1 * 7.5 +
            self.shoot_run_l_2 * 7.5 +
            self.shoot_run_l_3 * 7.5 +
            self.finisher_r_1 * 7.5 +
            self.finisher_r_2 * 7.5 +
            self.finisher_r_3 * 7.5 +
            self.finisher_l_1 * 7.5 +
            self.finisher_l_2 * 7.5 +
            self.finisher_l_3 * 7.5
        )
        return ceil(calc)

    @property
    def calc_total(self):
        add = (
            self.calc_control +
            self.calc_dribbling +
            self.calc_passing +
            self.calc_shooting
        )
        calc = add / 4

        return ceil(calc)

    def save(self, *args, **kwargs):
        '''save calculated fields'''
        self.total_control = self.calc_control
        self.total_dribbling = self.calc_dribbling
        self.total_passing = self.calc_passing
        self.total_shooting = self.calc_shooting
        self.grand_total = self.calc_total

        super(PlayerScorecard, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.player)

    class Meta:
        verbose_name = "Player Scorecard"


class Showcase(models.Model):
    showcase_name = models.CharField(max_length=100)
    showcase_date = models.DateField()
    showcase_location = models.CharField(max_length=100, null=True, blank=True)
    rain = models.BooleanField(default=False)
    grass_field = models.BooleanField(default=False)

    def __str__(self):
        return self.showcase_name


class Club(models.Model):
    club_name = models.CharField(max_length=100, help_text='Enter the club name here')
    director = models.OneToOneField(Director, on_delete=models.SET_NULL, null=True, blank=True, help_text='Associate the club to a director\'s account here')
    photo = models.ImageField(upload_to='club_logos', null=True, blank=True, validators=[file_size_validator.file_size])
    registration_code = models.CharField(help_text='Club registration code used for player signup. Autogenerated upon save.', max_length=10, null=True, unique=True)
    '''control'''
    control_thigh_avg = models.FloatField(default=0.0)
    control_foot_avg = models.FloatField(default=0.0)
    foot_tap_avg = models.FloatField(default=0.0)
    '''dribbling'''
    speed_dribble_avg = models.FloatField(default=0.0)
    dribble_r_avg = models.FloatField(default=0.0)
    dribble_l_avg = models.FloatField(default=0.0)
    dribble_3_cone_avg = models.FloatField(default=0.0)
    '''passing'''
    long_r_1_avg = models.FloatField(default=0.0)
    long_r_2_avg = models.FloatField(default=0.0)
    long_l_1_avg = models.FloatField(default=0.0)
    long_l_2_avg = models.FloatField(default=0.0)
    cross_r_1_avg = models.FloatField(default=0.0)
    cross_r_2_avg = models.FloatField(default=0.0)
    cross_l_1_avg = models.FloatField(default=0.0)
    cross_l_2_avg = models.FloatField(default=0.0)
    side_pass_r_1_avg = models.FloatField(default=0.0)
    side_pass_r_2_avg = models.FloatField(default=0.0)
    side_pass_r_3_avg = models.FloatField(default=0.0)
    side_pass_l_1_avg = models.FloatField(default=0.0)
    side_pass_l_2_avg = models.FloatField(default=0.0)
    side_pass_l_3_avg = models.FloatField(default=0.0)
    weigh_pass_r_1_avg = models.FloatField(default=0.0)
    weigh_pass_r_2_avg = models.FloatField(default=0.0)
    weigh_pass_r_3_avg = models.FloatField(default=0.0)
    weigh_pass_l_1_avg = models.FloatField(default=0.0)
    weigh_pass_l_2_avg = models.FloatField(default=0.0)
    weigh_pass_l_3_avg = models.FloatField(default=0.0)
    throw_inside_1_avg = models.FloatField(default=0.0)
    throw_inside_2_avg = models.FloatField(default=0.0)
    throw_between_1_avg = models.FloatField(default=0.0)
    throw_between_2_avg = models.FloatField(default=0.0)
    '''shooting'''
    shoot_pk_avg = models.FloatField(default=0.0)
    shoot_run_r_1_avg = models.FloatField(default=0.0)
    shoot_run_r_2_avg = models.FloatField(default=0.0)
    shoot_run_r_3_avg = models.FloatField(default=0.0)
    shoot_run_l_1_avg = models.FloatField(default=0.0)
    shoot_run_l_2_avg = models.FloatField(default=0.0)
    shoot_run_l_3_avg = models.FloatField(default=0.0)
    finisher_r_1_avg = models.FloatField(default=0.0)
    finisher_r_2_avg = models.FloatField(default=0.0)
    finisher_r_3_avg = models.FloatField(default=0.0)
    finisher_l_1_avg = models.FloatField(default=0.0)
    finisher_l_2_avg = models.FloatField(default=0.0)
    finisher_l_3_avg = models.FloatField(default=0.0)
    '''aggregates'''
    total_control_avg = models.FloatField(default=0.0)
    total_dribbling_avg = models.FloatField(default=0.0)
    total_passing_avg = models.FloatField(default=0.0)
    total_shooting_avg = models.FloatField(default=0.0)
    grand_total_avg = models.FloatField(default=0.0)

    def __str__(self):
        return self.club_name

    def generate_uuid(self):
        unique_uuid = uuid.uuid4().hex[:6]

        while Club.objects.filter(registration_code=unique_uuid).exists():
            unique_uuid = uuid.uuid4().hex[:6]

        return unique_uuid

    def save(self, *args, **kwargs):
        if not self.registration_code:
            self.registration_code = self.generate_uuid()

        super().save(*args, **kwargs)


class Team(models.Model):
    team_name = models.CharField(max_length=100, help_text='Enter the team name here')
    coach = models.ForeignKey(Coach, on_delete=models.SET_NULL, null=True, blank=True, help_text='Associate the team to a coaches account here')
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=3, choices=choices.states, default='N/A')
    club = models.ForeignKey(Club, on_delete=models.SET_NULL, null=True, blank=True)

    '''control'''
    control_thigh_avg = models.FloatField(default=0.0)
    control_foot_avg = models.FloatField(default=0.0)
    foot_tap_avg = models.FloatField(default=0.0)
    '''dribbling'''
    speed_dribble_avg = models.FloatField(default=0.0)
    dribble_r_avg = models.FloatField(default=0.0)
    dribble_l_avg = models.FloatField(default=0.0)
    dribble_3_cone_avg = models.FloatField(default=0.0)
    '''passing'''
    long_r_1_avg = models.FloatField(default=0.0)
    long_r_2_avg = models.FloatField(default=0.0)
    long_l_1_avg = models.FloatField(default=0.0)
    long_l_2_avg = models.FloatField(default=0.0)
    cross_r_1_avg = models.FloatField(default=0.0)
    cross_r_2_avg = models.FloatField(default=0.0)
    cross_l_1_avg = models.FloatField(default=0.0)
    cross_l_2_avg = models.FloatField(default=0.0)
    side_pass_r_1_avg = models.FloatField(default=0.0)
    side_pass_r_2_avg = models.FloatField(default=0.0)
    side_pass_r_3_avg = models.FloatField(default=0.0)
    side_pass_l_1_avg = models.FloatField(default=0.0)
    side_pass_l_2_avg = models.FloatField(default=0.0)
    side_pass_l_3_avg = models.FloatField(default=0.0)
    weigh_pass_r_1_avg = models.FloatField(default=0.0)
    weigh_pass_r_2_avg = models.FloatField(default=0.0)
    weigh_pass_r_3_avg = models.FloatField(default=0.0)
    weigh_pass_l_1_avg = models.FloatField(default=0.0)
    weigh_pass_l_2_avg = models.FloatField(default=0.0)
    weigh_pass_l_3_avg = models.FloatField(default=0.0)
    throw_inside_1_avg = models.FloatField(default=0.0)
    throw_inside_2_avg = models.FloatField(default=0.0)
    throw_between_1_avg = models.FloatField(default=0.0)
    throw_between_2_avg = models.FloatField(default=0.0)
    '''shooting'''
    shoot_pk_avg = models.FloatField(default=0.0)
    shoot_run_r_1_avg = models.FloatField(default=0.0)
    shoot_run_r_2_avg = models.FloatField(default=0.0)
    shoot_run_r_3_avg = models.FloatField(default=0.0)
    shoot_run_l_1_avg = models.FloatField(default=0.0)
    shoot_run_l_2_avg = models.FloatField(default=0.0)
    shoot_run_l_3_avg = models.FloatField(default=0.0)
    finisher_r_1_avg = models.FloatField(default=0.0)
    finisher_r_2_avg = models.FloatField(default=0.0)
    finisher_r_3_avg = models.FloatField(default=0.0)
    finisher_l_1_avg = models.FloatField(default=0.0)
    finisher_l_2_avg = models.FloatField(default=0.0)
    finisher_l_3_avg = models.FloatField(default=0.0)
    '''aggregates'''
    total_control_avg = models.FloatField(default=0.0)
    total_dribbling_avg = models.FloatField(default=0.0)
    total_passing_avg = models.FloatField(default=0.0)
    total_shooting_avg = models.FloatField(default=0.0)
    grand_total_avg = models.FloatField(default=0.0)

    def __str__(self):
        return self.team_name


class Station(models.Model):
    '''
    Station model
    '''
    index_choices = tuple((i, i) for i in range(1, 60, 1))
    group_choices = (
        ('Shooting', 'Shooting'),
        ('Dribbling', 'Dribbling'),
        ('Passing', 'Passing'),
        ('Control', 'Control')
    )

    name = models.CharField(max_length=100, help_text='Enter the station name here')
    attempts = ArrayField(models.CharField(max_length=100), null=True, blank=True, help_text='Array of associated field names')
    display = models.BooleanField(default=False, help_text='Determines if station is displayed on format page')
    index = models.SmallIntegerField(
        null=True,
        blank=True,
        choices=index_choices,
        help_text='Used to order stations in showcase'
    )
    description = models.TextField(max_length=1500, null=True, blank=True)
    scoring_criteria = models.ManyToManyField(
        'ScoringCriteria',
        related_name='stations',
        help_text='Add as many scoring criteria as apply'
    )
    weight = models.FloatField(default=0.0)
    group = models.CharField(choices=group_choices, null=True, max_length=30)
    image = models.ImageField(
        upload_to='stations',
        null=True,
        blank=True,
        validators=[file_size_validator.file_size]
    )
    diagram = models.FileField(
        upload_to='stations',
        null=True,
        blank=True,
        validators=[file_size_validator.file_size]
    )
    scorecard_diagram = models.FileField(
        upload_to='stations',
        null=True,
        blank=True,
        validators=[file_size_validator.file_size]
    )
    animation = models.FileField(
        upload_to='stations',
        null=True,
        blank=True
    )
    webm_animation = models.FileField(
        upload_to='stations',
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('index',)


class ScoringCriteria(models.Model):
    '''
    Used as ManytoMany field in Station model
    '''
    name = models.CharField(max_length=100, help_text='Enter the field layout name here')
    value = models.SmallIntegerField(null=True, blank=True)
    description = models.TextField(
        max_length=1500,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-value',)


class FieldLayout(models.Model):
    '''
    Field layout models for scorecards
    '''
    name = models.CharField(max_length=100, help_text='Enter the field layout name here')
    image = models.ImageField(
        upload_to='field-layouts',
        null=True,
        blank=True,
        validators=[file_size_validator.file_size]
    )
    diagram = models.FileField(
        upload_to='field-layouts',
        null=True,
        blank=True,
        validators=[file_size_validator.file_size]
    )

    def __str__(self):
        return self.name


# Make email field required apparently. Need for abstract user class
AbstractUser._meta.get_field('email').blank = False
