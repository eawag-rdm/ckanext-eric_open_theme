// Module to be bound to the "Advanced Search Button".
// Makes the button visible, implements toggling of
// the next element that contains helptext and searchbox,
// which it also hides.

"use strict"

ckan.module('eaw_theme_hidewithjs', function($, _) {
    return {
	initialize: function () {
	    var target = this.options.target;
	    var hidden = this.sandbox.jQuery( target );
	    var query = this.options.query;
	    this.el.show();
	    if (typeof query !== "string")
		hidden.hide();
	    else
		hidden.show();
	    hidden.find( 'h4' ).hide();
	    this.el.click(function () {
		hidden.toggle();
		return(false);
	    });
	}
    };
});
	    
