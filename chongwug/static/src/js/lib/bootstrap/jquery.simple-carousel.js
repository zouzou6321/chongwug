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
               $prev = $(settings.prev),
               $next = $(settings.next);

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

            function nextLi(){
                var $next = $curr.next('li');
                return $next.length ? $next : $li.first();
            }

            function prevLi(){
                var $prev = $curr.prev('li');
                return $prev.length ? $prev : $li.last();
            }
        });
    }

})(jQuery);