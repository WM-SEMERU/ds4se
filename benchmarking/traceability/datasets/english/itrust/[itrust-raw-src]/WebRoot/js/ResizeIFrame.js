var IFG__isResizing = false;

function IFG__doResizing(frameName, optionalMinHeight) {
	IFG__isResizing = true;
	
	try {
		optionalMinHeight = (optionalMinHeight == null ? 10 : optionalMinHeight);
		
		if ((document.body.scrollWidth != 0 && document.body.clientWidth) ||
			(document.body.scrollHeight != 0 && document.body.clientHeight != 0 && document.body.scrollHeight > optionalMinHeight)) {
				parent.resizeFrame(frameName, document.body.scrollWidth, document.body.scrollHeight);
			}
		else {
			IFG__isResizing = false;
			setTimeout("IFG__resizeParent()", 100);			
		}
	}
	catch (e) {
		// IE6 throws an "Access Denied" error if the user clicks the browser's 
		// scrollbar when active and then causes window.resizeBy() to be called...
	}
	
	IFG__isResizing = false;
	
	return false;
}

function IFG__resizeParent(frameName, optionalMinHeight) {
	// Resize event is fired continuously when a browser is resized; only resize 
	// if we're not currently resizing...
	if (!IFG__isResizing) {
		IFG__doResizing(frameName, optionalMinHeight);		
	}
}

function centerElement(id)
{
	var elem = document.getElementById(id);	
	elem.style.position = 'absolute';
	elem.style.top = ((document.body.clientHeight - elem.offsetHeight) / 2) + document.body.scrollTop;
	elem.style.left = ((document.body.clientWidth - elem.offsetWidth) / 2) + document.body.scrollLeft;
}

function hideElement(id) {
	var elem = document.getElementById(id);		
	elem.style.display = 'none';	
}

function showElement(id) {
	var elem = document.getElementById(id);
	elem.style.display = '';
}

function resizeFrame(fn, w, h) {
	var elem = document.getElementById(fn);
	elem.Width = w;
	elem.Height = h;
	//alert(elem.Height);
}