$(document).ready(function() {
    $('#id_team_predictor_values').multiselect({
        buttonClass: 'btn btn-theme',
        includeSelectAllOption: true,
        enableCaseInsensitiveFiltering: true
    });
    $('#id_player_stats_to_predict').multiselect({
        buttonClass: 'btn btn-theme',
        includeSelectAllOption: true,
        enableCaseInsensitiveFiltering: true
    });
    $('#id_blue_team').multiselect({
        buttonClass: 'btn btn-blue',
        enableCaseInsensitiveFiltering: true,
    });
    $('#id_red_team').multiselect({
        buttonClass: 'btn btn-dashboard-red form-control',
        enableCaseInsensitiveFiltering: true,
    });
    $('#id_player_name').multiselect({
        buttonClass: 'btn btn-theme',
        enableCaseInsensitiveFiltering: true,
    });
    $('#id_player_predictor_values').multiselect({
        buttonClass: 'btn btn-theme',
        enableCaseInsensitiveFiltering: true,
    });
    $('#select-columns-team').multiselect({
        buttonClass: 'btn btn-theme',
        enableCaseInsensitiveFiltering: true,
    });
    $('#select-columns-filters').multiselect({
        buttonClass: 'btn btn-theme',
        buttonContainer: '<div class="col-md-4"/>'
    });
    $('#id_opposing_team').multiselect({
        buttonClass: 'btn btn-theme',
        enableCaseInsensitiveFiltering: true,
    });
    $('#id_player_game_range').multiselect({
        buttonClass: 'btn btn-theme',
        enableCaseInsensitiveFiltering: true,
    });
    $('#id_team_game_range').multiselect({
        buttonClass: 'btn btn-theme',
        enableCaseInsensitiveFiltering: true,
    });
    var ajaxCallTeamWithButton = function(form_id, form_button_id, chart_id){
        $(form_id).on('submit', function(e) {
            e.preventDefault();
            var btnName = $(form_button_id).attr('name');
            var btnVal = $(form_button_id).val();
            var btnData = '&'+btnName+'='+btnVal;
            $.ajax({
                url : "http://127.0.0.1:8000/dashboard/",
                type: "POST",
                data: $(this).serialize() + btnData,
                success: function (data) {
                    $(chart_id).html("");
                    Morris.Donut({
                        element: 'team-donut-chart',
                        data: data['data'],
                        formatter: function (y, data) { return Math.round(y * 100) + '%' },
                        colors: ["#085e86", "#A80818"]
                    });},
                error: function (jXHR, textStatus, errorThrown) {
                    alert(errorThrown);
                }
            });
        });
    }
    var ajaxCallPlayerWithButton = function(form_id, form_button_id, chart_id){
        $(form_id).on('submit', function(e) {
            e.preventDefault();
            var btnName = $(form_button_id).attr('name');
            var btnVal = $(form_button_id).val();
            var btnData = '&'+btnName+'='+btnVal;
            $.ajax({
                url : "http://127.0.0.1:8000/dashboard/",
                type: "POST",
                data: $(this).serialize() + btnData,
                success: function (data) {
                    $(chart_id).html("");
                    Morris.Donut({
                        element: 'player-donut-chart',
                        data: data['data'],
                        formatter: function (y, data) { return y.toFixed(2) },
                    });},
                error: function (jXHR, textStatus, errorThrown) {
                    alert(errorThrown);
                }
            });
        });
    }
    ajaxCallTeamWithButton('#predict-team-outcome', '#submit-id-submit_team', '#team-donut-chart')
    ajaxCallPlayerWithButton('#predict-player-outcome', '#submit-id-submit_player', '#player-donut-chart')
});