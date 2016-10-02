getAjax();
function getAjax() {
	$.ajax({
	url: "https://api.myjson.com/bins/2imwo",
	dataType: 'json',
	//data: {},
	type: 'GET',
	success: function(data) {
	  console.log("success");
	 $('#cards').html(showMenu(data));	
	}
	})
}


function showMenu(data) {
	imageArray = [];
	priceArray = [];
	string = "";
	images = data.length;
	for(j=0;j<images;j++) {
		imageArray[j] = data[j]["name"];
		priceArray[j] = data[j]["price"];
	}
	string = "<form method=\'POST\' id=\'menu\'>"	
	for(i = 0; i < images; i++) {
		
		string += "<div class=\"col s12 m4 l4 center-align\"><div class=\"card\"><div class=\"card-image\"><img class=\"responsive-img\" id=\"menuTag\" src=\"../static/images/" + imageArray[i] + ".jpg\"><span class=\"card-title\">" + imageArray[i] + "</span></div><div class=\"card-action\"><p>Rs. " + priceArray[i] +"</p><input class=\"validate\" type=\"text\" name=\"" + imageArray[i] + "\" id=\"" + imageArray[i] +"\"></div></div></div>";
		console.log(string);
	}
	string +="<input placeholder=\"Address\" class=\"validate\" type=\"text\" name=\"Address\" id=\"Address\"></form><button type=\'submit\' form=\'menu\' method=\'POST\' class=\"btn waves-effect waves-light\">Submit</button>";
	return string;
}