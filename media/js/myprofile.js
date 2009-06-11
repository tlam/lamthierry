var popupStatus = 0;

function centerPopup(popup)
{    
    //request data for centering 
    var windowWidth = document.body.clientWidth;
    var windowHeight = document.body.clientHeight;
    var popupHeight = popup.height();
    var popupWidth = popup.width();

    //centering 
    popup.css({
        'position': 'absolute',
        'top': windowHeight/2-popupHeight/2, 
        'left': windowWidth/2-popupWidth/2
    }); 
} 

/*
 * Close the popup
 */
function closePopup() 
{
    //disables popup only if it is enabled 
    if (popupStatus == 1) 
    {
        $('.background_popup').fadeOut('slow'); 
        $('.popup_image').fadeOut('slow'); 
        popupStatus = 0; 
    }
} 

//loading popup with jQuery magic!
function loadPopup(background, popup)
{ 
    //loads popup only if it is disabled 
    if(popupStatus==0) 
    { 
        background.css({ 
            'opacity': '0.7'
        });

        background.fadeIn('def');
        popup.fadeIn('def'); 
        popupStatus = 1;
    } 
} 

$(document).ready(function() 
{
    $('div.my_work> div').hide();

    $('div.my_work> span').click(function() {
        $(this).next().slideToggle('fast');
    });

    $('div.my_work> a').click(function(e) {
        var background = $(this).next().next();
        var popup = $(this).next();

        centerPopup(popup); 
        loadPopup(background, popup);
    });

    //CLOSING POPUP 
    //Click the x event! 
    $('.popup_image_close').click(function() {
        closePopup();
    }); 

    //Click out event! 
    $('.background_popup').click(function() {
        closePopup(); 
    });

    // Press Escape event! 
    $(document).keyup(function(e) {
        if (e.keyCode == 27 && popupStatus == 1)
            closePopup();
    });
});
