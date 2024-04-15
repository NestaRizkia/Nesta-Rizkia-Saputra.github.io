const mntoggle = document.querySelector('.menu-toggle input');
const nav = document.querySelector('nav ul');
// Select the image element
const image = document.getElementById('image1');

mntoggle.addEventListener('click',function(){
   nav.classList.toggle('menushow');
})


// Add an event listener for the scroll event
window.addEventListener('scroll', function() {
    // Get the current scroll position
    let scrollTop = window.scrollY;

    // Set the top position of the image to the scroll position
    image.style.top = scrollTop + 'px';
});

