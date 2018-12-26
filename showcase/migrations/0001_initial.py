# Generated by Django 2.0.8 on 2018-09-04 00:12

from django.db import migrations, models
import django.db.models.deletion
import showcase.file_size_validator


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('club_name', models.CharField(help_text='Enter the club name here', max_length=100)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='club_logos', validators=[showcase.file_size_validator.file_size])),
                ('registration_code', models.CharField(help_text='Club registration code used for player signup. Autogenerated upon save.', max_length=10, null=True, unique=True)),
                ('control_thigh_avg', models.FloatField(default=0.0)),
                ('control_foot_avg', models.FloatField(default=0.0)),
                ('foot_tap_avg', models.FloatField(default=0.0)),
                ('speed_dribble_avg', models.FloatField(default=0.0)),
                ('dribble_r_avg', models.FloatField(default=0.0)),
                ('dribble_l_avg', models.FloatField(default=0.0)),
                ('dribble_3_cone_avg', models.FloatField(default=0.0)),
                ('long_r_1_avg', models.FloatField(default=0.0)),
                ('long_r_2_avg', models.FloatField(default=0.0)),
                ('long_l_1_avg', models.FloatField(default=0.0)),
                ('long_l_2_avg', models.FloatField(default=0.0)),
                ('cross_r_1_avg', models.FloatField(default=0.0)),
                ('cross_r_2_avg', models.FloatField(default=0.0)),
                ('cross_l_1_avg', models.FloatField(default=0.0)),
                ('cross_l_2_avg', models.FloatField(default=0.0)),
                ('side_pass_r_1_avg', models.FloatField(default=0.0)),
                ('side_pass_r_2_avg', models.FloatField(default=0.0)),
                ('side_pass_r_3_avg', models.FloatField(default=0.0)),
                ('side_pass_l_1_avg', models.FloatField(default=0.0)),
                ('side_pass_l_2_avg', models.FloatField(default=0.0)),
                ('side_pass_l_3_avg', models.FloatField(default=0.0)),
                ('weigh_pass_r_1_avg', models.FloatField(default=0.0)),
                ('weigh_pass_r_2_avg', models.FloatField(default=0.0)),
                ('weigh_pass_r_3_avg', models.FloatField(default=0.0)),
                ('weigh_pass_l_1_avg', models.FloatField(default=0.0)),
                ('weigh_pass_l_2_avg', models.FloatField(default=0.0)),
                ('weigh_pass_l_3_avg', models.FloatField(default=0.0)),
                ('throw_inside_1_avg', models.FloatField(default=0.0)),
                ('throw_inside_2_avg', models.FloatField(default=0.0)),
                ('throw_between_1_avg', models.FloatField(default=0.0)),
                ('throw_between_2_avg', models.FloatField(default=0.0)),
                ('shoot_pk_avg', models.FloatField(default=0.0)),
                ('shoot_run_r_1_avg', models.FloatField(default=0.0)),
                ('shoot_run_r_2_avg', models.FloatField(default=0.0)),
                ('shoot_run_r_3_avg', models.FloatField(default=0.0)),
                ('shoot_run_l_1_avg', models.FloatField(default=0.0)),
                ('shoot_run_l_2_avg', models.FloatField(default=0.0)),
                ('shoot_run_l_3_avg', models.FloatField(default=0.0)),
                ('finisher_r_1_avg', models.FloatField(default=0.0)),
                ('finisher_r_2_avg', models.FloatField(default=0.0)),
                ('finisher_r_3_avg', models.FloatField(default=0.0)),
                ('finisher_l_1_avg', models.FloatField(default=0.0)),
                ('finisher_l_2_avg', models.FloatField(default=0.0)),
                ('finisher_l_3_avg', models.FloatField(default=0.0)),
                ('total_control_avg', models.FloatField(default=0.0)),
                ('total_dribbling_avg', models.FloatField(default=0.0)),
                ('total_passing_avg', models.FloatField(default=0.0)),
                ('total_shooting_avg', models.FloatField(default=0.0)),
                ('grand_total_avg', models.FloatField(default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='Coach',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(help_text='First Name', max_length=100)),
                ('last_name', models.CharField(help_text='Last Name', max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Coaches',
            },
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(help_text='First Name', max_length=100)),
                ('last_name', models.CharField(help_text='Last Name', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(help_text='First Name', max_length=100)),
                ('last_name', models.CharField(help_text='Last Name', max_length=100)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='players', validators=[showcase.file_size_validator.file_size])),
                ('trading_card', models.ImageField(blank=True, help_text='Autogenerated. Do not load file unless necessary.', null=True, upload_to='cards')),
                ('birth_year', models.SmallIntegerField(blank=True, choices=[(1990, 1990), (1991, 1991), (1992, 1992), (1993, 1993), (1994, 1994), (1995, 1995), (1996, 1996), (1997, 1997), (1998, 1998), (1999, 1999), (2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018)], null=True)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('state', models.CharField(blank=True, choices=[('AK', 'Alaska'), ('AL', 'Alabama'), ('AR', 'Arkansas'), ('AS', 'American Samoa'), ('AZ', 'Arizona'), ('CA', 'California'), ('CO', 'Colorado'), ('CT', 'Connecticut'), ('DC', 'District of Columbia'), ('DE', 'Delaware'), ('FL', 'Florida'), ('GA', 'Georgia'), ('GU', 'Guam'), ('HI', 'Hawaii'), ('IA', 'Iowa'), ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'), ('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('MA', 'Massachusetts'), ('MD', 'Maryland'), ('ME', 'Maine'), ('MI', 'Michigan'), ('MN', 'Minnesota'), ('MO', 'Missouri'), ('MP', 'Northern Mariana Islands'), ('MS', 'Mississippi'), ('MT', 'Montana'), ('NA', 'National'), ('NC', 'North Carolina'), ('ND', 'North Dakota'), ('NE', 'Nebraska'), ('NH', 'New Hampshire'), ('NJ', 'New Jersey'), ('NM', 'New Mexico'), ('NV', 'Nevada'), ('NY', 'New York'), ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'), ('PA', 'Pennsylvania'), ('PR', 'Puerto Rico'), ('RI', 'Rhode Island'), ('SC', 'South Carolina'), ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'), ('UT', 'Utah'), ('VA', 'Virginia'), ('VI', 'Virgin Islands'), ('VT', 'Vermont'), ('WA', 'Washington'), ('WI', 'Wisconsin'), ('WV', 'West Virginia'), ('WY', 'Wyoming'), ('N/A', 'N/A')], max_length=3, null=True)),
                ('region', models.CharField(blank=True, choices=[('South', 'South'), ('West', 'West'), ('East', 'East'), ('Midwest', 'Midwest')], max_length=10, null=True)),
                ('country', models.CharField(blank=True, choices=[('United States', 'United States'), ('Afghanistan', 'Afghanistan'), ('Albania', 'Albania'), ('Algeria', 'Algeria'), ('American Samoa', 'American Samoa'), ('Andorra', 'Andorra'), ('Angola', 'Angola'), ('Anguilla', 'Anguilla'), ('Antarctica', 'Antarctica'), ('Antigua And Barbuda', 'Antigua And Barbuda'), ('Argentina', 'Argentina'), ('Armenia', 'Armenia'), ('Aruba', 'Aruba'), ('Australia', 'Australia'), ('Austria', 'Austria'), ('Azerbaijan', 'Azerbaijan'), ('Bahamas', 'Bahamas'), ('Bahrain', 'Bahrain'), ('Bangladesh', 'Bangladesh'), ('Barbados', 'Barbados'), ('Belarus', 'Belarus'), ('Belgium', 'Belgium'), ('Belize', 'Belize'), ('Benin', 'Benin'), ('Bermuda', 'Bermuda'), ('Bhutan', 'Bhutan'), ('Bolivia', 'Bolivia'), ('Bosnia And Herzegowina', 'Bosnia And Herzegowina'), ('Botswana', 'Botswana'), ('Bouvet Island', 'Bouvet Island'), ('Brazil', 'Brazil'), ('Brunei Darussalam', 'Brunei Darussalam'), ('Bulgaria', 'Bulgaria'), ('Burkina Faso', 'Burkina Faso'), ('Burundi', 'Burundi'), ('Cambodia', 'Cambodia'), ('Cameroon', 'Cameroon'), ('Canada', 'Canada'), ('Cape Verde', 'Cape Verde'), ('Cayman Islands', 'Cayman Islands'), ('Central African Rep', 'Central African Rep'), ('Chad', 'Chad'), ('Chile', 'Chile'), ('China', 'China'), ('Christmas Island', 'Christmas Island'), ('Cocos Islands', 'Cocos Islands'), ('Colombia', 'Colombia'), ('Comoros', 'Comoros'), ('Congo', 'Congo'), ('Cook Islands', 'Cook Islands'), ('Costa Rica', 'Costa Rica'), ('Cote D`ivoire', 'Cote D`ivoire'), ('Croatia', 'Croatia'), ('Cuba', 'Cuba'), ('Cyprus', 'Cyprus'), ('Czech Republic', 'Czech Republic'), ('Denmark', 'Denmark'), ('Djibouti', 'Djibouti'), ('Dominica', 'Dominica'), ('Dominican Republic', 'Dominican Republic'), ('East Timor', 'East Timor'), ('Ecuador', 'Ecuador'), ('Egypt', 'Egypt'), ('El Salvador', 'El Salvador'), ('Equatorial Guinea', 'Equatorial Guinea'), ('Eritrea', 'Eritrea'), ('Estonia', 'Estonia'), ('Ethiopia', 'Ethiopia'), ('Falkland Islands (Malvinas)', 'Falkland Islands (Malvinas)'), ('Faroe Islands', 'Faroe Islands'), ('Fiji', 'Fiji'), ('Finland', 'Finland'), ('France', 'France'), ('French Guiana', 'French Guiana'), ('French Polynesia', 'French Polynesia'), ('French S. Territories', 'French S. Territories'), ('Gabon', 'Gabon'), ('Gambia', 'Gambia'), ('Georgia', 'Georgia'), ('Germany', 'Germany'), ('Ghana', 'Ghana'), ('Gibraltar', 'Gibraltar'), ('Greece', 'Greece'), ('Greenland', 'Greenland'), ('Grenada', 'Grenada'), ('Guadeloupe', 'Guadeloupe'), ('Guam', 'Guam'), ('Guatemala', 'Guatemala'), ('Guinea', 'Guinea'), ('Guinea-bissau', 'Guinea-bissau'), ('Guyana', 'Guyana'), ('Haiti', 'Haiti'), ('Honduras', 'Honduras'), ('Hong Kong', 'Hong Kong'), ('Hungary', 'Hungary'), ('Iceland', 'Iceland'), ('India', 'India'), ('Indonesia', 'Indonesia'), ('Iran', 'Iran'), ('Iraq', 'Iraq'), ('Ireland', 'Ireland'), ('Israel', 'Israel'), ('Italy', 'Italy'), ('Jamaica', 'Jamaica'), ('Japan', 'Japan'), ('Jordan', 'Jordan'), ('Kazakhstan', 'Kazakhstan'), ('Kenya', 'Kenya'), ('Kiribati', 'Kiribati'), ('Korea (North)', 'Korea (North)'), ('Korea (South)', 'Korea (South)'), ('Kuwait', 'Kuwait'), ('Kyrgyzstan', 'Kyrgyzstan'), ('Laos', 'Laos'), ('Latvia', 'Latvia'), ('Lebanon', 'Lebanon'), ('Lesotho', 'Lesotho'), ('Liberia', 'Liberia'), ('Libya', 'Libya'), ('Liechtenstein', 'Liechtenstein'), ('Lithuania', 'Lithuania'), ('Luxembourg', 'Luxembourg'), ('Macau', 'Macau'), ('Macedonia', 'Macedonia'), ('Madagascar', 'Madagascar'), ('Malawi', 'Malawi'), ('Malaysia', 'Malaysia'), ('Maldives', 'Maldives'), ('Mali', 'Mali'), ('Malta', 'Malta'), ('Marshall Islands', 'Marshall Islands'), ('Martinique', 'Martinique'), ('Mauritania', 'Mauritania'), ('Mauritius', 'Mauritius'), ('Mayotte', 'Mayotte'), ('Mexico', 'Mexico'), ('Micronesia', 'Micronesia'), ('Moldova', 'Moldova'), ('Monaco', 'Monaco'), ('Mongolia', 'Mongolia'), ('Montserrat', 'Montserrat'), ('Morocco', 'Morocco'), ('Mozambique', 'Mozambique'), ('Myanmar', 'Myanmar'), ('Namibia', 'Namibia'), ('Nauru', 'Nauru'), ('Nepal', 'Nepal'), ('Netherlands', 'Netherlands'), ('Netherlands Antilles', 'Netherlands Antilles'), ('New Caledonia', 'New Caledonia'), ('New Zealand', 'New Zealand'), ('Nicaragua', 'Nicaragua'), ('Niger', 'Niger'), ('Nigeria', 'Nigeria'), ('Niue', 'Niue'), ('Norfolk Island', 'Norfolk Island'), ('Northern Mariana Islands', 'Northern Mariana Islands'), ('Norway', 'Norway'), ('Oman', 'Oman'), ('Pakistan', 'Pakistan'), ('Palau', 'Palau'), ('Panama', 'Panama'), ('Papua New Guinea', 'Papua New Guinea'), ('Paraguay', 'Paraguay'), ('Peru', 'Peru'), ('Philippines', 'Philippines'), ('Pitcairn', 'Pitcairn'), ('Poland', 'Poland'), ('Portugal', 'Portugal'), ('Puerto Rico', 'Puerto Rico'), ('Qatar', 'Qatar'), ('Reunion', 'Reunion'), ('Romania', 'Romania'), ('Russian Federation', 'Russian Federation'), ('Rwanda', 'Rwanda'), ('Saint Kitts And Nevis', 'Saint Kitts And Nevis'), ('Saint Lucia', 'Saint Lucia'), ('St Vincent/Grenadines', 'St Vincent/Grenadines'), ('Samoa', 'Samoa'), ('San Marino', 'San Marino'), ('Sao Tome', 'Sao Tome'), ('Saudi Arabia', 'Saudi Arabia'), ('Senegal', 'Senegal'), ('Seychelles', 'Seychelles'), ('Sierra Leone', 'Sierra Leone'), ('Singapore', 'Singapore'), ('Slovakia', 'Slovakia'), ('Slovenia', 'Slovenia'), ('Solomon Islands', 'Solomon Islands'), ('Somalia', 'Somalia'), ('South Africa', 'South Africa'), ('Spain', 'Spain'), ('Sri Lanka', 'Sri Lanka'), ('St. Helena', 'St. Helena'), ('St.Pierre', 'St.Pierre'), ('Sudan', 'Sudan'), ('Suriname', 'Suriname'), ('Swaziland', 'Swaziland'), ('Sweden', 'Sweden'), ('Switzerland', 'Switzerland'), ('Syrian Arab Republic', 'Syrian Arab Republic'), ('Taiwan', 'Taiwan'), ('Tajikistan', 'Tajikistan'), ('Tanzania', 'Tanzania'), ('Thailand', 'Thailand'), ('Togo', 'Togo'), ('Tokelau', 'Tokelau'), ('Tonga', 'Tonga'), ('Trinidad And Tobago', 'Trinidad And Tobago'), ('Tunisia', 'Tunisia'), ('Turkey', 'Turkey'), ('Turkmenistan', 'Turkmenistan'), ('Tuvalu', 'Tuvalu'), ('Uganda', 'Uganda'), ('Ukraine', 'Ukraine'), ('United Arab Emirates', 'United Arab Emirates'), ('United Kingdom', 'United Kingdom'), ('Uruguay', 'Uruguay'), ('Uzbekistan', 'Uzbekistan'), ('Vanuatu', 'Vanuatu'), ('Vatican City State', 'Vatican City State'), ('Venezuela', 'Venezuela'), ('Viet Nam', 'Viet Nam'), ('Virgin Islands (British)', 'Virgin Islands (British)'), ('Virgin Islands (U.S.)', 'Virgin Islands (U.S.)'), ('Western Sahara', 'Western Sahara'), ('Yemen', 'Yemen'), ('Yugoslavia', 'Yugoslavia'), ('Zaire', 'Zaire'), ('Zambia', 'Zambia'), ('Zimbabwe', 'Zimbabwe')], max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PlayerScorecard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('height', models.SmallIntegerField(default=None, null=True, verbose_name='Height in inches')),
                ('muscle', models.SmallIntegerField(default=None, null=True, verbose_name='Muscle Percentage')),
                ('body_fat', models.SmallIntegerField(default=None, null=True, verbose_name='Body Fat Percentage')),
                ('pulse', models.SmallIntegerField(default=None, null=True)),
                ('oxygen', models.SmallIntegerField(default=None, null=True)),
                ('player_number', models.SmallIntegerField(default=None, null=True)),
                ('control_thigh', models.FloatField(choices=[(1.0, '5 Star'), (0.75, '4 Star'), (0.5, '3 Star'), (0.25, '2 Star'), (0, '1 Star')], default=0.0, help_text='Select an option. Weight: 33.33', verbose_name='Thigh Control')),
                ('control_foot', models.FloatField(choices=[(1.0, '5 Star'), (0.75, '4 Star'), (0.5, '3 Star'), (0.25, '2 Star'), (0, '1 Star')], default=0.0, help_text='Select an option. Weight: 33.33', verbose_name='Foot Control')),
                ('foot_tap', models.FloatField(choices=[(1.0, '5 Star'), (0.75, '4 Star'), (0.5, '3 Star'), (0.25, '2 Star'), (0, '1 Star')], default=0.0, help_text='Select an option. Weight: 33.33', verbose_name='Taps')),
                ('speed_dribble', models.FloatField(choices=[(1.0, '5 Star'), (0.75, '4 Star'), (0.5, '3 Star'), (0.25, '2 Star'), (0, '1 Star')], default=0.0, help_text='Select an option. Weight: 25', verbose_name='Speed Dribble')),
                ('dribble_r', models.FloatField(choices=[(1.0, '5 Star'), (0.75, '4 Star'), (0.5, '3 Star'), (0.25, '2 Star'), (0, '1 Star')], default=0.0, help_text='Select an option. Weight: 25', verbose_name='Dribble Right Foot')),
                ('dribble_l', models.FloatField(choices=[(1.0, '5 Star'), (0.75, '4 Star'), (0.5, '3 Star'), (0.25, '2 Star'), (0, '1 Star')], default=0.0, help_text='Select an option. Weight: 25', verbose_name='Dribble Left Foot')),
                ('dribble_3_cone', models.FloatField(choices=[(1.0, '5 Star'), (0.75, '4 Star'), (0.5, '3 Star'), (0.25, '2 Star'), (0, '1 Star')], default=0.0, help_text='Select an option. Weight: 25', verbose_name='Dribble 3-Cone')),
                ('long_r_1', models.FloatField(choices=[(1.0, '5 Star'), (0.75, '4 Star'), (0.5, '3 Star'), (0.25, '2 Star'), (0, '1 Star')], default=0.0, help_text='Select an option. Weight: 4.5', verbose_name='Long Pass Right Foot 1')),
                ('long_r_2', models.FloatField(choices=[(1.0, '5 Star'), (0.75, '4 Star'), (0.5, '3 Star'), (0.25, '2 Star'), (0, '1 Star')], default=0.0, help_text='Select an option. Weight: 4.5', verbose_name='Long Pass Right Foot 2')),
                ('long_l_1', models.FloatField(choices=[(1.0, '5 Star'), (0.75, '4 Star'), (0.5, '3 Star'), (0.25, '2 Star'), (0, '1 Star')], default=0.0, help_text='Select an option. Weight: 4.5', verbose_name='Long Pass Left Foot 1')),
                ('long_l_2', models.FloatField(choices=[(1.0, '5 Star'), (0.75, '4 Star'), (0.5, '3 Star'), (0.25, '2 Star'), (0, '1 Star')], default=0.0, help_text='Select an option. Weight: 4.5', verbose_name='Long Pass Left Foot 2')),
                ('cross_r_1', models.FloatField(choices=[(1.0, '5 Star'), (0.75, '4 Star'), (0.5, '3 Star'), (0.25, '2 Star'), (0, '1 Star')], default=0.0, help_text='Select an option. Weight: 4.5', verbose_name='Cross Right 1')),
                ('cross_r_2', models.FloatField(choices=[(1.0, '5 Star'), (0.75, '4 Star'), (0.5, '3 Star'), (0.25, '2 Star'), (0, '1 Star')], default=0.0, help_text='Select an option. Weight: 4.5', verbose_name='Cross Right 2')),
                ('cross_l_1', models.FloatField(choices=[(1.0, '5 Star'), (0.75, '4 Star'), (0.5, '3 Star'), (0.25, '2 Star'), (0, '1 Star')], default=0.0, help_text='Select an option. Weight: 4.5', verbose_name='Cross Left 1')),
                ('cross_l_2', models.FloatField(choices=[(1.0, '5 Star'), (0.75, '4 Star'), (0.5, '3 Star'), (0.25, '2 Star'), (0, '1 Star')], default=0.0, help_text='Select an option. Weight: 4.5', verbose_name='Cross Left 2')),
                ('side_pass_r_1', models.FloatField(choices=[(1.0, '5 Star'), (0.75, '4 Star'), (0.5, '3 Star'), (0.25, '2 Star'), (0, '1 Star')], default=0.0, help_text='Select an option. Weight: 4.5', verbose_name='Side Pass Right 1')),
                ('side_pass_r_2', models.FloatField(choices=[(1.0, '5 Star'), (0.75, '4 Star'), (0.5, '3 Star'), (0.25, '2 Star'), (0, '1 Star')], default=0.0, help_text='Select an option. Weight: 4.5', verbose_name='Side Pass Right 2')),
                ('side_pass_r_3', models.FloatField(choices=[(1.0, '5 Star'), (0.75, '4 Star'), (0.5, '3 Star'), (0.25, '2 Star'), (0, '1 Star')], default=0.0, help_text='Select an option. Weight: 4.5', verbose_name='Side Pass Right 3')),
                ('side_pass_l_1', models.FloatField(choices=[(1.0, '5 Star'), (0.75, '4 Star'), (0.5, '3 Star'), (0.25, '2 Star'), (0, '1 Star')], default=0.0, help_text='Select an option. Weight: 4.5', verbose_name='Side Pass Left 1')),
                ('side_pass_l_2', models.FloatField(choices=[(1.0, '5 Star'), (0.75, '4 Star'), (0.5, '3 Star'), (0.25, '2 Star'), (0, '1 Star')], default=0.0, help_text='Select an option. Weight: 4.5', verbose_name='Side Pass Left 2')),
                ('side_pass_l_3', models.FloatField(choices=[(1.0, '5 Star'), (0.75, '4 Star'), (0.5, '3 Star'), (0.25, '2 Star'), (0, '1 Star')], default=0.0, help_text='Select an option. Weight: 4.5', verbose_name='Side Pass Left 3')),
                ('weigh_pass_r_1', models.FloatField(choices=[(1.0, '5 Star'), (0.75, '4 Star'), (0.5, '3 Star'), (0.25, '2 Star'), (0, '1 Star')], default=0.0, help_text='Select an option. Weight: 4.5', verbose_name='Weighted Pass Right 1')),
                ('weigh_pass_r_2', models.FloatField(choices=[(1.0, '5 Star'), (0.75, '4 Star'), (0.5, '3 Star'), (0.25, '2 Star'), (0, '1 Star')], default=0.0, help_text='Select an option. Weight: 4.5', verbose_name='Weighted Pass Right 2')),
                ('weigh_pass_r_3', models.FloatField(choices=[(1.0, '5 Star'), (0.75, '4 Star'), (0.5, '3 Star'), (0.25, '2 Star'), (0, '1 Star')], default=0.0, help_text='Select an option. Weight: 4.5', verbose_name='Weighted Pass Right 3')),
                ('weigh_pass_l_1', models.FloatField(choices=[(1.0, '5 Star'), (0.75, '4 Star'), (0.5, '3 Star'), (0.25, '2 Star'), (0, '1 Star')], default=0.0, help_text='Select an option. Weight: 4.5', verbose_name='Weighted Pass Left 1')),
                ('weigh_pass_l_2', models.FloatField(choices=[(1.0, '5 Star'), (0.75, '4 Star'), (0.5, '3 Star'), (0.25, '2 Star'), (0, '1 Star')], default=0.0, help_text='Select an option. Weight: 4.5', verbose_name='Weighted Pass Left 2')),
                ('weigh_pass_l_3', models.FloatField(choices=[(1.0, '5 Star'), (0.75, '4 Star'), (0.5, '3 Star'), (0.25, '2 Star'), (0, '1 Star')], default=0.0, help_text='Select an option. Weight: 4.5', verbose_name='Weighted Pass Left 3')),
                ('throw_inside_1', models.FloatField(choices=[(1.0, '5 Star'), (0.75, '4 Star'), (0.5, '3 Star'), (0.25, '2 Star'), (0, '1 Star')], default=0.0, help_text='Select an option. Weight: 2.5', verbose_name='Throw Inside Box 1')),
                ('throw_inside_2', models.FloatField(choices=[(1.0, '5 Star'), (0.75, '4 Star'), (0.5, '3 Star'), (0.25, '2 Star'), (0, '1 Star')], default=0.0, help_text='Select an option. Weight: 2.5', verbose_name='Throw Inside Box 2')),
                ('throw_between_1', models.FloatField(choices=[(1.0, '5 Star'), (0.75, '4 Star'), (0.5, '3 Star'), (0.25, '2 Star'), (0, '1 Star')], default=0.0, help_text='Select an option. Weight: 2.5', verbose_name='Throw-in between far cones 1')),
                ('throw_between_2', models.FloatField(choices=[(1.0, '5 Star'), (0.75, '4 Star'), (0.5, '3 Star'), (0.25, '2 Star'), (0, '1 Star')], default=0.0, help_text='Select an option. Weight: 2.5', verbose_name='Throw-in between far cones 2')),
                ('shoot_pk', models.FloatField(choices=[(1.0, '5 Star'), (0.75, '4 Star'), (0.5, '3 Star'), (0.25, '2 Star'), (0, '1 Star')], default=0.0, help_text='Select an option. Weight: 10.0', verbose_name='Penalty Kick')),
                ('shoot_run_r_1', models.FloatField(choices=[(1.0, '5 Star'), (0.75, '4 Star'), (0.5, '3 Star'), (0.25, '2 Star'), (0, '1 Star')], default=0.0, help_text='Select an option. Weight: 7.5', verbose_name='Shot Right Foot 1')),
                ('shoot_run_r_2', models.FloatField(choices=[(1.0, '5 Star'), (0.75, '4 Star'), (0.5, '3 Star'), (0.25, '2 Star'), (0, '1 Star')], default=0.0, help_text='Select an option. Weight: 7.5', verbose_name='Shot Right Foot 2')),
                ('shoot_run_r_3', models.FloatField(choices=[(1.0, '5 Star'), (0.75, '4 Star'), (0.5, '3 Star'), (0.25, '2 Star'), (0, '1 Star')], default=0.0, help_text='Select an option. Weight: 7.5', verbose_name='Shot Right Foot 3')),
                ('shoot_run_l_1', models.FloatField(choices=[(1.0, '5 Star'), (0.75, '4 Star'), (0.5, '3 Star'), (0.25, '2 Star'), (0, '1 Star')], default=0.0, help_text='Select an option. Weight: 7.5', verbose_name='Shot Left Foot 1')),
                ('shoot_run_l_2', models.FloatField(choices=[(1.0, '5 Star'), (0.75, '4 Star'), (0.5, '3 Star'), (0.25, '2 Star'), (0, '1 Star')], default=0.0, help_text='Select an option. Weight: 7.5', verbose_name='Shot Left Foot 2')),
                ('shoot_run_l_3', models.FloatField(choices=[(1.0, '5 Star'), (0.75, '4 Star'), (0.5, '3 Star'), (0.25, '2 Star'), (0, '1 Star')], default=0.0, help_text='Select an option. Weight: 7.5', verbose_name='Shot Left Foot 3')),
                ('finisher_r_1', models.FloatField(choices=[(1.0, '5 Star'), (0.75, '4 Star'), (0.5, '3 Star'), (0.25, '2 Star'), (0, '1 Star')], default=0.0, help_text='Select an option. Weight: 7.5', verbose_name='Finish Right Foot 1')),
                ('finisher_r_2', models.FloatField(choices=[(1.0, '5 Star'), (0.75, '4 Star'), (0.5, '3 Star'), (0.25, '2 Star'), (0, '1 Star')], default=0.0, help_text='Select an option. Weight: 7.5', verbose_name='Finish Right Foot 2')),
                ('finisher_r_3', models.FloatField(choices=[(1.0, '5 Star'), (0.75, '4 Star'), (0.5, '3 Star'), (0.25, '2 Star'), (0, '1 Star')], default=0.0, help_text='Select an option. Weight: 7.5', verbose_name='Finish Right Foot 3')),
                ('finisher_l_1', models.FloatField(choices=[(1.0, '5 Star'), (0.75, '4 Star'), (0.5, '3 Star'), (0.25, '2 Star'), (0, '1 Star')], default=0.0, help_text='Select an option. Weight: 7.5', verbose_name='Finish Left Foot 1')),
                ('finisher_l_2', models.FloatField(choices=[(1.0, '5 Star'), (0.75, '4 Star'), (0.5, '3 Star'), (0.25, '2 Star'), (0, '1 Star')], default=0.0, help_text='Select an option. Weight: 7.5', verbose_name='Finish Left Foot 2')),
                ('finisher_l_3', models.FloatField(choices=[(1.0, '5 Star'), (0.75, '4 Star'), (0.5, '3 Star'), (0.25, '2 Star'), (0, '1 Star')], default=0.0, help_text='Select an option. Weight: 7.5', verbose_name='Finish Left Foot 3')),
                ('total_control', models.FloatField(default=0.0)),
                ('total_dribbling', models.FloatField(default=0.0)),
                ('total_passing', models.FloatField(default=0.0)),
                ('total_shooting', models.FloatField(default=0.0)),
                ('grand_total', models.FloatField(default=0.0)),
                ('player', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='player', to='showcase.Player')),
            ],
            options={
                'verbose_name': 'Player Scorecard',
            },
        ),
        migrations.CreateModel(
            name='Showcase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('showcase_name', models.CharField(max_length=100)),
                ('showcase_date', models.DateField()),
                ('showcase_location', models.CharField(blank=True, max_length=100, null=True)),
                ('weather', models.CharField(blank=True, max_length=100, null=True)),
                ('field_condition', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(help_text='Enter the team name here', max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(choices=[('AK', 'Alaska'), ('AL', 'Alabama'), ('AR', 'Arkansas'), ('AS', 'American Samoa'), ('AZ', 'Arizona'), ('CA', 'California'), ('CO', 'Colorado'), ('CT', 'Connecticut'), ('DC', 'District of Columbia'), ('DE', 'Delaware'), ('FL', 'Florida'), ('GA', 'Georgia'), ('GU', 'Guam'), ('HI', 'Hawaii'), ('IA', 'Iowa'), ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'), ('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('MA', 'Massachusetts'), ('MD', 'Maryland'), ('ME', 'Maine'), ('MI', 'Michigan'), ('MN', 'Minnesota'), ('MO', 'Missouri'), ('MP', 'Northern Mariana Islands'), ('MS', 'Mississippi'), ('MT', 'Montana'), ('NA', 'National'), ('NC', 'North Carolina'), ('ND', 'North Dakota'), ('NE', 'Nebraska'), ('NH', 'New Hampshire'), ('NJ', 'New Jersey'), ('NM', 'New Mexico'), ('NV', 'Nevada'), ('NY', 'New York'), ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'), ('PA', 'Pennsylvania'), ('PR', 'Puerto Rico'), ('RI', 'Rhode Island'), ('SC', 'South Carolina'), ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'), ('UT', 'Utah'), ('VA', 'Virginia'), ('VI', 'Virgin Islands'), ('VT', 'Vermont'), ('WA', 'Washington'), ('WI', 'Wisconsin'), ('WV', 'West Virginia'), ('WY', 'Wyoming'), ('N/A', 'N/A')], default='N/A', max_length=3)),
                ('control_thigh_avg', models.FloatField(default=0.0)),
                ('control_foot_avg', models.FloatField(default=0.0)),
                ('foot_tap_avg', models.FloatField(default=0.0)),
                ('speed_dribble_avg', models.FloatField(default=0.0)),
                ('dribble_r_avg', models.FloatField(default=0.0)),
                ('dribble_l_avg', models.FloatField(default=0.0)),
                ('dribble_3_cone_avg', models.FloatField(default=0.0)),
                ('long_r_1_avg', models.FloatField(default=0.0)),
                ('long_r_2_avg', models.FloatField(default=0.0)),
                ('long_l_1_avg', models.FloatField(default=0.0)),
                ('long_l_2_avg', models.FloatField(default=0.0)),
                ('cross_r_1_avg', models.FloatField(default=0.0)),
                ('cross_r_2_avg', models.FloatField(default=0.0)),
                ('cross_l_1_avg', models.FloatField(default=0.0)),
                ('cross_l_2_avg', models.FloatField(default=0.0)),
                ('side_pass_r_1_avg', models.FloatField(default=0.0)),
                ('side_pass_r_2_avg', models.FloatField(default=0.0)),
                ('side_pass_r_3_avg', models.FloatField(default=0.0)),
                ('side_pass_l_1_avg', models.FloatField(default=0.0)),
                ('side_pass_l_2_avg', models.FloatField(default=0.0)),
                ('side_pass_l_3_avg', models.FloatField(default=0.0)),
                ('weigh_pass_r_1_avg', models.FloatField(default=0.0)),
                ('weigh_pass_r_2_avg', models.FloatField(default=0.0)),
                ('weigh_pass_r_3_avg', models.FloatField(default=0.0)),
                ('weigh_pass_l_1_avg', models.FloatField(default=0.0)),
                ('weigh_pass_l_2_avg', models.FloatField(default=0.0)),
                ('weigh_pass_l_3_avg', models.FloatField(default=0.0)),
                ('throw_inside_1_avg', models.FloatField(default=0.0)),
                ('throw_inside_2_avg', models.FloatField(default=0.0)),
                ('throw_between_1_avg', models.FloatField(default=0.0)),
                ('throw_between_2_avg', models.FloatField(default=0.0)),
                ('shoot_pk_avg', models.FloatField(default=0.0)),
                ('shoot_run_r_1_avg', models.FloatField(default=0.0)),
                ('shoot_run_r_2_avg', models.FloatField(default=0.0)),
                ('shoot_run_r_3_avg', models.FloatField(default=0.0)),
                ('shoot_run_l_1_avg', models.FloatField(default=0.0)),
                ('shoot_run_l_2_avg', models.FloatField(default=0.0)),
                ('shoot_run_l_3_avg', models.FloatField(default=0.0)),
                ('finisher_r_1_avg', models.FloatField(default=0.0)),
                ('finisher_r_2_avg', models.FloatField(default=0.0)),
                ('finisher_r_3_avg', models.FloatField(default=0.0)),
                ('finisher_l_1_avg', models.FloatField(default=0.0)),
                ('finisher_l_2_avg', models.FloatField(default=0.0)),
                ('finisher_l_3_avg', models.FloatField(default=0.0)),
                ('total_control_avg', models.FloatField(default=0.0)),
                ('total_dribbling_avg', models.FloatField(default=0.0)),
                ('total_passing_avg', models.FloatField(default=0.0)),
                ('total_shooting_avg', models.FloatField(default=0.0)),
                ('grand_total_avg', models.FloatField(default=0.0)),
                ('club', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='showcase.Club')),
                ('coach', models.ForeignKey(blank=True, help_text='Associate the team to a coaches account here', null=True, on_delete=django.db.models.deletion.SET_NULL, to='showcase.Coach')),
            ],
        ),
        migrations.AddField(
            model_name='playerscorecard',
            name='showcase_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='showcase.Showcase'),
        ),
        migrations.AddField(
            model_name='player',
            name='team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='showcase.Team'),
        ),
    ]