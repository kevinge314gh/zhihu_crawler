#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'wkguo'

import json,cookielib
import logging


from settings import *
from utils.format import *
from bs4 import BeautifulSoup
from lxml.html.clean import Cleaner
from datetime import datetime

_LOGGER = logging.getLogger('zhihu_crawler')


def load_cookie():
    #load cookie
    cookie = cookielib.MozillaCookieJar()
    #从文件中读取cookie内容到变量
    cookie.load('%s/data/cookie.txt'%ROOT_PATH, ignore_discard=True, ignore_expires=True)
    handler = urllib2.HTTPCookieProcessor(cookie)
    opener = urllib2.build_opener(handler, urllib2.HTTPHandler)
    urllib2.install_opener(opener)


def get_html(url, max_try_count=3):
    resp = download(url, max_try_count)
    html = resp.read()
    cleaner = Cleaner(
        scripts=False, javascript=False, comments=True,
        style=False, links=True, meta=False, add_nofollow=False,
        page_structure=False, processing_instructions=True, embedded=False,
        frames=False, forms=False, annoying_tags=False, remove_tags=None,
        remove_unknown_tags=False, safe_attrs_only=False)
    html = cleaner.clean_html(html)
    f = open('%s/data/html.txt' % ROOT_PATH, 'w')
    f.write(html)
    f.close()
    return html


def download(url, max_try_count):
    _LOGGER.debug('Start download %s at %s' % (url, datetime.now()))
    try_count = 1
    while try_count <= max_try_count:
        try:
            load_cookie()
            request = urllib2.Request(url = url, headers=HEADERS)
            header = request.get_full_url()
            response = urllib2.urlopen(request, timeout=10)
            if response is None:
                _LOGGER.warning('Empty response for head request, url: %s' % url)
                try_count += 1
                print 'try again----\n [url]%s' % url
                continue
            return response
        except urllib2.HTTPError as err:
            _LOGGER.warning('Download http request failed url=%s, Exception: %s', url, err)
            try_count += 1
            print 'try again----\n [url]%s' % url
            continue


def get_followees_dynamic(followees_num, hash_id, _xsrf):
    #page_num:动态刷新次数，每次20条
    page_num = int(followees_num) / 20
    rt = []
    for idx in range(page_num + 1):
        offset = idx * 20
        data = {"method":"next", "params":{"offset":'$%s$' % str(offset),"order_by":"created","hash_id":hash_id}, "_xsrf":_xsrf}
        post_data = filter_urlencode(urllib.urlencode(data))
        request = urllib2.Request(url = URL_FOLLOWEES_DYNAMIC, data=post_data, headers=HEADERS)
        response = urllib2.urlopen(request, timeout=10)
        json_data = json.loads(response.read(), encoding='utf-8')
        data_list = json_data.get('msg', None)
        if data_list is None:
            continue
        for dt in data_list:
            soup = BeautifulSoup(dt, 'lxml')
            display_name = soup.find('a', class_='zm-item-link-avatar')['title']
            p_name = soup.find('a', class_='zm-item-link-avatar')['href'].split('/')[2]
            details = soup.find_all('a', class_='zg-link-gray-normal')
            followers_num = details[0].string.split(' ')[0]
            asks_num = details[1].string.split(' ')[0]
            answers_num = details[2].string.split(' ')[0]
            agree_num = details[3].string.split(' ')[0]
            followee_infos = {
                'p_name':p_name,
                'display_name':display_name,
                'agree_num':int(agree_num),
                'asks_num':int(asks_num),
                'answers_num':int(answers_num),
                'followers_num':int(followers_num),
            }
            rt.append(followee_infos)
    return rt
