import os
import sys
import jinja2
import logging
import tempfile
import subprocess

logger = logging.getLogger(__name__)

# javascript to pass to node and take a screen shot
JS_TEMPLATE_FILE=os.path.join(os.path.dirname(sys.argv[0]), 'js/screen.js')

def build(url, timeout=5000):
    js_tmp = tempfile.mkstemp(prefix='script.', suffix='.js', dir='.')[-1]
    img_tmp = tempfile.mkstemp(prefix='screen.', suffix='.png', dir='.')[-1]
    script = jinja2.Template(open(JS_TEMPLATE_FILE, 'rb').read().decode())
    rendered = script.render(url=url, image=img_tmp, timeout=timeout)
    open(js_tmp, 'wb').write(rendered.encode())
    return js_tmp, img_tmp

def run(script_path, node_path='node'):
    cmd = [node_path, script_path]
    logger.debug('Running script: {}'.format(' '.join(cmd)))
    try:
        subprocess.check_call(cmd)
    except:
        return False
    return True
