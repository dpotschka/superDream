// This all the code from the original file I got from:
// http://jsfiddle.net/m1erickson/zw9S4/  and
// http://stackoverflow.com/questions/21537845/fading-a-loaded-image-into-canvas-with-drawimage

/*
body {
    background-color: ivory;
}
canvas {
    border:1px solid red;
}

	<script
	src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js">
	</script>

*/



/*
<button id="fade">Fade to next Image</button><br>
<canvas id="canvas" width=204 height=204></canvas><br>
*/

//$("#fade").hide();


/*

var imageURLs = []; // put the paths to your images here
var imagesOK = 0;
var imgs = [];
imageURLs.push("https://dl.dropboxusercontent.com/u/139992952/stackoverflow/house204-1.jpg");
imageURLs.push("https://dl.dropboxusercontent.com/u/139992952/stackoverflow/house204-2.jpg");
imageURLs.push("https://dl.dropboxusercontent.com/u/139992952/stackoverflow/house204-3.jpg");
imageURLs.push("https://dl.dropboxusercontent.com/u/139992952/stackoverflow/house204-4.jpg");


loadAllImages();
//
function loadAllImages() {
    for (var i = 0; i < imageURLs.length; i++) {
        var img = new Image();
        imgs.push(img);
        img.onload = function () {
            imagesOK++;
            if (imagesOK >= imageURLs.length) {
                $("#fade").show();
                ctx.drawImage(imgs[0], 0, 0);
            }
        };
        img.onerror = function () {
            alert("image load failed");
        }
        img.crossOrigin = "anonymous";
        img.src = imageURLs[i];
    }
}


*/

/////////////////////////////////////////// Mine starts here.


// Get the proper rAF for your browser.
var requestAnimationFrame = window.requestAnimationFrame ||
							window.mozRequestAnimationFrame ||
							window.webkitRequestAnimationFrame ||
							window.msRequestAnimationFrame;

// Get the proper cancel rAF for your browser.  I think these are called poly fills.
var cancelRAF = window.cancelAnimationFrame ||
				window.mozCancelAnimationFrame ||
				window.webkitCancelAnimationFrame ||
				window.msCancelAnimationFrame;


// I'm adding a counter to stop the slide show after it has shown all the images once, to help prevent my site from
// going over quota if a user leaves the slide show running forever.
var preventOverQuotaCounter = 0;  // In update().
// Adding one just for fun, in case you didn't see the first slide on boot up.
// The slides are counted twice each so multiply by 2.
var numOfSlides = null;

// I now have the width and height with the directory in a 2D array.
var assets = null;

// This array contains a reference to every image.  It holds all your image objects.
var imagesArray = [];   //new Array();  Used to store the width and height, dx dy etc for each image.


// WARNING: Declare your variables in the correct order.  You had howMuchWin after canvasWidth/Height and
// it screwed up drawImage.
var howMuchWin = 0.6;  // I scale the canvas size down a bit to make it fit better in the window.

var canvasWidth = Math.floor(window.innerWidth * howMuchWin);
var canvasHeight = Math.floor(9*canvasWidth/16);  // My aspect ratio is 16:9 movie size.

// if the user clicks on "Get Next Image" before they load the images the ss jams.
var imagesLoaded = false;

var canvas = document.getElementById("canvas");
var ctx = canvas.getContext("2d");

var fadeOutIndex = undefined;
var fadeInIndex = 0;
var fadePct = 0;

// Used for putting the current images name and price into the top field of the 'Add to Cart' button.
var payPalItem = {};


// Three scenarios when saving the state of the page:
// 1. User goes to paypal without choosing whichDollar range.  Then comes back to art.html
// 2. User just landed on art.html and chooses whichDollar range.
// 3. User goes to buy some art then comes back to art.html.
// State saved programatically by whichDollar, inIndex (fadeInIndex), and outIndex (fadeOutIndex).
// whichDollar is the price range the user has clicked on.

