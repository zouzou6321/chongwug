import os, json, string
from django import template

register = template.Library()


def process_json_file(json_file):
    fin = open(json_file, 'r')
    s = json.loads(fin.read())
    fin.close()
    return s


@register.filter
def assets_petfarm(value):
    # config
    root = '/static/'
    curr = 'petfarm/'
    flag = 'SERVER_SOFTWARE' in os.environ
    cdn = False
    prod = False
    folder = '/static/petfarm/assets/dist/' if prod else ''
    cdn_url = '//chongwug-cdn.b0.upaiyun.com' if flag or cdn else ''
    js_version = '?v2'
    css_version = '?v1'
    img_version = '?v1'
    version = ''
    path = ''

    if value.endswith('.css'):
        version = css_version
    elif value.endswith('.js'):
        version = js_version
    else:
        version = img_version

    if prod:
        path = folder + value + version
    else:
        path = cdn_url + '/' + curr + folder + value + version

    if flag or prod or cdn:
        return path
    else:
        return root + curr + 'assets/dev/' + value + version
