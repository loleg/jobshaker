$(function() {
	$(".datePicker").datepicker();
	$(".button").button();
	$(".btnCancel").click(function() { window.history.back(); });
});
