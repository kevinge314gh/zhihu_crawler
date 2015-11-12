#!/usr/bin/env python
# -*- coding:utf-8 -*-
from db.mongo import *
from db.connection import connect
from settings import MONGO_IP, MONGO_PORT, ROOT_PATH, HEADERS
from crawler.login import set_cookie
from cookielib import Cookie, CookieJar

import urllib, urllib2
import copy
import  json
import cookielib


if __name__ == "__main__":
    # crawler = crawler()
    # cnn = connect(host=MONGO_IP, port=MONGO_PORT)
    # people_infos = crawler.get_people_infos("linan")
    # print save_people_infos(people_infos, cnn.zhihu_crawler)
    # url = "http://www.zhihu.com/node/ProfileFolloweesListV2"
    # data = {
    #     "method":"next",
    #     "params":{"offset":20,"order_by":"created","hash_id":"f9de84865e3e8455a09af78bfe4d1da5"}
    #     "_xsrf":"327696efedfd4529121f81c7017cc593"
    #         }
    #set cookie
    # cookie = set_cookie()
    # url = "http://www.zhihu.com/people/zhang-jia-wei/followees"
    # request = urllib2.Request(url = url, headers=HEADERS)
    # response = urllib2.urlopen(request, timeout=10)
    # cookie.save(ignore_discard=True, ignore_expires=True)

    url = "http://www.zhihu.com/node/ProfileFolloweesListV2"
    data = {"method":"next",
            "params":{"offset":20,"order_by":"created","hash_id":"f9de84865e3e8455a09af78bfe4d1da5"},
            "_xsrf":"327696efedfd4529121f81c7017cc593"}
    cookie= {
        "_xsrf":"327696efedfd4529121f81c7017cc593",
        "cap_id":"MzE5NDNhMjk5ZGUxNDVjOGE1MjdiMGU0OWY4NWE2NGE=|1447144327|c8ff179a25d92c46a9feb20932ecc113af968d6a",
        "z_c0":"QUFEQUxSRWFBQUFYQUFBQVlRSlZUYmM0YVZZQ05SSlpDVE5VcGhtRjF2ZHJKOW9NWE1FclFnPT0=|1447144375|6af54804f83075343dcd0d829c8498b6dd9a999e"
    }
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

    # cookie = "_xsrf=327696efedfd4529121f81c7017cc593;cap_id=MzE5NDNhMjk5ZGUxNDVjOGE1MjdiMGU0OWY4NWE2NGE=|1447144327|c8ff179a25d92c46a9feb20932ecc113af968d6a;z_c0=QUFEQUxSRWFBQUFYQUFBQVlRSlZUYmM0YVZZQ05SSlpDVE5VcGhtRjF2ZHJKOW9NWE1FclFnPT0=|1447144375|6af54804f83075343dcd0d829c8498b6dd9a999e"
    # cookie = urllib.urlencode(cookie)

    def quote_dict(v):
        if isinstance(v,dict):
            v = urllib.urlencode(v)
        return v
    data1 = "&".join([k+'='+urllib.quote_plus(quote_dict(v)) for (k,v) in data.items()])
    data = urllib.urlencode(data)
    # data = "&".join([k+'='+urllib.quote_plus(v) for (k,v) in data.items()])
    # print data
    # data=json.dumps(data)
    cookie = "_za=48c9299b-9303-45e5-8b14-524f3532d096; _ga=GA1.2.2042055099.1430719447; q_c1=72748956eca44e3c85f0e497476af63c|1445219490000|1428630306000; _xsrf=327696efedfd4529121f81c7017cc593; cap_id=NWM0MzUyMzdhYzRhNDU3NmI3NGRjYzZiZmJjM2JhN2U=|1447233570|a1417c024ca048968d9e6a3ab3cdca45f9c3837a; z_c0=QUJDS2VSNkJ0UWdYQUFBQVlRSlZUU3FWYWxhTFZlTkIwUGp4N2ktQkYyUjRWcUg4bVdlbC1nPT0=|1447233578|c48338967457e99145eee18e56e69ff62195e25a; __utmt=1; __utma=51854390.2042055099.1430719447.1447237315.1447316896.9; __utmb=51854390.6.10.1447316896; __utmc=51854390; __utmz=51854390.1447127358.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmv=51854390.100-2|2=registration_date=20150916=1^3=entry_date=20150410=1"
    print data1
    print data
    data = 'method=next&params=%7B%22offset%22%3A20%2C%22order_by%22%3A%22created%22%2C%22hash_id%22%3A%22f9de84865e3e8455a09af78bfe4d1da5%22%7D&_xsrf=327696efedfd4529121f81c7017cc593'
    request = urllib2.Request(url = url, data=data, headers=HEADERS2)
    request.add_header("Cookie", cookie)
    response = urllib2.urlopen(request, timeout=10)
    print response.read()


