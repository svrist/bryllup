// Initialize Flash
function initFlash() 
{
  if (document.getElementById && document.getElementById("gallery")) {
    var FO = {movie: "./images/flash/gallery.swf", width:"743", height:"508", majorversion:"7", build:"0", wmode: "transparent"};
    UFO.create(FO, "gallery");
  }
  
}

// Cross-browser event handling for IE5+, NS6 and Mozilla 
// By John Resig 
function addEvent( obj, type, fn ) {
	if (obj.addEventListener) {
		obj.addEventListener( type, fn, false );
 }	else if (obj.attachEvent)	{
		obj["e"+type+fn] = fn;
		obj[type+fn] = function() { obj["e"+type+fn]( window.event ); }
		obj.attachEvent( "on"+type, obj[type+fn] );
	}
}

addEvent(window, 'load', initFlash);

