$(document).ready(function () {

    $('#error_id_dni').hide();

    $(window).keydown(function(event){
        if( (event.keyCode == 13) ) {
            event.preventDefault();
            return false;
        }
    });

    $('#submit-id-submit').click( function()
        {
            dni = $('#id_dni').val()
            $.ajax({
                url: '/api/participante/' + dni + '/',
                timeout: 5000,
            })
            .done(function(response) {
                $('#error_id_dni').hide();
                $('#div_id_dni').removeClass('has-error')
                $('#id_dni').val('')
            })
            .fail(function() {
                $('#div_id_dni').addClass('has-error');
                $('#error_mensaje_id_dni').empty().append('DNI no es valido o no esta inscrito.');
                $("#error_id_dni").show()
            })
        }
    );

});