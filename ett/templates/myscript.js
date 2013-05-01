console.log("hello");

/*
 * jQuery replaceText - v1.1 - 11/21/2009
 * http://benalman.com/projects/jquery-replacetext-plugin/
 * 
 * Copyright (c) 2009 "Cowboy" Ben Alman
 * Dual licensed under the MIT and GPL licenses.
 * http://benalman.com/about/license/
 */
(function($){$.fn.replaceText=function(b,a,c){return this.each(function(){var f=this.firstChild,g,e,d=[];if(f){do{if(f.nodeType===3){g=f.nodeValue;e=g.replace(b,a);if(e!==g){if(!c&&/</.test(e)){$(f).before(e);d.push(f)}else{f.nodeValue=e}}}}while(f=f.nextSibling)}d.length&&$(d).remove()})}})(jQuery);


////// CSV Reader
$(document).ready(function() {
    $.ajax({
        type: "GET",
        url: chrome.extension.getURL("/dummy.csv"),
        dataType: "text",
        success: function(data) {processData(data);}
     });
});


////// Processing CSV into array
function processData(allText) {

	console.log('initiate');
	console.log(allText);
    var record_num = 2;  // or however many elements there are in each row
    var allTextLines = allText.split(/\r\n|\n/);
	console.log(allTextLines);

   // var entries = allTextLines[0].split(',');
	//console.log(entries);

	var entries = [];

	for(var i = 0; i < allTextLines.length - 1; i++){
		entries.push(allTextLines[i].split(','));
		console.log(entries[i]);
	}
	console.log(entries);

////////// Processing "entries" into 2 arrays (rt1 = before, rt2 = after)
	
	var rt1 = [];
	var rt2 = [];
	for(var i = 0; i < entries.length; i++){
		rt1.push(entries[i][0]);
		rt2.push(entries[i][1]);
	}


/////// Replace

for(var i = 0; i < rt1.length; i++){

	var re = new RegExp(rt1[i], "i");

	$("body *").replaceText( re, "<b>" + rt2[i] + "</b>" );
	$("body *").replaceText( "\\F1" , "ñ");

}







}



