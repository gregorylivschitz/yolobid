# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone


class DataSource(models.Model):
    created_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    external_location = models.CharField(max_length=255, blank=True, null=True)
    tournament = models.ForeignKey('Tournament', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'data_source'


class Game(models.Model):
    created_date = models.DateTimeField(blank=True, null=True)
    game_length_minutes = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    external_id = models.IntegerField(blank=True, null=True)
    data_source = models.ForeignKey(DataSource, blank=True, null=True)
    tournament = models.ForeignKey('Tournament', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'game'


class Player(models.Model):
    created_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    # role = models.CharField(max_length=255, blank=True, null=True)
    # image = models.CharField(max_length=255, blank=True, null=True)
    external_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'player'


class PlayerStats(models.Model):
    created_date = models.DateTimeField(blank=True, null=True)
    champion_played = models.CharField(max_length=255, blank=True, null=True)
    kills = models.IntegerField(blank=True, null=True)
    deaths = models.IntegerField(blank=True, null=True)
    assists = models.IntegerField(blank=True, null=True)
    gold = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    minions_killed = models.IntegerField(blank=True, null=True)
    game = models.ForeignKey(Game, blank=True, null=True)
    team = models.ForeignKey('Team', blank=True, null=True)
    player = models.ForeignKey(Player, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'player_stats'


class PlayerStatsDf(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    assists = models.BigIntegerField(blank=True, null=True)
    champion_played = models.TextField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    deaths = models.BigIntegerField(blank=True, null=True)
    game_id = models.BigIntegerField(blank=True, null=True)
    game_length_minutes = models.FloatField(blank=True, null=True)
    gold = models.FloatField(blank=True, null=True)
    id = models.BigIntegerField(blank=True, primary_key=True)
    kills = models.BigIntegerField(blank=True, null=True)
    minions_killed = models.BigIntegerField(blank=True, null=True)
    player_id = models.BigIntegerField(blank=True, null=True)
    player_name = models.TextField(blank=True, null=True)
    team_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'player_stats_df'


class ProcessedPlayerStatsDf(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    assists = models.BigIntegerField(blank=True, null=True)
    champion_played = models.TextField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    deaths = models.BigIntegerField(blank=True, null=True)
    game = models.ForeignKey(Game, blank=True, null=True)
    game_length_minutes = models.FloatField(blank=True, null=True)
    gold = models.FloatField(blank=True, null=True)
    id = models.BigIntegerField(blank=True, primary_key=True)
    kills = models.BigIntegerField(blank=True, null=True)
    minions_killed = models.BigIntegerField(blank=True, null=True)
    player_id = models.BigIntegerField(blank=True, null=True)
    player_name = models.TextField(blank=True, null=True)
    # team = models.ForeignKey('Team', blank=True, null=True)
    csum_game_length_minutes = models.FloatField(blank=True, null=True)
    csum_prev_game_length_minutes = models.FloatField(blank=True, null=True)
    per_min_game_length_minutes = models.FloatField(blank=True, null=True)
    csum_kills = models.BigIntegerField(blank=True, null=True)
    csum_prev_kills = models.BigIntegerField(blank=True, null=True)
    per_min_kills = models.FloatField(blank=True, null=True)
    csum_min_kills = models.FloatField(blank=True, null=True)
    csum_prev_min_kills = models.FloatField(blank=True, null=True)
    csum_deaths = models.BigIntegerField(blank=True, null=True)
    csum_prev_deaths = models.BigIntegerField(blank=True, null=True)
    per_min_deaths = models.FloatField(blank=True, null=True)
    csum_min_deaths = models.FloatField(blank=True, null=True)
    csum_prev_min_deaths = models.FloatField(blank=True, null=True)
    csum_assists = models.BigIntegerField(blank=True, null=True)
    csum_prev_assists = models.BigIntegerField(blank=True, null=True)
    per_min_assists = models.FloatField(blank=True, null=True)
    csum_min_assists = models.FloatField(blank=True, null=True)
    csum_prev_min_assists = models.FloatField(blank=True, null=True)
    csum_minions_killed = models.BigIntegerField(blank=True, null=True)
    csum_prev_minions_killed = models.BigIntegerField(blank=True, null=True)
    per_min_minions_killed = models.FloatField(blank=True, null=True)
    csum_min_minions_killed = models.FloatField(blank=True, null=True)
    csum_prev_min_minions_killed = models.FloatField(blank=True, null=True)
    csum_gold = models.FloatField(blank=True, null=True)
    csum_prev_gold = models.FloatField(blank=True, null=True)
    per_min_gold = models.FloatField(blank=True, null=True)
    csum_min_gold = models.FloatField(blank=True, null=True)
    csum_prev_min_gold = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'processed_player_stats_df'


class ProcessedTeamStatsDf(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    allowed_assists = models.BigIntegerField(blank=True, null=True)
    allowed_deaths = models.BigIntegerField(blank=True, null=True)
    allowed_gold = models.BigIntegerField(blank=True, null=True)
    allowed_kills = models.BigIntegerField(blank=True, null=True)
    allowed_minions_killed = models.BigIntegerField(blank=True, null=True)
    assists = models.BigIntegerField(blank=True, null=True)
    barons = models.BigIntegerField(blank=True, null=True)
    color = models.TextField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    deaths = models.BigIntegerField(blank=True, null=True)
    dragons = models.BigIntegerField(blank=True, null=True)
    game = models.ForeignKey(Game, blank=True, null=True)
    game_length_minutes = models.FloatField(blank=True, null=True)
    game_number = models.BigIntegerField(blank=True, null=True)
    gold = models.BigIntegerField(blank=True, null=True)
    id = models.BigIntegerField(primary_key=True)
    kills = models.BigIntegerField(blank=True, null=True)
    minions_killed = models.BigIntegerField(blank=True, null=True)
    team = models.ForeignKey('Team', blank=True, null=True)
    team_name = models.TextField(blank=True, null=True)
    total_gold = models.TextField(blank=True, null=True)
    turrets = models.BigIntegerField(blank=True, null=True)
    won = models.NullBooleanField()
    clean_kills = models.BigIntegerField(blank=True, null=True)
    allowed_clean_kills = models.BigIntegerField(blank=True, null=True)
    k_a = models.BigIntegerField(blank=True, null=True)
    a_over_k = models.FloatField(blank=True, null=True)
    allowed_k_a = models.BigIntegerField(blank=True, null=True)
    allowed_a_over_k = models.FloatField(blank=True, null=True)
    allowed_assists_for_game = models.BigIntegerField(blank=True, null=True)
    allowed_deaths_for_game = models.BigIntegerField(blank=True, null=True)
    allowed_gold_for_game = models.BigIntegerField(blank=True, null=True)
    allowed_kills_for_game = models.BigIntegerField(blank=True, null=True)
    allowed_minions_killed_for_game = models.BigIntegerField(blank=True, null=True)
    assists_for_game = models.BigIntegerField(blank=True, null=True)
    barons_for_game = models.BigIntegerField(blank=True, null=True)
    deaths_for_game = models.BigIntegerField(blank=True, null=True)
    dragons_for_game = models.BigIntegerField(blank=True, null=True)
    game_length_minutes_for_game = models.FloatField(blank=True, null=True)
    game_number_for_game = models.BigIntegerField(blank=True, null=True)
    gold_for_game = models.BigIntegerField(blank=True, null=True)
    id_for_game = models.BigIntegerField(blank=True, null=True)
    kills_for_game = models.BigIntegerField(blank=True, null=True)
    minions_killed_for_game = models.BigIntegerField(blank=True, null=True)
    team_id_for_game = models.BigIntegerField(blank=True, null=True)
    turrets_for_game = models.BigIntegerField(blank=True, null=True)
    won_for_game = models.NullBooleanField()
    clean_kills_for_game = models.BigIntegerField(blank=True, null=True)
    allowed_clean_kills_for_game = models.BigIntegerField(blank=True, null=True)
    k_a_for_game = models.BigIntegerField(blank=True, null=True)
    a_over_k_for_game = models.FloatField(blank=True, null=True)
    allowed_k_a_for_game = models.BigIntegerField(blank=True, null=True)
    allowed_a_over_k_for_game = models.FloatField(blank=True, null=True)
    csum_game_number = models.BigIntegerField(blank=True, null=True)
    csum_total_game_number = models.BigIntegerField(blank=True, null=True)
    csum_prev_game_number = models.BigIntegerField(blank=True, null=True)
    csum_total_prev_game_number = models.BigIntegerField(blank=True, null=True)
    csum_prev_avg_game_number = models.FloatField(blank=True, null=True)
    per_min_game_number = models.FloatField(blank=True, null=True)
    csum_prev_percent_game_number = models.FloatField(blank=True, null=True)
    margin_game_number = models.FloatField(blank=True, null=True)
    eff_game_number = models.FloatField(blank=True, null=True)
    csum_game_length_minutes = models.FloatField(blank=True, null=True)
    csum_total_game_length_minutes = models.FloatField(blank=True, null=True)
    csum_prev_game_length_minutes = models.FloatField(blank=True, null=True)
    csum_total_prev_game_length_minutes = models.FloatField(blank=True, null=True)
    csum_prev_avg_game_length_minutes = models.FloatField(blank=True, null=True)
    per_min_game_length_minutes = models.FloatField(blank=True, null=True)
    csum_prev_percent_game_length_minutes = models.FloatField(blank=True, null=True)
    margin_game_length_minutes = models.FloatField(blank=True, null=True)
    eff_game_length_minutes = models.FloatField(blank=True, null=True)
    csum_kills = models.BigIntegerField(blank=True, null=True)
    csum_total_kills = models.BigIntegerField(blank=True, null=True)
    csum_prev_kills = models.BigIntegerField(blank=True, null=True)
    csum_total_prev_kills = models.BigIntegerField(blank=True, null=True)
    csum_prev_avg_kills = models.FloatField(blank=True, null=True)
    per_min_kills = models.FloatField(blank=True, null=True)
    csum_prev_percent_kills = models.FloatField(blank=True, null=True)
    margin_kills = models.FloatField(blank=True, null=True)
    eff_kills = models.FloatField(blank=True, null=True)
    csum_min_kills = models.FloatField(blank=True, null=True)
    csum_prev_min_kills = models.FloatField(blank=True, null=True)
    csum_deaths = models.BigIntegerField(blank=True, null=True)
    csum_total_deaths = models.BigIntegerField(blank=True, null=True)
    csum_prev_deaths = models.BigIntegerField(blank=True, null=True)
    csum_total_prev_deaths = models.BigIntegerField(blank=True, null=True)
    csum_prev_avg_deaths = models.FloatField(blank=True, null=True)
    per_min_deaths = models.FloatField(blank=True, null=True)
    csum_prev_percent_deaths = models.FloatField(blank=True, null=True)
    margin_deaths = models.FloatField(blank=True, null=True)
    eff_deaths = models.FloatField(blank=True, null=True)
    csum_min_deaths = models.FloatField(blank=True, null=True)
    csum_prev_min_deaths = models.FloatField(blank=True, null=True)
    csum_assists = models.BigIntegerField(blank=True, null=True)
    csum_total_assists = models.BigIntegerField(blank=True, null=True)
    csum_prev_assists = models.BigIntegerField(blank=True, null=True)
    csum_total_prev_assists = models.BigIntegerField(blank=True, null=True)
    csum_prev_avg_assists = models.FloatField(blank=True, null=True)
    per_min_assists = models.FloatField(blank=True, null=True)
    csum_prev_percent_assists = models.FloatField(blank=True, null=True)
    margin_assists = models.FloatField(blank=True, null=True)
    eff_assists = models.FloatField(blank=True, null=True)
    csum_min_assists = models.FloatField(blank=True, null=True)
    csum_prev_min_assists = models.FloatField(blank=True, null=True)
    csum_minions_killed = models.BigIntegerField(blank=True, null=True)
    csum_total_minions_killed = models.BigIntegerField(blank=True, null=True)
    csum_prev_minions_killed = models.BigIntegerField(blank=True, null=True)
    csum_total_prev_minions_killed = models.BigIntegerField(blank=True, null=True)
    csum_prev_avg_minions_killed = models.FloatField(blank=True, null=True)
    per_min_minions_killed = models.FloatField(blank=True, null=True)
    csum_prev_percent_minions_killed = models.FloatField(blank=True, null=True)
    margin_minions_killed = models.FloatField(blank=True, null=True)
    eff_minions_killed = models.FloatField(blank=True, null=True)
    csum_min_minions_killed = models.FloatField(blank=True, null=True)
    csum_prev_min_minions_killed = models.FloatField(blank=True, null=True)
    csum_gold = models.BigIntegerField(blank=True, null=True)
    csum_total_gold = models.BigIntegerField(blank=True, null=True)
    csum_prev_gold = models.BigIntegerField(blank=True, null=True)
    csum_total_prev_gold = models.BigIntegerField(blank=True, null=True)
    csum_prev_avg_gold = models.FloatField(blank=True, null=True)
    per_min_gold = models.FloatField(blank=True, null=True)
    csum_prev_percent_gold = models.FloatField(blank=True, null=True)
    margin_gold = models.FloatField(blank=True, null=True)
    eff_gold = models.FloatField(blank=True, null=True)
    csum_min_gold = models.FloatField(blank=True, null=True)
    csum_prev_min_gold = models.FloatField(blank=True, null=True)
    csum_k_a = models.BigIntegerField(blank=True, null=True)
    csum_total_k_a = models.BigIntegerField(blank=True, null=True)
    csum_prev_k_a = models.BigIntegerField(blank=True, null=True)
    csum_total_prev_k_a = models.BigIntegerField(blank=True, null=True)
    csum_prev_avg_k_a = models.FloatField(blank=True, null=True)
    per_min_k_a = models.FloatField(blank=True, null=True)
    csum_prev_percent_k_a = models.FloatField(blank=True, null=True)
    margin_k_a = models.FloatField(blank=True, null=True)
    eff_k_a = models.FloatField(blank=True, null=True)
    csum_min_k_a = models.FloatField(blank=True, null=True)
    csum_prev_min_k_a = models.FloatField(blank=True, null=True)
    csum_a_over_k = models.FloatField(blank=True, null=True)
    csum_total_a_over_k = models.FloatField(blank=True, null=True)
    csum_prev_a_over_k = models.FloatField(blank=True, null=True)
    csum_total_prev_a_over_k = models.FloatField(blank=True, null=True)
    csum_prev_avg_a_over_k = models.FloatField(blank=True, null=True)
    per_min_a_over_k = models.FloatField(blank=True, null=True)
    csum_prev_percent_a_over_k = models.FloatField(blank=True, null=True)
    margin_a_over_k = models.FloatField(blank=True, null=True)
    eff_a_over_k = models.FloatField(blank=True, null=True)
    csum_min_a_over_k = models.FloatField(blank=True, null=True)
    csum_prev_min_a_over_k = models.FloatField(blank=True, null=True)
    csum_allowed_kills = models.BigIntegerField(blank=True, null=True)
    csum_total_allowed_kills = models.BigIntegerField(blank=True, null=True)
    csum_prev_allowed_kills = models.BigIntegerField(blank=True, null=True)
    csum_total_prev_allowed_kills = models.BigIntegerField(blank=True, null=True)
    csum_prev_avg_allowed_kills = models.FloatField(blank=True, null=True)
    per_min_allowed_kills = models.FloatField(blank=True, null=True)
    csum_prev_percent_allowed_kills = models.FloatField(blank=True, null=True)
    margin_allowed_kills = models.FloatField(blank=True, null=True)
    eff_allowed_kills = models.FloatField(blank=True, null=True)
    csum_min_allowed_kills = models.FloatField(blank=True, null=True)
    csum_prev_min_allowed_kills = models.FloatField(blank=True, null=True)
    csum_allowed_deaths = models.BigIntegerField(blank=True, null=True)
    csum_total_allowed_deaths = models.BigIntegerField(blank=True, null=True)
    csum_prev_allowed_deaths = models.BigIntegerField(blank=True, null=True)
    csum_total_prev_allowed_deaths = models.BigIntegerField(blank=True, null=True)
    csum_prev_avg_allowed_deaths = models.FloatField(blank=True, null=True)
    per_min_allowed_deaths = models.FloatField(blank=True, null=True)
    csum_prev_percent_allowed_deaths = models.FloatField(blank=True, null=True)
    margin_allowed_deaths = models.FloatField(blank=True, null=True)
    eff_allowed_deaths = models.FloatField(blank=True, null=True)
    csum_min_allowed_deaths = models.FloatField(blank=True, null=True)
    csum_prev_min_allowed_deaths = models.FloatField(blank=True, null=True)
    csum_allowed_assists = models.BigIntegerField(blank=True, null=True)
    csum_total_allowed_assists = models.BigIntegerField(blank=True, null=True)
    csum_prev_allowed_assists = models.BigIntegerField(blank=True, null=True)
    csum_total_prev_allowed_assists = models.BigIntegerField(blank=True, null=True)
    csum_prev_avg_allowed_assists = models.FloatField(blank=True, null=True)
    per_min_allowed_assists = models.FloatField(blank=True, null=True)
    csum_prev_percent_allowed_assists = models.FloatField(blank=True, null=True)
    margin_allowed_assists = models.FloatField(blank=True, null=True)
    eff_allowed_assists = models.FloatField(blank=True, null=True)
    csum_min_allowed_assists = models.FloatField(blank=True, null=True)
    csum_prev_min_allowed_assists = models.FloatField(blank=True, null=True)
    csum_allowed_minions_killed = models.BigIntegerField(blank=True, null=True)
    csum_total_allowed_minions_killed = models.BigIntegerField(blank=True, null=True)
    csum_prev_allowed_minions_killed = models.BigIntegerField(blank=True, null=True)
    csum_total_prev_allowed_minions_killed = models.BigIntegerField(blank=True, null=True)
    csum_prev_avg_allowed_minions_killed = models.FloatField(blank=True, null=True)
    per_min_allowed_minions_killed = models.FloatField(blank=True, null=True)
    csum_prev_percent_allowed_minions_killed = models.FloatField(blank=True, null=True)
    margin_allowed_minions_killed = models.FloatField(blank=True, null=True)
    eff_allowed_minions_killed = models.FloatField(blank=True, null=True)
    csum_min_allowed_minions_killed = models.FloatField(blank=True, null=True)
    csum_prev_min_allowed_minions_killed = models.FloatField(blank=True, null=True)
    csum_allowed_gold = models.BigIntegerField(blank=True, null=True)
    csum_total_allowed_gold = models.BigIntegerField(blank=True, null=True)
    csum_prev_allowed_gold = models.BigIntegerField(blank=True, null=True)
    csum_total_prev_allowed_gold = models.BigIntegerField(blank=True, null=True)
    csum_prev_avg_allowed_gold = models.FloatField(blank=True, null=True)
    per_min_allowed_gold = models.FloatField(blank=True, null=True)
    csum_prev_percent_allowed_gold = models.FloatField(blank=True, null=True)
    margin_allowed_gold = models.FloatField(blank=True, null=True)
    eff_allowed_gold = models.FloatField(blank=True, null=True)
    csum_min_allowed_gold = models.FloatField(blank=True, null=True)
    csum_prev_min_allowed_gold = models.FloatField(blank=True, null=True)
    csum_allowed_k_a = models.BigIntegerField(blank=True, null=True)
    csum_total_allowed_k_a = models.BigIntegerField(blank=True, null=True)
    csum_prev_allowed_k_a = models.BigIntegerField(blank=True, null=True)
    csum_total_prev_allowed_k_a = models.BigIntegerField(blank=True, null=True)
    csum_prev_avg_allowed_k_a = models.FloatField(blank=True, null=True)
    per_min_allowed_k_a = models.FloatField(blank=True, null=True)
    csum_prev_percent_allowed_k_a = models.FloatField(blank=True, null=True)
    margin_allowed_k_a = models.FloatField(blank=True, null=True)
    eff_allowed_k_a = models.FloatField(blank=True, null=True)
    csum_min_allowed_k_a = models.FloatField(blank=True, null=True)
    csum_prev_min_allowed_k_a = models.FloatField(blank=True, null=True)
    csum_allowed_a_over_k = models.FloatField(blank=True, null=True)
    csum_total_allowed_a_over_k = models.FloatField(blank=True, null=True)
    csum_prev_allowed_a_over_k = models.FloatField(blank=True, null=True)
    csum_total_prev_allowed_a_over_k = models.FloatField(blank=True, null=True)
    csum_prev_avg_allowed_a_over_k = models.FloatField(blank=True, null=True)
    per_min_allowed_a_over_k = models.FloatField(blank=True, null=True)
    csum_prev_percent_allowed_a_over_k = models.FloatField(blank=True, null=True)
    margin_allowed_a_over_k = models.FloatField(blank=True, null=True)
    eff_allowed_a_over_k = models.FloatField(blank=True, null=True)
    csum_min_allowed_a_over_k = models.FloatField(blank=True, null=True)
    csum_prev_min_allowed_a_over_k = models.FloatField(blank=True, null=True)
    csum_prev_kda = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'processed_team_stats_df'


class Team(models.Model):
    created_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    external_name = models.CharField(max_length=255, blank=True, null=True)
    external_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'team'


class TopTenTeam(models.Model):
    created_date = models.DateTimeField(blank=True, null=True, default=timezone.now())
    name = models.CharField(max_length=255, blank=True, null=True)
    score = models.IntegerField(blank=True, null=True)
    rank = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'top_ten_team'

class TeamPlayer(models.Model):
    team = models.ForeignKey(Team, blank=True, null=True)
    player = models.ForeignKey(Player, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'team_player'


class TeamStats(models.Model):
    created_date = models.DateTimeField(blank=True, null=True)
    total_gold = models.CharField(max_length=255, blank=True, null=True)
    won = models.NullBooleanField()
    color = models.CharField(max_length=255, blank=True, null=True)
    deaths = models.IntegerField(blank=True, null=True)
    minions_killed = models.IntegerField(blank=True, null=True)
    assists = models.IntegerField(blank=True, null=True)
    kills = models.IntegerField(blank=True, null=True)
    gold = models.IntegerField(blank=True, null=True)
    barons = models.IntegerField(blank=True, null=True)
    dragons = models.IntegerField(blank=True, null=True)
    turrets = models.IntegerField(blank=True, null=True)
    team = models.ForeignKey(Team, blank=True, null=True)
    game = models.ForeignKey(Game, blank=True, null=True)
    game_number = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'team_stats'


class TeamStatsDf(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    assists = models.BigIntegerField(blank=True, null=True)
    barons = models.BigIntegerField(blank=True, null=True)
    color = models.TextField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    deaths = models.BigIntegerField(blank=True, null=True)
    dragons = models.BigIntegerField(blank=True, null=True)
    game_id = models.BigIntegerField(blank=True, null=True)
    game_length_minutes = models.FloatField(blank=True, null=True)
    game_number = models.BigIntegerField(blank=True, null=True)
    gold = models.BigIntegerField(blank=True, null=True)
    id = models.BigIntegerField(blank=True, primary_key=True)
    kills = models.BigIntegerField(blank=True, null=True)
    minions_killed = models.BigIntegerField(blank=True, null=True)
    team_id = models.BigIntegerField(blank=True, null=True)
    team_name = models.TextField(blank=True, null=True)
    total_gold = models.FloatField(blank=True, null=True)
    turrets = models.BigIntegerField(blank=True, null=True)
    won = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'team_stats_df'


class Tournament(models.Model):
    created_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    region = models.CharField(max_length=255, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    season = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tournament'
