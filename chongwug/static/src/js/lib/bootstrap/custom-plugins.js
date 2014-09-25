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

(function($){
    $.args = function (key){
        var qs = (location.search.length > 0 ? location.search.substring(1) : ""),
            args = {},
            items = qs.length ? qs.split("&") : [],
            item = null,
            name = null,
            value = null,
            i = 0,
            len = items.length;

        for (i=0; i < len; i++){
            item = items[i].split("=");
            name = decodeURIComponent(item[0]);
            value = decodeURIComponent(item[1]);

            if (name.length){
                args[name] = value;
            }
        }

        return args[key] || args;
    };
})(jQuery);