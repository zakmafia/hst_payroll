var messagesElement = document.getElementById('messages');

if (messagesElement) {
  messagesElement.style.opacity = '1';

  setTimeout(function() {
    messagesElement.style.opacity = '0';
    messagesElement.style.transition = 'opacity 1s ease-in-out';

    // Add an event listener to remove the element after the fade-out animation
    messagesElement.addEventListener('transitionend', function() {
      messagesElement.remove();
    });
  }, 4000);
}
  