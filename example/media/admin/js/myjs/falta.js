(function($){
    $(document).ready(function(){
        
        $('input.falta_extra').each(function(index, value) {
            var classe = $(this).parent().attr('class');
            $(this).hide();
        });

        $('.outras').click(function() {
            $('input.falta_extra').each(function(index, value) {
                $(this).toggle();
            });
        });
        
    });
}(jQuery));