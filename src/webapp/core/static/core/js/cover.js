$("#positive_message").click(function(){
    $.ajax({
        url: "positive_message", 
        success: function(result) {
            console.log("positive_message");
            console.log(result);
        }
    });
});

$("#play_music").click(function(){
    $.ajax({
        url: "play_music",
        success: function(result) {
            console.log("play_music");
            console.log(result);
        }
    });
});