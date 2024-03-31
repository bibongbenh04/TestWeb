/*!
* Start Bootstrap - Clean Blog v6.0.9 (https://startbootstrap.com/theme/clean-blog)
* Copyright 2013-2023 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-clean-blog/blob/master/LICENSE)
*/
window.addEventListener('DOMContentLoaded', () => {
    let scrollPos = 0;
    const mainNav = document.getElementById('mainNav');
    if (!mainNav) return;
    const headerHeight = mainNav.clientHeight;
    window.addEventListener('scroll', function() {
        const currentTop = document.body.getBoundingClientRect().top * -1;
        if ( currentTop < scrollPos) {
            // Scrolling Up
            if (currentTop > 0 && mainNav.classList.contains('is-fixed')) {
                mainNav.classList.add('is-visible');
            } else {
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
const load_more_posts = document.querySelector('.moreblogs');
const load_more_sciences = document.querySelector('.moresciences');
const checkSearch = document.querySelector('.search');

$(document).ready(function() {
    var offset = 5;
    var intervalID = null;

    // Hàm để tải thêm bài viết hoặc khoa học
    function loadMore() {
        if (load_more_posts) {
            $.get('/load-more-posts/?offset=' + offset, function(data) {
                $('.moreblogs').append(data);
                offset += 5;
            });
        } else if (load_more_sciences) {
            $.get('/load-more-sciences/?offset=' + offset, function(data) {
                $('.moresciences').append(data);
                offset += 5;
            });
        }
    }

    // Hàm kiểm tra điều kiện và tải thêm nội dung khi cần
    function checkAndLoad() {
        if (parseInt($(window).scrollTop()) * 2.5 >= parseInt($(document).height()) - 10 - parseInt($(window).height())) {
            loadMore(); // Tải thêm bài viết hoặc khoa học nếu cần
        }
    }

    // Bắt đầu kiểm tra sau mỗi khoảng thời gian 5 giây
    intervalID = setInterval(checkAndLoad, 5000);

    // Dừng kiểm tra khi người dùng thực hiện tìm kiếm
    $(window).scroll(function() {
        if(checkSearch) {
            clearInterval(intervalID); // Dừng kiểm tra khi người dùng tìm kiếm
            return;
        }
    });
});
