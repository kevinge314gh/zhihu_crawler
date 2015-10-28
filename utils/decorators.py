__author__ = 'wkguo'

from functools import wraps
from time import time
from status import StatusBase, InternalError, ErrorCode
import logging
import sys
import  traceback

_LOGGER = logging.getLogger('douban_crawler.perf')

def performance(method):
    '''Decorate methods with this to handle performance logging
    '''
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        '''performance wrapper
        '''
        start_time = time()
        try:
            return method(self, *args, **kwargs)
        except:
            raise
        finally:
            message = 'path=%s, get =%s, post =%s, %.4f ms' % (
                self.request.path,
                self.request.query,
                self.request.body,
                (time() - start_time) * 1000
            )
            _LOGGER.info(message)
    return wrapper

def exception(method):
    '''Decorate methods with this to handle exception
    '''
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        '''exception wrapper
        '''
        try:
            return method(self, *args, **kwargs)
        except StatusBase as error:
            message = '%s: path=%s get=%s post=%s' % (
                error.message,
                self.request.path,
                self.request.query,
                self.request.body,
            )
            _LOGGER.warning(message)
            error.emit(self)
        except Exception:
            exc_type, value, detail = sys.exc_info()
            formatted_tb = traceback.format_tb(detail)
            message = '%s: %s traceback=%s path=%s get=%s post= %s' %(
                exc_type,
                value,
                formatted_tb,
                self.request.path,
                self.request.query,
                self.request.body,
            )
            _LOGGER.exception(message)
            error = InternalError(ErrorCode.INTERNAL_UNKNOWN_ERROR, 'unknown error ocuured')
            error.emit(self)
    return wrapper
