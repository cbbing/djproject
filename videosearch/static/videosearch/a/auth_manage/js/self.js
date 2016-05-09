$(document).ready(function(){
	$(".form-control").parent().addClass("has-error");

	$(".form-control").keyup(function(event){
		if($(event.target).val() != ""){
			$(event.target).parent().removeClass("has-error");
			$(event.target).parent().addClass("has-success");
		}
		else{
			$(event.target).parent().removeClass("has-success");
			$(event.target).parent().addClass("has-error");
		}
	})

	$(".form-control").click(function(event){
		if($(event.target).val() != ""){
			$(event.target).parent().removeClass("has-error");
			$(event.target).parent().addClass("has-success");
		}
		else{
			$(event.target).parent().removeClass("has-success");
			$(event.target).parent().addClass("has-error");
		}
	})

	$(".form-control").mouseover(function(event){
		if($(event.target).val() != ""){
			$(event.target).parent().removeClass("has-error");
			$(event.target).parent().addClass("has-success");
		}
		else{
			$(event.target).parent().removeClass("has-success");
			$(event.target).parent().addClass("has-error");
		}
	})
})
