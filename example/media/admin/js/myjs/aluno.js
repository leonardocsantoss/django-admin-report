(function($){
    $(document).ready(function(){
        $('.sitio').hide();
        if($('input[name="zona"]:checked').val() == 'R'){
            $('.sitio').slideDown();
        }
        $('input[name="zona"]').change(function() {
            if(this.value == 'R'){
                $('.sitio').slideDown();
            }else{
                $('.sitio').slideUp();
            }
        });

//        $('.onibus').hide();
//        if($('input[name="vai_onibus"]').attr('checked')){
//            $('.onibus').slideDown();
//        }
//        $('input[name="vai_onibus"]').change(function() {
//            $('.onibus').slideToggle();
//        });

    });
}(jQuery));