$(document).ready(function(){
	$("#btn_test").click(function(){
		$("#my_text").fadeToggle(2000);
	})

	
	$("#dd_sample_type_lst li a").on("click", function(){
		var sampType_selection = $(this).text();
		$.ajax({
			type : "POST",
			url  : $SCRIPT_ROOT + "/Search",
			contentType: 'application/json;charset=UTF-8',
			data : JSON.stringify({"sample_type" : sampType_selection}),

			success: function(response) {
                    console.log(response);
                    $("#input_sample_type").val(sampType_selection)
                }
		});
		alert(new_sampTypes_values)
	});
});