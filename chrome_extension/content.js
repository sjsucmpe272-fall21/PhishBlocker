window.onload = function() {
	//alert('Hello world! I am '+ window.location.href)
	var urls = document.getElementsByTagName('a');
	for (url in urls) {
		console.log ( urls[url].href );
		urls[url].style.backgroundColor = "#FDFF47";
	}
	//highlightText(document.body,"create");
}

// function highlightText(element,text) {
// 	var nodes = element.childNodes;
// 	for (var i = 0, l = nodes.length; i < l; i++) {
// 	  if (nodes[i].nodeType === 3) { // Node Type 3 is a text node
// 		nodes[i].innerHTML = "<span style='background-color:red'>" + text + "</span>";
// 	  }
// 	  else if (nodes[i].childNodes.length > 0) {
// 		highlightText(nodes[i],text);  // Not a text node or leaf, so check it's children
// 	  }
// 	}
// }