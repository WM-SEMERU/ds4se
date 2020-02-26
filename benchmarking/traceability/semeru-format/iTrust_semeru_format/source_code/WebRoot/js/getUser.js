	function setUser(sName, uid, name) {
		if (0 < document.getElementsByName("UID_"+sName).length) {
			popField("UID_" + sName, uid);
		}
		
		if (0 < document.getElementsByName("NAME_"+sName).length) {
			popField("NAME_" + sName, name);
		}
		
		if (0 < document.getElementsByName(sName).length) {
			popField(sName, uid);
		}
		
		hideElement("getUserFrame");
	}
	
	function popField(fieldName, val) {
		if (document.getElementsByName(fieldName)[0].tagName.toUpperCase() == "INPUT")
			document.getElementsByName(fieldName)[0].value = val;
		else
			document.getElementsByName(fieldName)[0].innerHTML = val;
	}
	function getUser(sName) {
		document.getElementById("getUserFrame").src = "/iTrust/util/getUser.jsp?s=" + sName;
		showElement("getUserFrame");
		centerElement("getUserFrame");
	}
	function getUserClose() {
		hideElement("getUserFrame");
	}
