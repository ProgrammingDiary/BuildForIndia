getAjax();
$(document).ready(function() {
    $('select').material_select();
    //getAjax()
  });

function getAjax() {
	$.ajax({
		url: "https://api.myjson.com/bins/467yw",
		dataType: 'json',
		type: 'GET',
		success: function(data) {
			console.log("Got the request");
			console.log(data[0]["name"]);
			$('#collegeNames').html(populateSelect(data));	
		},
		async: false
	})
}

function populateSelect(data) {
	name = ""
	for(i=0;i<6;i++) {
		name += "<option>" + data[i]["name"] + "</option>";
		console.log(name)
	}

	return name
}