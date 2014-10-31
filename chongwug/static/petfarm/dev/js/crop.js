/**
 * author: ren wei
 * mail: 371151833@qq.com
 * TODO:
 * 1.img-type-input 这个字段已经弃用，需删除相关操作
 * 2.根据 select 选项动态变化截图区大小的功能已经弃用，需删除相关代码
 */

(function($){
    $.fn.uploadAndCrop = function(options){
        var defaultOptions = {
            //custom options
            previewItemTpl: '#preview-item-tpl',
            uploadBtn: '#js-uploadify',
            cropModal: '#js-crop-modal',
            imgCount: '#js-img-count',
            previewSize: [120, 80],
            
            //uploadify options
            buttonText: '浏览并上传',
            buttonClass: 'btn-info',
            fileTypeExts: '*.jpg;*.jpeg;*.gif;*.png;*.bmp;',
            fileSizeLimit: '4MB',
            multi: false,
            formData: {}
        };

        options = $.extend(defaultOptions, options);

        return this.each(function(){
            var $container = $(this),
                
                //if the preview ul is present, just use it, or append it to cintainer
                $previewUl = $container.find('.preview-img'),
                $previewUl = $previewUl.length ? $previewUl : $('<ul>').addClass('preview-img').appendTo($container),
                
                previewItemTpl = $(options.previewItemTpl).html(),
                $uploadBtn = $container.find(options.uploadBtn),
                $cropModal = $(options.cropModal),
                $imgCount= $(options.imgCount),
                previewSize = options.previewSize,
                
                $currCropImg = $('<img>').appendTo($cropModal.find('.modal-body')),
                $currPreviewImg = null,
                $currPreviewLi = null,
                jCrop = null,

                cropSize = $container.data('size'),//[width, height]
                radio = cropSize[0] / cropSize[1],
                currActualSize = [],
                index = 0;

            /**
             * data: {width: '', height: '', url: ''}
             */
            $container.on('uploadAndCrop.uploadSuccess', function(event, data){
                currActualSize = [data.width, data.height];
                $cropModal.addClass('loading').modal('show');
                $container.trigger('uploadAndCrop.preloadImg', data);
            });

            $container.on('uploadAndCrop.preloadImg', function(event, data){
                var $img = $('<img>');

                $img.on('load', function(){
                    index++;
                    $imgCount.val(index);
                    $container.trigger('uploadAndCrop.initCrop', data);
                }).attr('src', data.url);
            });

            $container.on('uploadAndCrop.initCrop', function(event, data){
                $currCropImg.attr('src', data.url).removeAttr('style');

                if(data.img){
                    $currPreviewImg = data.img;
                }else{
                    $currPreviewLi = $(compileTpl({src: data.url, index: index})).appendTo($previewUl);
                    $currPreviewImg = $currPreviewLi.find('img').data({width: data.width, height: data.height});

                    if(!hasChecked()){
                        $currPreviewLi.find('.img-main-input').prop('checked', true);
                    }
                }

                $container.trigger('uploadAndCrop.startCrop', {select: data.select});
            });

            $container.on('uploadAndCrop.startCrop', function(event, data){
                $cropModal.removeClass('loading');

                $currCropImg.Jcrop({
                    aspectRatio: radio,
                    minSize: cropSize,
                    setSelect: [0, 0, cropSize[0], cropSize[1]]
                }, function(){
                    jCrop = this;
                });

                if($.isArray(data.select)){
                    jCrop.setSelect(data.select);
                }
            });

            function compileTpl(data){
                var tpl = previewItemTpl;

                for(var i in data){
                    tpl = tpl.replace(new RegExp('{'+ i +'}', 'gm'), data[i]);
                }

                return tpl;
            }

            function hasChecked(){
                return !!$previewUl.find('.img-main-input').filter(':checked').length;
            }

            $cropModal.on('hidden.bs.modal', function(){
                syncPreview(jCrop.tellSelect());
                jCrop.destroy();
            });

            //sync crop area to preview, fill the crop coords to hidden input
            function syncPreview(coords){
                var rx = previewSize[0] / coords.w;
                var ry = previewSize[1] / coords.h;

                $currPreviewImg.css({
                    width: Math.round(rx * currActualSize[0]) + 'px',
                    height: Math.round(ry * currActualSize[1]) + 'px',
                    marginLeft: '-' + Math.round(rx * coords.x) + 'px',
                    marginTop: '-' + Math.round(ry * coords.y) + 'px'
                });

                $currPreviewLi.find('.img-position-input').val(JSON.stringify(coords));
            }


            $previewUl.on('click', '.img-crop', function(){
                $cropModal.addClass('loading').modal('show');

                $currPreviewLi = $(this).closest('li');

                var $positionInput = $currPreviewLi.find('.img-position-input'),
                    $img = $currPreviewLi.find('img'),
                    data = $img.data(),
                    select = $.parseJSON($positionInput.val());

                currActualSize = [data.width, data.height];

                $container.trigger('uploadAndCrop.initCrop', {
                    url: $img.attr('src'),
                    img: $img,
                    width: data.width,
                    height: data.height,
                    select: [select.x, select.y, select.x2, select.y2]
                });
            });

            $previewUl.on('click', '.img-del', function(){
                var $li = $(this).closest('li');

                options.beforeDel && options.beforeDel($li.data('id'));

                $li.remove();

                if(!hasChecked()){
                    var $first = $previewUl.find('.img-main-input').first();
                    if($first.length){
                        $first.prop('checked', true);
                    }
                }
            });

            //init upload button
            $uploadBtn.uploadify({
                buttonText: options.buttonText,
                buttonClass: options.buttonClass,
                swf: options.swf,
                uploader: options.uploader,
                fileTypeExts: options.fileTypeExts,
                fileSizeLimit: options.fileSizeLimit,
                multi: options.multi,
                formData: options.formData,
                onUploadError: function(file, errorCode, errorMsg, errorString){
                    if(errorMsg == "500"){
                        errorString = '服务器内部错误';
                    }

                    alert('"' + file.name + '" 上传失败：' + errorString + '，请重试！');
                },
                onUploadSuccess: function(file, data, response){
                    if (!response) {
                        alert('请求超时，请稍后重试！');
                        return;
                    }

                    data = $.parseJSON(data);

                    if(data.status == 0){
                        $container.trigger('uploadAndCrop.uploadSuccess', data);
                    }else{
                        alert('图片上传失败：' + data.message + '，请重试。');
                    }
                }
            });
        });
    };
})(jQuery);
