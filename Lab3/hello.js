const promise = new Promise(function(resolve, reject) {
    setTimeout(function() {
        resolve('Rejected!');
    }, 1000);
})

promise.catch(function(value) {
    console.log(value);
});