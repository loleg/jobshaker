$(document).ready(function () {

	// Initialize UI components
	$(".datePicker").datepicker();
	$(".button").button();
	
	// Setup form submits
	$(".btnCancel").click(function() { window.history.back(); });
	$(".btnSend").click(function() { this.disabled = true; $(this).addClass("disabled"); });

	// Menu navigation
	switch (document.location.pathname) {
	case '/':
		$('.menu .home').addClass('current'); break;
	case '/userprofile/':
		$('.menu .profile').addClass('current'); break;
	case '/userprofile/replies/':
		$('.menu .posts').addClass('current'); break;
	}
	
	// Keyword search field
	$("#jobsearch input").on("keyup", function() {
		var searchterm = $.trim(this.value.toLowerCase());
		var searchflds = ".tags li:contains('" + searchterm + "')";
		$(".post").each(function() {
			if (searchterm == "" || $(this).find(searchflds).length > 0) {
				$(this).show();
			} else {
				$(this).hide();
			}
		});
	});
	
});
