if (document.getElementById("request-method").content === "GET") {
    var formContainers = document.getElementsByClassName('form-container');
    
    setTimeout(function() {
        for (var i = 0; i < formContainers.length; i++) {
            formContainers[i].style.transition = "opacity 1s ease-in-out";
            formContainers[i].style.opacity = '1';
        }
    }, 100);
}

if (document.getElementById("request-method").content === "POST") {
    var formContainers = document.getElementsByClassName('form-container');
    setTimeout(function() {
        for (var i = 0; i < formContainers.length; i++) {
            formContainers[i].style.transition = "none";
            formContainers[i].style.opacity = '1';
        }
    }, 1);
};

