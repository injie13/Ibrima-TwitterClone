////////////////////////
// JavaScript for Posts page
////////////////////////

$(function() {
    // Executed when js-menu-icon js clicked
    $('.js-menu-icon').click(function() {
        // $(this) : Self element, namely div.js-menu-icon
        // Next : Next to div.js-menu-icon, namely
        // toggle() : Switch show and hide
        $(this).next().toggle();
    })
        
})

function like() {
    document.getElementById("like").style.color = "red";
    console.log("Hello")
}