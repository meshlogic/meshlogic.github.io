/*******************************************************************************
** Include sidebar from root output folder
*******************************************************************************/
$(function(){
    $("#page_sidebar").load("/sidebar-en.inc"); 
});


/*******************************************************************************
** - Make Navbar sticky on top when the page scrolls down
** - Keep Navbar width inside container
*******************************************************************************/
var offsetTop = $('#body_header').outerHeight() + parseInt($('body').css('padding-top'), 10);

function stiky_navbar()
{
    var scrollTop = $(document).scrollTop();

    if (scrollTop >= offsetTop)
        $('.navbar').removeClass('navbar-static-top').addClass('navbar-fixed-top');
    else
        $('.navbar').removeClass('navbar-fixed-top').addClass('navbar-static-top');
}

function update_navbar_width()
{
    var w = $('.container').width();
    $('.navbar').width(w);
}

$(document).ready(function(){
    update_navbar_width();
    stiky_navbar();
});

$(window).resize(function(){
    update_navbar_width();
    stiky_navbar();
});

$(document).scroll(function(){
    stiky_navbar();
});


/*******************************************************************************
** Add target _blank to specified links
*******************************************************************************/
/* Add target _blank to external links */
$(document).ready(function() {
    $("a[href^='http']").attr('target','_blank');
});

/* Add target _blank to source links */
$(document).ready(function(){
    $("a.sourcelink").attr('target', '_blank');
});


/*******************************************************************************
** Colorbox
*******************************************************************************/
$('a.image-reference:not(.islink) img:not(.islink)').parent().colorbox({rel:"gal", maxWidth:"100%", maxHeight:"100%", scalePhotos:true, transition:"elastic", speed:300, fadeOut:300});


