// Scroll animation ===================================================================================================================
const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
        console.log(entry);
        if (entry.isIntersecting){
            entry.target.classList.add('show');
        } else {
            entry.target.classList.remove('show');
        }
    })
}, {threshold: 0.7})

const hiddenElements = document.querySelectorAll('.hidden');
hiddenElements.forEach((e1) => observer.observe(e1));

// Button actions =======================================================================================================================
// Menu toggle
const toggleBtn = document.querySelector('.toggle-btn');
const toggleBtnIcon = document.querySelector('.toggle-btn i');
const dropDownMenu = document.querySelector('.dropdown-menu');

toggleBtn.onclick = () => {
    dropDownMenu.classList.toggle('open')

    toggleBtnIcon.classList = (dropDownMenu.classList.contains('open'))? "fa-solid fa-xmark": "fa-solid fa-bars"
}