$(document).ready(function(){
    /* Initialise bxSlider */
    $('.bxslider').bxSlider({
        captions: true
    });

    //Apply img-thumbnail class to body-content images
    $('.body-content img').addClass("img-thumbnail");

    // For the Person page. Hide bios at smaller sizes.
    showOrHideBio();
});


function showOrHideBio() {
	if ($(window).width() < 767) {
	    $('.person-biography').hide();
	} else {
	    $('.person-biography').show();
	}
};

var resizeTimer;
$(window).resize(function() {
    clearTimeout(resizeTimer);
    resizeTimer = setTimeout(showOrHideBio, 100);
});


$('.person-bio-trigger').click(function() {
	if ($(window).width() < 767) {
		$(this).parent().next('.person-biography').slideToggle();

		if ($(this).find('.fa').hasClass('fa-angle-right')) {
			$(this).find('.fa').removeClass('fa-angle-right').addClass('fa-angle-down');
		} else if ($(this).find('.fa').hasClass('fa-angle-down')) {
			$(this).find('.fa').removeClass('fa-angle-down').addClass('fa-angle-right');
		}
	}
});