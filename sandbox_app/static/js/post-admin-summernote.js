$(document).ready(function () {
    $('.summernote-widget').each(function (index) {
        // Select summernote container (#id-body)
        var $sn = $('#' + $(this).attr('id'));

        $sn.summernote({
            placeholder: 'Enter your message.',
            tabsize: 2,
            width: 800,
            height: 600
        });
    });
});
