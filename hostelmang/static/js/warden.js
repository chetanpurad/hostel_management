/* static/js/warden_dashboard.js */
document.addEventListener('DOMContentLoaded', function() {
    const tableRows = document.querySelectorAll('table tr');
    
    tableRows.forEach(row => {
        row.addEventListener('mouseover', () => {
            row.classList.add('highlight');
        });
        
        row.addEventListener('mouseout', () => {
            row.classList.remove('highlight');
        });
    });
});
