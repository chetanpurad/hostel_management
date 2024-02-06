document.addEventListener('DOMContentLoaded', function() {
    const loginForm = document.getElementById('loginForm');
    const forgotPasswordLink = document.getElementById('forgotPassword');
    const registerLink = document.getElementById('registerLink');
  
    loginForm.addEventListener('submit', function(event) {
      const usernameInput = document.getElementById('username');
      const passwordInput = document.getElementById('password');
  
      if (usernameInput.value.trim() === '' || passwordInput.value.trim() === '') {
        event.preventDefault();
        alert('Please fill in all fields.');
      }
    });
  
    forgotPasswordLink.addEventListener('click', function(event) {
      event.preventDefault();
      // Implement your forgot password functionality here
    });
  
    registerLink.addEventListener('click', function(event) {
      event.preventDefault();
      // Redirect to the registration page or implement the registration process here
    });
  });
  