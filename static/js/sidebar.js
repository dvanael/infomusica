
$(document).on('click', '.open-btn', function () {
    $('.sidebar').addClass('active');
});

$(document).on('click', '.close-btn', function () {
    $('.sidebar').removeClass('active');
});

// $(".sidebar ul li").on('click', function () {
//     $(".sidebar ul li.active").removeClass('active');
//     $(this).addClass('active');
// });
const tooltipTriggerList = document.querySelectorAll('[data-bs-toggle="tooltip"]')
const tooltipList = [...tooltipTriggerList].map(tooltipTriggerEl => new bootstrap.Tooltip(tooltipTriggerEl))