var getAssets = function getAssets(whichDollar, inIndex = undefined, outIndex = undefined) {

	//Put a green border around the button the user clicked on.

	//theButton.style.display = '';
	//document.getElementById(theButton).innerHTML = "";
	document.getElementById('10').style.borderStyle = null;
	document.getElementById('20').style.borderStyle = null;
	document.getElementById('40').style.borderStyle = null;
	document.getElementById('80').style.borderStyle = null;
	document.getElementById('140').style.borderStyle = null;
	document.getElementById('220').style.borderStyle = null;

	document.getElementById(whichDollar).style.borderStyle = 'solid';
	document.getElementById(whichDollar).style.borderColor = 'green';

	// Note: A span tag does not have a value.
	// Used to save the state for window.onload
	document.getElementById('whichDollar').innerHTML = whichDollar;

    var ssBasePath = "/static/myDream/webImages"

	if (whichDollar === "10") {
		assets =
		// $10 art
		[
		[ssBasePath + '/SlideShow/JewelN.jpg', 3200, 2400],
		[ssBasePath + '/SlideShow/GlassBlackN.jpg', 1600, 1200],
		[ssBasePath + '/SlideShow/sharkMonkeyN.jpg', 1778, 870],
		[ssBasePath + '/SlideShow/SmudgeSN.jpg', 800,600],
		[ssBasePath + '/SlideShow/fallingN.jpg', 1867, 863],
		[ssBasePath + '/SlideShow/HandN.jpeg', 1600, 1200],
		[ssBasePath + '/SlideShow/GlassBallN.jpg', 800, 600],
		[ssBasePath + '/SlideShow/monkeyN.JPG', 561,794],
		[ssBasePath + '/SlideShow/greenLifeN.jpg', 800, 600]
		];

// The value in array[0] is the value in the paypal form and must be identical to what paypal has on record when I created
// the paypal button.  The key is which slide the user is on.  I am injecting the current slide into position one of the paypal button.
// So all the user has to do is click 'Add to Cart'.
		payPalItem = {0: ['Jewel', 'Jewel $10'],
					  1: ['GlassBlack', 'GlassBlack $10'],
					  2: ['sharkMonkey', 'sharkMonkey $10'],
					  3: ['SmudgeS', 'SmudgeS $10'],
					  4: ['falling', 'falling $10'],
					  5: ['Hand', 'Hand $10'],
					  6: ['GlassBall', 'GlassBall $10'],
					  7: ['monkey', 'monkey $10'],
					  8: ['greenLife', 'greenLife $10']
					  };


	} else if (whichDollar === "20") {
		assets =
		// $20 art
		[
		[ssBasePath + '/SlideShow/FireN.jpg', 800, 600] ,
		[ssBasePath + '/SlideShow/Log1N.jpg', 1600, 1200] ,
		[ssBasePath + '/SlideShow/squirN.jpg', 800,600],
		[ssBasePath + '/SlideShow/PurpleIceN.jpg', 800, 600] ,
		[ssBasePath + '/SlideShow/backR3N.jpg', 1720, 1080] ,
		[ssBasePath + '/SlideShow/lIn4N.jpg', 1920, 1080] ,
		[ssBasePath + '/SlideShow/lOut2N.jpg', 1600, 1030] ,
		[ssBasePath + '/SlideShow/rIn3N.jpg', 1600, 1030] ,
		[ssBasePath + '/SlideShow/rlcN.jpg', 1600, 994] ,
		[ssBasePath + '/SlideShow/rOut4N.jpg', 1600, 994] ,
		[ssBasePath + '/SlideShow/StarsJPEGN.jpeg', 800, 600] ,
		[ssBasePath + '/SlideShow/YOURaiIShereN.jpg', 1800, 1016],
		[ssBasePath + '/SlideShow/dragon16N.jpg', 1920, 1078],
		[ssBasePath + '/SlideShow/nebulaN.jpg', 800, 600]
		];

		payPalItem = {0: ['Fire', 'Fire $20'],
					  1: ['Log1', 'Log1 $20'],
					  2: ['squir', 'squir $20'],
					  3: ['PurpleIce', 'PurpleIce $20'],
					  4: ['backR3', 'backR3 $20'],
					  5: ['lIn4', 'lIn4 $20'],
					  6: ['lOut2', 'lOut2 $20'],
					  7: ['rIn3', 'rIn3 $20'],
					  8: ['rlc', 'rlc $20'],
					  9: ['rOut4', 'rOut4 $20'],
					  10: ['Stars', 'Stars $20'],
					  11: ['YOURaiIShere', 'YOURaiIShere $20'],
					  12: ['dragon', 'dragon $20'],
					  13: ['nebula', 'nebula $20']
					 };

	} else if (whichDollar === "40") {
		assets =
		//$40 art
		[
		[ssBasePath + '/SlideShow/FlowersN.jpg', 1231, 644] ,
		[ssBasePath + '/SlideShow/cometN.jpeg', 1231, 624],
		[ssBasePath + '/SlideShow/Ferns3N.jpg', 800, 600] ,
		[ssBasePath + '/SlideShow/leftPalmFN.jpg', 1920, 1080] ,
		[ssBasePath + '/SlideShow/catHand7FN.jpg', 1080, 1920] ,
		[ssBasePath + '/SlideShow/MaggieFrog8N.jpg', 1280, 677] ,
		[ssBasePath + '/SlideShow/twoLegs3N.jpg', 1600, 994] ,
		[ssBasePath + '/SlideShow/spaceGasesN.jpeg', 1231, 624],
		[ssBasePath + '/SlideShow/eyeN.jpg', 800, 600]
		];

		payPalItem = {0: ['Flowers', 'Flowers $40'],
		              1: ['comet', 'comet $40'],
					  2: ['Ferns', 'Ferns $40'],
					  3: ['leftPalm', 'leftPalm $40'],
					  4: ['catHand', 'catHand $40'],
					  5: ['MaggieFrog', 'MaggieFrog $40'],
					  6: ['twoLegs', 'twoLegs $40'],
					  7: ['spaceGases', 'spaceGases $40'],
					  8: ['eye', 'eye $40']
					  };


	} else if (whichDollar === "80") {  // ['/SlideShow/catAttack3Imp.jpg', 3840, 2167] ,  // get rid of Ingrid in this one, it's tacky.
		assets =
		// $80 art
		[
		[ssBasePath + '/SlideShow/GlowySwirlN.jpg', 800, 600],
		[ssBasePath + '/SlideShow/AlienN.jpg', 1024, 1024] ,
		[ssBasePath + '/SlideShow/ArmPNGN.jpg', 800, 600] ,
		[ssBasePath + '/SlideShow/Bubbles1N.jpg', 3840, 2160] ,
		[ssBasePath + '/SlideShow/theEcho7NetN.jpg', 1527, 1142] ,
		[ssBasePath + '/SlideShow/w5N.jpg', 1920, 1080] ,
		[ssBasePath + '/SlideShow/wa8N.jpg', 1920, 1080] ,
		[ssBasePath + '/SlideShow/wb6N.jpg', 1920, 1080] ,
		[ssBasePath + '/SlideShow/fun1CpngN.jpg', 1920, 212] ,
		[ssBasePath + '/SlideShow/IngridBodyN.jpg', 1920, 1080] ,
		[ssBasePath + '/SlideShow/dragonDecClipN.jpg', 1802, 252],
		[ssBasePath + '/SlideShow/RashidaBodyN.jpg', 1280, 677] ,
		[ssBasePath + '/SlideShow/bustN.jpg', 800, 600] ,
		];

		payPalItem = {0: ['glowySwirl', 'glowySwirl $80'],
		              1: ['Alien', 'Alien $80'],
					  2: ['Arm', 'Arm $80'],
					  3: ['Bubbles', 'Bubbles $80'],
					  4: ['theEcho7Net', 'theEcho7Net $80'],
					  5: ['w5', 'w5 $80'],
					  6: ['w8', 'w8 $80'],
					  7: ['wb6', 'wb6 $80'],
					  8: ['fun', 'fun $80'],
					  9: ['IngridBody', 'IngridBody $80'],
					  10: ['dragonMountain', 'dragonMountain $80'],
					  11: ['RashidaBody', 'RashidaBody $80'],
					  12: ['bust', 'bust $80']
		     		};


	} else if (whichDollar === "140") {
		assets =
		// $140 art
		[
		[ssBasePath + '/SlideShow/BLACKbunny6N.jpg', 800, 600] ,
		[ssBasePath + '/SlideShow/Rashida13N.jpg', 1280, 677] ,
		[ssBasePath + '/SlideShow/squ6N.jpg', 1280, 677],
		[ssBasePath + '/SlideShow/IngridCropN.jpg', 800, 600] ,
		[ssBasePath + '/SlideShow/roseN.jpg', 1041, 587]
		];

	    payPalItem = {0: ['BLACKbunny', 'BLACKbunny $140'],
		              1: ['Rashida', 'Rashida $140'],
					  2: ['squ6', 'squ6 $140'],
					  3: ['Ingrid', 'Ingrid $140'],
					  4: ['rose', 'rose $140']
					 };

	// $220 art limit of 500 prints.
	} else if (whichDollar === "220") {
		assets =
		[
		[ssBasePath + '/SlideShow/firstFrostForestN.jpg', 3840, 2167],
		[ssBasePath + '/SlideShow/ab2N.jpg', 1280, 677] ,
		[ssBasePath + '/SlideShow/desert2pngN.jpg', 1920, 754],
		[ssBasePath + '/SlideShow/volcanoN.jpg', 1920, 794],
		[ssBasePath + '/SlideShow/FrostNoRoseN.jpg', 3840, 2167]
		];

		payPalItem = {0: ['firstFrostForest', 'firstFrostForest $220'],
		              1: ['abstract', 'abstract $220'],
					  2: ['desert', 'desert $220'],
					  3: ['volcano', 'volcano $220'],
					  4: ['frostNoRose', 'frostNoRose $220']
					 };
	}

// 55 slides in total, Dec 16/16.

	numOfSlides = (assets.length + 1)*2;
	imagesArray = [];

	//console.log('bottom of get assets')
    // create images
	ci(inIndex, outIndex);

}  // End getAssets


