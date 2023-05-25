const checkbox1 = document.getElementById('checkbox1');
const checkbox2 = document.getElementById('checkbox2');
const message1 = document.getElementById('message1');
const message2 = document.getElementById('message2');
const nextButton = document.getElementById('nextButton');

nextButton.addEventListener('click', function() {
    if (!checkbox1.checked) {
        message1.innerText = "Please agree to Terms of Service.";
    } else {
        message1.innerText = "";
    }

    if (!checkbox2.checked) {
        message2.innerText = "Please agree to Privacy Policy and the processing of your health information.";
    } else {
        message2.innerText = "";
    }
    if (checkbox1.checked && checkbox2.checked) {
        window.location.href = "{% url 'interview0'%}";
    }
});

var slideButton = document.getElementById('slideButton');
var slider = document.getElementById('slider');
var closeButton = document.getElementById('closeButton');

slideButton.addEventListener('click', function() {
    slider.classList.add('active');
});

closeButton.addEventListener('click', function() {
    slider.classList.remove('active');
});

pageContent.addEventListener('click', function(event) {
    if (!slider.contains(event.target)) {
        slider.classList.remove('active');
    }
});