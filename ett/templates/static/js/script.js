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
localStorage['quizWords'] = entries;
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


	var engWords = [];
	var spanWords = [];
	var tempArr = localStorage['quizWords'].split(',');

	for(var i = 0; i < tempArr.length; i = i+2){
		engWords.push(tempArr[i]);
	};

	for(var i = 1; i < tempArr.length; i = i+2){
		spanWords.push(tempArr[i]);
	};
	


	$("#quizDiv").html('<center>\n\
	    <h4>Write the translated words in the boxes, then click submit</h4>\n\
	' + engWords[0] + ': <input id="w1" type="text" class="input-medium" name="word1" /><p id="r1"></p><br />\n\
	' + engWords[1] + ': <input id="w2" type="text" class="input-medium" name="word2" /><p id="r2"></p><br />\n\
	' + engWords[2] + ': <input id="w3" type="text" class="input-medium" name="word3" /><p id="r3"></p><br />\n\
	' + engWords[3] + ': <input id="w4" type="text" class="input-medium" name="word4" /><p id="r4"></p><br />\n\
	' + engWords[4] + ': <input id="w5" type="text" class="input-medium" name="word5" /><p id="r5"></p><br />\n\
	' + engWords[5] + ': <input id="w6" type="text" class="input-medium" name="word6" /><p id="r6"></p><br />\n\
          <input type="button" id="submitQuiz" value="Submit" class="btn" />\n\
         </center>');

	$("#submitQuiz").click(submitQuiz);


}

function seePast() {
	$("#past").html(localStorage['rt1']);

}

function submitQuiz(){
	$("#quizDiv").html('<button id="nextWords">Move On! (Take a Quiz)</button>');
	$("#nextWords").click(nextWords);
	for( var i = 0; i < 6; i ++){
				
		
	}

}

function submitQuizYes() {


	$("#quizDiv").html('<button id="nextWords">Move On! (Take a Quiz)</button>');
	$("#nextWords").click(nextWords);
	$("#past").html(localStorage['entries']);
	//localStorage['rt1'] = localStorage['rt1'] + localStorage['entries'];
	localStorage['rt1'] = localStorage['entries'];


}

