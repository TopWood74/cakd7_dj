jQuery(document).ready(function($) {
    var index = 0;
    $("#navbar-menu .nav-item .nav-link").each(function(oi) {
        var url = $(this).attr("href")
        var pathname = window.location.pathname.substr(0,url.length)
        if (pathname == url) { index = oi; }
    });
    $("#navbar-menu .nav-item").eq(index).addClass('active');
});
