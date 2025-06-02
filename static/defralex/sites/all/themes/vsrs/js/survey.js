/*Survey
 *
 One-liner: Adds survey link to right of page
 Requirements: jQuery framework: http://jquery.com/
 
 Notes:
 
 History:
 v0.01	TE Created
 
 */
 (function($) {
 $(document).ready(function(){
	 
	 var link = "#";
	 
		 
	 
	 // problems with z-index and positioning, open external window instead
	 //if($.browser.msie && $.browser.version < 7){
		 $("#feedback")
		 .hover(function() {
			 $(this).animate({width: "38px"}, {duration: 100, queue: false});
		 },
		 function() {
				$(this).animate({width: "30px"}, {duration: 100, queue: false});
		 })
		 
		 /*$("#feedback").click(function(){
				window.open(link);
		 });*/
		 
		 // move up if obscured
		 if ($(window).height() < 450)
		 {
				 $("#feedback").css("top", "240px");
		 }
 });
 })(jQuery);