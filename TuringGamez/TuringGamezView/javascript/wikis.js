// Buttons nested within slider, appear when button is clicked
// Second Button appears when first field is entered
$(document).ready(function () {
    $("#new-game-slider").click(function () {
        $("#inputs, #topic").slideToggle("slow");
    });
    $("#topic-button").click(function () {
        var x = $("#wiki-topic").val();
        if (x != "") {
            $("#links").show();
        }
    });
    $('#links-button').click(function () {
        var linkField = $('#wiki-links')
        var linkCount = linkField.val();

        // If the user input contains at least non-digit character, it is invalid.
        // This includes the "." character, so non-integer values are invalid.
        var pattern = new RegExp(/\D+/);
        if (linkCount == "" || pattern.test(String(linkCount))) {
            alert('Number of links must be a whole number. Please re-enter.');
            linkField.val("");
        } else {
            console.log("Number of wikipedia pages to traverse: " + linkCount);
        }
    });
});

$(document).ready(function(){
  $(".start-game").click(function(){
    // This is to be changed once we know specific file path
    var value = "Hello-World"
    $("#wiki-text").text(value).show()
    $("#inputs, #topic, #links").slideUp(5000);
    $("#wiki-topic, #wiki-links").val("")
  });
});