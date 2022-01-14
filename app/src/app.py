# -*- coding: utf-8 -*-
from logging import getLogger, config, StreamHandler, DEBUG
import os

import sys
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

FILE_HOME = os.path.join(PYTHON_APP_HOME, *['file'])

KEYS = ['name', 'version', 'require-dev', 'require-dev-version']
SUB_KEYS = ['packages', 'packages-dev']

def output(filepath, dic, keys, mode='w'):
    with open(filepath, mode=mode) as f:
        f.write('\t'.join(keys) + "\r\n")
        for item in dic:
            for key, value in item.get(keys[2], {'-':'-'}).items():
                f.write('{}\t{}\t{}\t{}\r\n'.format(item[keys[0]], item[keys[1]], key, value))
    
if __name__ == '__main__':
    # .envの取得
    # setting.ENV_DIC[ImportEnvKeyEnum.importenvに書いた値.value]
    
    # 起動引数の取得
    args = sys.argv
    # args[0]はpythonのファイル名。
    # 実際の引数はargs[1]から。
    args_index = 1

    COMPOSER_LOCK_PATH = os.path.join(FILE_HOME, *[args[args_index]]) ; args_index += 1
    filename_format = args[args_index] ; args_index += 1

    with open(COMPOSER_LOCK_PATH, mode='r') as f:
        composer = json.loads(f.read())

    for i in range(len(SUB_KEYS)):
        output(
            os.path.join(FILE_HOME, *[filename_format.format(SUB_KEYS[i])]),
            composer[SUB_KEYS[i]],
            KEYS,
            mode=('w' if i == 0 else 'a')
        )
    
