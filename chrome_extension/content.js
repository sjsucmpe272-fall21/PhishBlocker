window.onload = function() {
	alert('Hello world! I am '+ window.location.href)
	var urls = document.getElementsByTagName('a');
	let urlList  =  [];
	for (url in urls) {
		urlList.push( urls[url].href+"" );
		//urls[url].style.backgroundColor = "#FDFF47";
	}

	fetch("http://3.22.236.108/", {
		method: "POST",
		mode: "cors",
		referrer:"unsafe-url",
		headers: {'Content-Type': 'application/json'} ,
		body: {data:urlList}
	}).then(res => {
		console.log('result is:',res);
	}).catch(err=> {
		console.log('error is:',err)
	});
		//highlightText(document.body,"create");
}