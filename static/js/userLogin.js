getAjax();
$(document).ready(function() {
    $('select').material_select();
    //getAjax()
  });

function getAjax() {
	$.ajax({
		url: "../../college.json",
		dataType: 'json',
		type: 'GET',
		success: function(data) {
			console.log("Got the request");
			console.log(data[0]["name"]);
			$('#collegeNames').html("<option>" + data[0]["name"] + "</option><option>" + data[1]["name"] + "</option>");
			//$('#collegeNames').selectpicker('refresh');	
		},
		async: false
	})
}