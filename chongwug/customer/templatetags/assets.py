import os,json,string
from django import template
from chongwug.settings import WEB_CONFIG_ROOT, PROD_TEST

register = template.Library()


def process_json_file(json_file):
    fin = open(json_file, 'r')
    s = json.loads(fin.read())
    fin.close()
    return s


@register.filter
def assets(value):
    flag = 'SERVER_SOFTWARE' in os.environ

    if flag or PROD_TEST:
        arr = value.strip().split('/')
        prefix = arr[0]
        del arr[0]
        basename = '/'.join(arr)
        manifest = process_json_file(WEB_CONFIG_ROOT + '/' + prefix + '-manifest.json')

        try:
            path = prefix + '/' + manifest[basename]
        except:
            path = value

        return '/prod/assets/' + path
    else:
        return '/assets/' + value