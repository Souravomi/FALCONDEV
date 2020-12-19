$(document).ready(function() {
  function setClasses(index, steps) {
    if (index < 0 || index > steps) return;
    if(index == 0) {
      $("#prev").prop('disabled', true);
    } else {
      $("#prev").prop('disabled', false);
    }
    if(index == steps) {
      $("#next").text('done');
    } else {
      $("#next").text('next');
    }
    $("ul li").each(function() {
      $(this).removeClass();
    });
    $("ul li:lt(" + index + ")").each(function() {
      $(this).addClass("done");
    });
    $("ul li:eq(" + index + ")").addClass("active")
    var p = index * (100 / steps);
    $("#prog").width(p + '%');
  }
  $(".step-wizard ul a").click(function() {
    var step = $(this).find("span.step")[0].innerText;
    var steps = $(".step-wizard ul li").length;
    setClasses(step - 1, steps - 1)
  });
  $("#prev").click(function(){
    var step = $(".step-wizard ul li.active span.step")[0].innerText;
    var steps = $(".step-wizard ul li").length;    
    setClasses(step - 2, steps - 1);
  });
  $("#next").click(function(){
    if ($(this).text() == 'done') {
      alert("submit the form?!?")
    } else {
      var step = $(".step-wizard ul li.active span.step")[0].innerText;
      var steps = $(".step-wizard ul li").length;    
      setClasses(step, steps - 1);
    }
  });
  
  // initial state setup
  setClasses(0, $(".step-wizard ul li").length);
});