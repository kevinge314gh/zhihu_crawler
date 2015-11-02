__author__ = 'wkguo'

from logging import config

MONGO_IP = '127.0.0.1'
MONGO_PORT = 27017

HEADERS = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:14.0) Gecko/20100101 Firefox/14.0.1',
                   'Referer' : 'http:www.zhihu.com'}

'''PATH'''
ROOT_PATH = 'D:\github\zhihu_crawler'

'''URL'''
URL = 'http://www.zhihu.com'
URL_PEOPLE = 'http://www.zhihu.com/people/'


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'detail': {
            'format': '%(asctime)s %(levelname)s %(module)s %(message)s'
        },
        'message_only': {
            'format': '%(asctime)s %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(asctime)s %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'file': {
            'level': 'INFO',
            'class': 'logging.handlers.WatchedFileHandler',
            'formatter': 'detail',
            'filename': '/tmp/zhihu_crawler.log',
        },
        'perf': {
            'level': 'DEBUG',
            'class': 'logging.handlers.WatchedFileHandler',
            'formatter': 'message_only',
            'filename': '/tmp/zhihu_crawler_perf.log',
        },
        'err': {
            'level': 'ERROR',
            'class': 'logging.handlers.WatchedFileHandler',
            'formatter': 'detail',
            'filename': '/tmp/zhihu_crawler.erro',
        },
    },
    'loggers': {
        'zhihu_crawler': {
            'handlers': ['file', 'err'],
            'level': 'INFO',
        },
        'zhihu_crawler.perf': {
            'handlers': ['perf'],
            'level': 'DEBUG',
        },
        'default': {
            'handlers': ['file', 'err'],
            'level': 'INFO',
        },
    }
}

config.dictConfig(LOGGING)
