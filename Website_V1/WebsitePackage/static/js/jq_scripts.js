$(document).ready(function(){

/////////////////////// DELETE RECORD \\\\\\\\\\\\\\\\\\\\\\\

	$("#dd_sample_type_lst_d li a").on("click", function(){
		var sampType_selection = $(this).text();
		$.ajax({
			type : "POST",
			url  : $SCRIPT_ROOT + "/Delete_Record",
			contentType: 'application/json;charset=UTF-8',
			data : JSON.stringify({"sample_type" : sampType_selection}),

			success: function(response) {
                    console.log(response);
                    $("#delete_sample_type").val(sampType_selection)
                }
		});
		alert(new_sampTypes_values)
	});

/////////////////////// SEARCH RECORD \\\\\\\\\\\\\\\\\\\\\\\
	
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


	$("#dd_analysis_type_lst li a").on("click", function(){
		var analysType_selection = $(this).text();
		$.ajax({
			type : "POST",
			url  : $SCRIPT_ROOT + "/Search",
			contentType: 'application/json;charset=UTF-8',
			data : JSON.stringify({"analysis_type" : analysType_selection}),

			success: function(response) {
                    console.log(response);
                    $("#input_analysis_type").val(analysType_selection)
                }
		});
		//alert(analysType_selection)
	});

/////////////////////// NEW RECORD \\\\\\\\\\\\\\\\\\\\\\\
	
	$("#dd_subject_group_lst_n li a").on("click", function(){
		var subject_g = $(this).text();
		$.ajax({
			type : "POST",
			url  : $SCRIPT_ROOT + "/New_Record",
			contentType: 'application/json;charset=UTF-8',
			data : JSON.stringify({"subjects_group" : subject_g}),

			success: function(response) {
                    console.log(response);
                    $("#input_subject_group_n").val(subject_g)
                }
		});
	});

	$("#subject_id").val();


});