$("#twords").text("Hi");
$(document).ready(function() {
    
    $("#saveText").click(saveText);
    $("#seeStore").click(seeStore);

    seeNumWords();

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


////// localStorage test

function saveText() {

var data = document.getElementById("this_input").value; //Pull text from user inputbox
localStorage["inputText"] = data; //Save it to the localStorage variable which will always remember what you store in it

};

function seeStore() {
	$("#wtwo").html(localStorage['inputText']);
}

  function seeNumWords() {
	if (localStorage['numWords']){
		$('#numWords').html("Number of Words Learned: " + localStorage['numWords']);
	}

	else $('#numWords').html("Number of Words Learned: 0");

  }


