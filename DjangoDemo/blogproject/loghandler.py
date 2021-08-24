import logging


ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG) # 指定被处理的信息级别为最低级DEBUG，低于level级别的信息将被忽略
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logger.addHandler(ch)
