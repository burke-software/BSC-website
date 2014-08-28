$(document).ready(function(){
    /* Initialise bxSlider */
    $('.bxslider').bxSlider({
        captions: true
    });

    //Apply img-thumbnail class to body-content images
    $('.body-content img').addClass("img-thumbnail");

    $(document).scroll(function() {
		var scrollTop = $(this).scrollTop();
		var heroHeight = $('#hero').height();
		var heroStripHeight = $('.hero-strip').height();

		if (scrollTop > heroHeight/2 + heroStripHeight/2) {
			$('.navbar-brand').fadeIn();
		} else {
			$('.navbar-brand').fadeOut();
		}
	});
});