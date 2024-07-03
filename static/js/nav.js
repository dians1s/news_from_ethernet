const navbarfixed = document.querySelector('.navigation');
window.onscroll = () => {
    if (window.scrollY > 80) {
        navbarfixed.classList.add('nav_active');
    }
    else {
        navbarfixed.classList.remove('nav_active');
    }
};