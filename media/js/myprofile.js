$(document).ready(function() {
    $('div.my_work> div').hide();

    $('div.my_work> span').click(function() {
       $(this).next().slideToggle('fast');
    });
});
