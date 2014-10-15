(function($){
    $.crop = function(options){
            /*modal*/
        var $cropModal = $('#js-crop-modal'),
            $cropModalBody = $cropModal.find('.modal-body'),

        /*image type, min-size, radio*/
            $imgType = $('#js-img-type'),
            $imgTypeOption = $imgType.find('option'),

        /*jcrop api*/
            jcrop = null,

        /*preview wrapper*/
            $previewImg = $('#js-preview-img'),

        /*preview item template for insert*/
            $previewItemTpl = $('#preview-item-tpl').html(),

        /*current preview item, for update preview*/
            $currPreview = null,
            $currCropImg = null,
        /*store current image's position data*/
            $currPositionInput = null,
            $currTypeInput = null,
            $imgCountInput = $('#js-img-count');

        /*point to current image's actual size*/
            actualSize = null,

        /*point to current image's preview size*/
            previewSize = [120, 80],

        /*point to current index of the upload image, start from 1*/
            index = 0,

            minSize = getSizeInfo().minSize,
            typeObject = generateTypeObject();

        function getSizeInfo(){
            var $selected = $imgTypeOption.filter(':selected');

            return {
                minSize: $selected.data('size'),
                type: $selected.attr('value')
            };
        }

        function generateTypeObject(){
            var o = {};

            $.each($imgTypeOption, function(i, e){
                var $e = $(e);

                o[$e.attr('value')] = {
                  minSize: $e.data('size'),
                  text: $e.text()
                };
            });

            return o;
        }

        //预加载图片
        function loadImage(url, callback){
            var $img = $('<img>');

            $img.on('load', function(){
                callback();
            });

            $img.attr('src', url);
        }

        //开始截图
        function startCrop($img, minSize, select){
            var radio = minSize[0] / minSize[1];

            $img.Jcrop({
                aspectRatio: radio,
                minSize: minSize,
                setSelect: [0, 0, minSize[0], minSize[1]]
            }, function(){
                jcrop = this;
            });

            if($.isArray(select)){
                jcrop.setSelect(select);
            }
        }

        //同步截图数据到 input hidden
        function updateCoords(coords){
            $currPositionInput.val(JSON.stringify(coords));
        }

        //同步更新缩略图
        function syncPreview(coords){
            var rx = previewSize[0] / coords.w;
            var ry = previewSize[1] / coords.h;

            $currPreview.css({
                width: Math.round(rx * actualSize[0]) + 'px',
                height: Math.round(ry * actualSize[1]) + 'px',
                marginLeft: '-' + Math.round(rx * coords.x) + 'px',
                marginTop: '-' + Math.round(ry * coords.y) + 'px'
            });

            updateCoords(coords);
        }

        function compileTpl(data){
            var tpl = $previewItemTpl;

            for(var i in data){
                tpl = tpl.replace(new RegExp('{'+ i +'}', 'gm'), data[i]);
            }

            return tpl;
        }

        //上传图片成功后准备开始截图
        function afterUploadSuccess(data){
            $currCropImg = $cropModalBody.html('<img src="'+ data.url +'">').find('img');

            $currPreview = data.img || $(compileTpl({src: data.url, index: index})).appendTo($previewImg).find('img');

            if(!data.img){
                $currPreview.data({width: data.width, height: data.height});
            }

            $currPositionInput = data.positionInput || $currPreview.closest('li').find('.img-position-input');
            $currTypeInput = data.typeInput || $currPreview.closest('li').find('.img-type-input');

            $cropModal.removeClass('loading');
            startCrop($currCropImg, data.minSize || minSize, data.select);
        }

        //关闭截图弹窗后
        $cropModal.on('hidden.bs.modal', function(){
            //store type info
            var type = getSizeInfo().type;

            $currTypeInput.val(type);
            syncPreview(jcrop.tellSelect());

            $currTypeInput.closest('li').find('.img-tit').text(typeObject[type].text);

            jcrop && jcrop.destroy();
            $cropModalBody.html('');
            $imgType[0].selectedIndex = 0;
        });

        //重新截取图片
        $previewImg.on('click', '.img-crop', function(){
            $cropModal.modal('show').addClass('loading');

            var $currLi = $(this).closest('li'),
                $positionInput = $currLi.find('.img-position-input'),
                $typeInput = $currLi.find('.img-type-input'),
                $img = $currLi.find('img'),
                select = $.parseJSON($positionInput.val());

            actualSize = [$img.data('width'), $img.data('height')];

            afterUploadSuccess({
                url: $img.attr('src'),
                positionInput: $positionInput,
                typeInput: $typeInput,
                img: $img,
                select: [select.x, select.y, select.x2, select.y2],
                minSize: typeObject[$typeInput.val()].minSize
            });
        });

        //update crop area when image type select change
        $imgType.on('change', function(){
            var $this = $(this),
                minSize = typeObject[$this.val()].minSize,
                select = [0, 0].concat(minSize);

            jcrop && jcrop.destroy();
            startCrop($currCropImg, minSize, select);
        });

        //删除图片
        $previewImg.on('click', '.img-del', function(){
            $(this).closest('li').remove();
        });

        $('#js-uploadify').uploadify({
            buttonText: '浏览并上传',
            buttonClass: 'btn-info',
            swf: '/static/back-assets/dist/uploadify/uploadify.swf',
            uploader: options.uploader,
            fileTypeExts: '*.jpg;*.jpeg;*.gif;*.png;*.bmp;',
            fileSizeLimit: '4MB',
            multi: 'false',
            formData: {},
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
                actualSize = [data.width, data.height];

                $cropModal.modal('show').addClass('loading');
                loadImage(data.url, function(){
                    index++;
                    $imgCountInput.val(index);
                    afterUploadSuccess(data);
                });
            }
        });
    };
})(jQuery);