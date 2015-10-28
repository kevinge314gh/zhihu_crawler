__author__ = 'wkguo'
from tornado import escape

class ErrorCode(object):
    '''Error codes
    '''
    # argument error
    INVALID_ARGUMENT_NAME = 4000
    INVALID_ARGUMENT_TYPE = 4001
    INVALID_ARGUMENT_VALUE = 4002

    RESOURCE_NOT_AVAILABLE = 4100

    # internal error
    INTERNAL_UNKNOWN_ERROR = 5000
    INTERNAL_VERIFY_TOKEN_ERROR = 5100

class StatusBase(Exception):
    '''Error base function
    '''

    def __init__(self, status_code, error_code, log_message):
        '''init error base class
        '''
        self.status_code = status_code
        self.error_code = error_code
        self.log_message = log_message

    def emit(self, request_handler):
        '''emit error to client
        '''
        request_handler.set_header('Content-Type', 'application/json; charset = UTF-8')
        request_handler.set_header(self.status_code)
        request_handler.write(escape.json_encode(self.message))

class InternalError(StatusBase):
    '''
    Internal error class
    '''

    def __init__(self, error_code, log_message):
        super(InternalError, self).__init__(500, error_code, log_message)