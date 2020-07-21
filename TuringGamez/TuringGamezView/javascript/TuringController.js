$(document).ready(() => {
    $('.start-game').click(() => {
        /**
         * Gametype agnostic parameters
         */
        // Gametype is the title of the webpage
        var gameType = document.title.trim().replace(/ /g, '-').toLowerCase()
        console.log(`Game Type: ${gameType}`)
        var difficultyLevel = $('#level').val() // Game difficulty level
        console.log(`Difficulty: ${difficultyLevel}`)

        /**
         * Gametype specific parameters
         */
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
        } else {
            // If no artist or topic is found, it's a quote game.
            // Set artistName and wikiTopic to null for uniformity within the JSON packet.
            artistName = null;
            wikiTopic = null;
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
