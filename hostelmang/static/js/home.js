document.addEventListener('DOMContentLoaded', function() {
    const menuButton = document.querySelector('.menu-button');
    const menuList = document.querySelector('.menu-list');
  
    menuButton.addEventListener('click', function() {
      menuButton.classList.toggle('open');
      menuList.classList.toggle('show');
    });
  });
  