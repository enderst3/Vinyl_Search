'use strict';

$(document).ready(function(){
    
    function clear() {
    
        $('#choose_img').on('click', function(evt){// btn click event
            $('#info_box').remove();// removes album info if any there  
         });
        
        $('#submit').on('click', function(evt){// btn click event
            $('#wait').append('<div id="loading">Searching...</div>');// add searching text
        });
        
    };
    
    clear();

});
    