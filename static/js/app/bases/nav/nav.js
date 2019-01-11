define(function (require) {
	"use strict";
	var $ = require('jquery'),
		_ = require('underscore'),
		Gonrin = require('gonrin');
	return [
	    {
			"text":"Tỉnh thành",
			"icon":"fa fa-child",
			"type":"view",
			"collectionName":"tinhthanh",
		    "route":"tinhthanh/collection"
		},
		{
			"text":"Quốc gia",
			"icon":"fa fa-child",
			"type":"view",
			"collectionName":"quocgia",
		    "route":"quocgia/collection"
		},
	];

});