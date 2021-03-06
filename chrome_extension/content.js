window.onload = function() {
	//alert('Hello world! I am '+ window.location.href)
	var urls = document.getElementsByTagName('a');
	let urlList  =  [];
	for (url in urls) {
		urlList.push( urls[url].href+"" );
		//urls[url].style.backgroundColor = "#FDFF47";
	}

	//console.log('Sending input:',urlList)

	fetch("https://ec2-18-218-107-148.us-east-2.compute.amazonaws.com:8000/", {
		method: "POST",
		referrer:"unsafe-url",
		headers: {'Content-Type': 'application/json'} ,
		body: JSON.stringify({data:urlList})
	}).then(res => {
		res.text().then(function(text) {
			console.log('result is:',text);
			text = JSON.parse(text);
			let urlResp = text.data;
			let hoverDiv = document.createElement("div");
			hoverDiv.innerHTML = "<span style='color: red;'>This link is possibly malicious</span>";
			let go = document.createElement("button");
			go.innerHTML = "Go to Link";
			hoverDiv.appendChild(go);

			let safebutton = document.createElement("button");
			safebutton.innerHTML = "Safe URL?";
			hoverDiv.appendChild(safebutton);

			//hoverDiv.innerHTML = "I warn you malicious url";
			let malUrls = [];
			let malUrlScoreMap = {};
			for(let index in urlResp) {
				malUrls.push(urlResp[index].url);
				malUrlScoreMap[urlResp[index].url] = urlResp[index].prediction;
			} 
			for (url in urls) {
				if(malUrls.includes(urls[url].href+"")) {
					let ele = urls[url];
					let urltext = urls[url].href+"";
					let score = parseFloat(malUrlScoreMap[urltext])*100;
					score = Number((score).toFixed(2));
					if(urltext.length>100) {
						urltext = urltext.slice(0,100)+"...";
					}
					ele.title="We are "+score+"% sure that this link is Malicious. Please open it at your own risk. Following is the url:\n\n"+urltext;
					
					
					ele.onclick = (e)=>{
						e.preventDefault();
						ele.appendChild(hoverDiv);

						// cancel.onclick = ()=> {
						// 	ele.removeChild(hoverDiv);
						// }
						go.onclick = () => {
							alert('You are about to be redirected to a possibly to a malicious website. Click OK to continue or exit the window.');
							console.log(urltext);
							window.location.replace(urltext);
						}

						safebutton.onclick = () => {
							//ele.removeChild(hoverDiv);
							fetch("https://ec2-18-218-107-148.us-east-2.compute.amazonaws.com:8000/db", {
								method: "POST",
								referrer:"unsafe-url",
								headers: {'Content-Type': 'application/json'} ,
								body: JSON.stringify({url:urltext})
							}).then(response => {
								console.log(response);
							})
							alert("Recorded your input. Thanks for your time.");
						}
						
						//e.preventDefault();
						//alert('You are about to be redirected to a possibly to a malicious website. Click OK to continue or exit the window.');

					}
					urls[url].style.backgroundColor = "#FDFF47";
					// ele.onmouseover  = () => {
					// 	ele.appendChild(hoverDiv);
					// }
					// ele.onmouseout = () => {
					// 	ele.removeChild(hoverDiv);
					// }
				}
					
			}
			// for (url in urlResp) {
			// 	if(urlResp.includes(urls[url].href+"")) {
			// 		console.log('includes url:',url);
			// 		urls[url].style.backgroundColor = "#FDFF47";
			// 	}

					
			// 	//urls[url].style.backgroundColor = "#FDFF47";
			// }
		  });
		
	}).catch(err=> {
		console.log('error is:',err)
	});
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