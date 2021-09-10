import logging
from logging.config import dictConfig

#ch = logging.StreamHandler()
#ch.setLevel(logging.DEBUG) # 指定被处理的信息级别为最低级DEBUG，低于level级别的信息将被忽略
#logger = logging.getLogger()
#logger.setLevel(logging.DEBUG)
#logger.addHandler(ch)
logging_config = {
        'version': 1,
        'formatters': {
            'default': {
                #'format': #'%(asctime)s %(name)-12s %(levelname)-8s %(message)s'%(asctime)s [%(name)s:%(lineno)d] '
                'format':'%(asctime)s [%(name)s] [%(module)s:%(funcName)s:%(lineno)d] [%(levelname)s]- %(message)s'                },
            'simple': {
                'format': '%(asctime)s %(levelname)-8s %(message)s'
                }
            },
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
                'formatter': 'default',
                'level': logging.DEBUG
                },
            'simple_console': {
                'class': 'logging.StreamHandler',
                'formatter': 'simple',
                'level': logging.WARNING
                }
            },
        'loggers': {
            '': {
                'handlers': ['console'],
                'level': logging.DEBUG,
                },
            'simple': {
                'handlers': ['simple_console'],
                'level': logging.ERROR,
                'propagate': False,
                }
            },
        }
dictConfig(logging_config)
logger = logging.getLogger(__name__)
logger.debug('this is the debug log: %s', 'debug')
simple_logger = logging.getLogger('simple')
simple_logger.debug('this is the simplelog: %s', 'debug')

