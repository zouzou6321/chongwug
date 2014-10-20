# -*- coding: UTF-8 -*-
from django.core import signals
from django.db import close_connection

# 取消信号关联，实现数据库长连接
signals.request_finished.disconnect(close_connection)