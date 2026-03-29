$(document).ready(function () {
    let scrolled = 0;
    let yPosition = 0;

    const $parallaxElements = $('.icons-for-parallax img');
    const $logo = $('.parallax-logo');

    const basePositions = [];
    $parallaxElements.each(function () {
        basePositions.push(parseFloat($(this).css('top')) || 0);
    });

    const baseLogoTop = parseFloat($logo.css('top')) || 0;

    $(window).on('scroll', function () {
        scrolled = $(window).scrollTop();

        for (let i = 0; i < $parallaxElements.length; i++) {
            yPosition = basePositions[i] + (scrolled * 0.15 * (i + 1));
            $parallaxElements.eq(i).css({ top: yPosition + 'px' });
        }

        $logo.css({
            top: (baseLogoTop + scrolled * 0.08) + 'px'
        });
    });
});