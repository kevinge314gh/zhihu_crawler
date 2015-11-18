#!/usr/bin/env python
# -*- coding:utf-8 -*-
# from db.mongo import *
# from db.connection import connect
from settings import MONGO_IP, MONGO_PORT, ROOT_PATH, HEADERS
from crawler.login import set_cookie
from cookielib import Cookie, CookieJar
from utils.format import filter_urlencode

import urllib, urllib2
import copy
import  json
import cookielib
import re






if __name__ == "__main__":

    url = "http://www.zhihu.com/node/ProfileFolloweesListV2"
    data = {"method":"next",
            "params":{"offset":'$20$',"order_by":"created","hash_id":"f9de84865e3e8455a09af78bfe4d1da5"},
            "_xsrf":"d5d81a63cdfdc885a0600a5045b6e865"}
    param = data['params']
    HEADERS2 = {"User-Agent" : "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36",
                "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                "Host": "www.zhihu.com",
                "Connection": "keep-alive",
                "Content-Length": 171,
                "Accept-Language": "zh-CN,zh;q=0.8,en;q=0.6",
                "Accept-Encoding": "gzip, deflate",
                "Accept": "*/*",
                "X-Requested-With": "XMLHttpRequest",
                "Origin": "http://www.zhihu.com",
                "Referer":" http://www.zhihu.com/",
           }
    cookie = '_za=71e81c06-589d-46b1-a8ed-ef692345a11c; __utma=51854390.998027989.1447818923.1447818923.1447831543.2; __utmc=51854390; __utmz=51854390.1447831543.2.2.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/people/zhang-jia-wei/followees; __utmv=51854390.100-2|2=registration_date=20150916=1^3=entry_date=20150916=1; q_c1=0bf4b6a004aa414b9548728d67bf6573|1447819061000|1447819061000; cap_id="MWFhM2ZkYWY5ZGMzNGExMWExNTQ0NWNlNDM5MWQwZjY=|1447819061|9f2d08054e374fea4d2a390185f3a2d89398c336"; z_c0="QUJDS2VSNkJ0UWdYQUFBQVlRSlZUVHVFYzFhdkpCQklsZV91SUxaNlJxREJwMmJKNWJVTHNRPT0=|1447819067|c5e2e55f748e4c30ee2ad905f08dce27b8a5c7c7"; _xsrf=d5d81a63cdfdc885a0600a5045b6e865; __utmb=51854390.4.10.1447831543'
    post_data = filter_urlencode(urllib.urlencode(data))
    request = urllib2.Request(url = url, data=post_data, headers=HEADERS2)
    request.add_header("Cookie", cookie)
    response = urllib2.urlopen(request, timeout=3)
    print response.read()