var onImageLoad = function(){
    console.log("IMAGESfound davvee!!");

};


// Before refreshing the page, save the form data to sessionStorage
// For saving the users email and location in the ss after coming back from paypal or on window.load.
// I no longer save the email this way, but I do save the other data.  The email is just
// injected into the form by handler artForSale.

window.onbeforeunload = function() {

	//var userEmail = document.getElementById('userEmail').value;

	// If you use localStorage.setItem it will save the data forever.
	//sessionStorage.setItem("userEmail", userEmail);

	//  innerHTML here, is set to the string 'stop' by default in art.html
	var whichDollar = document.getElementById('whichDollar').innerHTML;
	sessionStorage.setItem("whichDollar", whichDollar);

	var inIndex = document.getElementById('fadeInIndex').innerHTML;
	sessionStorage.setItem("inIndex", inIndex);

	var outIndex = document.getElementById('fadeOutIndex').innerHTML;
	sessionStorage.setItem("outIndex", outIndex);

		//console.log('in onbeforeunload outIndex, inIndex, whichDollar == ', outIndex, inIndex, whichDollar);

}


// WARNING:  You cannot return from any type of onload function.  So canvasWidth/height are undefined.
// I reset them just above createImages().  It takes a few seconds for the resize to take effect.

//  Resize the canvas when the window resizes.
window.onload = window.onresize = function() {

// for keeping the users email address in place after coming back from paypal.
// Not in use!  I just inject the email directly from handler artForSale so the user
// doesn't have to type it in anymore.
/*
	var userEmail = sessionStorage.getItem('userEmail');
	if (userEmail !== null) {
		document.getElementById('userEmail').value = userEmail;
	}
*/

	// CAUTION: A span tag does not have a value.
// All these if statements were required so getAssets wouldn't run with "theButton" being undefined if
// the user went to paypal before loading any images.  The images got screwed up if they loaded them after that.
// id whichDollar, inIndex, and outIndex has the word 'stop' for it's innerHTML as default.


	var whichDollar = sessionStorage.getItem('whichDollar');
	if (whichDollar !== null) {
		if (whichDollar !== 'stop') {
			//console.log('in onload whichDollar = ', whichDollar);

			var inIndex = Number( sessionStorage.getItem('inIndex') );
			var outIndex = Number( sessionStorage.getItem('outIndex') );
			//console.log('in onload outIndex, inIndex, whichDollar = ', outIndex, inIndex, whichDollar);
			getAssets(whichDollar, inIndex, outIndex);
		}
	}

	window.sessionStorage.clear();

    canvasWidth = Math.floor(window.innerWidth * howMuchWin);  // A percentage of the window makes the canvas fit better in the window.
	canvasHeight = Math.floor(9*canvasWidth/16);  // My aspect ratio is 16:9 movie size.

    canvas.style.position = "relative";
	canvas.setAttribute("width", canvasWidth);
	canvas.setAttribute("height", canvasHeight);

	canvas.style.top = 10 + 'px';
	// To perfectly center this you would have to add half the width of the scroll bar, if there is one.
	canvas.style.left = 10+"px";
	//canvas.style.left = (window.innerWidth - canvasWidth) / 2 + "px";

};  // End window.onload




