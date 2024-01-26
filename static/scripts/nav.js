document.addEventListener("DOMContentLoaded", function() {
    var header = document.querySelector("header");
    var nav = document.querySelector("nav");
    var offset = header.offsetHeight;

    function toggleFixedHeader() {
        if (window.scrollY > offset) {
            header.classList.add("fixed-header");
            nav.style.marginTop = offset + "px";
        } else {
            header.classList.remove("fixed-header");
            nav.style.marginTop = "0";
        }
    }

    window.addEventListener("scroll", toggleFixedHeader);
    toggleFixedHeader();
});