(function($){
    //image light-box
    var $thumb = $('.cwg-thumb'),
        $imgSmall = $thumb.find('.img-small'),
        $thumbnail = $('.cwg-thumbnail'),
        $li = $thumbnail.find('li'),
        items = [];

    $.each($li, function(i, e){
        items.push({
            src: $(e).data('src')
        });
    });

    $thumb.on('click', function(){
        $.magnificPopup.open({
            items: items,
            type: 'image',
            gallery: {
                enabled: true
            }
        }, $li.filter('.active').index());
    });

    //carousel
    $('.thumbnail-wrap').simpleCarousel({
        itemWidth: 66,
        prev: '.prev-thumb',
        next: '.next-thumb',
        callback: function($curr){
            $thumb.find('.img-original').remove();
            $imgSmall.attr('src', $curr.find('img').attr('src'));
            $('<img/>').addClass('img-full img-original mfp-zoom').attr('src', $curr.data('src')).insertAfter($imgSmall);
        }
    });

    //order
    var $orderModal = $('#js-order-modal'),
        $orderForm = $orderModal.find('#js-order-form'),
        $needReset = $orderModal.find('.js-need-reset'),
        $otherOrder = $orderModal.find('#js-other-order'),
        $queueNum = $orderModal.find('#js-queue-num'),
        $kennelLocation = $orderModal.find('#js-kennel-location'),
        $waitLocation = $orderModal.find('#js-wait-location'),
        $waitTime = $orderModal.find('#js-wait-time'),
        $serviceCharge = $orderModal.find('#js-service-charge'),
        $chargeType = $orderModal.find('#js-charge-type'),
        $toFirst = $orderModal.find('#js-to-first'),
        $liftInput = $orderModal.find('#js-lift-btn'),
        $sendMessage = $orderModal.find('#js-send-message'),
        $agreement = $orderModal.find('#js-agreement'),
        $payLink = $orderModal.find('#js-pay-link'),
        $chargeNum = $orderModal.find('#js-charge-num');

    //pass the pet id
    $('.js-btn-order').on('click', function(){
        $orderModal.data('id', $(this).data('id')).modal('show');
    });

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

    $payLink.on('click', function(){
        $('#js-go-status').tab('show');
    });

    $('#js-go-success').on('click', function(e){
        e.preventDefault();
        e.stopPropagation();

        var $this = $(this);

        $.ajax({
            url: '/buy/detail/attention/',
            data: {id: $orderModal.data('appointmentId')},
            dataType: 'json',
            success: function(data){
                if(data.status == 0){
                    $this.tab('show');
                }else{
                    alert(data.message);
                }
            }
        });
    });

    //validate
    var validator = $orderForm.validate({
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
    });

    $('#js-order-info').on('click', '.next-step', function(){
        var $this = $(this),
            arr = $('#js-order-form').serializeArray(),
            data = {};

        data.id = $orderModal.data('id');

        for(var i = 0, len = arr.length; i < len; i++){
            var curr = arr[i];
            data[curr.name] = curr.value;
        }

        $orderModal.data('transportation', data.transportation);

        validator.form();

        if(validator.numberOfInvalids()){
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

    $('#js-order-confirm').on('click', '.next-step', function(e){
        e.preventDefault();
        //var $this = $(this);

        if(!$agreement.is(':checked')){
            alert('同意《宠物购用户协议》才能预约哟~');
            e.stopPropagation();
        }

        //$.ajax({
        //    url: '/buy/detail/attention/',
        //    data: {id: $orderModal.data('appointmentId')},
        //    dataType: 'json',
        //    beforeSend: function(){
        //        $this.button('loading');
        //    },
        //    success: function(data){
        //        if(data.status == 0){
        //            $this.tab('show');
        //        }else{
        //            alert(data.message);
        //        }
        //    },
        //    complete: function(){
        //        $this.button('reset');
        //    }
        //});
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

    //order steps
    $orderModal.on('show.bs.modal', function(){
        resetOrderInfo($needReset, $orderForm);
    });

    //detail nav affix
    var $affixScrollspy = $('#js-affix-scrollspy');
    $affixScrollspy.affix({
        offset: {
            top: 600
        }
    });
    //scroll spy
    $('body').scrollspy({ target: '#js-affix-scrollspy' });

    var animateIn = 'slideInDown',
        animateOut = 'slideInUp';

    $affixScrollspy.on('affix.bs.affix', function(){
        $affixScrollspy.addClass(animateIn + ' animated').removeClass(animateOut);
    });

    $affixScrollspy.on('affix-top.bs.affix', function(){
        $affixScrollspy.addClass(animateOut).removeClass(animateIn);
    });

    //location select
    var $locationBox = $('#js-location-box'),
        $btnLocation = $('#js-btn-location');

    //time select
    var $btnTime = $('#js-btn-time'),
        $timeBox = $('#js-time-box'),
        $time = $('#js-time');

    $timeBox.on('click', 'td', function(){
        var $this = $(this),
            time = $this.closest('tr').find('th').text(),
            data = $this.data();

        if($this.hasClass('disabled')){
            return;
        }

        $timeBox.find('td').not($this.addClass('active')).removeClass('active');

        var text = data.year + '-' + data.date + '（'+ data.day +'）' + time;
        $time.text(text);
        $('#js-time-input').val( data.year + '-' + data.date + ' ' + time);
        validator.element('#js-time-input');
        $timeBox.hide();
    });


//地址选择


var $locationBox = $('#js-location-box'),
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
        $('#js-location').text(text);
        $('#js-location-input').val(JSON.stringify(param));
        validator.element('#js-location-input');
        $locationBox.hide();
    });

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

}(jQuery));