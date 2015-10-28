__author__ = 'wkguo'

from connection import ConnectionPool, connect

DBS = {}

def config(module, servers, replset=None):
    assert servers is not None and type(servers) is dict, 'servers must be a dict'
    name = module.__name__
    DBS[name] = ConnectionPool()
    for key, value in servers.items():
        repl = None
        if replset is not None and type(replset) is dict and key in replset:
            repl = replset[key]
        conn = connect(value['host'], value['port'], replset=repl)
        DBS[name] = conn[value['db']]

