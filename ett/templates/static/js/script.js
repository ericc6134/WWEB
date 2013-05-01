$("#twords").text("Hi");
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


    var record_num = 2;  // or however many elements there are in each row
    var allTextLines = allText.split(/\r\n|\n/);
	var entries = [];
	var ans = "";

	for(var i = 0; i < allTextLines.length - 1; i++){
		entries.push(allTextLines[i].split(','));
		ans = ans + entries[i][0] + ", " + entries[i][1] + "<br />";
	}

   $("#twords").html(ans);
}
