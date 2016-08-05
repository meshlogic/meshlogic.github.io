/*******************************************************************************
** Make Navbar sticky in the top when scrolling page down
*******************************************************************************/
$('.navbar').affix({
	offset: {
		top: $('header').height() + 20
	}
});
	
function update_navbar_width(){
	var w = $('.container').width();
	$('.navbar').width(w);
}

$(document).ready(function(){
    update_navbar_width()
});

$(window).resize(function(){
    update_navbar_width()
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
    $("a#sourcelink").attr('target', '_blank');
});


/*******************************************************************************
** Colorbox
*******************************************************************************/
$('a.image-reference:not(.islink) img:not(.islink)').parent().colorbox({rel:"gal", maxWidth:"100%", maxHeight:"100%", scalePhotos:true, transition:"elastic", speed:300, fadeOut:300});


