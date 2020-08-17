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
        const packet = {
            'game-type': gameType,
            'difficulty': difficultyLevel,
            'artist-name': artistName,
            'song-title': songTitle,
            'wiki-topic': wikiTopic,
            'wiki-links': wikiLinkNum,
        };
        console.log(JSON.stringify(packet));


        // Generate an HTTP POST request
        // var httpRequest = new XMLHttpRequest();
        // httpRequest.open('POST', document.URL);
        // httpRequest.responseType = 'text';
        // httpRequest.onreadystatechange = (e) => {
        //     console.log(`Response: ${httpRequest.response}`);
        // };
        // httpRequest.send(packet);

        // TODO: Attempt HTTP Post request using JQuery
        $.post(document.URL,
            packet,
            (data, textStatus, jqXHR) => {
                console.log('SUCces.');
                console.log(`Data received: ${data}`);
                console.log(`Text Status: ${textStatus}`);
                console.log(`jQuery XHR:  ${jqXHR}`);
            },
            'json');
        // $.ajax({
        //     type: 'POST',
        //     url: document.URL,
        //     data: JSON.stringify({
        //         'game-type': gameType,
        //         'difficulty': difficultyLevel,
        //         'artist-name': artistName,
        //         'song-title': songTitle,
        //         'wiki-topic': wikiTopic,
        //         'wiki-links': wikiLinkNum,
        //     }),
        //     contentType: 'application/json; charset=utf-8',
        //     dataType: 'json',
        //     success: (data) => { console.log(data); },
        //     error: (jqXHR, textStatus, errorThrown) => { console.log(jqXHR); alert(textStatus);alert(errorThrown); }
        // });
    });
});
