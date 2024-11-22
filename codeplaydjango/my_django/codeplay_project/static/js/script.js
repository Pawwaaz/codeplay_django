$(document).ready(function () {
  $(".accordion-item-header").click(function () {
    // Toggle active class on click
    $(this).toggleClass("active");

    // Get the next sibling (accordion body)
    var accordionItemBody = $(this).next(".accordion-item-body");

    // Check if the header is active, then expand/collapse the body
    if ($(this).hasClass("active")) {
      accordionItemBody.css(
        "max-height",
        accordionItemBody.prop("scrollHeight") + "px"
      );
    } else {
      accordionItemBody.css("max-height", "0");
    }
  });
});
