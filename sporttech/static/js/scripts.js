/* DATE IN NAVBAR */

$(function () {
    $("#insert-date").text(function () {
        var monthNames = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sept", "Oct", "Nov", "Dec"];
        var today = new Date();
        var new_date = monthNames[today.getMonth()] + " " + today.getDate() + ", " + today.getFullYear();
        return new_date;
    });
});


/* SMOOTH SCROLL TO ANCHOR LINKS */

$(document).on("click", 'a[href^="#"]', function (event) {
    event.preventDefault();
    var href = $.attr(this, 'href');
    $("html, body").animate({
        scrollTop: $(href).offset().top
    }, 550, function () {
        window.location.hash = href;
    });
});



/* SELECTABLE DROPDOWN MENU */

$(function () {
    $(".dropdown-menu a:not(.disabled)").click(function () {
        $(this).parents(".dropdown").find('.btn').html($(this).text() + ' <span class="caret"></span>');
        $(this).parents(".dropdown").find('.btn').val($(this).data('value'));
        $(this).parents(".dropdown").find('.dropdown-toggle').dropdown('toggle');
    });
});

function loadChart(data) {
    var chart;
    if (data === 1) {
        chart = barChart;
        var c = 'selection_1';
        var d = 'selection_2';
    } else {
        chart = barChart2;
        var c = 'selection_3';
        var d = 'selection_4';
    };
    var a = document.getElementById(c).value;
    var b = document.getElementById(d).value;
    var data1 = playerData[a];
    var data2 = playerData[b];
    var col = [data1, data2];
    chart.data.colors()[data1[0]] = "rgb(68, 170, 67)";
    chart.data.colors()[data2[0]] = "rgb(53, 80, 139)";
    chart.load({
        unload:true,
        columns: col
    });
};
/*MAKE TH FIXED IF PLUGIN LOADED*/

$(function () {
    if (jQuery().floatThead) {
        $('table.stats-table').floatThead({
            position: 'fixed',
            top: $('#top-menu').height()
        });
    }
});

/*ADD INFO BUTOONS*/

$(function () {
    $(".info-full").each(function () {
        $(this).wrap("<span style='position:relative;display:inline-block'></span>");
        $(this).after("<a href='#' class='info-i-button'></a>");
    });

    $(".info-full").siblings(".info-i-button").popover({
        content: `Each Technique's score is based on scores from multiple stations. See Player Stats & Club Stats for more detail.`,
        trigger: "click",
        placement: "bottom",
        container: "body",
        html: true,
        boundary: "window"
    });
    $('html').on('click', function(e) {
        if (typeof $(e.target).data('original-title') == 'undefined' &&
           !$(e.target).parents().is('.popover.in')) {
          $('[data-original-title]').popover('hide');
        }
      });
});

