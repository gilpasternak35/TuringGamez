// Buttons nested within slider, appear when button is clicked
// Second Button appears when first field is entered 
$(document).ready(function () {
    $("#new-game-slider").click(function () {
        $("#inputs, #artist").slideToggle("slow");
    });
    $("#artist-button").click(function () {
        var x = $("#artist-name").val();
        if (x != "") {
            $("#song").show();
        } else {
            //alert('Please enter an artist name.');
        }
    });
    $('#title-button').click(function () { // This function belongs in the controller
        var title = $('#song-title').val();
        
        if(title != "") { 
            // **NOTE: Remember to now double check that artist name is still a
            // valid string 
            var artist = $('#artist-name').val();

            if(artist != "") {
                $('#song-text').text(title).show();
            } else {
                //alert('Please resubmit a valid artist name.'); 
            }
        } else {
            //alert('Please enter a song title.');
            
        }
    });
});

//As referenced on the following page: https://stackoverflow.com/questions/7099916/how-to-pass-parameter-from-backend-to-frontend-if-dont-use-hidden-field-control
$(document).ready(function(){
  $(".start-game").click(function(){
    // This is to be changed once we know specific file path
    var value = "Hello-World"
    $("#song-text").text(value).show()
    $("#inputs, #artist, #song").slideUp(5000);
    $("#artist-name, #song-title").val("")
  });
});