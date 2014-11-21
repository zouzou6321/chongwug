//image gallery
;(function($){
    var $thumb = $('.cwg-thumb'), //big img wrapper
        $imgSmall = $thumb.find('.img-small'), //small img from thumbnail for progressive display
        $thumbnail = $('.cwg-thumbnail'),
        $li = $thumbnail.find('li'),
        items = [];

    //iterator thumbnail for magnificPopup lightbox
    $.each($li, function(i, e){
        items.push({
            src: $(e).data('src')
        });
    });

    //magnificPopup plugin
    $thumb.on('click', function(){
        $.magnificPopup.open({
            items: items,
            type: 'image',
            gallery: {
                enabled: true
            }
        }, $li.filter('.active').index());
    });

    //thumbnail
    $('.thumbnail-wrap').simpleCarousel({
        itemWidth: 66,
        prev: '.prev-thumb',
        next: '.next-thumb',
        callback: function($curr){
            //progressive img display
            //need to remove the big img first, because change the img's url will not display the new img util the new img is fully download
            $thumb.find('.img-original').remove();
            $imgSmall.attr('src', $curr.find('img').attr('src'));
            $('<img/>').addClass('img-full img-original mfp-zoom').attr('src', $curr.data('src')).insertAfter($imgSmall);
        }
    });
}(jQuery));

//affix and scrollspy
;(function($){
    var $affixScrollspy = $('#js-affix-scrollspy');

    $affixScrollspy.affix({
        offset: {
            top: 600
        }
    });

    $('body').scrollspy({ target: '#js-affix-scrollspy' });

    var animateIn = 'slideInDown',
        animateOut = 'slideInUp';

    $affixScrollspy.on('affix.bs.affix', function(){
        $affixScrollspy.addClass(animateIn + ' animated').removeClass(animateOut);
    });

    $affixScrollspy.on('affix-top.bs.affix', function(){
        $affixScrollspy.addClass(animateOut).removeClass(animateIn);
    });
}(jQuery));

//select box - location and time
;(function($){
        //time
    var $timeBox = $('#js-time-box'), //time wrapper
        $btnTime = $('#js-btn-time'), //time choose btn
        $timeInput = $('#js-time-input'), // hidden time input
        $time = $('#js-time'), //time text

        //location
        $locationBox = $('#js-location-box'), //location wrapper
        $btnLocation = $('#js-btn-location'), //location choose btn
        $locationInput = $('#js-location-input'), //hidden location input
        $location = $('#js-location'), //location text
        $province = $locationBox.find('#province'),
        $city = $locationBox.find('#city'),
        $toCity = $locationBox.find('#js-to-city'),
        $district = $locationBox.find('#district'),
        $toDistrict = $locationBox.find('#js-to-district'),
        $street = $locationBox.find('#street'),
        $toStreet = $locationBox.find('#js-to-street'),
        render = template('location-select-tpl'),
        param = {},
        location = [];

    //global click handle
    $btnTime.on('click', function(e){
        $locationBox.hide();
        $timeBox.is(':visible') ? $timeBox.hide() : $timeBox.show();
    });

    $btnLocation.on('click', function(e){
        $timeBox.hide();
        $locationBox.is(':visible') ? $locationBox.hide() : $locationBox.show();
    });

    $(document).on('click', function(e){
        var $target = $(e.target),
            $targetLocation = $target.closest('#js-location-box'),
            $targetTime = $target.closest('#js-time-box'),
            $targetBtn = $target.closest('.btn-select');

        if(!$targetLocation.length && !$targetTime.length && !$targetBtn.length){
            $timeBox.hide();
            $locationBox.hide();
        }
    });

    //时间选择
    $timeBox.on('click', 'td', function(){
        var $this = $(this),
            time = $.trim($this.closest('tr').find('th').text()),
            data = $this.data();

        if($this.hasClass('disabled')){
            return;
        }

        changeActive($timeBox, $this);

        var text = data.year + '-' + data.date + '（'+ data.day +'）' + time;
        $time.text(text);
        $timeInput.val(data.year + '-' + data.date + ' ' + time);
        $(document).trigger('validate', {el: '#js-time-input'});
        $timeBox.hide();
    });

    //地址选择
    $province.on('click', 'a', function(){
        var $this = $(this);

        changeActive($province, $this);

        location[0] = $this.text();

        param.province = $this.data('id');
        param.range = $this.closest('dl').find('dt').data('id');
        delete param.city;
        delete param.district;
        delete param.street;

        $district.html('');
        $street.html('');

        renderData(param, $city, function(){
           $toCity.tab('show');
        });
    });

    $city.on('click', 'a', function(){
        var $this = $(this);

        changeActive($city, $this);

        location[1] = $this.text();

        param.city = $this.data('id');
        delete param.district;
        delete param.street;

        $street.html('');

        renderData(param, $district, function(){
            $toDistrict.tab('show');
        });
    });

    $district.on('click', 'a', function(){
        var $this = $(this);

        changeActive($district, $this);

        location[2] = $this.text();

        param.district = $this.data('id');
        delete param.street;

        renderData(param, $street, function(){
           $toStreet.tab('show');
        });
    });

    $street.on('click', 'a', function(){
        var $this = $(this);

        changeActive($street, $this);

        location[3] = $this.text();

        param.street = $this.data('id');

        var text = location.join('-');
        $location.text(text);
        $locationInput.val(JSON.stringify(param));
        $(document).trigger('validate', {el: '#js-location-input'});
        $locationBox.hide();
    });

    function renderData(param, $parent, cb){
        $.ajax({
            url: './',
            data: param,
            dataType: 'json',
            success: function(data){
                if(data.status == 0){
                    $parent.html(render(data));
                    cb();
                }else{
                    alert(data.message);
                }
            }
        });
    }

    function changeActive($parent, $this){
        if(!$this.hasClass('active')){
            var $active = $parent.find('.active');
            $active.removeClass('active');
            $this.addClass('active');
        }
    }
}(jQuery));


