$("li.resource-item").click(function(e) {
    var url = $(this).children("a.heading").first().attr("href");
    console.log(url);
    if ($(e.target).is("li.resource-item")) {
        window.location = url;
    }
});
