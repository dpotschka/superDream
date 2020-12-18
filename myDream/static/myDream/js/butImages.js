/* c:/Daves_Python_Programs/wiki/whatdoesthefroggot/js_L/butImages.js
This file manipulates the buttons in your back end when the user does some mouse action on them.
The dictionary was built with one of my helper functions found at
c:/Daves_Python_Programs/HelperPrograms/imageButLoader.py.  I only used the dictionary generation part of imageButLoader
for this file.  Go check out the loader for more details and front.html */

/* machine learning is cool */

    /* This function is called by mouseover in the html files.  When the mouse is over a button we get the id of that image.     */
function getid(obj) {

	var id =(obj.id);

    var logoNetPath = "/static/myDream/webImages/buttons/logoNet/";
    var logOnButPath = "/static/myDream/webImages/buttons/logOn/";
    var logOutButPath = "/static/myDream/webImages/buttons/logOut/";
    var signUpPath = "/static/myDream/webImages/buttons/signUp/";
    var fiveSecondsPath = "/static/myDream/webImages/buttons/fiveSeconds/";
    var sendMessagePath = "/static/myDream/webImages/buttons/sendMessage/";
    var yourProfilePath = "/static/myDream/webImages/buttons/yourProfile/";
    var booksPath = "/static/myDream/webImages/buttons/books/";
    var artForSalePath = "/static/myDream/webImages/buttons/artForSale/";
    var messagePath = "/static/myDream/webImages/buttons/message/";
    var quickPath = "/static/myDream/webImages/buttons/quick/";
    var contactPath = "/static/myDream/webImages/buttons/contact/";
    var contactPath2 = "/static/myDream/webImages/buttons/contact/";
    var forgotPath = "/static/myDream/webImages/buttons/forgot/";
    var passwordPath = "/static/myDream/webImages/buttons/password/";
    var guitarVideosPath = "/static/myDream/webImages/buttons/guitarVideos/";
    var stockMarketPath = "/static/myDream/webImages/buttons/stocks/";
    var greyPath = "/static/myDream/webImages/buttons/daveBuilder/";
    var thdPath = "/static/myDream/webImages/buttons/";
    var builderPath = "/static/myDream/webImages/buttons/";
    var theFrogPath = "/static/myDream/webImages/buttons/theFrog/";

    var images = {'logOn': [logOnButPath + 'logOn1.jpg', logOnButPath + 'logOn2.jpg', logOnButPath + 'logOn3.jpg', logOnButPath + 'logOn4.jpg'],
                  'logOut': [logOutButPath + 'logOut1.jpg', logOutButPath + 'logOut2.jpg', logOutButPath + 'logOut3.jpg', logOutButPath + 'logOut4.jpg'],
                  'logoNet': [logoNetPath + 'hyperDreamLogo1.jpg', logoNetPath + 'hyperDreamLogo2.jpg', logoNetPath + 'hyperDreamLogo3.jpg', logoNetPath + 'hyperDreamLogo4.jpg'],
                  'books': [booksPath + 'books1.png', booksPath + 'books2.png', booksPath + 'books3.png', booksPath + 'books4.png'],
                  'artForSale':[artForSalePath + 'artForSale1.png', artForSalePath + 'artForSale2.png', artForSalePath + 'artForSale3.png', artForSalePath + 'artForSale4.png'],
                  'yourProfile':[yourProfilePath + 'yourProfile1.jpg', yourProfilePath + 'yourProfile2.jpg', yourProfilePath + 'yourProfile3.jpg', yourProfilePath + 'yourProfile4.jpg'],
                  'signUp':[signUpPath + 'signUp1.jpg', signUpPath + 'signUp2.jpg', signUpPath + 'signUp3.jpg', signUpPath + 'signUp4.jpg'],
                  'message':[messagePath + 'message1.jpg', messagePath + 'message2.jpg', messagePath + 'message3.jpg', messagePath + 'message4.jpg'],
                  'quick':[quickPath + 'quick1.jpg', quickPath + 'quick2.jpg', quickPath + 'quick3.jpg', quickPath + 'quick4.jpg'],
                  'contact':[contactPath + 'contact1.png', contactPath + 'contact2.png', contactPath + 'contact3.png', contactPath + 'contact4.png'],
                  'contact2':[contactPath2 + 'contact1.png', contactPath + 'contact2.png', contactPath + 'contact3.png', contactPath + 'contact4.png'],
                  'forgot':[forgotPath + 'forgot1.jpg', forgotPath + 'forgot2.jpg', forgotPath + 'forgot3.jpg', forgotPath + 'forgot4.jpg'],
                  'password':[passwordPath + 'password1.jpg', passwordPath + 'password2.jpg', passwordPath + 'password3.jpg', passwordPath + 'password4.jpg'],
                  'guitarVideos':[guitarVideosPath + 'dgv1.png', guitarVideosPath + 'dgv2.png', guitarVideosPath + 'dgv3.png', guitarVideosPath + 'dgv4.png'],
                  'stocks':[stockMarketPath + 'stocks1.png', stockMarketPath + 'stocks2.png', stockMarketPath + 'stocks3.png', stockMarketPath + 'stocks4.png'],
                  'grey':[greyPath + 'greyBut1.png', greyPath + 'greyBut2.png', greyPath + 'greyBut3.png', greyPath + 'greyBut4.png'],
                  'thd':[thdPath + 'thd1.png', thdPath + 'thd2.png', thdPath + 'thd3.png', thdPath + 'thd4.png'],
                  'builder':[builderPath + 'builder1.png', builderPath + 'builder2.png', builderPath + 'builder3.png', builderPath + 'builder4.png'],
                  'theFrog':[theFrogPath + 'theFrog1.png', theFrogPath + 'theFrog2.png', theFrogPath + 'theFrog3.png', theFrogPath + 'theFrog4.png']
    };


	/* We then must override the mouseover from the html file with this line.  */
	document.getElementById(id).src = images[id][1];

    /*  Button image manipulation then continues with these guys.  */

	document.getElementById(id).onmouseout = function() {mOut(id)};
	document.getElementById(id).onmouseover = function() {mOver(id)};
	document.getElementById(id).onmousedown = function() {mDown(id)};
	document.getElementById(id).onmouseup = function() {mUp(id)};


	function mOut(id) {
			document.getElementById(id).src = images[id][0];
		}

		function mOver(id) {
			document.getElementById(id).src = images[id][1];
		}

		function mDown(id) {
			document.getElementById(id).src = images[id][2];
		}

		function mUp(id) {
			document.getElementById(id).src = images[id][3];
		}


}  /* End getid   */