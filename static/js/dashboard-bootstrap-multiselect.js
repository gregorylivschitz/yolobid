$(document).ready(function() {
    $('#id_team_predictor_values').multiselect({
        buttonClass: 'btn btn-theme',
        includeSelectAllOption: true,
        enableCaseInsensitiveFiltering: true
    });
    $('#id_player_stats_to_predict').multiselect({
        buttonClass: 'btn btn-theme',
        includeSelectAllOption: true
    });
//    $('#select-default-predictors-button').on('click', function() {
//        $('#select-predictors').multiselect('select', ['mushrooms', 'mozarella']);
//    });
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
    });
    $('#id_player_predictor_values').multiselect({
        buttonClass: 'btn btn-theme',
    });
    $('#select-columns-team').multiselect({
        buttonClass: 'btn btn-theme',
    });
    $('#select-columns-filters').multiselect({
        buttonClass: 'btn btn-theme',
        buttonContainer: '<div class="col-md-4"/>'
    });
});


$(function () {
    Morris.Donut({
      element: 'team-donut-chart',
      data: [
        {label: "CLG", value: 40},
        {label: "TSM", value: 60},
      ],
      formatter: function (y, data) { return y + '%' },
      colors: ["#085e86", "#A80818"]
    });
    Morris.Donut({
      element: 'player-donut-chart',
      data: [
        {label: "Predicted Kills", value: 4.3},
        {label: "Predicted Assists", value: 7},
        {label: "Predicted Deaths", value: 9},
      ],
    });
});
