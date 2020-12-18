// c:/Daves_Python_Programs/wiki/whatdoesthefroggot/js_L/scrollButtons.js




var requestAnimationFrame = window.requestAnimationFrame || 
                            window.mozRequestAnimationFrame || 
                            window.webkitRequestAnimationFrame ||
                            window.msRequestAnimationFrame;

var bodyElement = document.querySelector("body");							

var floatieUp = document.querySelector("#floatieUp");
var floatieDn = document.querySelector("#floatieDn");
var clicker = document.querySelector("#clicker");

// Total height of the body including off screen content.  Used to determine distance to bottom for floatieDn.
var scrollHeight = bodyElement.scrollHeight;

// These are all used in the easing function.
var currentScrollPosition;
var theDirection;
var iteration;  

var start = false;   // Starts the animation when you click on a floatie.
var clickBool = false;  // Did the user want to go straight to the top?


function setup() {
	// do something when a floatie is clicked.

	// I'm using animateToTopOfPage for animateToBottom of page as well, triple duty.
	clicker.addEventListener("click", function(evt){animateToTopOfPage(evt, 'clicker');}, false);  // bubbling
		
	// I'm using animateToTopOfPage for animateToBottom of page as well.
	floatieUp.addEventListener("mousedown", function(evt){animateToTopOfPage(evt, 'floatieUp');}, false);  // bubbling
	floatieUp.addEventListener("mouseup", stopEverything, false);
	
	// I'm using animateToTopOfPage for animateToBottom of page as well.
	floatieDn.addEventListener("mousedown", function(evt){animateToTopOfPage(evt, 'floatieDown');}, false);
	floatieDn.addEventListener("mouseup", stopEverything, false);
	
	// Deal with the mouse wheel, turn it off when using a floatie.
	bodyElement.addEventListener("mousewheel", stopEverything, false);
	bodyElement.addEventListener("DOMMouseScroll", stopEverything, false);
	
	// wheeeeeeee!
	animationLoop();
}
setup();

//
// kick of the animation to scroll your window back to the top/bottom.
//
function animateToTopOfPage(evt, theButton) {

	currentScrollPosition = getScrollPosition();

	if (theButton === 'floatieUp') {
		theDirection = -currentScrollPosition;  // num of px to the top of the page.
	} else if (theButton === 'floatieDown') {
	    // This could be negative if scrollHeight is < currentScrollPosition, so get the abs.
		theDirection = Math.abs(scrollHeight - currentScrollPosition);  // num of px to the Bottom of the page.
	} else if (theButton === 'clicker') {
		clickBool = true;
		theDirection = -currentScrollPosition;  // num of px to the top of the page.
	}
	
	
	// The ^ is xor so we have start = start ^ true.  And true is = 1.  And start is false.
	// And false == 0.  so we have 0^1 which = 1 = true.  This isn't the exponent ^.  The ^ means change
	// the bit as in toggle it so for eg in binary 0110^1 = 0111 and 0110^2 = 0101.
	// I don't know why he is using this here, just get rid of the ^.  Maybe it is faster
	// but not in javascript.
	
	// Bit operators work on 32 bits numbers. Any numeric operand in the operation is 
	// converted into a 32 bit number. The result is converted back to a JavaScript number.
	// See http://www.w3schools.com/jsref/jsref_operators.asp
	
	//start ^= true;
	start = true;
	iteration = 0;  // Reset the iteration.
}

//
// Stop the animation and reset start. 
//
//function stopEverything(evt = null, theButton = null) {
function stopEverything() {	
	start = false;
	/*
	if ( (theButton === 'floatieUp') || (theButton === 'floatieDown') ) {
	start = false;
	} else if (theButton === 'clicker') {
		start = false;
	}
	*/
	//console.log('top = ', scrollHeight);
	
}

//
// a cross-browser (minus Opera) way of getting the current scroll position
//
function getScrollPosition() {
	if (document.documentElement.scrollTop == 0) {  // scrollTop should always be zero, if not then we are in a different browser.
		return document.body.scrollTop;  // Some browsers use this,
	} else {
		return document.documentElement.scrollTop;  // and other browsers use this one.
	}
}

// I have all the Penner easing functions at:
// c:/Daves_Python_Programs/Kirupa/DaveAnimationMaster/page361PennerEasingfunctions.js
function easeInOutCubic(currentIteration, startValue, changeInValue, totalIterations) {
	if ((currentIteration /= totalIterations / 2) < 1) {
		return changeInValue / 2 * Math.pow(currentIteration, 3) + startValue;
	}
	return changeInValue / 2 * (Math.pow(currentIteration - 2, 3) + 2) + startValue;
}

//
// kicks into high gear only when the start variable is true
//
function animationLoop() {
	// start is true when you click on a floatie.
	if (start) {
		// scrollTo takes two arguments xaxis and yaxis.  x is set to 0 since we 
		// aren't going left or right.  
	 
		//  Eases in/out, in both directions Yea!
		window.scrollTo(0, easeInOutCubic(iteration, // current iteration.
										currentScrollPosition,  // initial value.
										theDirection, // change in value.  It will have to be positive if we are scrolling 
										              // down and neg if scrolling up.  
										180));  // total iterations ie how fast to scroll, 180 = 3 sec, at 60 cycles per sec rAF.
		
		iteration++;
		
// once you reach the top of the document, stop the scrolling
		if ( (clickBool) && (getScrollPosition() <= 0) ) {
			console.log('bottom = ', currentScrollPosition);
			clickBool = false;
			stopEverything();
			//stopEverything(null, 'clicker');
		}
		
	}
	requestAnimationFrame(animationLoop);
}