//order progress
(function($){
    var $orderModal = $('#js-order-modal'), //order modal
        $needReset = $orderModal.find('.js-need-reset'), //the filed that need to be reset when reopen the modal

        //order info Tab
        $orderInfo = $orderModal.find('#js-order-info'),
        $orderForm = $orderInfo.find('#js-order-form'), //order info form
        $liftInput = $orderForm.find('#js-lift-btn'), //接送按钮
        validator = $orderForm.validate({ //attach validate
            onsubmit: false,
            errorElement: 'p',
            errorClass: 'help-block',
            ignore: '',
            rules: {
                "phone": {
                    minlength: 11,
                    maxlength: 11,
                    digits: true
                }
            },
            highlight: function (el) {
                $(el).closest('.form-group').addClass('has-error');
            },
            success: function (el) {
                $(el).closest('.form-group').removeClass('has-error');
                $(el).remove();
            }
        }),

        //order confirm Tab
        $orderConfirm = $orderModal.find('#js-order-confirm'),
        $otherOrder = $orderConfirm.find('#js-other-order'), //已预约用户
        $queueNum = $orderConfirm.find('#js-queue-num'), //排队号
        $agreement = $orderConfirm.find('#js-agreement'), //是否同意购犬协议 checkbox
        $toFirst = $orderConfirm.find('#js-to-first'), //go to order info Tab

        //order pay Tab
        $kennelLocation = $orderModal.find('.js-kennel-location'), //犬舍位置
        $waitLocation = $orderModal.find('.js-wait-location'), //等待接送地点
        $waitTime = $orderModal.find('.js-wait-time'), //等待接送时间
        $serviceCharge = $orderModal.find('#js-service-charge'), //支付费用
        $chargeType = $orderModal.find('#js-charge-type'), //支付费用类别
        $payLink = $orderModal.find('.js-pay-link'), //支付链接
        $chargeNum = $orderModal.find('#js-charge-num'), //订单号
        $toStatus = $orderModal.find('#js-to-status'), // got to order pay status Tab (hide)

        //order pay status Tab
        $toSuccess = $orderModal.find('#js-to-success'), //go to order success Tab

        //order success Tab
        $sendMessage = $orderModal.find('#js-send-message'); //发送短信


    //store the pet id when click the order btn
    $('.js-btn-order').on('click', function(){
        $orderModal.data('id', $(this).data('id')).modal('show');
    });

    //reset modal when modal open
    $orderModal.on('show.bs.modal', function(){
        resetOrderInfo($needReset, $orderForm);
    });

    $(document).on('validate', function(event, data){
        validator.element(data.el);
    });

    //go to order pay status Tab when click pay link
    $payLink.on('click', function(){
        $toStatus.tab('show');
    });

    $toSuccess.on('click', function(e){
        //prevent Tab switch
        e.preventDefault();
        e.stopPropagation();

        var $this = $(this);

        $.ajax({
            url: '/buy/detail/attention/',
            data: {id: $orderModal.data('appointmentId')},
            dataType: 'json',
            beforeSend: function(){
                $this.button('loading');
            },
            success: function(data){
                if(data.status == 0){
                    $this.tab('show');
                }else{
                    alert(data.message);
                }
            },
            complete: function(){
                $this.button('reset');
            }
        });
    });

    $orderInfo.on('click', '.next-step', function(){
        var $this = $(this),
            arr = $orderForm.serializeArray(),
            data = {};

        data.id = $orderModal.data('id');
        data.csrfmiddlewaretoken = $.cookie('csrftoken');

        for(var i = 0, len = arr.length; i < len; i++){
            var curr = arr[i];
            data[curr.name] = curr.value;
        }

        //存储交通方式，便于 reset text
        $orderModal.data('transportation', data.transportation);

        validator.form();

        if(!$orderForm.valid()){
            return;
        }

        $.ajax({
            url: '/buy/detail/attention/',
            type: 'post',
            data: data,
            dataType: 'json',
            beforeSend: function(){
                $this.button('loading');
            },
            success: function(data){
                if(data.status == 0){
                    fillOrderInfo(data);
                    $orderModal.data('appointmentId', data.id);
                    $this.tab('show');
                }else{
                    alert(data.message);
                }
            },
            complete: function(){
                $this.button('reset');
            }
        });
    });

    $orderConfirm.on('click', '.next-step', function(e){
        e.preventDefault();

        if(!$agreement.is(':checked')){
            alert('同意《宠物购用户协议》才能预约哟~');
            //prevent tab switch
            e.stopPropagation();
        }
    });

    $sendMessage.on('click', function(){
        $.ajax({
            url: '/buy/detail/attention/sendsms/',
            data: {id: $orderModal.data('appointmentId')},
            dataType: 'json',
            beforeSend: function(){
                $sendMessage.prop('disabled', true).addClass('disabled');
            },
            success: function(data){
                if(data.status == 0){
                    alert('发送成功，请注意查收');
                    countTime($sendMessage);
                }else{
                    alert(data.message);
                    $sendMessage.prop('disabled', false).removeClass('disabled');
                }
            },
            error: function(){
                $sendMessage.prop('disabled', false).removeClass('disabled');
            }
        });
    });

    function countTime($el){
        if($el.data('counting')){
            return false;
        }

        var delay = $el.data('delay'),
            text = '重新发送 ';

        delay = !isNaN(delay) && parseInt(delay, 10) || 60,


        $el.text(text + delay);

        function updateText(){
            delay--;

            if(delay > 0){
                $el.text(text + delay);
                setTimeout(updateText, 1000);
            }else{
                $el.data('counting', false);
                $el.prop('disabled', false).removeClass('disabled').text(text);
            }
        }
        $el.data('counting', true);
        setTimeout(updateText, 1000);
    }

    function resetOrderInfo($needReset, $form){
        $form[0].reset();
        validator.resetForm();
        $form.find('.has-error').removeClass('has-error');
        $liftInput.trigger('click');

        $needReset.text(function(){
            return $(this).data('text');
        });

        $toFirst.tab('show');
    }

    function fillOrderInfo(data){
        $otherOrder.text(data.count);
        $queueNum.text(data.ordernum);
        $kennelLocation.text(data.farm);
        $waitLocation.text(data.waitpoint);
        $waitTime.text(data.waittime);
        $serviceCharge.text(data.pay);
        $chargeNum.text(data.orderno);
        $payLink.attr('href', data.alipayurl);

        if($orderModal.data('transportation') != 'lift'){
            $chargeType.text('服务费');
        }
    }
}(jQuery));