const toggleButton = document.getElementById('darkModeToggle');
const icon = document.getElementById('darkModeIcon');

// Load preference from localStorage
if(localStorage.getItem('darkMode') === 'enabled') {
		document.body.classList.add('dark-mode');
		icon.classList.replace('bi-sun-fill', 'bi-moon-fill');
}

toggleButton.addEventListener('click', () => {
		document.body.classList.toggle('dark-mode');

		if(document.body.classList.contains('dark-mode')) {
				icon.classList.replace('bi-sun-fill', 'bi-moon-fill');
				localStorage.setItem('darkMode', 'enabled');
		} else {
				icon.classList.replace('bi-moon-fill', 'bi-sun-fill');
				localStorage.setItem('darkMode', 'disabled');
		}
});