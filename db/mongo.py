__author__ = 'wkguo'


from connection import connect
import logging
from utils.decorators import exception
from pymongo import MongoClient

_LOGGER = logging.getLogger('zhihu_crawler')

# @exception
def config_mongodb(host, port):
    '''Config mongodb instance
    '''
    db = None
    try:
        db = MongoClient(host,port).get_default_database()
        _LOGGER.info('config mongodb ok: %s, %s' % host % port)
    except Exception as ex:
        _LOGGER.error('config mongodbfailed: %s %s %s' % (ex, host, port))
    return db

if __name__ == '__main__':
    db = config_mongodb(host='172.16.77.53', port=27017)
    print db




