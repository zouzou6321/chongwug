import os
import json
import time
from django import template
from chongwug.settings import WEB_CONFIG_ROOT, PROD_TEST, CDN_TEST, CDN_ROOT

register = template.Library()


def process_json_file(json_file):
    try:
        fin = open(json_file, 'r')
        s = json.loads(fin.read())
        fin.close()
    except:
        s = {}
    return s

manifest_map = {
    'js': process_json_file(WEB_CONFIG_ROOT + '/manage/js-manifest.json'),
    'css': process_json_file(WEB_CONFIG_ROOT + '/manage/css-manifest.json'),
    'imgs': process_json_file(WEB_CONFIG_ROOT + '/manage/imgs-manifest.json'),
}


@register.filter
def assets_manage(value):
    flag = ('SERVER_SOFTWARE' in os.environ) or ('TEST_SERVER' in os.environ)
    cdn = True if (flag or CDN_TEST) else False
    cdnUrl = CDN_ROOT if cdn else '/static'
    dist = 'dist/' if PROD_TEST else ''
    folder = 'manage/'

    arr = value.strip().split('/')
    prefix = arr[0]
    del arr[0]
    basename = '/'.join(arr)

    if 'jquery.uploadify.js' in value:
        value = value + '?random=' + str(time.time())
        basename = basename + '?random=' + str(time.time())

    if cdn or PROD_TEST:
        if prefix == 'lib':
            path = 'lib/' + dist + basename
        else:
            try:
                manifest = manifest_map[prefix]
                try:
                    path = folder + dist + prefix + '/' + manifest[basename]
                except:
                    path = folder + dist + value
            except:
                #patch for temp vendor folder
                path = folder + dist + value

        return cdnUrl + '/' + path
    else:
        if prefix == 'lib':
            path = 'lib/dist/' + basename
        else:
            path = folder + 'dev/' + value

        return '/static/' + path
