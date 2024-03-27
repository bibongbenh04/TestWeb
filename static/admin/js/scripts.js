/*!
* Start Bootstrap - Clean Blog v6.0.9 (https://startbootstrap.com/theme/clean-blog)
* Copyright 2013-2023 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-clean-blog/blob/master/LICENSE)
*/
window.addEventListener('DOMContentLoaded', () => {
    let scrollPos = 0;
    const mainNav = document.getElementById('mainNav');
    const headerHeight = mainNav.clientHeight;
    window.addEventListener('scroll', function() {
        const currentTop = document.body.getBoundingClientRect().top * -1;
        if ( currentTop < scrollPos) {
            // Scrolling Up
            if (currentTop > 0 && mainNav.classList.contains('is-fixed')) {
                mainNav.classList.add('is-visible');
            } else {
                console.log(123);
                mainNav.classList.remove('is-visible', 'is-fixed');
            }
        } else {
            // Scrolling Down
            mainNav.classList.remove(['is-visible']);
            if (currentTop > headerHeight && !mainNav.classList.contains('is-fixed')) {
                mainNav.classList.add('is-fixed');
            }
        }
        scrollPos = currentTop;
    });
})
src="https://code.jquery.com/jquery-3.6.0.min.js";

$(document).ready(function() {
    var offset = 5;
    $(window).scroll(function() {
    // $('.btn.btn-primary.text-uppercase').click(function() {
        // console.log("check");    
        if(parseInt($(window).scrollTop()) * 2.5 >= parseInt($(document).height()) - 10 - parseInt($(window).height())) {
            $.get('/load-more-posts/?offset=' + offset, function(data) {
                // console.log(data);
                // $('.col-md-10.col-lg-8.col-xl-7.blogs').append(data);
                $('.moreblogs').append(data);
                // $('.col-md-10 col-lg-8 col-xl-7').append(data);
                offset += 5;
            });
        }
    });
});