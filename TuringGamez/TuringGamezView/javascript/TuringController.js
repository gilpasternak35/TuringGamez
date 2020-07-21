$(document).ready(function () {
    $('.start-game').click(function () {
        // Gametype Agnostic parameters
        var gameType = document.title // Gametype is the title of the webpage
        console.log(`Game Type: ${gameType}`)
        var difficultyLevel = $('#level').val() // Game difficulty level
        console.log(`Difficulty: ${difficultyLevel}`)

        // Gametype specific parameters
        var artistName = $('#artist-name').val(); // Song game args
        var songTitle = null;
        var wikiTopic = $('#wiki-topic').val(); // Wiki game args
        var wikiLinkNum = null;

        // Look for an artist
        if (artistName != undefined) {
            songTitle = $('#song-title').val();

            // Guarantees uniformity in the json packet
            wikiTopic = null;
        } else if (wikiTopic != undefined) {
            // If no artist, look for a topic
            wikiLinkNum = $('#wiki-links').val();

            // Guarantees uniformity in the json packet
            artistName = null;
        }
        // If none of the above, then it's a quote game. All inputs found. JSONify.  
        packet = JSON.stringify({
            'game-type': gameType,
            'difficulty': difficultyLevel,
            'artist-name': artistName,
            'song-title': songTitle,
            'wiki-topic': wikiTopic,
            'wiki-links': wikiLinkNum,
        });
        console.log(`JSON Packet: ${packet}`)
    });
});
