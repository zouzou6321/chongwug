+function(t){"use strict";function e(e){return this.each(function(){var n=t(this),o=n.data("bs.carousel"),a=t.extend({},i.DEFAULTS,n.data(),"object"==typeof e&&e),r="string"==typeof e?e:a.slide;o||n.data("bs.carousel",o=new i(this,a)),"number"==typeof e?o.to(e):r?o[r]():a.interval&&o.pause().cycle()})}var i=function(e,i){this.$element=t(e).on("keydown.bs.carousel",t.proxy(this.keydown,this)),this.$indicators=this.$element.find(".carousel-indicators"),this.options=i,this.paused=this.sliding=this.interval=this.$active=this.$items=null,"hover"==this.options.pause&&this.$element.on("mouseenter.bs.carousel",t.proxy(this.pause,this)).on("mouseleave.bs.carousel",t.proxy(this.cycle,this))};i.VERSION="3.2.0",i.DEFAULTS={interval:5e3,pause:"hover",wrap:!0},i.prototype.keydown=function(t){switch(t.which){case 37:this.prev();break;case 39:this.next();break;default:return}t.preventDefault()},i.prototype.cycle=function(e){return e||(this.paused=!1),this.interval&&clearInterval(this.interval),this.options.interval&&!this.paused&&(this.interval=setInterval(t.proxy(this.next,this),this.options.interval)),this},i.prototype.getItemIndex=function(t){return this.$items=t.parent().children(".item"),this.$items.index(t||this.$active)},i.prototype.to=function(e){var i=this,n=this.getItemIndex(this.$active=this.$element.find(".item.active"));return e>this.$items.length-1||0>e?void 0:this.sliding?this.$element.one("slid.bs.carousel",function(){i.to(e)}):n==e?this.pause().cycle():this.slide(e>n?"next":"prev",t(this.$items[e]))},i.prototype.pause=function(e){return e||(this.paused=!0),this.$element.find(".next, .prev").length&&t.support.transition&&(this.$element.trigger(t.support.transition.end),this.cycle(!0)),this.interval=clearInterval(this.interval),this},i.prototype.next=function(){return this.sliding?void 0:this.slide("next")},i.prototype.prev=function(){return this.sliding?void 0:this.slide("prev")},i.prototype.slide=function(e,i){var n=this.$element.find(".item.active"),o=i||n[e](),a=this.interval,r="next"==e?"left":"right",s="next"==e?"first":"last",l=this;if(!o.length){if(!this.options.wrap)return;o=this.$element.find(".item")[s]()}if(o.hasClass("active"))return this.sliding=!1;var c=o[0],d=t.Event("slide.bs.carousel",{relatedTarget:c,direction:r});if(this.$element.trigger(d),!d.isDefaultPrevented()){if(this.sliding=!0,a&&this.pause(),this.$indicators.length){this.$indicators.find(".active").removeClass("active");var u=t(this.$indicators.children()[this.getItemIndex(o)]);u&&u.addClass("active")}var p=t.Event("slid.bs.carousel",{relatedTarget:c,direction:r});return t.support.transition&&this.$element.hasClass("slide")?(o.addClass(e),o[0].offsetWidth,n.addClass(r),o.addClass(r),n.one("bsTransitionEnd",function(){o.removeClass([e,r].join(" ")).addClass("active"),n.removeClass(["active",r].join(" ")),l.sliding=!1,setTimeout(function(){l.$element.trigger(p)},0)}).emulateTransitionEnd(1e3*n.css("transition-duration").slice(0,-1))):(n.removeClass("active"),o.addClass("active"),this.sliding=!1,this.$element.trigger(p)),a&&this.cycle(),this}};var n=t.fn.carousel;t.fn.carousel=e,t.fn.carousel.Constructor=i,t.fn.carousel.noConflict=function(){return t.fn.carousel=n,this},t(document).on("click.bs.carousel.data-api","[data-slide], [data-slide-to]",function(i){var n,o=t(this),a=t(o.attr("data-target")||(n=o.attr("href"))&&n.replace(/.*(?=#[^\s]+$)/,""));if(a.hasClass("carousel")){var r=t.extend({},a.data(),o.data()),s=o.attr("data-slide-to");s&&(r.interval=!1),e.call(a,r),s&&a.data("bs.carousel").to(s),i.preventDefault()}}),t(window).on("load",function(){t('[data-ride="carousel"]').each(function(){var i=t(this);e.call(i,i.data())})})}(jQuery),+function(t){"use strict";function e(e){return this.each(function(){var n=t(this),o=n.data("bs.collapse"),a=t.extend({},i.DEFAULTS,n.data(),"object"==typeof e&&e);!o&&a.toggle&&"show"==e&&(e=!e),o||n.data("bs.collapse",o=new i(this,a)),"string"==typeof e&&o[e]()})}var i=function(e,n){this.$element=t(e),this.options=t.extend({},i.DEFAULTS,n),this.transitioning=null,this.options.parent&&(this.$parent=t(this.options.parent)),this.options.toggle&&this.toggle()};i.VERSION="3.2.0",i.DEFAULTS={toggle:!0},i.prototype.dimension=function(){var t=this.$element.hasClass("width");return t?"width":"height"},i.prototype.show=function(){if(!this.transitioning&&!this.$element.hasClass("in")){var i=t.Event("show.bs.collapse");if(this.$element.trigger(i),!i.isDefaultPrevented()){var n=this.$parent&&this.$parent.find("> .panel > .in");if(n&&n.length){var o=n.data("bs.collapse");if(o&&o.transitioning)return;e.call(n,"hide"),o||n.data("bs.collapse",null)}var a=this.dimension();this.$element.removeClass("collapse").addClass("collapsing")[a](0),this.transitioning=1;var r=function(){this.$element.removeClass("collapsing").addClass("collapse in")[a](""),this.transitioning=0,this.$element.trigger("shown.bs.collapse")};if(!t.support.transition)return r.call(this);var s=t.camelCase(["scroll",a].join("-"));this.$element.one("bsTransitionEnd",t.proxy(r,this)).emulateTransitionEnd(350)[a](this.$element[0][s])}}},i.prototype.hide=function(){if(!this.transitioning&&this.$element.hasClass("in")){var e=t.Event("hide.bs.collapse");if(this.$element.trigger(e),!e.isDefaultPrevented()){var i=this.dimension();this.$element[i](this.$element[i]())[0].offsetHeight,this.$element.addClass("collapsing").removeClass("collapse").removeClass("in"),this.transitioning=1;var n=function(){this.transitioning=0,this.$element.trigger("hidden.bs.collapse").removeClass("collapsing").addClass("collapse")};return t.support.transition?(this.$element[i](0).one("bsTransitionEnd",t.proxy(n,this)).emulateTransitionEnd(350),void 0):n.call(this)}}},i.prototype.toggle=function(){this[this.$element.hasClass("in")?"hide":"show"]()};var n=t.fn.collapse;t.fn.collapse=e,t.fn.collapse.Constructor=i,t.fn.collapse.noConflict=function(){return t.fn.collapse=n,this},t(document).on("click.bs.collapse.data-api",'[data-toggle="collapse"]',function(i){var n,o=t(this),a=o.attr("data-target")||i.preventDefault()||(n=o.attr("href"))&&n.replace(/.*(?=#[^\s]+$)/,""),r=t(a),s=r.data("bs.collapse"),l=s?"toggle":o.data(),c=o.attr("data-parent"),d=c&&t(c);s&&s.transitioning||(d&&d.find('[data-toggle="collapse"][data-parent="'+c+'"]').not(o).addClass("collapsed"),o[r.hasClass("in")?"addClass":"removeClass"]("collapsed")),e.call(r,l)})}(jQuery),+function(t){"use strict";function e(e){e&&3===e.which||(t(o).remove(),t(a).each(function(){var n=i(t(this)),o={relatedTarget:this};n.hasClass("open")&&(n.trigger(e=t.Event("hide.bs.dropdown",o)),e.isDefaultPrevented()||n.removeClass("open").trigger("hidden.bs.dropdown",o))}))}function i(e){var i=e.attr("data-target");i||(i=e.attr("href"),i=i&&/#[A-Za-z]/.test(i)&&i.replace(/.*(?=#[^\s]*$)/,""));var n=i&&t(i);return n&&n.length?n:e.parent()}function n(e){return this.each(function(){var i=t(this),n=i.data("bs.dropdown");n||i.data("bs.dropdown",n=new r(this)),"string"==typeof e&&n[e].call(i)})}var o=".dropdown-backdrop",a='[data-toggle="dropdown"]',r=function(e){t(e).on("click.bs.dropdown",this.toggle)};r.VERSION="3.2.0",r.prototype.toggle=function(n){var o=t(this);if(!o.is(".disabled, :disabled")){var a=i(o),r=a.hasClass("open");if(e(),!r){"ontouchstart"in document.documentElement&&!a.closest(".navbar-nav").length&&t('<div class="dropdown-backdrop"/>').insertAfter(t(this)).on("click",e);var s={relatedTarget:this};if(a.trigger(n=t.Event("show.bs.dropdown",s)),n.isDefaultPrevented())return;o.trigger("focus"),a.toggleClass("open").trigger("shown.bs.dropdown",s)}return!1}},r.prototype.keydown=function(e){if(/(38|40|27)/.test(e.keyCode)){var n=t(this);if(e.preventDefault(),e.stopPropagation(),!n.is(".disabled, :disabled")){var o=i(n),r=o.hasClass("open");if(!r||r&&27==e.keyCode)return 27==e.which&&o.find(a).trigger("focus"),n.trigger("click");var s=" li:not(.divider):visible a",l=o.find('[role="menu"]'+s+', [role="listbox"]'+s);if(l.length){var c=l.index(l.filter(":focus"));38==e.keyCode&&c>0&&c--,40==e.keyCode&&c<l.length-1&&c++,~c||(c=0),l.eq(c).trigger("focus")}}}};var s=t.fn.dropdown;t.fn.dropdown=n,t.fn.dropdown.Constructor=r,t.fn.dropdown.noConflict=function(){return t.fn.dropdown=s,this},t(document).on("click.bs.dropdown.data-api",e).on("click.bs.dropdown.data-api",".dropdown form",function(t){t.stopPropagation()}).on("click.bs.dropdown.data-api",a,r.prototype.toggle).on("keydown.bs.dropdown.data-api",a+', [role="menu"], [role="listbox"]',r.prototype.keydown)}(jQuery),+function(t){"use strict";function e(e,n){return this.each(function(){var o=t(this),a=o.data("bs.modal"),r=t.extend({},i.DEFAULTS,o.data(),"object"==typeof e&&e);a||o.data("bs.modal",a=new i(this,r)),"string"==typeof e?a[e](n):r.show&&a.show(n)})}var i=function(e,i){this.options=i,this.$body=t(document.body),this.$element=t(e),this.$backdrop=this.isShown=null,this.scrollbarWidth=0,this.options.remote&&this.$element.find(".modal-content").load(this.options.remote,t.proxy(function(){this.$element.trigger("loaded.bs.modal")},this))};i.VERSION="3.2.0",i.DEFAULTS={backdrop:!0,keyboard:!0,show:!0},i.prototype.toggle=function(t){return this.isShown?this.hide():this.show(t)},i.prototype.show=function(e){var i=this,n=t.Event("show.bs.modal",{relatedTarget:e});this.$element.trigger(n),this.isShown||n.isDefaultPrevented()||(this.isShown=!0,this.checkScrollbar(),this.$body.addClass("modal-open"),this.setScrollbar(),this.escape(),this.$element.on("click.dismiss.bs.modal",'[data-dismiss="modal"]',t.proxy(this.hide,this)),this.backdrop(function(){var n=t.support.transition&&i.$element.hasClass("fade");i.$element.parent().length||i.$element.appendTo(i.$body),i.$element.show().scrollTop(0),n&&i.$element[0].offsetWidth,i.$element.addClass("in").attr("aria-hidden",!1),i.enforceFocus();var o=t.Event("shown.bs.modal",{relatedTarget:e});n?i.$element.find(".modal-dialog").one("bsTransitionEnd",function(){i.$element.trigger("focus").trigger(o)}).emulateTransitionEnd(300):i.$element.trigger("focus").trigger(o)}))},i.prototype.hide=function(e){e&&e.preventDefault(),e=t.Event("hide.bs.modal"),this.$element.trigger(e),this.isShown&&!e.isDefaultPrevented()&&(this.isShown=!1,this.$body.removeClass("modal-open"),this.resetScrollbar(),this.escape(),t(document).off("focusin.bs.modal"),this.$element.removeClass("in").attr("aria-hidden",!0).off("click.dismiss.bs.modal"),t.support.transition&&this.$element.hasClass("fade")?this.$element.one("bsTransitionEnd",t.proxy(this.hideModal,this)).emulateTransitionEnd(300):this.hideModal())},i.prototype.enforceFocus=function(){t(document).off("focusin.bs.modal").on("focusin.bs.modal",t.proxy(function(t){this.$element[0]===t.target||this.$element.has(t.target).length||this.$element.trigger("focus")},this))},i.prototype.escape=function(){this.isShown&&this.options.keyboard?this.$element.on("keyup.dismiss.bs.modal",t.proxy(function(t){27==t.which&&this.hide()},this)):this.isShown||this.$element.off("keyup.dismiss.bs.modal")},i.prototype.hideModal=function(){var t=this;this.$element.hide(),this.backdrop(function(){t.$element.trigger("hidden.bs.modal")})},i.prototype.removeBackdrop=function(){this.$backdrop&&this.$backdrop.remove(),this.$backdrop=null},i.prototype.backdrop=function(e){var i=this,n=this.$element.hasClass("fade")?"fade":"";if(this.isShown&&this.options.backdrop){var o=t.support.transition&&n;if(this.$backdrop=t('<div class="modal-backdrop '+n+'" />').appendTo(this.$body),this.$element.on("click.dismiss.bs.modal",t.proxy(function(t){t.target===t.currentTarget&&("static"==this.options.backdrop?this.$element[0].focus.call(this.$element[0]):this.hide.call(this))},this)),o&&this.$backdrop[0].offsetWidth,this.$backdrop.addClass("in"),!e)return;o?this.$backdrop.one("bsTransitionEnd",e).emulateTransitionEnd(150):e()}else if(!this.isShown&&this.$backdrop){this.$backdrop.removeClass("in");var a=function(){i.removeBackdrop(),e&&e()};t.support.transition&&this.$element.hasClass("fade")?this.$backdrop.one("bsTransitionEnd",a).emulateTransitionEnd(150):a()}else e&&e()},i.prototype.checkScrollbar=function(){document.body.clientWidth>=window.innerWidth||(this.scrollbarWidth=this.scrollbarWidth||this.measureScrollbar())},i.prototype.setScrollbar=function(){var t=parseInt(this.$body.css("padding-right")||0,10);this.scrollbarWidth&&this.$body.css("padding-right",t+this.scrollbarWidth)},i.prototype.resetScrollbar=function(){this.$body.css("padding-right","")},i.prototype.measureScrollbar=function(){var t=document.createElement("div");t.className="modal-scrollbar-measure",this.$body.append(t);var e=t.offsetWidth-t.clientWidth;return this.$body[0].removeChild(t),e};var n=t.fn.modal;t.fn.modal=e,t.fn.modal.Constructor=i,t.fn.modal.noConflict=function(){return t.fn.modal=n,this},t(document).on("click.bs.modal.data-api",'[data-toggle="modal"]',function(i){var n=t(this),o=n.attr("href"),a=t(n.attr("data-target")||o&&o.replace(/.*(?=#[^\s]+$)/,"")),r=a.data("bs.modal")?"toggle":t.extend({remote:!/#/.test(o)&&o},a.data(),n.data());n.is("a")&&i.preventDefault(),a.one("show.bs.modal",function(t){t.isDefaultPrevented()||a.one("hidden.bs.modal",function(){n.is(":visible")&&n.trigger("focus")})}),e.call(a,r,this)})}(jQuery),+function(t){"use strict";function e(){var t=document.createElement("bootstrap"),e={WebkitTransition:"webkitTransitionEnd",MozTransition:"transitionend",OTransition:"oTransitionEnd otransitionend",transition:"transitionend"};for(var i in e)if(void 0!==t.style[i])return{end:e[i]};return!1}t.fn.emulateTransitionEnd=function(e){var i=!1,n=this;t(this).one("bsTransitionEnd",function(){i=!0});var o=function(){i||t(n).trigger(t.support.transition.end)};return setTimeout(o,e),this},t(function(){t.support.transition=e(),t.support.transition&&(t.event.special.bsTransitionEnd={bindType:t.support.transition.end,delegateType:t.support.transition.end,handle:function(e){return t(e.target).is(this)?e.handleObj.handler.apply(this,arguments):void 0}})})}(jQuery),function(t){var e,i,n,o,a,r,s,l="Close",c="BeforeClose",d="AfterClose",u="BeforeAppend",p="MarkupParse",f="Open",h="Change",m="mfp",g="."+m,v="mfp-ready",b="mfp-removing",y="mfp-prevent-close",w=function(){},C=!!window.jQuery,k=t(window),x=function(t,i){e.ev.on(m+t+g,i)},I=function(e,i,n,o){var a=document.createElement("div");return a.className="mfp-"+e,n&&(a.innerHTML=n),o?i&&i.appendChild(a):(a=t(a),i&&a.appendTo(i)),a},T=function(i,n){e.ev.triggerHandler(m+i,n),e.st.callbacks&&(i=i.charAt(0).toLowerCase()+i.slice(1),e.st.callbacks[i]&&e.st.callbacks[i].apply(e,t.isArray(n)?n:[n]))},E=function(i){return i===s&&e.currTemplate.closeBtn||(e.currTemplate.closeBtn=t(e.st.closeMarkup.replace("%title%",e.st.tClose)),s=i),e.currTemplate.closeBtn},$=function(){t.magnificPopup.instance||(e=new w,e.init(),t.magnificPopup.instance=e)},S=function(){var t=document.createElement("p").style,e=["ms","O","Moz","Webkit"];if(void 0!==t.transition)return!0;for(;e.length;)if(e.pop()+"Transition"in t)return!0;return!1};w.prototype={constructor:w,init:function(){var i=navigator.appVersion;e.isIE7=-1!==i.indexOf("MSIE 7."),e.isIE8=-1!==i.indexOf("MSIE 8."),e.isLowIE=e.isIE7||e.isIE8,e.isAndroid=/android/gi.test(i),e.isIOS=/iphone|ipad|ipod/gi.test(i),e.supportsTransition=S(),e.probablyMobile=e.isAndroid||e.isIOS||/(Opera Mini)|Kindle|webOS|BlackBerry|(Opera Mobi)|(Windows Phone)|IEMobile/i.test(navigator.userAgent),o=t(document),e.popupsCache={}},open:function(i){n||(n=t(document.body));var a;if(i.isObj===!1){e.items=i.items.toArray(),e.index=0;var s,l=i.items;for(a=0;a<l.length;a++)if(s=l[a],s.parsed&&(s=s.el[0]),s===i.el[0]){e.index=a;break}}else e.items=t.isArray(i.items)?i.items:[i.items],e.index=i.index||0;if(e.isOpen)return e.updateItemHTML(),void 0;e.types=[],r="",e.ev=i.mainEl&&i.mainEl.length?i.mainEl.eq(0):o,i.key?(e.popupsCache[i.key]||(e.popupsCache[i.key]={}),e.currTemplate=e.popupsCache[i.key]):e.currTemplate={},e.st=t.extend(!0,{},t.magnificPopup.defaults,i),e.fixedContentPos="auto"===e.st.fixedContentPos?!e.probablyMobile:e.st.fixedContentPos,e.st.modal&&(e.st.closeOnContentClick=!1,e.st.closeOnBgClick=!1,e.st.showCloseBtn=!1,e.st.enableEscapeKey=!1),e.bgOverlay||(e.bgOverlay=I("bg").on("click"+g,function(){e.close()}),e.wrap=I("wrap").attr("tabindex",-1).on("click"+g,function(t){e._checkIfClose(t.target)&&e.close()}),e.container=I("container",e.wrap)),e.contentContainer=I("content"),e.st.preloader&&(e.preloader=I("preloader",e.container,e.st.tLoading));var c=t.magnificPopup.modules;for(a=0;a<c.length;a++){var d=c[a];d=d.charAt(0).toUpperCase()+d.slice(1),e["init"+d].call(e)}T("BeforeOpen"),e.st.showCloseBtn&&(e.st.closeBtnInside?(x(p,function(t,e,i,n){i.close_replaceWith=E(n.type)}),r+=" mfp-close-btn-in"):e.wrap.append(E())),e.st.alignTop&&(r+=" mfp-align-top"),e.fixedContentPos?e.wrap.css({overflow:e.st.overflowY,overflowX:"hidden",overflowY:e.st.overflowY}):e.wrap.css({top:k.scrollTop(),position:"absolute"}),(e.st.fixedBgPos===!1||"auto"===e.st.fixedBgPos&&!e.fixedContentPos)&&e.bgOverlay.css({height:o.height(),position:"absolute"}),e.st.enableEscapeKey&&o.on("keyup"+g,function(t){27===t.keyCode&&e.close()}),k.on("resize"+g,function(){e.updateSize()}),e.st.closeOnContentClick||(r+=" mfp-auto-cursor"),r&&e.wrap.addClass(r);var u=e.wH=k.height(),h={};if(e.fixedContentPos&&e._hasScrollBar(u)){var m=e._getScrollbarSize();m&&(h.marginRight=m)}e.fixedContentPos&&(e.isIE7?t("body, html").css("overflow","hidden"):h.overflow="hidden");var b=e.st.mainClass;return e.isIE7&&(b+=" mfp-ie7"),b&&e._addClassToMFP(b),e.updateItemHTML(),T("BuildControls"),t("html").css(h),e.bgOverlay.add(e.wrap).prependTo(e.st.prependTo||n),e._lastFocusedEl=document.activeElement,setTimeout(function(){e.content?(e._addClassToMFP(v),e._setFocus()):e.bgOverlay.addClass(v),o.on("focusin"+g,e._onFocusIn)},16),e.isOpen=!0,e.updateSize(u),T(f),i},close:function(){e.isOpen&&(T(c),e.isOpen=!1,e.st.removalDelay&&!e.isLowIE&&e.supportsTransition?(e._addClassToMFP(b),setTimeout(function(){e._close()},e.st.removalDelay)):e._close())},_close:function(){T(l);var i=b+" "+v+" ";if(e.bgOverlay.detach(),e.wrap.detach(),e.container.empty(),e.st.mainClass&&(i+=e.st.mainClass+" "),e._removeClassFromMFP(i),e.fixedContentPos){var n={marginRight:""};e.isIE7?t("body, html").css("overflow",""):n.overflow="",t("html").css(n)}o.off("keyup"+g+" focusin"+g),e.ev.off(g),e.wrap.attr("class","mfp-wrap").removeAttr("style"),e.bgOverlay.attr("class","mfp-bg"),e.container.attr("class","mfp-container"),!e.st.showCloseBtn||e.st.closeBtnInside&&e.currTemplate[e.currItem.type]!==!0||e.currTemplate.closeBtn&&e.currTemplate.closeBtn.detach(),e._lastFocusedEl&&t(e._lastFocusedEl).focus(),e.currItem=null,e.content=null,e.currTemplate=null,e.prevHeight=0,T(d)},updateSize:function(t){if(e.isIOS){var i=document.documentElement.clientWidth/window.innerWidth,n=window.innerHeight*i;e.wrap.css("height",n),e.wH=n}else e.wH=t||k.height();e.fixedContentPos||e.wrap.css("height",e.wH),T("Resize")},updateItemHTML:function(){var i=e.items[e.index];e.contentContainer.detach(),e.content&&e.content.detach(),i.parsed||(i=e.parseEl(e.index));var n=i.type;if(T("BeforeChange",[e.currItem?e.currItem.type:"",n]),e.currItem=i,!e.currTemplate[n]){var o=e.st[n]?e.st[n].markup:!1;T("FirstMarkupParse",o),e.currTemplate[n]=o?t(o):!0}a&&a!==i.type&&e.container.removeClass("mfp-"+a+"-holder");var r=e["get"+n.charAt(0).toUpperCase()+n.slice(1)](i,e.currTemplate[n]);e.appendContent(r,n),i.preloaded=!0,T(h,i),a=i.type,e.container.prepend(e.contentContainer),T("AfterChange")},appendContent:function(t,i){e.content=t,t?e.st.showCloseBtn&&e.st.closeBtnInside&&e.currTemplate[i]===!0?e.content.find(".mfp-close").length||e.content.append(E()):e.content=t:e.content="",T(u),e.container.addClass("mfp-"+i+"-holder"),e.contentContainer.append(e.content)},parseEl:function(i){var n,o=e.items[i];if(o.tagName?o={el:t(o)}:(n=o.type,o={data:o,src:o.src}),o.el){for(var a=e.types,r=0;r<a.length;r++)if(o.el.hasClass("mfp-"+a[r])){n=a[r];break}o.src=o.el.attr("data-mfp-src"),o.src||(o.src=o.el.attr("href"))}return o.type=n||e.st.type||"inline",o.index=i,o.parsed=!0,e.items[i]=o,T("ElementParse",o),e.items[i]},addGroup:function(t,i){var n=function(n){n.mfpEl=this,e._openClick(n,t,i)};i||(i={});var o="click.magnificPopup";i.mainEl=t,i.items?(i.isObj=!0,t.off(o).on(o,n)):(i.isObj=!1,i.delegate?t.off(o).on(o,i.delegate,n):(i.items=t,t.off(o).on(o,n)))},_openClick:function(i,n,o){var a=void 0!==o.midClick?o.midClick:t.magnificPopup.defaults.midClick;if(a||2!==i.which&&!i.ctrlKey&&!i.metaKey){var r=void 0!==o.disableOn?o.disableOn:t.magnificPopup.defaults.disableOn;if(r)if(t.isFunction(r)){if(!r.call(e))return!0}else if(k.width()<r)return!0;i.type&&(i.preventDefault(),e.isOpen&&i.stopPropagation()),o.el=t(i.mfpEl),o.delegate&&(o.items=n.find(o.delegate)),e.open(o)}},updateStatus:function(t,n){if(e.preloader){i!==t&&e.container.removeClass("mfp-s-"+i),n||"loading"!==t||(n=e.st.tLoading);var o={status:t,text:n};T("UpdateStatus",o),t=o.status,n=o.text,e.preloader.html(n),e.preloader.find("a").on("click",function(t){t.stopImmediatePropagation()}),e.container.addClass("mfp-s-"+t),i=t}},_checkIfClose:function(i){if(!t(i).hasClass(y)){var n=e.st.closeOnContentClick,o=e.st.closeOnBgClick;if(n&&o)return!0;if(!e.content||t(i).hasClass("mfp-close")||e.preloader&&i===e.preloader[0])return!0;if(i===e.content[0]||t.contains(e.content[0],i)){if(n)return!0}else if(o&&t.contains(document,i))return!0;return!1}},_addClassToMFP:function(t){e.bgOverlay.addClass(t),e.wrap.addClass(t)},_removeClassFromMFP:function(t){this.bgOverlay.removeClass(t),e.wrap.removeClass(t)},_hasScrollBar:function(t){return(e.isIE7?o.height():document.body.scrollHeight)>(t||k.height())},_setFocus:function(){(e.st.focus?e.content.find(e.st.focus).eq(0):e.wrap).focus()},_onFocusIn:function(i){return i.target===e.wrap[0]||t.contains(e.wrap[0],i.target)?void 0:(e._setFocus(),!1)},_parseMarkup:function(e,i,n){var o;n.data&&(i=t.extend(n.data,i)),T(p,[e,i,n]),t.each(i,function(t,i){if(void 0===i||i===!1)return!0;if(o=t.split("_"),o.length>1){var n=e.find(g+"-"+o[0]);if(n.length>0){var a=o[1];"replaceWith"===a?n[0]!==i[0]&&n.replaceWith(i):"img"===a?n.is("img")?n.attr("src",i):n.replaceWith('<img src="'+i+'" class="'+n.attr("class")+'" />'):n.attr(o[1],i)}}else e.find(g+"-"+t).html(i)})},_getScrollbarSize:function(){if(void 0===e.scrollbarSize){var t=document.createElement("div");t.style.cssText="width: 99px; height: 99px; overflow: scroll; position: absolute; top: -9999px;",document.body.appendChild(t),e.scrollbarSize=t.offsetWidth-t.clientWidth,document.body.removeChild(t)}return e.scrollbarSize}},t.magnificPopup={instance:null,proto:w.prototype,modules:[],open:function(e,i){return $(),e=e?t.extend(!0,{},e):{},e.isObj=!0,e.index=i||0,this.instance.open(e)},close:function(){return t.magnificPopup.instance&&t.magnificPopup.instance.close()},registerModule:function(e,i){i.options&&(t.magnificPopup.defaults[e]=i.options),t.extend(this.proto,i.proto),this.modules.push(e)},defaults:{disableOn:0,key:null,midClick:!1,mainClass:"",preloader:!0,focus:"",closeOnContentClick:!1,closeOnBgClick:!0,closeBtnInside:!0,showCloseBtn:!0,enableEscapeKey:!0,modal:!1,alignTop:!1,removalDelay:0,prependTo:null,fixedContentPos:"auto",fixedBgPos:"auto",overflowY:"auto",closeMarkup:'<button title="%title%" type="button" class="mfp-close">&times;</button>',tClose:"Close (Esc)",tLoading:"Loading..."}},t.fn.magnificPopup=function(i){$();var n=t(this);if("string"==typeof i)if("open"===i){var o,a=C?n.data("magnificPopup"):n[0].magnificPopup,r=parseInt(arguments[1],10)||0;a.items?o=a.items[r]:(o=n,a.delegate&&(o=o.find(a.delegate)),o=o.eq(r)),e._openClick({mfpEl:o},n,a)}else e.isOpen&&e[i].apply(e,Array.prototype.slice.call(arguments,1));else i=t.extend(!0,{},i),C?n.data("magnificPopup",i):n[0].magnificPopup=i,e.addGroup(n,i);return n};var A,_,P,O="inline",z=function(){P&&(_.after(P.addClass(A)).detach(),P=null)};t.magnificPopup.registerModule(O,{options:{hiddenClass:"hide",markup:"",tNotFound:"Content not found"},proto:{initInline:function(){e.types.push(O),x(l+"."+O,function(){z()})},getInline:function(i,n){if(z(),i.src){var o=e.st.inline,a=t(i.src);if(a.length){var r=a[0].parentNode;r&&r.tagName&&(_||(A=o.hiddenClass,_=I(A),A="mfp-"+A),P=a.after(_).detach().removeClass(A)),e.updateStatus("ready")}else e.updateStatus("error",o.tNotFound),a=t("<div>");return i.inlineElement=a,a}return e.updateStatus("ready"),e._parseMarkup(n,{},i),n}}});var M,B="ajax",F=function(){M&&n.removeClass(M)},L=function(){F(),e.req&&e.req.abort()};t.magnificPopup.registerModule(B,{options:{settings:null,cursor:"mfp-ajax-cur",tError:'<a href="%url%">The content</a> could not be loaded.'},proto:{initAjax:function(){e.types.push(B),M=e.st.ajax.cursor,x(l+"."+B,L),x("BeforeChange."+B,L)},getAjax:function(i){M&&n.addClass(M),e.updateStatus("loading");var o=t.extend({url:i.src,success:function(n,o,a){var r={data:n,xhr:a};T("ParseAjax",r),e.appendContent(t(r.data),B),i.finished=!0,F(),e._setFocus(),setTimeout(function(){e.wrap.addClass(v)},16),e.updateStatus("ready"),T("AjaxContentAdded")},error:function(){F(),i.finished=i.loadError=!0,e.updateStatus("error",e.st.ajax.tError.replace("%url%",i.src))}},e.st.ajax.settings);return e.req=t.ajax(o),""}}});var j,H=function(i){if(i.data&&void 0!==i.data.title)return i.data.title;var n=e.st.image.titleSrc;if(n){if(t.isFunction(n))return n.call(e,i);if(i.el)return i.el.attr(n)||""}return""};t.magnificPopup.registerModule("image",{options:{markup:'<div class="mfp-figure"><div class="mfp-close"></div><figure><div class="mfp-img"></div><figcaption><div class="mfp-bottom-bar"><div class="mfp-title"></div><div class="mfp-counter"></div></div></figcaption></figure></div>',cursor:"mfp-zoom-out-cur",titleSrc:"title",verticalFit:!0,tError:'<a href="%url%">The image</a> could not be loaded.'},proto:{initImage:function(){var t=e.st.image,i=".image";e.types.push("image"),x(f+i,function(){"image"===e.currItem.type&&t.cursor&&n.addClass(t.cursor)}),x(l+i,function(){t.cursor&&n.removeClass(t.cursor),k.off("resize"+g)}),x("Resize"+i,e.resizeImage),e.isLowIE&&x("AfterChange",e.resizeImage)},resizeImage:function(){var t=e.currItem;if(t&&t.img&&e.st.image.verticalFit){var i=0;e.isLowIE&&(i=parseInt(t.img.css("padding-top"),10)+parseInt(t.img.css("padding-bottom"),10)),t.img.css("max-height",e.wH-i)}},_onImageHasSize:function(t){t.img&&(t.hasSize=!0,j&&clearInterval(j),t.isCheckingImgSize=!1,T("ImageHasSize",t),t.imgHidden&&(e.content&&e.content.removeClass("mfp-loading"),t.imgHidden=!1))},findImageSize:function(t){var i=0,n=t.img[0],o=function(a){j&&clearInterval(j),j=setInterval(function(){return n.naturalWidth>0?(e._onImageHasSize(t),void 0):(i>200&&clearInterval(j),i++,3===i?o(10):40===i?o(50):100===i&&o(500),void 0)},a)};o(1)},getImage:function(i,n){var o=0,a=function(){i&&(i.img[0].complete?(i.img.off(".mfploader"),i===e.currItem&&(e._onImageHasSize(i),e.updateStatus("ready")),i.hasSize=!0,i.loaded=!0,T("ImageLoadComplete")):(o++,200>o?setTimeout(a,100):r()))},r=function(){i&&(i.img.off(".mfploader"),i===e.currItem&&(e._onImageHasSize(i),e.updateStatus("error",s.tError.replace("%url%",i.src))),i.hasSize=!0,i.loaded=!0,i.loadError=!0)},s=e.st.image,l=n.find(".mfp-img");if(l.length){var c=document.createElement("img");c.className="mfp-img",i.img=t(c).on("load.mfploader",a).on("error.mfploader",r),c.src=i.src,l.is("img")&&(i.img=i.img.clone()),c=i.img[0],c.naturalWidth>0?i.hasSize=!0:c.width||(i.hasSize=!1)}return e._parseMarkup(n,{title:H(i),img_replaceWith:i.img},i),e.resizeImage(),i.hasSize?(j&&clearInterval(j),i.loadError?(n.addClass("mfp-loading"),e.updateStatus("error",s.tError.replace("%url%",i.src))):(n.removeClass("mfp-loading"),e.updateStatus("ready")),n):(e.updateStatus("loading"),i.loading=!0,i.hasSize||(i.imgHidden=!0,n.addClass("mfp-loading"),e.findImageSize(i)),n)}}});var D,W=function(){return void 0===D&&(D=void 0!==document.createElement("p").style.MozTransform),D};t.magnificPopup.registerModule("zoom",{options:{enabled:!1,easing:"ease-in-out",duration:300,opener:function(t){return t.is("img")?t:t.find("img")}},proto:{initZoom:function(){var t,i=e.st.zoom,n=".zoom";if(i.enabled&&e.supportsTransition){var o,a,r=i.duration,s=function(t){var e=t.clone().removeAttr("style").removeAttr("class").addClass("mfp-animated-image"),n="all "+i.duration/1e3+"s "+i.easing,o={position:"fixed",zIndex:9999,left:0,top:0,"-webkit-backface-visibility":"hidden"},a="transition";return o["-webkit-"+a]=o["-moz-"+a]=o["-o-"+a]=o[a]=n,e.css(o),e},d=function(){e.content.css("visibility","visible")};x("BuildControls"+n,function(){if(e._allowZoom()){if(clearTimeout(o),e.content.css("visibility","hidden"),t=e._getItemToZoom(),!t)return d(),void 0;a=s(t),a.css(e._getOffset()),e.wrap.append(a),o=setTimeout(function(){a.css(e._getOffset(!0)),o=setTimeout(function(){d(),setTimeout(function(){a.remove(),t=a=null,T("ZoomAnimationEnded")},16)},r)},16)}}),x(c+n,function(){if(e._allowZoom()){if(clearTimeout(o),e.st.removalDelay=r,!t){if(t=e._getItemToZoom(),!t)return;a=s(t)}a.css(e._getOffset(!0)),e.wrap.append(a),e.content.css("visibility","hidden"),setTimeout(function(){a.css(e._getOffset())},16)}}),x(l+n,function(){e._allowZoom()&&(d(),a&&a.remove(),t=null)})}},_allowZoom:function(){return"image"===e.currItem.type},_getItemToZoom:function(){return e.currItem.hasSize?e.currItem.img:!1},_getOffset:function(i){var n;n=i?e.currItem.img:e.st.zoom.opener(e.currItem.el||e.currItem);var o=n.offset(),a=parseInt(n.css("padding-top"),10),r=parseInt(n.css("padding-bottom"),10);o.top-=t(window).scrollTop()-a;var s={width:n.width(),height:(C?n.innerHeight():n[0].offsetHeight)-r-a};return W()?s["-moz-transform"]=s.transform="translate("+o.left+"px,"+o.top+"px)":(s.left=o.left,s.top=o.top),s}}});var N="iframe",R="//about:blank",U=function(t){if(e.currTemplate[N]){var i=e.currTemplate[N].find("iframe");i.length&&(t||(i[0].src=R),e.isIE8&&i.css("display",t?"block":"none"))}};t.magnificPopup.registerModule(N,{options:{markup:'<div class="mfp-iframe-scaler"><div class="mfp-close"></div><iframe class="mfp-iframe" src="//about:blank" frameborder="0" allowfullscreen></iframe></div>',srcAction:"iframe_src",patterns:{youtube:{index:"youtube.com",id:"v=",src:"//www.youtube.com/embed/%id%?autoplay=1"},vimeo:{index:"vimeo.com/",id:"/",src:"//player.vimeo.com/video/%id%?autoplay=1"},gmaps:{index:"//maps.google.",src:"%id%&output=embed"}}},proto:{initIframe:function(){e.types.push(N),x("BeforeChange",function(t,e,i){e!==i&&(e===N?U():i===N&&U(!0))}),x(l+"."+N,function(){U()})},getIframe:function(i,n){var o=i.src,a=e.st.iframe;t.each(a.patterns,function(){return o.indexOf(this.index)>-1?(this.id&&(o="string"==typeof this.id?o.substr(o.lastIndexOf(this.id)+this.id.length,o.length):this.id.call(this,o)),o=this.src.replace("%id%",o),!1):void 0});var r={};return a.srcAction&&(r[a.srcAction]=o),e._parseMarkup(n,r,i),e.updateStatus("ready"),n}}});var Q=function(t){var i=e.items.length;return t>i-1?t-i:0>t?i+t:t},Z=function(t,e,i){return t.replace(/%curr%/gi,e+1).replace(/%total%/gi,i)};t.magnificPopup.registerModule("gallery",{options:{enabled:!1,arrowMarkup:'<button title="%title%" type="button" class="mfp-arrow mfp-arrow-%dir%"></button>',preload:[0,2],navigateByImgClick:!0,arrows:!0,tPrev:"Previous (Left arrow key)",tNext:"Next (Right arrow key)",tCounter:"%curr% of %total%"},proto:{initGallery:function(){var i=e.st.gallery,n=".mfp-gallery",a=Boolean(t.fn.mfpFastClick);return e.direction=!0,i&&i.enabled?(r+=" mfp-gallery",x(f+n,function(){i.navigateByImgClick&&e.wrap.on("click"+n,".mfp-img",function(){return e.items.length>1?(e.next(),!1):void 0}),o.on("keydown"+n,function(t){37===t.keyCode?e.prev():39===t.keyCode&&e.next()})}),x("UpdateStatus"+n,function(t,i){i.text&&(i.text=Z(i.text,e.currItem.index,e.items.length))}),x(p+n,function(t,n,o,a){var r=e.items.length;o.counter=r>1?Z(i.tCounter,a.index,r):""}),x("BuildControls"+n,function(){if(e.items.length>1&&i.arrows&&!e.arrowLeft){var n=i.arrowMarkup,o=e.arrowLeft=t(n.replace(/%title%/gi,i.tPrev).replace(/%dir%/gi,"left")).addClass(y),r=e.arrowRight=t(n.replace(/%title%/gi,i.tNext).replace(/%dir%/gi,"right")).addClass(y),s=a?"mfpFastClick":"click";
o[s](function(){e.prev()}),r[s](function(){e.next()}),e.isIE7&&(I("b",o[0],!1,!0),I("a",o[0],!1,!0),I("b",r[0],!1,!0),I("a",r[0],!1,!0)),e.container.append(o.add(r))}}),x(h+n,function(){e._preloadTimeout&&clearTimeout(e._preloadTimeout),e._preloadTimeout=setTimeout(function(){e.preloadNearbyImages(),e._preloadTimeout=null},16)}),x(l+n,function(){o.off(n),e.wrap.off("click"+n),e.arrowLeft&&a&&e.arrowLeft.add(e.arrowRight).destroyMfpFastClick(),e.arrowRight=e.arrowLeft=null}),void 0):!1},next:function(){e.direction=!0,e.index=Q(e.index+1),e.updateItemHTML()},prev:function(){e.direction=!1,e.index=Q(e.index-1),e.updateItemHTML()},goTo:function(t){e.direction=t>=e.index,e.index=t,e.updateItemHTML()},preloadNearbyImages:function(){var t,i=e.st.gallery.preload,n=Math.min(i[0],e.items.length),o=Math.min(i[1],e.items.length);for(t=1;t<=(e.direction?o:n);t++)e._preloadItem(e.index+t);for(t=1;t<=(e.direction?n:o);t++)e._preloadItem(e.index-t)},_preloadItem:function(i){if(i=Q(i),!e.items[i].preloaded){var n=e.items[i];n.parsed||(n=e.parseEl(i)),T("LazyLoad",n),"image"===n.type&&(n.img=t('<img class="mfp-img" />').on("load.mfploader",function(){n.hasSize=!0}).on("error.mfploader",function(){n.hasSize=!0,n.loadError=!0,T("LazyLoadError",n)}).attr("src",n.src)),n.preloaded=!0}}}});var Y="retina";t.magnificPopup.registerModule(Y,{options:{replaceSrc:function(t){return t.src.replace(/\.\w+$/,function(t){return"@2x"+t})},ratio:1},proto:{initRetina:function(){if(window.devicePixelRatio>1){var t=e.st.retina,i=t.ratio;i=isNaN(i)?i():i,i>1&&(x("ImageHasSize."+Y,function(t,e){e.img.css({"max-width":e.img[0].naturalWidth/i,width:"100%"})}),x("ElementParse."+Y,function(e,n){n.src=t.replaceSrc(n,i)}))}}}}),function(){var e=1e3,i="ontouchstart"in window,n=function(){k.off("touchmove"+a+" touchend"+a)},o="mfpFastClick",a="."+o;t.fn.mfpFastClick=function(o){return t(this).each(function(){var r,s=t(this);if(i){var l,c,d,u,p,f;s.on("touchstart"+a,function(t){u=!1,f=1,p=t.originalEvent?t.originalEvent.touches[0]:t.touches[0],c=p.clientX,d=p.clientY,k.on("touchmove"+a,function(t){p=t.originalEvent?t.originalEvent.touches:t.touches,f=p.length,p=p[0],(Math.abs(p.clientX-c)>10||Math.abs(p.clientY-d)>10)&&(u=!0,n())}).on("touchend"+a,function(t){n(),u||f>1||(r=!0,t.preventDefault(),clearTimeout(l),l=setTimeout(function(){r=!1},e),o())})})}s.on("click"+a,function(){r||o()})})},t.fn.destroyMfpFastClick=function(){t(this).off("touchstart"+a+" click"+a),i&&k.off("touchmove"+a+" touchend"+a)}}(),$()}(window.jQuery||window.Zepto),function(t){t.fn.simpleCarousel=function(e){var i={};return e=t.extend(i,e),this.each(function(){function i(){var t=s.next("li");return t.length?t:r.first()}function n(){var t=s.prev("li");return t.length?t:r.last()}var o=t(this),a=o.find("ul"),r=a.find("li"),s=r.filter(".active"),l=e.itemWidth||s.outerWidth(),c=l*r.length,d=(o.width(),t(e.prev)),u=t(e.next);a.width(c),u.on("click",function(){s.removeClass("active"),(s=i()).addClass("active"),e.callback(s)}),d.on("click",function(){s.removeClass("active"),(s=n()).addClass("active"),e.callback(s)}),a.on("click","li",function(){var i=t(this);i.hasClass("active")||(s.removeClass("active"),(s=i).addClass("active"),e.callback(s))})})}}(jQuery),function(t){t.args=function(t){var e=location.search.length>0?location.search.substring(1):"",i={},n=e.length?e.split("&"):[],o=null,a=null,r=null,s=0,l=n.length;for(s=0;l>s;s++)o=n[s].split("="),a=decodeURIComponent(o[0]),r=decodeURIComponent(o[1]),a.length&&(i[a]=r);return i[t]||i}}(jQuery),function(t,e,i,n){var o=t(e);t.fn.lazyload=function(a){function r(){var e=0;l.each(function(){var i=t(this);if(!c.skip_invisible||i.is(":visible"))if(t.abovethetop(this,c)||t.leftofbegin(this,c));else if(t.belowthefold(this,c)||t.rightoffold(this,c)){if(++e>c.failure_limit)return!1}else i.trigger("appear"),e=0})}var s,l=this,c={threshold:0,failure_limit:0,event:"scroll",effect:"show",container:e,data_attribute:"original",skip_invisible:!0,appear:null,load:null,placeholder:"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsQAAA7EAZUrDhsAAAANSURBVBhXYzh8+PB/AAffA0nNPuCLAAAAAElFTkSuQmCC"};return a&&(n!==a.failurelimit&&(a.failure_limit=a.failurelimit,delete a.failurelimit),n!==a.effectspeed&&(a.effect_speed=a.effectspeed,delete a.effectspeed),t.extend(c,a)),s=c.container===n||c.container===e?o:t(c.container),0===c.event.indexOf("scroll")&&s.bind(c.event,function(){return r()}),this.each(function(){var e=this,i=t(e);e.loaded=!1,(i.attr("src")===n||i.attr("src")===!1)&&i.is("img")&&i.attr("src",c.placeholder),i.one("appear",function(){if(!this.loaded){if(c.appear){var n=l.length;c.appear.call(e,n,c)}t("<img />").bind("load",function(){var n=i.attr("data-"+c.data_attribute);i.hide(),i.is("img")?i.attr("src",n):i.css("background-image","url('"+n+"')"),i[c.effect](c.effect_speed),e.loaded=!0;var o=t.grep(l,function(t){return!t.loaded});if(l=t(o),c.load){var a=l.length;c.load.call(e,a,c)}}).attr("src",i.attr("data-"+c.data_attribute))}}),0!==c.event.indexOf("scroll")&&i.bind(c.event,function(){e.loaded||i.trigger("appear")})}),o.bind("resize",function(){r()}),/(?:iphone|ipod|ipad).*os 5/gi.test(navigator.appVersion)&&o.bind("pageshow",function(e){e.originalEvent&&e.originalEvent.persisted&&l.each(function(){t(this).trigger("appear")})}),t(i).ready(function(){r()}),this},t.belowthefold=function(i,a){var r;return r=a.container===n||a.container===e?(e.innerHeight?e.innerHeight:o.height())+o.scrollTop():t(a.container).offset().top+t(a.container).height(),r<=t(i).offset().top-a.threshold},t.rightoffold=function(i,a){var r;return r=a.container===n||a.container===e?o.width()+o.scrollLeft():t(a.container).offset().left+t(a.container).width(),r<=t(i).offset().left-a.threshold},t.abovethetop=function(i,a){var r;return r=a.container===n||a.container===e?o.scrollTop():t(a.container).offset().top,r>=t(i).offset().top+a.threshold+t(i).height()},t.leftofbegin=function(i,a){var r;return r=a.container===n||a.container===e?o.scrollLeft():t(a.container).offset().left,r>=t(i).offset().left+a.threshold+t(i).width()},t.inviewport=function(e,i){return!(t.rightoffold(e,i)||t.leftofbegin(e,i)||t.belowthefold(e,i)||t.abovethetop(e,i))},t.extend(t.expr[":"],{"below-the-fold":function(e){return t.belowthefold(e,{threshold:0})},"above-the-top":function(e){return!t.belowthefold(e,{threshold:0})},"right-of-screen":function(e){return t.rightoffold(e,{threshold:0})},"left-of-screen":function(e){return!t.rightoffold(e,{threshold:0})},"in-viewport":function(e){return t.inviewport(e,{threshold:0})},"above-the-fold":function(e){return!t.belowthefold(e,{threshold:0})},"right-of-fold":function(e){return t.rightoffold(e,{threshold:0})},"left-of-fold":function(e){return!t.rightoffold(e,{threshold:0})}})}(jQuery,window,document),$(function(){$(".lazy").lazyload()}),function(){"use strict";if(navigator.userAgent.match(/IEMobile\/10\.0/)){var t=document.createElement("style");t.appendChild(document.createTextNode("@-ms-viewport{width:auto!important}")),document.querySelector("head").appendChild(t)}}();