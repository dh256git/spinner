document.addEventListener('DOMContentLoaded', function() {
  const easyReadButton = document.getElementById('easyread-button');
  const mainContent = document.querySelector('main .main-content');
  const easyReadContent = document.querySelector('main .easyread');

  easyReadButton.addEventListener('click', function(event) {
    event.preventDefault();
    document.body.classList.toggle('easyread');
    mainContent.classList.toggle('hidden');
    easyReadContent.classList.toggle('hidden');
  });
});
