$(document).ready(function () {

	$(".datePicker").datepicker();
	$(".button").button();
	$(".btnCancel").click(function() { window.history.back(); });

	switch (document.location.pathname) {
	case '/':
		$('.menu .home').addClass('current'); break;
	case '/userprofile/':
		$('.menu .profile').addClass('current'); break;
	case '/userprofile/replies/':
		$('.menu .posts').addClass('current'); break;
	}
	
	$("#jobsearch input").on("keyup", function() {
		var searchterm = $.trim(this.value);
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
