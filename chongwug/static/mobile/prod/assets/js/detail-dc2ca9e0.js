!function(t){function e(){var e=[t.trim(s.val()),t.trim(o.val())];a.val(e.join(" "))}function n(e,n,i){t.ajax({url:"./",data:e,dataType:"json",success:function(t){0==t.status?(n.html(g(t)),i()):alert(t.message)}})}function i(t,e){if(!e.hasClass("active")){var n=t.find(".active");n.removeClass("active"),e.addClass("active")}}var a=t("#js-time-input"),o=t("#js-appoint-time"),s=t("#js-appoint-date"),d=t("#js-location-box"),r=t("#js-btn-location"),c=t("#js-location-input"),l=t("#js-location"),f=d.find("#province"),u=d.find("#city"),p=d.find("#js-to-city"),m=d.find("#district"),j=d.find("#js-to-district"),h=d.find("#street"),v=d.find("#js-to-street"),g=template("location-select-tpl"),b={},w=[];r.on("click",function(){d.is(":visible")?d.hide():d.show()}),t(document).on("click",function(e){var n=t(e.target),i=n.closest("#js-location-box"),a=n.closest(".btn-select");i.length||a.length||d.hide()}),o.on("change",e),s.on("change",e),e(),f.on("click","a",function(){var e=t(this);i(f,e),w[0]=e.text(),b.province=e.data("id"),b.range=e.closest("dl").find("dt").data("id"),delete b.city,delete b.district,delete b.street,m.html(""),h.html(""),n(b,u,function(){window.segmented({target:p[0]})})}),u.on("click","a",function(){var e=t(this);i(u,e),w[1]=e.text(),b.city=e.data("id"),delete b.district,delete b.street,h.html(""),n(b,m,function(){window.segmented({target:j[0]})})}),m.on("click","a",function(){var e=t(this);i(m,e),w[2]=e.text(),b.district=e.data("id"),delete b.street,n(b,h,function(){window.segmented({target:v[0]})})}),h.on("click","a",function(){var e=t(this);i(h,e),w[3]=e.text(),b.street=e.data("id");var n=w.join("-");l.text(n),c.val(JSON.stringify(b)),d.hide()})}(jQuery),function(t){function e(t){function e(){n--,n>0?(t.text(i+n),setTimeout(e,1e3)):(t.data("counting",!1),t.prop("disabled",!1).removeClass("disabled").text(i))}if(t.data("counting"))return!1;var n=t.data("delay"),i="重新发送短信 ";n=!isNaN(n)&&parseInt(n,10)||60,t.text(i+n),t.data("counting",!0),setTimeout(e,1e3)}function n(e,n){n[0].reset(),n.find(".has-error").removeClass("has-error"),r.trigger("click"),e.text(function(){return t(this).data("text")}),window.segmented.show(p)}function i(t){l.text(t.count),f.text(t.ordernum),m.text(t.farm),j.text(t.waitpoint),h.text(t.waittime),v.text(t.pay),b.text(t.orderno),g.attr("href",t.alipayurl)}var a=t("#js-order-modal"),o=a.find(".js-need-reset"),s=a.find("#js-order-info"),d=s.find("#js-order-form"),r=d.find("#js-lift-btn"),c=a.find("#js-order-confirm"),l=c.find("#js-other-order"),f=c.find("#js-queue-num"),u=c.find("#js-agreement"),p=c.find("#js-to-first"),m=a.find(".js-kennel-location"),j=a.find(".js-wait-location"),h=a.find(".js-wait-time"),v=a.find("#js-service-charge"),g=a.find(".js-pay-link"),b=a.find("#js-charge-num"),w=a.find("#js-to-status"),x=a.find("#js-to-success"),y=a.find("#js-send-message");t(".js-btn-order").on("touchend",function(){a.data("id",t(this).data("id"))}),a.on("show.bs.modal",function(){n(o,d)}),g.on("click",function(){window.segmented.show(w)}),x.on("click",function(n){n.preventDefault(),n.stopPropagation();var i=t(this);t.ajax({url:"/buy/detail/attention/",data:{id:a.data("appointmentId")},dataType:"json",beforeSend:function(){i.prop("disabled",!0)},success:function(t){0==t.status?(window.segmented.show(i),e(y)):alert(t.message)},complete:function(){i.prop("disabled",!1)}})}),s.on("click",".next-step",function(){var e=t(this),n=d.serializeArray(),o={};o.id=a.data("id");for(var s=0,r=n.length;r>s;s++){var c=n[s];o[c.name]=c.value}o.csrfmiddlewaretoken=t.cookie("csrftoken")||o.csrfmiddlewaretoken,t.ajax({url:"/buy/detail/attention/",type:"post",data:o,dataType:"json",beforeSend:function(){e.prop("disabled",!0)},success:function(t){0==t.status?(i(t),a.data("appointmentId",t.id),window.segmented.show(e)):alert(t.message)},complete:function(){e.prop("disabled",!1)},error:function(t,e,n){alert(e+": "+n)}})}),c.on("click",".next-step",function(t){t.preventDefault(),u.is(":checked")||(alert("同意《宠物购用户协议》才能预约哟~"),t.stopPropagation())}),y.on("click",function(){t.ajax({url:"/buy/detail/attention/sendsms/",data:{id:a.data("appointmentId")},dataType:"json",beforeSend:function(){y.prop("disabled",!0).addClass("disabled")},success:function(t){0==t.status?(alert("发送成功，请注意查收"),e(y)):(alert(t.message),y.prop("disabled",!1).removeClass("disabled"))},error:function(){y.prop("disabled",!1).removeClass("disabled")}})})}(jQuery);