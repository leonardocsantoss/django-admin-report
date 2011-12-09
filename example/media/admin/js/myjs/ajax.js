function getAjax(url, thisId, field, thisNome, objHtmlReturn){
    objRetorno = thisId.split(thisNome)[0]+objHtmlReturn;
    document.getElementById(objRetorno).innerHTML = '<option value="" selected="selected">---------</option>';

    (function($) {
    	$.ajax({
	        type: "GET",
	        url: url,
	        dataType: "json",
	        success: function(retorno){
	            $.each(retorno, function(i, item){
	                document.getElementById(objRetorno).innerHTML += "<option value="+item.pk+">"+item.fields[field]+"</option>";
	            });
	        }
	    });
    })(jQuery);
}