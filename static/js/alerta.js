window.onload = function() {
    // Mostrar alertas usando el alert de JavaScript
    const messages = document.querySelectorAll('.messages .alert');
    if (messages.length > 0) {
        alert(messages[0].innerText);
    }

    // Agregar evento para el botón de cerrar
    const closeButtons = document.querySelectorAll('.alert .close-btn');
    closeButtons.forEach(function(button) {
        button.addEventListener('click', function() {
            const alert = this.parentElement;
            alert.classList.add('fade');
            setTimeout(function() {
                alert.remove();
            }, 500);
        });
    });
};