// The Image "constructor" is responsible for creating the image
// objects and defining the various properties they have.  Note the capital 'I' in Image.
function ImageConstructor(imageSrc, sx, sy, sw, sh, dx, dy, dw, dh) {


	this.imageSrc = imageSrc;
	this.sx = sx;
	this.sy = sy;
	this.sw = sw;
	this.sh = sh;
	this.dx = dx;
	this.dy = dy;
	this.dw = dw;
	this.dh = dh;

}; // End ImageConstructor





//
// Alter your dw dh with these aspect ratio makers.
//                                 sw          sh     canvasW    canvasH
var getResizeRatio = function(startWidth, startHeight, maxWidth, maxHeight){
	var ratioX = maxWidth / startWidth;
	var ratioY = maxHeight / startHeight;

	return ratioX <= ratioY ? ratioX : ratioY;
}

var getResizeDimensions = function(startWidth, startHeight, maxWidth, maxHeight){
	var ratio = getResizeRatio(startWidth, startHeight, maxWidth, maxHeight);

	return { 'width': Math.floor(startWidth * ratio), 'height': Math.floor(startHeight * ratio) };
}

// End aspect ratio makers.


// I must reset canvasWidth and canvasHeight if the user changes the window size as the window.onload does not return them.
// A percentage of the window makes the canvas fit better in the window.  You also get an error at line 576, doesn't matter.



