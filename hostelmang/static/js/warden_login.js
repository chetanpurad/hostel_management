/* static/js/warden_login.js */
document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('form');
    const spinner = document.querySelector('.spinner');

    form.addEventListener('submit', function() {
        spinner.style.display = 'block';
    });
});
