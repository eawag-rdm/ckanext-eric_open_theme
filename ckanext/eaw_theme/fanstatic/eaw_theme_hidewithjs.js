// Module to be bound to the "Advanced Search Button".
// Makes the button visible, implements toggling of
// the next element that contains helptext and searchbox,
// which it also hides.

"use strict"

ckan.module('eaw_theme_hidewithjs', function($, _) {
    return {
	initialize: function () {
	    var _this = this.el;
	    this.el.show();
	    this.el.next().hide();
	    this.el.next().find( 'h4' ).hide();
	    this.el.click(function () {
		_this.next().toggle();
		return(false);
	    });
	}
    };
});
	    
