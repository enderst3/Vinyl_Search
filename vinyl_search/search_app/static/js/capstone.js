'use strict';

$(document).ready(function(){
    
    function clear() {
    
        $('#choose_img').on('click', function(evt){// btn click event
            $('#info_box').remove();// removes album info if any there  
            $('#image').empty(); // removes thumb img
         });
        
        
        $('#submit').on('click', function(evt){// btn click event
            $('#wait').append('<div id="loading">Searching...</div>');// add searching text
        });
        
    };
    
    clear();
    
    function add_image() {
            
        // get image when choosen by user
        document.getElementById("choose_img").onchange = function () {
             var reader = new FileReader();

             reader.onload = function (e) {
                // get loaded data and render thumbnail.
                 document.getElementById("image").src = e.target.result;
              };

            // read the image file as a data URL.
                 reader.readAsDataURL(this.files[0]);
        };
        
    };
    
    add_image();
});
    