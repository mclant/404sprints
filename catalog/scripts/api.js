$((function(context) {
    return function() {
        
        $('#coolbtn').click(function() {

        $.ajax({
            "url": "/catalog/api.getdata/"
        }).done(function(data) {
            $('#coolTitle').html(data);
        });
        })


    }
})(DMP_CONTEXT.get()));