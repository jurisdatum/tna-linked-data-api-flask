(function ($) {
	$(document).ready(function(){
		$(".help").css({"display" : "none"});
		// Helpbox popups
		$("a.helpItemToTop").legHelpBox({horizBoxPos: 'middle', vertiBoxPos: 'top'});	
		$("a.helpItemToBot").legHelpBox({horizBoxPos: 'middle', vertiBoxPos: 'bottom'});
		$("a.helpItemToMidLeft").legHelpBox({horizBoxPos: 'left', vertiBoxPos: 'middle'});	
		$("a.helpItemToMidRight").legHelpBox({horizBoxPos: 'right',	vertiBoxPos: 'middle'});	
		$("a.helpItemToLeft").legHelpBox({horizBoxPos: 'left',vertiBoxPos: 'top'});	
		$("a.helpItemToRight").legHelpBox({horizBoxPos: 'right',	vertiBoxPos: 'top'});
		$("a.hover").legHelpBox({horizBoxPos: 'left', vertiBoxPos: 'middle', hover: "yes"});		   
	});

	/*

	Legislation HelpBox

	One-liner: Adds floating helpbox when help link clicked
	Requirements: jQuery framework: http://jquery.com/
	helpItem - The link that activated popup
	help - The popup contents

	Notes:


	History:
	v0.01	TE Created
	v0.02	2010-04-27	GE	Modified close link to reference box rather than 'this' hierachy so it will close box in any position
	v0.03	2010-04-27	GE	Added options to position where the box appears
	v0.04 2010-09-16	TE	Added hover functionality

	*/

	$.fn.legHelpBox = function(helpBoxOptions) {
			
		$(this).each(function () {		
				// retrieve helpbox associated with link
				var helpbox = $($(this).attr('href'));
				
				// Config area
				var defaults = {
					horizBoxPos: 'right', 
					vertiBoxPos: 'top',
					hover: "no"	
				}
				
				var option = $.extend(defaults, helpBoxOptions); // overwrite defaults if options were passed during init
				
				//set initial state			
				helpbox.css({display: "none", position: "absolute"});
				
				$(this).parent().append(helpbox); // fix tab order
				
				// enable helpbox images
				// enable helpbox arrow
				$(".icon", $(this)).css({
					display: "block"
					});
				
				if (option.hover == "no")
					$(".close", helpbox).show();
				else
					$(".close", helpbox).css("display", "none");
				
				$(".close", helpbox).click(function(e) {
					e.preventDefault(); // disable anchor link
					helpbox.animate({opacity: "hide"}, "fast");
				});
				
				var popup = function(e){
									var offset = $(this).position(); // offset from parent element
									
									/*
									-------- Set the position based on the config and add classes to show arrows -----------
									Use outerWidth() to include padding in measurements as width() does not find this.
									Include the link height in calculations to get absolute middle
									The calculation order cascades down with the later conditionals taking precedent over the first
									*/
									// Set the options for vertically positioned top and bottom boxes
									(option.horizBoxPos == 'left') ? leftPosition = 0-(helpbox.outerWidth()) : leftPosition = 20;
									(option.vertiBoxPos == 'top') ?  topShowPosition = 0-(helpbox.outerHeight()+10) : topShowPosition = 15;
									
									// Set the options for middle positioned boxes
									if (option.horizBoxPos == 'middle')
										leftPosition = 0-(helpbox.outerWidth()/2)+$(this).outerWidth()/2;
									
									// Set the options for to the side top positioned boxes
									if (option.horizBoxPos != 'middle' && option.vertiBoxPos == 'top')
										topShowPosition = -15;
										
									// Set the options for to the side middle positioned boxes
									if (option.horizBoxPos != 'middle' && option.vertiBoxPos == 'middle')
										topShowPosition = 0-(helpbox.outerHeight()/2)+$(this).outerHeight()/2;									
										
									topHidePosition = 0;
									
									addClasses();
									
									e.preventDefault(); // disable anchor link		
									
									// fix for IE7 - z-index is reset for positioned list elements. Ensures popup's parent has higher z-index than its siblings
									$(this).parent('li').css('z-index', 5).siblings('li').css('z-index',1);
									
									if (helpbox.css("display") == "none")
									{
										$(".help").animate({opacity: "hide"}, "fast"); // hide other helpboxes
										
										// topShowPosition,topHidePosition & leftPosition from inialisation
										helpbox.css({left: offset["left"] + leftPosition, top: offset["top"] + topHidePosition} ); //reset position
										
										helpbox.animate({opacity: "show", left: offset["left"] + leftPosition, top: offset["top"] + topShowPosition}, "fast", function() {
													
																																									   });
									}
									else
									{
										helpbox.animate({opacity: "hide", left: offset["left"] + leftPosition, top: offset["top"] + topHidePosition}, "fast");
									}
				
						
					
					function addClasses() {
						/* This function decides the class that gets added to the box
						   Format is helpTo[horizontalPosition][verticalPosition]		   
						   Usually this is to add an arrow in the right position, add side highlighting, etc.		
						*/
						
						// Use shorter var names for easier reading
						var opH = option.horizBoxPos;
						var opV = option.vertiBoxPos
						
						if (opH == 'left' && opV =='top'){
							helpbox.addClass('helpToLeftTop');		
						} else if (opH == 'left' && opV =='middle') {
							helpbox.addClass('helpToLeftMid');	
						} else if (opH == 'left' && opV =='bottom') {
							helpbox.addClass('helpToLeftBot');	
						} else if (opH == 'right' && opV =='top') {
							helpbox.addClass('helpToRightTop');	
						} else if (opH == 'right' && opV =='middle') {
							helpbox.addClass('helpToRightMid');	
						} else if (opH == 'right' && opV =='bottom') {
							helpbox.addClass('helpToRightBot');	
						} else if (opH == 'middle' && opV =='top') {
							helpbox.addClass('helpToMidBot');			
							// Middle Middle can't exist as it would put it over the link itself
						} else if (opH == 'middle' && opV =='bottom') {
							helpbox.addClass('helpToMidTop');	
						}
					}
				};
				
				// fade popup in/out on help link click
				$(this)
				.click(popup)
				// te - add hide when click outside helpbox
				.click(function (e) {
					$(document).bind("click.hidethepop", function (e) {
						helpbox.animate({opacity: "hide"});
						$(document).unbind("click.hidethepop");
					});
					 // dont close thepop when you click on thepop
				    jQuery(helpbox).click(function(e) {
				        e.stopPropagation();
				    });

					e.stopPropagation();
				});
				
				if (option.hover == "yes")
				{
					$(this)
					.hover(popup, function () {
						helpbox.animate({opacity: "hide"}, "fast");
					});
				}
				
		});
	};
	
		//expand
	
	/*
	(c)  Crown copyright
	 
	You may use and re-use this code free of charge under the terms of the Open Government Licence v3.0
	 
	http://www.nationalarchives.gov.uk/doc/open-government-licence/version/3

	*/
	/*
	Legislation Expand and Collapse

	One-liner: Expand and collapse box with the controlling link being created by another function
	Usage: .legExpandCollapse(['More', 'Close'], cookieArray);
	Requirements: jQuery framework: http://jquery.com/
	Notes:
	CSS - position: relative on the expanding element causes problems with IE by rendering all child
	elements after the animation, avoid if possible. By using on a child element that element is 
	rendered before the animation has begun and could look confusing.
	CookieArray is an object used to store cookie key value pairs. If it isnt passed, will default to contracted

	History:
	v0.01	GM	Created
	v0.02	GM	2010-03-15	Changed open/close text from 'open' to 'more'
	v0.03	TE 	2010-06-22	Added persistance using cookie

	*/
	$.fn.legExpandCollapse = function(htmlValues_arr, options){

		if (options)
		{
			var cookieArray = options.state;
			var expires = options.expires;
			if (!expires)
				expires = 0;
			var open = options.open;
		}
		
		if (cookieArray)
			readCookie("legExpandCollapse", cookieArray);
		var href = $(this).attr("href");
		
		var htmlExpanded, htmlContracted;
		
		// Check to see if any values have been passed to overwrite the defaults
		if (htmlValues_arr) {
			htmlContracted = htmlValues_arr[0];
			htmlExpanded = htmlValues_arr[1];
		}
		else {
			htmlContracted = "More";
			htmlExpanded = "Close";
		}
		
		// default is to hide the element
		if (href && cookieArray && (cookieArray[href.substring(1)] == "show")) {
			$(this).html(htmlExpanded).addClass("close");
			$(this).closest('.section').addClass("close");
			$($(this).attr('href')).show();
		}
		else if (href && cookieArray && (cookieArray[href.substring(1)] == "hide")) {
			$(this).html(htmlContracted);
			$(this).closest('.section').removeClass("close");
			$($(this).attr('href')).hide();
		}
		//default open
		else if (open)
		{
			$(this).html(htmlExpanded).addClass("close");
			$(this).closest('.section').addClass("close");
			$($(this).attr('href')).show();
			
		}
		else {	
			$(this).html(htmlContracted);
			$(this).closest('.section').removeClass("close");
			$($(this).attr('href')).hide();
		}
		
		// Event Handlers
		return $(this).click(function(e){
			if (!$(this).hasClass("close")) {
				var href = $(this).attr("href");
				$(href).slideDown(400);
				$(this).html(htmlExpanded).toggleClass("close");
				$(this).closest('.section').addClass("close");
				if (cookieArray)
					updateid("legExpandCollapse", cookieArray, href.substring(1), "show", expires);
				e.preventDefault();
			}
			else {
				var href = $(this).attr("href");
				$(href).slideUp(400);
				$(this).html(htmlContracted).toggleClass("close");
				$(this).closest('.section').removeClass("close");
				if (cookieArray)
					updateid("legExpandCollapse", cookieArray, href.substring(1), "hide", expires);
				e.preventDefault();
			}
		});
			
		/*
		 * Cookie Code
		 */
		
		function updateid(cookieName, cookieContents, id, value, cookieExpire) {
			cookieContents[id] = value;
			updateCookie(cookieName, cookieContents, cookieExpire);
		}
		
		function deleteid(cookieName, cookieContents, id, cookieExpire) {
			delete cookieContents[id];		
			updateCookie(cookieName, cookieContents, cookieExpire);
		}
		
		function updateCookie(cookieName, cookieContents, cookieExpire) {
			var temp = "";
			for (var i in cookieContents)
			{
					temp += (i + "#" + cookieContents[i] + ";");
			}		
			
			if (!cookieExpire)
				var cookieExpire = null;
			
			$.cookie(cookieName, temp, {path: '/', expires: cookieExpire});
		}
		
		// format is id#page;id#page
		function readCookie(cookieName, cookieContents) {
			var cookie = $.cookie(cookieName);
			if (cookie)
			{
				var elements = cookie.split(';');
			
				for (var i = 0; i < elements.length; i++) {
					if (elements[i] != "") 
					{
						var value = elements[i].split("#");
						var page = value[0];
						var value = value[1];
						cookieContents[page] = value;
					}				
				}		
			}		
		}
		
		function eraseCookie(cookieName) {
			$.cookie(cookieName, null, {path: "/"});
		}	
	};
	
}(jQuery));