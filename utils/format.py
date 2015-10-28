__author__ = 'wkguo'


def simple_params(params):
    entries = []
    for param in params:
        if isinstance(param[1], dict) or isinstance(param[1], list):
            entries.append((param[0], type(param[1])))
        elif (isinstance(param[1], basestring) or isinstance(param[1], unicode)) and len(param[1]) > 1024:
            entries.append((param[0], type(param[1])))
        else:
            if isinstance(param[1], str) and len(param[1]) > 0 and ord(max(param[1])) > 127:
                entries.append((param[0], type(param[1])))
            else:
                entries.append(param)
    return entries