var ci = function createImages(inIndex, outIndex) {

	var loadedImages = 0;

// Image loading indicator stuff
// If the user changes their browser size when the slide show is not playing then this fires off continuously.  Not a big deal.
// but I put an 'if block around it so it doesn't display' although it will still run in invisible land.
	if (assets !== null) {
		document.getElementById("loading").innerHTML = "<span style='color:blue;margin-left:30px;'> I'm Loading Images </span> <img src='/static/myDream/js/ajax-loader.gif' />";
	}


	function imageLoadPost(){
		loadedImages++;
		if (loadedImages >= assets.length){

			// if the user clicks on "Get Next Image" before they load the images the ss jams.
			imagesLoaded = true;


			// If we come from paypal and we want the old state.

			if ( (outIndex !== undefined) && (inIndex !== 'stop') ) {
				console.log('ci if top outIndex and inIndex == ', outIndex, inIndex );
				fadeInIndex = inIndex;
				fadeOutIndex = outIndex;

			} else {
				fadeInIndex = 0;
				fadeOutIndex = imagesArray.length - 1;

				console.log('ci else outIndex and inIndex == ', outIndex, inIndex);
			}

				// Used to store state if the user comes back from paypal before loading whichDollar range.
				document.getElementById("fadeInIndex").innerHTML = fadeInIndex;
				document.getElementById("fadeOutIndex").innerHTML = fadeOutIndex;

			// Display the first image to get the ball rolling.
			ctx.clearRect(0,0,canvas.width,canvas.height);
			ctx.drawImage(imagesArray[fadeInIndex].imageSrc, imagesArray[fadeInIndex].sx, imagesArray[fadeInIndex].sy, imagesArray[fadeInIndex].sw,
			imagesArray[fadeInIndex].sh, imagesArray[fadeInIndex].dx, imagesArray[fadeInIndex].dy, imagesArray[fadeInIndex].dw, imagesArray[fadeInIndex].dh);

			//fadeOutIndex = imagesArray.length - 1;
			//fadeInIndex = 0;

// Alter paypal so the "add to cart" displays the current images title and price in the top field of the select option tag in the form.
// Object payPalItem item is set by hand in getAssets.
			document.getElementById("currentImage").value = payPalItem[fadeInIndex][0];
			document.getElementById("currentImage").innerHTML = payPalItem[fadeInIndex][1];

			// Turn the indicator off when all the images are loaded.
			document.getElementById("loading").innerHTML = "";
			document.getElementById("percentLoaded").innerHTML = "";

		} else {
			var percentLoaded =  (loadedImages / assets.length) * 100;
			percentLoaded = percentLoaded.toFixed(0).toString();  // number of decimal places.

			document.getElementById("percentLoaded").innerHTML = percentLoaded + '% done';
		}
	}   	// end Image loading indicator stuff.


	/*

	if (imagesArray.length > 0){ // The window size has changed and the slide show imagesArray is already loaded, just alter the dw and dh.
	                             // Quick load.  This is faster than reloading the entire imagesArray

		//console.log('inside Quick load imagesArray.length = ', imagesArray.length);

		document.getElementById("loading").innerHTML = "";

		for (var i = 0; i < assets.length; i++) {
			dwdh = getResizeDimensions(imagesArray[i].sw, imagesArray[i].sh, canvasWidth, canvasHeight);
			imagesArray[i].dw = dwdh.width;
			imagesArray[i].dh = dwdh.height;
		}
		shiftDone = true;  // You need to do this so the shifter position re-syncs with the new canvas width.

		// If go === false, display the current image.
		if (!go) {
				imagesArray[index].dx = 0;
						  //                        sx       sy       sw       sh    dx            dy       dw      dh
				mainContext.drawImage(imagesArray[index].imageSrc, imagesArray[index].sx, imagesArray[index].sy, imagesArray[index].sw,
				imagesArray[index].sh, imagesArray[index].dx, imagesArray[index].dy, imagesArray[index].dw, imagesArray[index].dh);
		}
	} else {  // The web page just loaded and the slide show images still need to be loaded.


*/

		// Get all the vars for drawImage() for every image.
		// The drawImage vars, See definitions above.  I will draw the full image source so sx and sy = 0.
		var sx, sy, sw, sh, dx, dy, dw, dh, imageSrc, theImage;

		for (var i = 0; i < assets.length; i++) {

			imageSrc = new Image();
			//imageSrc.onload = onImageLoad();
			imageSrc.src = assets[i][0];

		// x/y coordinates for drawing your image onto the canvas.
		// Relative to your canvas width.  We start 'off canvas' and slide 'left to right' onto the canvas.
		// Set all your vars for drawImage().


			sx = sy = sw = sh = dx = dy = dw = dh = 0;
			sw = assets[i][1]; sh = assets[i][2];

		// Make all the images fit inside my 16:9 screen without squashing or stretching.

			dwdh = getResizeDimensions(sw, sh, canvasWidth, canvasHeight);
			dw = dwdh.width;
			dh = dwdh.height;


			// dx and dy are set in getTwoImages(), just leave them at zero as above.
			dx = Math.floor( (canvasWidth - dw) / 2 );
			dy = Math.floor( (canvasHeight - dh) / 2);
			/*
			console.log('sw = ', sw);
			console.log('sh = ', sh);
			console.log('dx = ', dx);
			console.log('dy = ', dy);
			console.log('canvasWidth = ', canvasWidth);
			console.log('canvasHeight = ', canvasHeight);
			*/

			// create the Image object
			theImage = new ImageConstructor(imageSrc, sx, sy, sw, sh, dx, dy, dw, dh);
			imagesArray.push(theImage);

			//imagesArray.push(imageSrc);

			// Image loading indicator stuff.  Turn the indicator off when all the images are loaded.
			imageSrc.onload=function(){
				imageLoadPost();
			}

			imageSrc.onerror = function () {
            alert("Image load failed, refresh your page and give it another go or email Dave and let him know, cheers!", imageSrc.src);
			}

		}  // End for




};  // End createImages

