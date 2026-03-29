$(document).ready(function () {
    const $logo = $('.header img');

    if (!$logo.length) {
        return;
    }

    const baseWidth = $logo.width();

    $logo.hover(
        function () {
            $(this).stop(true).animate({ width: baseWidth + 20 }, 200);
        },
        function () {
            $(this).stop(true).animate({ width: baseWidth }, 200);
        }
    );
});