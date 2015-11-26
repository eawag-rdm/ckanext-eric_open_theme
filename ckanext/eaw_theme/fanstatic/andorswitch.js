"use strict"

ckan.module('andorswitch', function ($, _) {
  return {
      initialize: function () {
	  this.el.bootstrapSwitch('onText', 'ANY');
	  this.el.bootstrapSwitch('offText', 'ALL');
    }
  };
});

