/* ========================================================================
 * Ratchet: segmented-controllers.js v2.0.2
 * http://goratchet.com/components#segmentedControls
 * ========================================================================
 * Copyright 2014 Connor Sears
 * Licensed under MIT (https://github.com/twbs/ratchet/blob/master/LICENSE)
 * ======================================================================== */

!(function () {
  'use strict';

  var getTarget = function (target) {
    var i;
    var segmentedControls = document.querySelectorAll('.segmented-control .control-item');

    for (; target && target !== document; target = target.parentNode) {
      for (i = segmentedControls.length; i--;) {
        if (segmentedControls[i] === target) {
          return target;
        }
      }
    }
  };

  function handler(e){
    var activeTab;
    var activeBodies;
    var targetBody;
    var targetTab     = getTarget(e.target);
    var className     = 'active';
    var classSelector = '.' + className;

    if (!targetTab) {
      return;
    }

    activeTab = targetTab.parentNode.querySelector(classSelector);

    if (activeTab) {
      activeTab.classList.remove(className);
    }

    targetTab.classList.add(className);

    if (!targetTab.hash) {
      return;
    }

    targetBody = document.querySelector(targetTab.hash);

    if (!targetBody) {
      return;
    }

    activeBodies = targetBody.parentNode.querySelectorAll(classSelector);

    for (var i = 0; i < activeBodies.length; i++) {
      activeBodies[i].classList.remove(className);
    }

    targetBody.classList.add(className);
  }

  var $content = $('.modal').find('.content');
  window.addEventListener('touchend', handler);
  window.segmented = handler;
  window.segmented.show = function($el){
    var href = $el.attr('href'),
        $target = $(href);

    $content.scrollTop(0);
    $target.addClass('active').siblings('.control-content').removeClass('active');
  };

  $(document).on('click', '[data-toggle="segmented"]', function (e) {
    e.preventDefault();
    window.segmented.show($(this));
  });

  window.addEventListener('click', function (e) { if (getTarget(e.target)) {e.preventDefault();} });
}());
