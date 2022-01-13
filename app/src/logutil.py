# -*- coding: utf-8 -*-
import json
import os

PYTHON_APP_HOME = os.getenv('PYTHON_APP_HOME')

class LogUtil:
  
  @classmethod
  def get_log_conf(cls, log_conf_path):
    """ ログ設定ファイルを読み込む
    """
    with open(log_conf_path, mode='r') as f:
      log_conf = json.loads(f.read())
      # Docker環境以外の場合コメントを外す。
      # log_conf['handlers']['fileHandler']['filename'] = PYTHON_APP_HOME + '/log/app.log'

    return log_conf