/*
ctx.drawImage(imagesArray[0].imageSrc, imagesArray[0].sx, imagesArray[0].sy, imagesArray[0].sw,
				imagesArray[0].sh, imagesArray[0].dx, imagesArray[0].dy, imagesArray[0].dw, imagesArray[0].dh);

ctx.drawImage(img.imageSrc, img.sx, img.sy, img.sw,
				img.sh, img.dx, img.dy, img.dw, img.dh);

*/


function animateFade() {
    if (fadePct > 100) {
        return;
    }
    requestId = requestAnimationFrame(animateFade);
    ctx.clearRect(0,0,canvas.width,canvas.height);  // he has this commented out originally.
    draw(imagesArray[fadeInIndex], fadePct / 100);
    draw(imagesArray[fadeOutIndex], (1 - fadePct / 100));
    fadePct++;
}

function draw(img, opacity) {
    ctx.save();
    ctx.globalAlpha = opacity;
    //ctx.drawImage(img, 0, 0);
	ctx.drawImage(img.imageSrc, img.sx, img.sy, img.sw, img.sh, img.dx, img.dy, img.dw, img.dh);
	//console.log('in draw imageSrc = ', img.imageSrc);
    ctx.restore();
}

// This is executed when the user clicks on the button 'Get Next Image'.
function startFade() {

    fadePct = 0;
    if (++fadeOutIndex == imagesArray.length) {
        fadeOutIndex = 0;
    }
    if (++fadeInIndex == imagesArray.length) {
        fadeInIndex = 0;
    }

// If the user clicks on "Get Next Image" before they load the images the ss jams.
	if (imagesLoaded) {

// Alter paypal so the "add to cart" displays the current images title and price in the top field of the select option tag in the form.
// Object payPalItem item is set by hand in getAssets.
		document.getElementById("currentImage").value = payPalItem[fadeInIndex][0];
		document.getElementById("currentImage").innerHTML = payPalItem[fadeInIndex][1];

// Used to store state if the user comes back from paypal.
		document.getElementById("fadeInIndex").innerHTML = fadeInIndex;
		document.getElementById("fadeOutIndex").innerHTML = fadeOutIndex;

		animateFade();
	}

}

/*

$("#fade").click(function () {
    fadePct = 0;
    if (++fadeOutIndex == imgs.length) {
        fadeOutIndex = 0;
    }
    if (++fadeInIndex == imgs.length) {
        fadeInIndex = 0;
    }
    animateFade();
});

*/



