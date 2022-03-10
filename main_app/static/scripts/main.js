const hamburger = document.querySelector(".navbar-burger");
const navMenu = document.querySelector(".navbar-menu");

hamburger.addEventListener("click", () => {
  hamburger.classList.toggle("is-active");
  navMenu.classList.toggle("is-active");
});
document.querySelectorAll(".AddToList").forEach(function (AddToList) {
  AddToList.addEventListener("click",function (event) {
    this.classList.toggle("is-active");
  })
});