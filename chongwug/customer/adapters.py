import os,json,string
from chongwug.settings import WEB_CONFIG_ROOT

def processJsonFile(inputJsonFile):  
    fin = open(inputJsonFile, 'r')
    s = fin.read()
    fin.close()
    return s

def web_configs():
    if 'SERVER_SOFTWARE' in os.environ:
        web_js =    processJsonFile(WEB_CONFIG_ROOT + "/js-manifest.json")
        web_css =   processJsonFile(WEB_CONFIG_ROOT + "/css-manifest.json")
        web_imgs = processJsonFile(WEB_CONFIG_ROOT + "/imgs-manifest.json")
    else:
        web_js =    processJsonFile(WEB_CONFIG_ROOT + "/local/js-manifest.json")
        web_css =   processJsonFile(WEB_CONFIG_ROOT + "/local/css-manifest.json")
        web_imgs = processJsonFile(WEB_CONFIG_ROOT + "/local/imgs-manifest.json")
    web_config = {
                  'js':web_js,
                  'css':web_css,
                  'imgs':web_imgs
                 }
    return web_config