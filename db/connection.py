__author__ = 'wkguo'

from pymongo import Connection
from settings import LOGGING

_CONNECTIONS = {}

def connect(host, port=None, replset=None):
    '''
    Connect to the database
    '''
    assert host, 'host of the database server may not null'
    port = port or 27017
    key = (host, port, replset)
    conn = None
    if key in _CONNECTIONS:
        conn = _CONNECTIONS[key]
    else:
        if replset:
            pass  #cluster db
        else:
            conn = Connection(host, port)
        _CONNECTIONS[key] = conn
    return conn

class ConnectionPool(dict):

    def __getitem__(self, key):
        if key not in self:
            raise Exception('Connections pool error, key not configure: %s' % key)
        else:
            return super(ConnectionPool, self).__getitem__(key)



if __name__ == '__main__':
    n = LOGGING
    cnn = connect('172.16.77.53', port=27017,)
    print cnn.is_locked