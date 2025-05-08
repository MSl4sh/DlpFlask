
document.addEventListener("DOMContentLoaded", function () {
  const currentPath = window.location.pathname;
  const links = document.querySelectorAll(".nav-link");

  links.forEach(link => {
    if (link.getAttribute("href") === currentPath) {
      link.classList.add("active");
    } else {
      link.classList.remove("active");
    }
  });
});

const navigate =(url)=>{
  window.location.href = url
}


const carousel = document.getElementById('carousel');
const btnLeft = document.getElementById('btn-left');
const btnRight = document.getElementById('btn-right');

function updateButtons() {
    btnLeft.disabled = carousel.scrollLeft <= 0;
    btnRight.disabled = carousel.scrollLeft + carousel.clientWidth >= carousel.scrollWidth - 1;
  }

function scrollCarouselLeft() {
    carousel.scrollBy({ left: -1000, behavior: 'smooth' });
}

function scrollCarouselRight() {
    carousel.scrollBy({ left: 1000, behavior: 'smooth' });
}

carousel.addEventListener('scroll', updateButtons);

window.addEventListener('load', updateButtons)