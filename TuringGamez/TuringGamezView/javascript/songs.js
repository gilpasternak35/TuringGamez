// Buttons nested within slider, appear when button is clicked
// Second Button appears when first field is entered 
$(document).ready(function () {
    $("#new-game-slider").click(function () {
        $("#inputs").slideToggle("slow");
    });
    $("#artist-button").click(function () {
        var x = $("#artist-name").val();
        if (x != "") {
            $("#song").show();
        } else {
            alert('Please enter an artist name.');
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
                alert('Please resubmit a valid artist name.'); 
            }
        } else {
            alert('Please enter a song title.');
            
        }
    });
});