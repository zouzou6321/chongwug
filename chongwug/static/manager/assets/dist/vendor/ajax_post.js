$("html").ajaxSend(function(t,e,n){function o(t){var e=null;if(document.cookie&&""!=document.cookie)for(var n=document.cookie.split(";"),o=0;o<n.length;o++){var r=jQuery.trim(n[o]);if(r.substring(0,t.length+1)==t+"="){e=decodeURIComponent(r.substring(t.length+1));break}}return e}/^http:.*/.test(n.url)||/^https:.*/.test(n.url)||e.setRequestHeader("X-CSRFToken",o("csrftoken"))});