!function(i){i.crop=function(){function t(){var i=p.filter(":selected");return{minSize:i.data("size"),type:i.attr("value")}}function n(){var t={};return i.each(p,function(n,e){var o=i(e);t[o.attr("value")]={minSize:o.data("size"),text:o.text()}}),t}function e(t,n){var e=i("<img>");e.on("load",function(){n()}),e.attr("src",t)}function o(t,n,e){var o=n[0]/n[1];t.Jcrop({aspectRatio:o,minSize:n,setSelect:[0,0,n[0],n[1]]},function(){f=this}),i.isArray(e)&&f.setSelect(e)}function a(i){y.val(JSON.stringify(i))}function l(i){var t=w[0]/i.w,n=w[1]/i.h;h.css({width:Math.round(t*S[0])+"px",height:Math.round(n*S[1])+"px",marginLeft:"-"+Math.round(t*i.x)+"px",marginTop:"-"+Math.round(n*i.y)+"px"}),a(i)}function r(i){var t=g;for(var n in i)t=t.replace(new RegExp("{"+n+"}","gm"),i[n]);return t}function s(t){v=u.html('<img src="'+t.url+'">').find("img"),h=t.img||i(r({src:t.url,index:z})).appendTo(m).find("img"),t.img||h.data({width:t.width,height:t.height}),y=t.positionInput||h.closest("li").find(".img-position-input"),x=t.typeInput||h.closest("li").find(".img-type-input"),d.removeClass("loading"),o(v,t.minSize||b,t.select)}var d=i("#js-crop-modal"),u=d.find(".modal-body"),c=i("#js-img-type"),p=c.find("option"),f=null,m=i("#js-preview-img"),g=i("#preview-item-tpl").html(),h=null,v=null,y=null,x=null,S=null,w=[120,80],z=0,b=t().minSize,j=n();d.on("hidden.bs.modal",function(){var i=t().type;x.val(i),l(f.tellSelect()),x.closest("li").find(".img-tit").text(j[i].text),f&&f.destroy(),u.html(""),c[0].selectedIndex=0}),m.on("click",".img-crop",function(){d.modal("show").addClass("loading");var t=i(this).closest("li"),n=t.find(".img-position-input"),e=t.find(".img-type-input"),o=t.find("img"),a=i.parseJSON(n.val());S=[o.data("width"),o.data("height")],s({url:o.attr("src"),positionInput:n,typeInput:e,img:o,select:[a.x,a.y,a.x2,a.y2],minSize:j[e.val()].minSize})}),c.on("change",function(){var t=i(this),n=j[t.val()].minSize,e=[0,0].concat(n);f&&f.destroy(),o(v,n,e)}),m.on("click",".img-del",function(){i(this).closest("li").remove()}),i("#js-uploadify").uploadify({buttonText:"浏览并上传",buttonClass:"btn-info",swf:"/static/back-assets/dist/uploadify/uploadify.swf",uploader:"/petfarm/petfarm/picadd/upload/",fileTypeExts:"*.jpg;*.jpeg;*.gif;*.png;*.bmp;",fileSizeLimit:"4MB",multi:"false",formData:{},onUploadError:function(i,t,n,e){"500"==n&&(e="服务器内部错误"),alert('"'+i.name+'" 上传失败：'+e+"，请重试！")},onUploadSuccess:function(t,n,o){return o?(n=i.parseJSON(n),S=[n.width,n.height],d.modal("show").addClass("loading"),e(n.url,function(){z++,s(n)}),void 0):(alert("请求超时，请稍后重试！"),void 0)}})}}(jQuery);