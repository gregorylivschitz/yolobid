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
    var ajaxCallWithButton = function(form_id, form_button_id, chart_id){
        $(form_id).on('submit', function(e) {
            e.preventDefault();
            var btnName = $(form_button_id).attr('name');
            var btnVal = $(form_button_id).val();
            var btnData = '&'+btnName+'='+btnVal;
            $.ajax({
                url : "http://127.0.0.1:8000/dashboard_test/",
                type: "POST",
                data: $(this).serialize() + btnData,
                success: function (data) {
                    $("#team-donut-chart").html("");
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
    ajaxCallWithButton('#predict-team-outcome', '#submit-id-submit_team', 'team-donut-chart')
});


//$(function () {
//    Morris.Donut({
//      element: 'team-donut-chart',
//      data: [
//        {label: "CLG", value: 40},
//        {label: "TSM", value: 60},
//      ],
//      formatter: function (y, data) { return y + '%' },
//      colors: ["#085e86", "#A80818"]
//    });
//    Morris.Donut({
//      element: 'player-donut-chart',
//      data: [
//        {label: "Predicted Kills", value: 4.3},
//        {label: "Predicted Assists", value: 7},
//        {label: "Predicted Deaths", value: 9},
//      ],
//    });
//});
