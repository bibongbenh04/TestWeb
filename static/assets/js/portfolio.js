// Xử lý bộ lọc danh mục
document.addEventListener('DOMContentLoaded', () => {
    const filterButtons = document.querySelectorAll('#portfolio-flters li');
    const portfolioItems = document.querySelectorAll('.portfolio-item');

    filterButtons.forEach(button => {
        button.addEventListener('click', () => {
            const filter = button.getAttribute('data-filter');

            // Cập nhật trạng thái active của bộ lọc
            filterButtons.forEach(btn => btn.classList.remove('filter-active'));
            button.classList.add('filter-active');

            // Hiển thị/ẩn các item theo bộ lọc
            portfolioItems.forEach(item => {
                if (filter === '*' || item.classList.contains(filter.substring(1))) {
                    item.style.display = 'block';
                    item.classList.add('fade-in');
                    item.classList.remove('fade-out');
                } else {
                    item.style.display = 'none';
                    item.classList.add('fade-out');
                    item.classList.remove('fade-in');
                }
            });
        });
    });

    // Mặc định hiển thị tất cả các item
    document.querySelector('#portfolio-flters .filter-active').click();
});
