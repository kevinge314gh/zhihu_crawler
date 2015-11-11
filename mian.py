from db.mongo import *
from db.connection import connect
from settings import MONGO_IP, MONGO_PORT, ROOT_PATH, HEADERS
from crawler.login import set_cookie

import urllib, urllib2
import copy
import  json
import cookielib


if __name__ == '__main__':
    # crawler = crawler()
    # cnn = connect(host=MONGO_IP, port=MONGO_PORT)
    # people_infos = crawler.get_people_infos('linan')
    # print save_people_infos(people_infos, cnn.zhihu_crawler)
    # url = 'http://www.zhihu.com/node/ProfileFolloweesListV2'
    # data = {
    #     'method':'next',
    #     'params':{"offset":20,"order_by":"created","hash_id":"f9de84865e3e8455a09af78bfe4d1da5"}
    #     '_xsrf':'327696efedfd4529121f81c7017cc593'
    #         }
    #set cookie
    cookie = set_cookie()
    cookie.save(ignore_discard=True, ignore_expires=True)
    url = 'http://www.zhihu.com/people/zhang-jia-wei/followees'
    request = urllib2.Request(url = url, headers=HEADERS)
    response = urllib2.urlopen(request, timeout=1)
    cookie = set_cookie()
    cookie.save(ignore_discard=True, ignore_expires=True)

    url = 'http://www.zhihu.com/node/ProfileFolloweesListV2'
    data = {
        'method':'next',
        'params':{"offset":60,"order_by":"created","hash_id":"f9de84865e3e8455a09af78bfe4d1da5"},
        '_xsrf':'327696efedfd4529121f81c7017cc593'
            }
    cookie= {
        '_xsrf':'327696efedfd4529121f81c7017cc593',
        'cap_id':'MzE5NDNhMjk5ZGUxNDVjOGE1MjdiMGU0OWY4NWE2NGE=|1447144327|c8ff179a25d92c46a9feb20932ecc113af968d6a',
        'z_c0':'QUFEQUxSRWFBQUFYQUFBQVlRSlZUYmM0YVZZQ05SSlpDVE5VcGhtRjF2ZHJKOW9NWE1FclFnPT0=|1447144375|6af54804f83075343dcd0d829c8498b6dd9a999e'
    }
    HEADERS2 = {'User-Agent' : ' Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36',
           'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
           'Host': 'www.zhihu.com',
           'Connection': 'keep-alive',
           'Content-Length': 171,
           'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
           'Accept': '*/*',
           'X-Requested-With': 'XMLHttpRequest',
           'Origin': 'http://www.zhihu.com',
           'Referer':'http://www.zhihu.com',
            # 'Cookie':cookie
           # 'Cookie':"_xsrf=327696efedfd4529121f81c7017cc593;cap_id='MzE5NDNhMjk5ZGUxNDVjOGE1MjdiMGU0OWY4NWE2NGE=|1447144327|c8ff179a25d92c46a9feb20932ecc113af968d6a';z_c0='QUFEQUxSRWFBQUFYQUFBQVlRSlZUYmM0YVZZQ05SSlpDVE5VcGhtRjF2ZHJKOW9NWE1FclFnPT0=|1447144375|6af54804f83075343dcd0d829c8498b6dd9a999e'"
           }

    # cookie = "_xsrf=327696efedfd4529121f81c7017cc593;cap_id=MzE5NDNhMjk5ZGUxNDVjOGE1MjdiMGU0OWY4NWE2NGE=|1447144327|c8ff179a25d92c46a9feb20932ecc113af968d6a;z_c0=QUFEQUxSRWFBQUFYQUFBQVlRSlZUYmM0YVZZQ05SSlpDVE5VcGhtRjF2ZHJKOW9NWE1FclFnPT0=|1447144375|6af54804f83075343dcd0d829c8498b6dd9a999e"
    cookie = urllib.urlencode(cookie)
    data = urllib.urlencode(data)
    # data=json.dumps(data)

    request = urllib2.Request(url = url, data=data, headers=HEADERS)
    response = urllib2.urlopen(request, timeout=100)
    print response


