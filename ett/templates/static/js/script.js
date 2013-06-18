$("#twords").text("Hi");
$(document).ready(function() {
    
    $("#saveText").click(saveText);
    $("#seeStore").click(seeStore);
    $("#nextWords").click(nextWords);
    $("#seePast").click(seePast);

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
	};

localStorage['entries'] = ans;
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

function nextWords() {

	$('#nextWords').click(function() { return false; });

	$("#quizDiv").html('<center>\n\
	    <h4>Write the translated words in the boxes, then click submit</h4>\n\
          <form name="quiz" method="get">\n\
          word1: <input type="text" class="input-medium" name="word1"><br>\n\
          word2: <input type="text" class="input-medium" name="word2"><br>\n\
	  word3: <input type="text" class="input-medium" name="word3"><br>\n\
          word4: <input type="text" class="input-medium" name="word4"><br>\n\
	  word5: <input type="text" class="input-medium" name="word5"><br>\n\
          word6: <input type="text" class="input-medium" name="word6"><br>\n\
	  word7: <input type="text" class="input-medium" name="word7"><br>\n\
          word8: <input type="text" class="input-medium" name="word8"><br>\n\
	   \n\
          <input type="button" id="submitQuiz" value="Submit" class="btn" />\n\
          </form>\n\
         </center>');

	$("#submitQuiz").click(submitQuiz);

}

function seePast() {
	$("#past").html(localStorage['rt1']);

}

function submitQuiz() {
	$("#quizDiv").html('<button id="nextWords">Move On! (Take a Quiz)</button>');
	$("#nextWords").click(nextWords);
	$("#past").html(localStorage['entries']);
	localStorage['rt1'] = localStorage['rt1'] + localStorage['entries'];
}

