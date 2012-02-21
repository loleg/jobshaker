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

});
