function changeText(){
	document.getElementById('clicked').innerHTML = 'Hello JavaScript!';
}

function undoChangeText(){
	document.getElementById('clicked').innerHTML = 'click to unlock text'
}

function frontPhone(){
	document.getElementById('camon').src='frontphone.png';
}

function backPhone(){
	document.getElementById('camon').src='backphone.png';
}

function bigFont(){
	document.getElementById('changing_text').style.fontSize='20px';
}

function biggerFont(){
	document.getElementById('changing_text').style.fontSize='40px';
}

function biggestFont(){
	document.getElementById('changing_text').style.fontSize='60px';
}

function hideElement(){
	document.getElementById('hidden_text').style.display='none';
}

function showElement(){
	document.getElementById('hidden_text').style.display='block';
}