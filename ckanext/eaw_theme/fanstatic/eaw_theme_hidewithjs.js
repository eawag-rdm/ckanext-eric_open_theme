"use strict"

ckan.module('eaw_theme_hidewithjs', function($, _) {
    return {
	initialize: function () {
	    // alert("initialized hidewithjs");
	    console.log("initialized hidewithjs", this.el);
	    this.el.show();
	    this.el.next().hide();
	    // this.el.style.color = "red";
	}
    };
});
	    
