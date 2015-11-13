#!/usr/bin/env python
# -*- coding:utf-8 -*-

import urllib, urllib2
import re


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

def data_quote_plus(data):
    k_v_list = []
    if isinstance(data, dict):
        for (k, v) in data.items():
            v, v_isdict = data_quote_plus(v) #递归解析dict中的dict
            if v_isdict:
                k_v = k + '=' + v
            else:
                k_v = k + '=' + urllib.quote_plus(v)
            k_v_list.append(k_v)
        rt = '&'.join(k_v_list)
        return rt, 1
    else:
        return data, 0

#urllib.urlencode转换结果后的处理
def filter_urlencode(encode_data):
    #3A+替换为3A, 2C+替换为2C，即去掉+
    encode_data = re.sub('\+', '', encode_data)
    #%27替换为%22
    encode_data = re.sub('%27', '%22', encode_data)
    #%22%2420%24%22是'$20$'的转码，只需要整数20，因为urlencode无法直接处理整数
    encode_data = re.sub('%22%24', '', encode_data)
    encode_data = re.sub('%24%22', '', encode_data)
    return encode_data

