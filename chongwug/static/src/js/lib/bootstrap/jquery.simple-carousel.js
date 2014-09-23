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
               itemWidth = $curr.outerWidth(),
               totalWidth = itemWidth * $li.length,
               wrapperWidth = $wrapper.width(),
               $prev = $(settings.prev),
               $next = $(settings.next);

            $ul.width(totalWidth);

            $next.on('click', function(){
                $curr.removeClass('active');
                ($curr = nextLi()).addClass('active');
                settings.callback($curr);
            });

            $prev.on('click', function(){
                $curr.removeClass('active');
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

            function animateUl(){
                var len = $curr.index() + 1;

                
            }
        });
    }

})(jQuery);