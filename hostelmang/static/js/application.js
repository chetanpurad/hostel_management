
$(document).ready(function() {
    $('#date_of_birth').datepicker({
      format: 'yyyy-mm-dd', // Set your desired date format
      autoclose: true
    });
  });



document.addEventListener('DOMContentLoaded', function() {
    const admissionForm = document.getElementById('admissionForm');
    admissionForm.addEventListener('submit', function(event) {
      if (!admissionForm.checkValidity()) {
        event.preventDefault();
        event.stopPropagation();
      }
  
      admissionForm.classList.add('was-validated');
    });
  });
  
document.addEventListener('DOMContentLoaded', function() {
    const differentAddressCheckbox = document.getElementById('different_address_checkbox');
    const currentAddressField = document.getElementById('current_address');
    
    // Initial state
    currentAddressField.disabled = differentAddressCheckbox.checked;
  
    differentAddressCheckbox.addEventListener('change', function() {
      currentAddressField.disabled = this.checked;
      if (this.checked) {
        currentAddressField.value = ''; // Clear the field if it's disabled
      }
    });
  });
  