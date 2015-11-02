__author__ = 'wkguo'


from connection import connect
import logging
from utils.decorators import exception

_LOGGER = logging.getLogger('zhihu_crawler')

# @exception
def config_mongodb(host, port):
    '''Config mongodb instance
    '''
    db = None
    try:
        db = connect(host, port)
        _LOGGER.info('config mongodb ok: %s, %s' % host % port)
    except Exception as ex:
        _LOGGER.error('config mongodbfailed: %s %s %s' % (ex, host, port))
    return db

if __name__ == '__main__':
    db = config_mongodb(host='172.16.77.53', port=27017)
    re = db.weibo_ru_ru.user.find({})
    re = [r for r in re]
    print re




