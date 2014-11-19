(function($){

    $.fn.simpleCarousel= function(settings){

        var defaultSettings = {

        };

        settings = $.extend(defaultSettings, settings);

        return this.each(function(){
           var $wrapper = $(this),
               $ul = $wrapper.find('ul'),
               $li = $ul.find('li'),
               $curr = $li.filter('.active'),
               itemWidth = settings.itemWidth || $curr.outerWidth(),
               itemTotal = $li.length,
               totalWidth = itemWidth * itemTotal,
               $prev = $(settings.prev),
               $next = $(settings.next);

            $ul.width(totalWidth);

            $next.on('click', function(){
                $curr.removeClass('active');
                moveNext();
                ($curr = nextLi()).addClass('active');
                settings.callback($curr);
            });

            $prev.on('click', function(){
                $curr.removeClass('active');
                movePrev();
                ($curr = prevLi()).addClass('active');
                settings.callback($curr);
            });

            $ul.on('click', 'li', function(){
                var $this = $(this);

                if($this.hasClass('active')){
                    return;
                }

                $curr.removeClass('active');
                ($curr = $this).addClass('active');
                settings.callback($curr);
            });

            function nextLi(){
                var $next = $curr.next('li');
                return $next.length ? $next : $li.first();
            }

            function prevLi(){
                var $prev = $curr.prev('li');
                return $prev.length ? $prev : $li.last();
            }

            function movePrev(){
                var prev = prevLi().index(),
                    left = parseInt($ul.css('left'), 10),
                    leftNum = Math.abs(left) / itemWidth;

                if(prev == itemTotal - 1){
                    $ul.css('left', -(itemTotal - 5) * itemWidth);
                }else if(leftNum == prev + 1){
                    $ul.css('left', left + itemWidth);
                }
            }

            function moveNext(){
                var next = nextLi().index(),
                    left = parseInt($ul.css('left'), 10),
                    leftNum = Math.abs(left) / itemWidth;

                if(next == 0){
                    $ul.css('left', 0);
                }else if(leftNum + 5 == next){
                    $ul.css('left', left - itemWidth);
                }
            }
        });
    }

})(jQuery);