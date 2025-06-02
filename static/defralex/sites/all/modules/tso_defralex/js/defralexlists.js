(function($) {

	$.QueryString = (function(a) {
        if (a == "") return {};
        var b = {};
        for (var i = 0; i < a.length; ++i)
        {
            var p=a[i].split('=');
            if (p.length != 2) continue;
            b[p[0]] = decodeURIComponent(p[1].replace(/\+/g, " "));
        }
        return b;
    })(window.location.search.substr(1).split('&'))




	$(document).ready(function() {
		
		//checkbox
		var url = $.QueryString;
		var urlExtent = $.QueryString['extent'];
		var recursiveEncoded = $.param( url );
		var recursiveDecoded = decodeURIComponent( $.param( url ) );
	
		if ($("#facet_status").length){
			// Slightly different way of adding the links, wrap the <a> element around the <h2> inner HTML
			var $facet_statusTitle = $(".title:first", "#facet_status").children("h3");
			var facet_statusTitleTxt = $facet_statusTitle.html();	 
			// Reset the inner HTML to nothing as added when open/close link is added
			$facet_statusTitle.html("");
			
			$("<a/>")
			.attr('href', '#openingfacet_status')
			.addClass("expandCollapseLink")	
			.appendTo($facet_statusTitle)
			.legExpandCollapse([facet_statusTitleTxt+'<span class="accessibleText">Expand opening options</span>',facet_statusTitleTxt+'<span class="accessibleText">Collapse opening options</span>'], {open: "open"});
		}


		if ($("#facet_year").length){
			// Slightly different way of adding the links, wrap the <a> element around the <h2> inner HTML
			var $facet_yearTitle = $(".title:first", "#facet_year").children("h3");
			var facet_yearTitleTxt = $facet_yearTitle.html();	 
			// Reset the inner HTML to nothing as added when open/close link is added
			$facet_yearTitle.html("");
			
			$("<a/>")
			.attr('href', '#openingfacet_year')
			.addClass("expandCollapseLink")	
			.appendTo($facet_yearTitle)
			.legExpandCollapse([facet_yearTitleTxt+'<span class="accessibleText">Expand opening options</span>',facet_yearTitleTxt+'<span class="accessibleText">Collapse opening options</span>'], {open: "open"});
		}

		if ($("#facet_type").length){
			// Slightly different way of adding the links, wrap the <a> element around the <h2> inner HTML
			var $facet_typeTitle = $(".title:first", "#facet_type").children("h3");
			var facet_typeTitleTxt = $facet_typeTitle.html();	 
			// Reset the inner HTML to nothing as added when open/close link is added
			$facet_typeTitle.html("");
			
			$("<a/>")
			.attr('href', '#openingfacet_type')
			.addClass("expandCollapseLink")	
			.appendTo($facet_typeTitle)
			.legExpandCollapse([facet_typeTitleTxt+'<span class="accessibleText">Expand opening options</span>',facet_typeTitleTxt+'<span class="accessibleText">Collapse opening options</span>'], {open: "open"});
		}

		if ($("#facet_chapter").length){
			// Slightly different way of adding the links, wrap the <a> element around the <h2> inner HTML
			var $facet_chapterTitle = $(".title:first", "#facet_chapter").children("h3");
			var facet_chapterTitleTxt = $facet_chapterTitle.html();	 
			// Reset the inner HTML to nothing as added when open/close link is added
			$facet_chapterTitle.html("");
			
			$("<a/>")
			.attr('href', '#openingfacet_chapter')
			.addClass("expandCollapseLink")	
			.appendTo($facet_chapterTitle)
			.legExpandCollapse([facet_chapterTitleTxt+'<span class="accessibleText">Expand opening options</span>',facet_chapterTitleTxt+'<span class="accessibleText">Collapse opening options</span>'], {open: "open"});
		}

		if ($("#facet_extent").length){
			// Slightly different way of adding the links, wrap the <a> element around the <h2> inner HTML
			var $facet_extentTitle = $(".title:first", "#facet_extent").children("h3");
			var facet_extentTitleTxt = $facet_extentTitle.html();	 
			// Reset the inner HTML to nothing as added when open/close link is added
			$facet_extentTitle.html("");
			
			$("<a/>")
			.attr('href', '#openingfacet_extent')
			.addClass("expandCollapseLink")	
			.appendTo($facet_extentTitle)
			.legExpandCollapse([facet_extentTitleTxt+'<span class="accessibleText">Expand opening options</span>',facet_extentTitleTxt+'<span class="accessibleText">Collapse opening options</span>'], {open: "open"});
		}

		if ($("#facet_source").length){
			// Slightly different way of adding the links, wrap the <a> element around the <h2> inner HTML
			var $facet_sourceTitle = $(".title:first", "#facet_source").children("h3");
			var facet_sourceTitleTxt = $facet_sourceTitle.html();	 
			// Reset the inner HTML to nothing as added when open/close link is added
			$facet_sourceTitle.html("");
			
			$("<a/>")
			.attr('href', '#openingfacet_source')
			.addClass("expandCollapseLink")	
			.appendTo($facet_sourceTitle)
			.legExpandCollapse([facet_sourceTitleTxt+'<span class="accessibleText">Expand opening options</span>',facet_sourceTitleTxt+'<span class="accessibleText">Collapse opening options</span>'], {open: "open"});
		}

		if ($("#facet_content").length){
			// Slightly different way of adding the links, wrap the <a> element around the <h2> inner HTML
			var $facet_contentTitle = $(".title:first", "#facet_content").children("h3");
			var facet_contentTitleTxt = $facet_contentTitle.html();	 
			// Reset the inner HTML to nothing as added when open/close link is added
			$facet_contentTitle.html("");
			
			$("<a/>")
			.attr('href', '#openingfacet_content')
			.addClass("expandCollapseLink")	
			.appendTo($facet_contentTitle)
			.legExpandCollapse([facet_contentTitleTxt+'<span class="accessibleText">Expand opening options</span>',facet_contentTitleTxt+'<span class="accessibleText">Collapse opening options</span>'], {open: "open"});
		}

		if ($("#facet_regulator").length){
			// Slightly different way of adding the links, wrap the <a> element around the <h2> inner HTML
			var $facet_regulatorTitle = $(".title:first", "#facet_regulator").children("h3");
			var facet_regulatorTitleTxt = $facet_regulatorTitle.html();	 
			// Reset the inner HTML to nothing as added when open/close link is added
			$facet_regulatorTitle.html("");
			
			$("<a/>")
			.attr('href', '#openingfacet_regulator')
			.addClass("expandCollapseLink")	
			.appendTo($facet_regulatorTitle)
			.legExpandCollapse([facet_regulatorTitleTxt+'<span class="accessibleText">Expand opening options</span>',facet_regulatorTitleTxt+'<span class="accessibleText">Collapse opening options</span>'], {open: "open"});
		}

		if ($("#facet_review").length){
			// Slightly different way of adding the links, wrap the <a> element around the <h2> inner HTML
			var $facet_reviewTitle = $(".title:first", "#facet_review").children("h3");
			var facet_reviewTitleTxt = $facet_reviewTitle.html();	 
			// Reset the inner HTML to nothing as added when open/close link is added
			$facet_reviewTitle.html("");
			
			$("<a/>")
			.attr('href', '#openingfacet_review')
			.addClass("expandCollapseLink")	
			.appendTo($facet_reviewTitle)
			.legExpandCollapse([facet_reviewTitleTxt+'<span class="accessibleText">Expand opening options</span>',facet_reviewTitleTxt+'<span class="accessibleText">Collapse opening options</span>'], {open: "open"});
		}

		if ($("#facet_heading").length){
			// Slightly different way of adding the links, wrap the <a> element around the <h2> inner HTML
			var $facet_headingTitle = $(".title:first", "#facet_heading").children("h3");
			var facet_headingTitleTxt = $facet_headingTitle.html();	 
			// Reset the inner HTML to nothing as added when open/close link is added
			$facet_headingTitle.html("");
			
			$("<a/>")
			.attr('href', '#openingfacet_heading')
			.addClass("expandCollapseLink")	
			.appendTo($facet_headingTitle)
			.legExpandCollapse([facet_headingTitleTxt+'<span class="accessibleText">Expand opening options</span>',facet_headingTitleTxt+'<span class="accessibleText">Collapse opening options</span>'], {open: "open"});
		}


		$checkboxes = $('#facet_extent .checkbox');
		var extentVal = '';
		var mainURL = window.location.origin + window.location.pathname + '?';
		$checkboxes.change(function(){	
		    
			extentVal = $checkboxes.filter(':checked').map(function(){
				return this.value;   
			}).get().join("-");

			if (extentVal != '')
				url['extent'] = extentVal;
			else
				delete url.extent

			var recursiveDecoded = decodeURIComponent( mainURL +  $.param( url ) );
			//window.location = recursiveDecoded;			
		});



	});
	
})(jQuery);