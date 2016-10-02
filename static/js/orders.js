getAjax();
/*$(document).ready(function(){
	$('#orderModal').on("click",function(){
		getAjax();
	})
})*/

function getAjax() {
	$.ajax({
	url: "https://api.myjson.com/bins/2lpbo",
	data: {},
	dataType: 'json',
	success: function(data) {
		string = "";
		idArray = []
		price = 0;
		var myObject = data;
		var count = Object.keys(myObject).length;
		console.log(count);
		j=1;
		for(var i=1;i<=count;i++)
		{	price = 0;
			Name = [];
			while(j<=count){
				console.log("Entered in while");
			if(j-1>count) {
				break;
			}

			if(data[j-1]["OrderID"]==i) {
				console.log('Entered in if');
				price += data[j-1]["Quantity"] * data[j-1]["Price"];
				Name.push(data[j-1]["Dish Name"]);
				idArray.push(data[j-1]["OrderID"]);
				console.log(idArray)
				console.log(price);
				j++;
			}
			else {
				console.log(price);
				console.log(Name);
				console.log(idArray);
				break;
			}

			}
			if(price == 0 || Name === 0){
				continue
			}
			else{
				uniqueArray = idArray.filter(function(item, pos) {
    			return idArray.indexOf(item) == pos;
			})
			$("#modalRow").append("<div class='col m6 s6 l6'>"+ price + "</div><div class='col m6 l6 s6'>" + Name + "</div><br>");

			}
		}	

	}
	})
} 