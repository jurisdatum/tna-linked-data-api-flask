(function ($) {
// http://ihatecode.blogspot.com/2008/04/jquery-time-delay-event-binding-plugin.html	
	
	$.fn.delayTimer = function(options) {
        var timer;
        var delayImpl = function(eventObj) {
            if (timer != null) {
                clearTimeout(timer);
            }
            var newFn = function() {
                options.fn(eventObj);
            };
            timer = setTimeout(newFn, options.delay);
        }
       
        return this.each(function() {			
            var obj = $(this);
            obj.bind(options.event, function(eventObj) {
                 delayImpl(eventObj);  
            });
        });
    };
} (jQuery));