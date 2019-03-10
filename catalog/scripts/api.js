$((function(context) {
    return function() {
        console.log('in the js');
    }
})(DMP_Context.get()));