$(document).ready(function(){
  $('.carosel').slick({
    autoplay: true,
    autoplaySpeed: 5000
  });
});


$(function() {
  $('#tabs .nav-tabs li').on('click', function() {
    
    //remove active class from header
    $('#tabs .nav-tabs li a').removeClass('active');
    // find panel to show
    var newPanel = $(this).attr('rel');
    
    //add active class to header
    $(this).children('a').addClass('active');
     
    
    // hide the current panel and display new panel
    
    $('#tabs .active-panel').removeClass('active-panel').addClass('panel', function() {
      $('#'+newPanel).removeClass('panel').addClass('active-panel');
    });
  });
});

