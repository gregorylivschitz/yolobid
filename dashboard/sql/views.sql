create view processed_team_stats_df_limit_5 as (select *
from processed_team_stats_df
where game_id in (select distinct game_id
from processed_team_stats_df ts1 where (select count(*) from processed_team_stats_df ts2
where ts2.team_id = ts1.team_id and ts2.game_id >= ts1.game_id) <=5
)order by game_id);

create view processed_player_stats_df_limit_5 as (select *
from processed_player_stats_df ps1 where (select count(*) from processed_player_stats_df ps2 
where ps2.team_id = ps1.team_id and ps2.game_id >= ps1.game_id) <=5
order by game_id);


create view processed_team_stats_df_limit_10 as (select *
from processed_team_stats_df
where game_id in (select distinct game_id
from processed_team_stats_df ts1 where (select count(*) from processed_team_stats_df ts2
where ts2.team_id = ts1.team_id and ts2.game_id >= ts1.game_id) <=10
)order by game_id);

create view processed_player_stats_df_limit_10 as (select *
from processed_player_stats_df ps1 where (select count(*) from processed_player_stats_df ps2 
where ps2.team_id = ps1.team_id and ps2.game_id >= ps1.game_id) <=10
order by game_id);