

// This file is used for two different video players.  The Youtube one and the user one.
// getid3() is for videos the user uploads, and playVid/pauseVid() are for the Youtube video player.
// Be careful about the interaction with YTVidToMP4.js, it also has a load() which is screwing things
// up with the vid.load() in getid3().  And you were loading this file twice, which is wrong also, fixed March 25/16.
// This file is hard wired in front.html near the Youtube player.
//WARNING:  You are bringing in the controls from here?????  They should be in the html via render template.

/*
function getid3(obj) {

	var id =(obj.id);
	var uVid = document.getElementById(id);
	console.log('id = ', id);
	//uVid.controls = true;
	uVid.load();

}
*/

// This actually works, you can also use autoplay inside the video tag at the html.
//document.onload(playVid("myVideo2"));

function playVid(myVideo) {
	var vid = document.getElementById(myVideo);
    vid.play();
	console.log('in playVid()');
}

function pauseVid(myVideo) {
	var vid = document.getElementById(myVideo);
    vid.pause();
	console.log('in pauseVid()');
}

function makeBig(myVideo) {
    var screenSize = document.getElementById(myVideo);
    screenSize.width = window.innerWidth*0.60;
//myVideo.width = 500;
}

function makeNormal(myVideo) {
    var screenSize = document.getElementById(myVideo);
	screenSize.width = 300;
}






