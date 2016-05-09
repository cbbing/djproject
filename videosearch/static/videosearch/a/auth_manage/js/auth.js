$(document).ready(function(){
	if($("#answer").val() =="郑松山"){
		$("#go").removeClass("btn-danger");
		$("#go").removeClass("disabled");
		$("#go").addClass("btn-success");
		$("#go").text("机智！GO");
	}

	$("#answer").input(function(){
		if($("#answer").val() == "郑松山"){
			$("#go").removeClass("btn-danger");
			$("#go").removeClass("disabled");
			$("#go").addClass("btn-success");
			$("#go").text("机智！GO");
		}
		else{
			$("#go").removeClass("btn-success");
			$("#go").addClass("disabled");
			$("#go").addClass("btn-danger");
			$("#go").text("不要骗我！");
		}
	})

	$("#go").click(function(){
		document.cookie = 'authorized=true';
		window.location.href = "self";
	})
})