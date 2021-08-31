var initialSrc = "/static/images/Logo_White.png";
var scrollSrc = "/static/images/Logo_black.png";
$(window).scroll(function(){
  $('nav').toggleClass('scrolled', $(this).scrollTop() > 50);
  $('li a').toggleClass('scrolled', $(this).scrollTop() > 50);
  $('.navbar-dark').toggleClass('scrolled', $(this).scrollTop() > 50);
  $('.navbar-toggler-icon').toggleClass('scrolled', $(this).scrollTop() > 50);
  $('.search').toggleClass('scrolled', $(this).scrollTop() > 50);
   var value = $(this).scrollTop();
   if (value > 50)
      $(".logo").attr("src", scrollSrc);
   else
      $(".logo").attr("src", initialSrc);

});


//Get the button
var mybutton = document.getElementById("myBtn");

// When the user scrolls down 20px from the top of the document, show the button
window.onscroll = function() {scrollFunction()};

function scrollFunction() {
  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    mybutton.style.display = "block";
  } else {
    mybutton.style.display = "none";
  }
}

// When the user clicks on the button, scroll to the top of the document
function topFunction() {
  document.body.scrollTop = 0;
  document.documentElement.scrollTop = 0;
}


// search
$(document).ready(function() {
  $('.search').click(function() {
      $('#searchbar').show();
      $('#close').show();
      $('#searchbtn').hide();
      $('#mainbar').hide();
  });
  $('#close').click(function() {
    $('#close').hide();
      $('#searchbar').hide();
      $('#mainbar').show();
      $('#searchbtn').show();
  });
});
