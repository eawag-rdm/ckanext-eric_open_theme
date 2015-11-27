"use strict"

ckan.module('andorswitch', function ($, _) {
  return {
      initialize: function () {
	  var options = {
	      onText: "ANY",
	      onColor: "primary",
	      offText: "ALL",
	      offColor: "info",
	      animate: false,
	  };
	  this.el.bootstrapSwitch(options);
    }
  };
});

