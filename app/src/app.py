# -*- coding: utf-8 -*-
from logging import getLogger, config, StreamHandler, DEBUG
import os

# import sys
from logutil import LogUtil
# from importenv import ImportEnvKeyEnum
# import importenv as setting

from util.sample import Util

import json

PYTHON_APP_HOME = os.getenv('PYTHON_APP_HOME')
LOG_CONFIG_FILE = ['config', 'log_config.json']

logger = getLogger(__name__)
log_conf = LogUtil.get_log_conf(os.path.join(PYTHON_APP_HOME, *LOG_CONFIG_FILE))
config.dictConfig(log_conf)
handler = StreamHandler()
handler.setLevel(DEBUG)
logger.setLevel(DEBUG)
logger.addHandler(handler)
logger.propagate = False

# composer.lockのパス
COMPOSER_LOCK_PATH = os.path.join(PYTHON_APP_HOME, *['file', 'composer.lock'])

# 出力先
OUTPUT_FILE_PATH = os.path.join(PYTHON_APP_HOME, *['file', 'result.tsv'])

if __name__ == '__main__':
    # .envの取得
    # setting.ENV_DIC[ImportEnvKeyEnum.importenvに書いた値.value]
    
    # 起動引数の取得
    # args = sys.argv
    # args[0]はpythonのファイル名。
    # 実際の引数はargs[1]から。

    with open(COMPOSER_LOCK_PATH, mode='r') as f:
        composer = json.loads(f.read())

    packages = composer['packages']

    packages_keys = ['name', 'version', 'require-dev']    
    with open(OUTPUT_FILE_PATH, mode='w') as f:
        f.write('\t'.join(packages_keys) + "\r\n")
        for item in packages:
            for key, value in item.get(packages_keys[2], {'-':'-'}).items():
                f.write('{}\t{}\t{}\t{}\r\n'.format(item[packages_keys[0]], item[packages_keys[1]], key, value))
            
    
