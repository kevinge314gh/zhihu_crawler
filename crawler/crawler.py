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

from settings import ROOT_PATH,HEADERS,URL_PEOPLE
from lxml.html.clean import Cleaner
from BeautifulSoup import UnicodeDammit
from BeautifulSoup import BeautifulSoup
from bs4 import BeautifulSoup
from datetime import datetime

_LOGGER = logging.getLogger('zhihu_crawler')

def download(url, max_try_count):

    _LOGGER.debug('Start download %s at %s' % (url, datetime.now()))
    try_count = 1
    while try_count <= max_try_count:
        try:
            request = urllib2.Request(url = url, headers=HEADERS)
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

def get_html(url, max_try_count):
    resp = download(url, max_try_count)
    html = resp.read()
    cleaner = Cleaner(
        scripts=False, javascript=False, comments=True,
        style=False, links=True, meta=False, add_nofollow=False,
        page_structure=False, processing_instructions=True, embedded=False,
        frames=False, forms=False, annoying_tags=False, remove_tags=None,
        remove_unknown_tags=False, safe_attrs_only=False)
    html = cleaner.clean_html(html)
    # f = open('%s/data/html.txt' % ROOT_PATH, 'w')
    # f.write(html)
    # f.close()
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
        soup = BeautifulSoup(html, 'lxml')
        soup_list = soup.find('div', class_='zm-profile-section-list')







if __name__ == '__main__':


    url = 'http://www.zhihu.com/node/ProfileFolloweesListV2'
    data = {
        'method':'next',
        'params':{"offset":60,"order_by":"created","hash_id":"f9de84865e3e8455a09af78bfe4d1da5"},
        '_xsrf':'327696efedfd4529121f81c7017cc593'
            }
    headers = copy.deepcopy(HEADERS)

    # cookie= {
    #     '_xsrf':'327696efedfd4529121f81c7017cc593',
    #     'cap_id':'MzE5NDNhMjk5ZGUxNDVjOGE1MjdiMGU0OWY4NWE2NGE=|1447144327|c8ff179a25d92c46a9feb20932ecc113af968d6a',
    #     'z_c0':'QUFEQUxSRWFBQUFYQUFBQVlRSlZUYmM0YVZZQ05SSlpDVE5VcGhtRjF2ZHJKOW9NWE1FclFnPT0=|1447144375|6af54804f83075343dcd0d829c8498b6dd9a999e',
    # }
    # cookie = "_xsrf=327696efedfd4529121f81c7017cc593;cap_id=MzE5NDNhMjk5ZGUxNDVjOGE1MjdiMGU0OWY4NWE2NGE=|1447144327|c8ff179a25d92c46a9feb20932ecc113af968d6a;z_c0=QUFEQUxSRWFBQUFYQUFBQVlRSlZUYmM0YVZZQ05SSlpDVE5VcGhtRjF2ZHJKOW9NWE1FclFnPT0=|1447144375|6af54804f83075343dcd0d829c8498b6dd9a999e"
    # cookie = urllib.urlencode(cookie)
    # headers['Cookie'] = cookie
    # data = urllib.urlencode(data)

    request = urllib2.Request(url = url, data=json.dumps(data), headers=HEADERS)
    response = urllib2.urlopen(request, timeout=100)
    print response



