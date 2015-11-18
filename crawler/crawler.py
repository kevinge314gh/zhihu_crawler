# -*- coding:utf-8 -*-
__author__ = 'kevin'

import libxml2
import urllib2
import urllib
import cookielib
import lxml.html as html
import lxml.etree as etree
import json
import logging
import requests
import copy
import re

from settings import ROOT_PATH,HEADERS,URL_PEOPLE
from lxml.html.clean import Cleaner
from BeautifulSoup import UnicodeDammit
from BeautifulSoup import BeautifulSoup
from bs4 import BeautifulSoup
from datetime import datetime
from utils.format import filter_urlencode

_LOGGER = logging.getLogger('zhihu_crawler')


def load_cookie():
    #load cookie
    cookie = cookielib.MozillaCookieJar()
    #从文件中读取cookie内容到变量
    cookie.load('%s/data/cookie.txt'%ROOT_PATH, ignore_discard=True, ignore_expires=True)
    handler = urllib2.HTTPCookieProcessor(cookie)
    opener = urllib2.build_opener(handler, urllib2.HTTPHandler)
    urllib2.install_opener(opener)

def download(url, max_try_count):

    _LOGGER.debug('Start download %s at %s' % (url, datetime.now()))
    try_count = 1
    while try_count <= max_try_count:
        try:
            load_cookie()
            request = urllib2.Request(url = url, headers=HEADERS)
            header = request.get_full_url()
            print header
            response = urllib2.urlopen(request, timeout=3)
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

def get_html(url, max_try_count=2):
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


class Crawler(object):


    def get_people_infos(self, p_name):
        url = URL_PEOPLE + p_name
        people_url = '/people/' + p_name
        html = get_html(url)
        soup = BeautifulSoup(html, 'lxml')
        soup_header = soup.find('div', class_ = 'zm-profile-header')
        soup_sidebar = soup.find('div', class_ = 'zu-main-sidebar')
        display_name = soup_header.find('span', class_ = 'name').string
        bio = soup_header.find('span', class_ = 'bio').string
        agree = soup_header.find('span', class_ = 'zm-profile-header-user-agree').strong.string
        thanks = soup_header.find('span', class_ = 'zm-profile-header-user-thanks').strong.string
        asks = soup_header.find('a', href = people_url + '/asks').span.string
        answers = soup_header.find('a', href = people_url + '/answers').span.string
        posts = soup_header.find('a', href = people_url + '/posts').span.string
        collections = soup_header.find('a', href = people_url + '/collections').span.string
        logs = soup_header.find('a', href = people_url + '/logs').span.string

        followees = soup_sidebar.find('a', href = people_url + '/followees').strong.string
        followers = soup_sidebar.find('a', href = people_url + '/followers').strong.string
        columns_followed = soup_sidebar.find('a', href = people_url + '/columns/followed').strong.string
        topics = soup_sidebar.find('a', href = people_url + '/topics').strong.string

        people_info = {
            'p_name':p_name,
            'display_name':display_name,
            'bio':bio,
            'agree_num':int(agree),
            'thanks_num':int(thanks),
            'asks_num':int(asks),
            'answers_num':int(answers),
            'posts_num':int(posts),
            'collections_num':int(collections),
            'logs_num':int(logs),
            'followees_num':int(followees),
            'followers_num':int(followers),
            'columns_followed_num':columns_followed,
            'topic_num':topics,
        }

        return people_info

    def get_followees(self, p_name):
        url = URL_PEOPLE + p_name + '/followees'
        html = get_html(url, max_try_count=3)
        hash_id = re.findall(r'data-init=.*\"hash_id\": \"(.*?)\"}, .*', html)[0]
        _xsrf = re.findall(r'<input.*name=\"_xsrf\" value=\"(.*?)\">', html)
        soup = BeautifulSoup(html, 'lxml')
        soup_list = soup.find_all('div', class_='zm-profile-card')
        for soup in soup_list:
            print soup.find('a', class_='zg-link-gray-normal').string
        data = {"method":"next", "params":{"offset":'$20$',"order_by":"created","hash_id":hash_id}, "_xsrf":_xsrf}
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
        post_data = filter_urlencode(urllib.urlencode(data))
        print post_data
        load_cookie()
        request = urllib2.Request(url = url, data=post_data, headers=HEADERS2)
        response = urllib2.urlopen(request, timeout=3)
        print response.read()


if __name__ == '__main__':

    crawler = Crawler()
    # people_infos = crawler.get_people_infos('zhang-jia-wei')
    crawler.get_followees('zhang-jia-wei')
    # print people_infos




