!function(e){function t(){return e("<div/>")}var o=Math.abs,i=Math.max,n=Math.min,s=Math.round;e.imgAreaSelect=function(r,d){function a(e){return e+bt.left-yt.left}function c(e){return e+bt.top-yt.top}function l(e){return e-bt.left+yt.left}function u(e){return e-bt.top+yt.top}function h(e){return e.pageX-yt.left}function f(e){return e.pageY-yt.top}function m(e){var t=e||Q,o=e||X;return{x1:s(wt.x1*t),y1:s(wt.y1*o),x2:s(wt.x2*t),y2:s(wt.y2*o),width:s(wt.x2*t)-s(wt.x1*t),height:s(wt.y2*o)-s(wt.y1*o)}}function p(e,t,o,i,n){var r=n||Q,d=n||X;wt={x1:s(e/r||0),y1:s(t/d||0),x2:s(o/r||0),y2:s(i/d||0)},wt.width=wt.x2-wt.x1,wt.height=wt.y2-wt.y1}function b(){lt.width()&&(bt={left:s(lt.offset().left),top:s(lt.offset().top)},D=lt.innerWidth(),R=lt.innerHeight(),bt.top+=lt.outerHeight()-R>>1,bt.left+=lt.outerWidth()-D>>1,F=s(d.minWidth/Q)||0,G=s(d.minHeight/X)||0,J=s(n(d.maxWidth/Q||1<<24,D)),U=s(n(d.maxHeight/X||1<<24,R)),"1.3.2"!=e().jquery||"fixed"!=xt||vt.getBoundingClientRect||(bt.top+=i(document.body.scrollTop,vt.scrollTop),bt.left+=i(document.body.scrollLeft,vt.scrollLeft)),yt=/absolute|relative/.test($.css("position"))?{left:s($.offset().left)-$.scrollLeft(),top:s($.offset().top)-$.scrollTop()}:"fixed"==xt?{left:e(document).scrollLeft(),top:e(document).scrollTop()}:{left:0,top:0},L=a(0),j=c(0),(wt.x2>D||wt.y2>R)&&k())}function y(t){if(Z){switch(ut.css({left:a(wt.x1),top:c(wt.y1)}).add(ht).width(dt=wt.width).height(at=wt.height),ht.add(ft).add(pt).css({left:0,top:0}),ft.width(i(dt-ft.outerWidth()+ft.innerWidth(),0)).height(i(at-ft.outerHeight()+ft.innerHeight(),0)),e(mt[0]).css({left:L,top:j,width:wt.x1,height:R}),e(mt[1]).css({left:L+wt.x1,top:j,width:dt,height:wt.y1}),e(mt[2]).css({left:L+wt.x2,top:j,width:D-wt.x2,height:R}),e(mt[3]).css({left:L+wt.x1,top:j+wt.y2,width:dt,height:R-wt.y2}),dt-=pt.outerWidth(),at-=pt.outerHeight(),pt.length){case 8:e(pt[4]).css({left:dt>>1}),e(pt[5]).css({left:dt,top:at>>1}),e(pt[6]).css({left:dt>>1,top:at}),e(pt[7]).css({top:at>>1});case 4:pt.slice(1,3).css({left:dt}),pt.slice(2,4).css({top:at})}t!==!1&&(e.imgAreaSelect.keyPress!=St&&e(document).unbind(e.imgAreaSelect.keyPress,e.imgAreaSelect.onKeyPress),d.keys&&e(document)[e.imgAreaSelect.keyPress](e.imgAreaSelect.onKeyPress=St)),e.browser.msie&&ft.outerWidth()-ft.innerWidth()==2&&(ft.css("margin",0),setTimeout(function(){ft.css("margin","auto")},0))}}function g(e){b(),y(e),_=a(wt.x1),et=c(wt.y1),tt=a(wt.x2),ot=c(wt.y2)}function x(e,t){d.fadeSpeed?e.fadeOut(d.fadeSpeed,t):e.hide()}function w(e){var t=l(h(e))-wt.x1,o=u(f(e))-wt.y1;ct||(b(),ct=!0,ut.one("mouseout",function(){ct=!1})),Y="",d.resizable&&(o<=d.resizeMargin?Y="n":o>=wt.height-d.resizeMargin&&(Y="s"),t<=d.resizeMargin?Y+="w":t>=wt.width-d.resizeMargin&&(Y+="e")),ut.css("cursor",Y?Y+"-resize":d.movable?"move":""),T&&T.toggle()}function v(){e("body").css("cursor",""),(d.autoHide||wt.width*wt.height==0)&&x(ut.add(mt),function(){e(this).hide()}),e(document).unbind("mousemove",C),ut.mousemove(w),d.onSelectEnd(r,m())}function S(t){return 1!=t.which?!1:(b(),Y?(e("body").css("cursor",Y+"-resize"),_=a(wt[/w/.test(Y)?"x2":"x1"]),et=c(wt[/n/.test(Y)?"y2":"y1"]),e(document).mousemove(C).one("mouseup",v),ut.unbind("mousemove",w)):d.movable?(q=L+wt.x1-h(t),B=j+wt.y1-f(t),ut.unbind("mousemove",w),e(document).mousemove(W).one("mouseup",function(){d.onSelectEnd(r,m()),e(document).unbind("mousemove",W),ut.mousemove(w)})):lt.mousedown(t),!1)}function z(e){V&&(e?(tt=i(L,n(L+D,_+o(ot-et)*V*(tt>_||-1))),ot=s(i(j,n(j+R,et+o(tt-_)/V*(ot>et||-1)))),tt=s(tt)):(ot=i(j,n(j+R,et+o(tt-_)/V*(ot>et||-1))),tt=s(i(L,n(L+D,_+o(ot-et)*V*(tt>_||-1)))),ot=s(ot)))}function k(){_=n(_,L+D),et=n(et,j+R),o(tt-_)<F&&(tt=_-F*(_>tt||-1),L>tt?_=L+F:tt>L+D&&(_=L+D-F)),o(ot-et)<G&&(ot=et-G*(et>ot||-1),j>ot?et=j+G:ot>j+R&&(et=j+R-G)),tt=i(L,n(tt,L+D)),ot=i(j,n(ot,j+R)),z(o(tt-_)<o(ot-et)*V),o(tt-_)>J&&(tt=_-J*(_>tt||-1),z()),o(ot-et)>U&&(ot=et-U*(et>ot||-1),z(!0)),wt={x1:l(n(_,tt)),x2:l(i(_,tt)),y1:u(n(et,ot)),y2:u(i(et,ot)),width:o(tt-_),height:o(ot-et)},y(),d.onSelectChange(r,m())}function C(e){return tt=/w|e|^$/.test(Y)||V?h(e):a(wt.x2),ot=/n|s|^$/.test(Y)||V?f(e):c(wt.y2),k(),!1}function A(t,o){tt=(_=t)+wt.width,ot=(et=o)+wt.height,e.extend(wt,{x1:l(_),y1:u(et),x2:l(tt),y2:u(ot)}),y(),d.onSelectChange(r,m())}function W(e){return _=i(L,n(q+h(e),L+D-wt.width)),et=i(j,n(B+f(e),j+R-wt.height)),A(_,et),e.preventDefault(),!1}function I(){e(document).unbind("mousemove",I),b(),tt=_,ot=et,k(),Y="",mt.is(":visible")||ut.add(mt).hide().fadeIn(d.fadeSpeed||0),Z=!0,e(document).unbind("mouseup",P).mousemove(C).one("mouseup",v),ut.unbind("mousemove",w),d.onSelectStart(r,m())}function P(){e(document).unbind("mousemove",I).unbind("mouseup",P),x(ut.add(mt)),p(l(_),u(et),l(_),u(et)),!this instanceof e.imgAreaSelect&&(d.onSelectChange(r,m()),d.onSelectEnd(r,m()))}function K(t){return 1!=t.which||mt.is(":animated")?!1:(b(),q=_=h(t),B=et=f(t),e(document).mousemove(I).mouseup(P),!1)}function N(){g(!1)}function H(){E=!0,O(d=e.extend({classPrefix:"imgareaselect",movable:!0,parent:"body",resizable:!0,resizeMargin:10,onInit:function(){},onSelectStart:function(){},onSelectChange:function(){},onSelectEnd:function(){}},d)),ut.add(mt).css({visibility:""}),d.show&&(Z=!0,b(),y(),ut.add(mt).hide().fadeIn(d.fadeSpeed||0)),setTimeout(function(){d.onInit(r,m())},0)}function M(e,t){for(option in t)void 0!==d[option]&&e.css(t[option],d[option])}function O(o){if(o.parent&&($=e(o.parent)).append(ut.add(mt)),e.extend(d,o),b(),null!=o.handles){for(pt.remove(),pt=e([]),st=o.handles?"corners"==o.handles?4:8:0;st--;)pt=pt.add(t());pt.addClass(d.classPrefix+"-handle").css({position:"absolute",fontSize:0,zIndex:gt+1||1}),!parseInt(pt.css("width"))>=0&&pt.width(5).height(5),(rt=d.borderWidth)&&pt.css({borderWidth:rt,borderStyle:"solid"}),M(pt,{borderColor1:"border-color",borderColor2:"background-color",borderOpacity:"opacity"})}for(Q=d.imageWidth/D||1,X=d.imageHeight/R||1,null!=o.x1&&(p(o.x1,o.y1,o.x2,o.y2),o.show=!o.hide),o.keys&&(d.keys=e.extend({shift:1,ctrl:"resize"},o.keys)),mt.addClass(d.classPrefix+"-outer"),ht.addClass(d.classPrefix+"-selection"),st=0;st++<4;)e(ft[st-1]).addClass(d.classPrefix+"-border"+st);M(ht,{selectionColor:"background-color",selectionOpacity:"opacity"}),M(ft,{borderOpacity:"opacity",borderWidth:"border-width"}),M(mt,{outerColor:"background-color",outerOpacity:"opacity"}),(rt=d.borderColor1)&&e(ft[0]).css({borderStyle:"solid",borderColor:rt}),(rt=d.borderColor2)&&e(ft[1]).css({borderStyle:"dashed",borderColor:rt}),ut.append(ht.add(ft).add(T).add(pt)),e.browser.msie&&((rt=mt.css("filter").match(/opacity=(\d+)/))&&mt.css("opacity",rt[1]/100),(rt=ft.css("filter").match(/opacity=(\d+)/))&&ft.css("opacity",rt[1]/100)),o.hide?x(ut.add(mt)):o.show&&E&&(Z=!0,ut.add(mt).fadeIn(d.fadeSpeed||0),g()),V=(nt=(d.aspectRatio||"").split(/:/))[0]/nt[1],lt.add(mt).unbind("mousedown",K),d.disable||d.enable===!1?(ut.unbind("mousemove",w).unbind("mousedown",S),e(window).unbind("resize",N)):((d.enable||d.disable===!1)&&((d.resizable||d.movable)&&ut.mousemove(w).mousedown(S),e(window).resize(N)),d.persistent||lt.add(mt).mousedown(K)),d.enable=d.disable=void 0}var E,T,L,j,D,R,$,q,B,Q,X,Y,F,G,J,U,V,Z,_,et,tt,ot,it,nt,st,rt,dt,at,ct,lt=e(r),ut=t(),ht=t(),ft=t().add(t()).add(t()).add(t()),mt=t().add(t()).add(t()).add(t()),pt=e([]),bt={left:0,top:0},yt={left:0,top:0},gt=0,xt="absolute",wt={x1:0,y1:0,x2:0,y2:0,width:0,height:0},vt=document.documentElement,St=function(e){var t,o,s=d.keys,r=e.keyCode;if(t=isNaN(s.alt)||!e.altKey&&!e.originalEvent.altKey?!isNaN(s.ctrl)&&e.ctrlKey?s.ctrl:!isNaN(s.shift)&&e.shiftKey?s.shift:isNaN(s.arrows)?10:s.arrows:s.alt,"resize"==s.arrows||"resize"==s.shift&&e.shiftKey||"resize"==s.ctrl&&e.ctrlKey||"resize"==s.alt&&(e.altKey||e.originalEvent.altKey)){switch(r){case 37:t=-t;case 39:o=i(_,tt),_=n(_,tt),tt=i(o+t,_),z();break;case 38:t=-t;case 40:o=i(et,ot),et=n(et,ot),ot=i(o+t,et),z(!0);break;default:return}k()}else switch(_=n(_,tt),et=n(et,ot),r){case 37:A(i(_-t,L),et);break;case 38:A(_,i(et-t,j));break;case 39:A(_+n(t,D-l(tt)),et);break;case 40:A(_,et+n(t,R-u(ot)));break;default:return}return!1};for(this.remove=function(){O({disable:!0}),ut.add(mt).remove()},this.getOptions=function(){return d},this.setOptions=O,this.getSelection=m,this.setSelection=p,this.cancelSelection=P,this.update=g,it=lt;it.length;)gt=i(gt,isNaN(it.css("z-index"))?gt:it.css("z-index")),"fixed"==it.css("position")&&(xt="fixed"),it=it.parent(":not(body)");gt=d.zIndex||gt,e.browser.msie&&lt.attr("unselectable","on"),e.imgAreaSelect.keyPress=e.browser.msie||e.browser.safari?"keydown":"keypress",e.browser.opera&&(T=t().css({width:"100%",height:"100%",position:"absolute",zIndex:gt+2||2})),ut.add(mt).css({visibility:"hidden",position:xt,overflow:"hidden",zIndex:gt||"0"}),ut.css({zIndex:gt+2||2}),ht.add(ft).css({position:"absolute",fontSize:0}),r.complete||"complete"==r.readyState||!lt.is("img")?H():lt.one("load",H),e.browser.msie&&e.browser.version>=7&&(r.src=r.src)},e.fn.imgAreaSelect=function(t){return t=t||{},this.each(function(){e(this).data("imgAreaSelect")?t.remove?(e(this).data("imgAreaSelect").remove(),e(this).removeData("imgAreaSelect")):e(this).data("imgAreaSelect").setOptions(t):t.remove||(void 0===t.enable&&void 0===t.disable&&(t.enable=!0),e(this).data("imgAreaSelect",new e.imgAreaSelect(this,t)))}),t.instance?e(this).data("imgAreaSelect"):this}}(jQuery);