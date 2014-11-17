import os
import json
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
    'js': process_json_file(WEB_CONFIG_ROOT + 'mobile/js-manifest.json'),
    'css': process_json_file(WEB_CONFIG_ROOT + 'mobile/css-manifest.json'),
    'imgs': process_json_file(WEB_CONFIG_ROOT + 'mobile/imgs-manifest.json'),
}


@register.filter
def mobile(value):
    flag = ('SERVER_SOFTWARE' in os.environ) or ('TEST_SERVER' in os.environ)
    cdn = CDN_ROOT if (flag or CDN_TEST) else ''
    production = '' if (flag or CDN_TEST) else 'static/mobile/prod/'

    if flag or PROD_TEST or CDN_TEST:
        arr = value.strip().split('/')
        prefix = arr[0]
        del arr[0]
        basename = '/'.join(arr)

        try:
            manifest = manifest_map[prefix]
            path = prefix + '/' + manifest[basename]
        except:
            path = value

        return cdn + '/' + production + '/' + path
    else:
        return '/static/mobile/assets/' + value
