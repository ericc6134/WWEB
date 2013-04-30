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

var rt1 = [];
var rt2 = [];
rt1.push("password", "Comfirm");
rt2.push("<b>the others</b>", "<b>real</b>");

for(var i = 0; i < rt1.length; i++){

	var re = new RegExp(rt1[i], "i");

	$("body *").replaceText( re, rt2[i] );

}
