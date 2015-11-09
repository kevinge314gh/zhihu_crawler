# -*- coding:utf-8 -*-
__author__ = 'kevin'

import libxml2
import urllib2
import cookielib
import lxml.html as html
import lxml.etree as etree
import json

from settings import ROOT_PATH,HEADERS,URL_PEOPLE
from lxml.html.clean import Cleaner
from BeautifulSoup import UnicodeDammit
from BeautifulSoup import BeautifulSoup
from bs4 import BeautifulSoup

def get_html( url):
        cookie = cookielib.MozillaCookieJar()
        cookie.load('%s/data/cookie.txt'%ROOT_PATH, ignore_discard=True, ignore_expires=True)
        handlder = urllib2.HTTPCookieProcessor(cookie)
        opener = urllib2.build_opener(handlder, urllib2.HTTPHandler)
        urllib2.install_opener(opener)

        request = urllib2.Request(url = url, headers=HEADERS)
        response = urllib2.urlopen(request)
        html = response.read()
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



class crawler(object):


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






if __name__ == '__main__':
    crawler = crawler()
    # html = get_html(url='http://www.zhihu.com/people/zhouyuan')
    # soup = BeautifulSoup(html, 'lxml')
    # soup_header = soup.find('div', class_ = 'zm-profile-header')
    # soup_sidebar = soup.find('div', class_ = 'zu-main-sidebar')
    # name = soup_header.find('span', class_ = 'name')
    # agree = soup_header.find('span', class_ = 'zm-profile-header-user-agree').strong.string
    # asks = soup_header.find('a', href = '/people/zhouyuan/asks').span.string

    people_infos = crawler.get_people_infos('zhouyuan')

    for k, v in people_infos.items():
        print k, ':', v




