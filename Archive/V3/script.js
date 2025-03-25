function toggleTheme() {
    const checkbox = document.querySelector('.theme-switch__checkbox');
    if (checkbox.checked) {
        // When checked, set dark mode (remove light-mode class)
        document.body.classList.remove('light-mode');
    } else {
        // When unchecked, set light mode (add light-mode class)
        document.body.classList.add('light-mode');
    }
}