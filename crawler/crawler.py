#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'kevin'

from crawler import *
from settings import *



def get_people_infos(p_name):
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


def get_followees(p_name):
    url = URL_PEOPLE + p_name + '/followees'
    html = get_html(url, max_try_count=3)
    hash_id = re.findall(r'data-init=.*\"hash_id\": \"(.*?)\"}, .*', html)[0]
    _xsrf = re.findall(r'<input.*name=\"_xsrf\" value=\"(.*?)\">', html)[0]
    soup = BeautifulSoup(html, 'lxml')
    followees_num =  soup.find('a', class_='item', href='/people/' + p_name + '/followees').strong.string
    followees_list = get_followees_dynamic(followees_num, hash_id, _xsrf)
    for followee in followees_list:
        print followee
    print len(followees_list)





if __name__ == '__main__':

    get_followees('guo-wen-kai-69')
    # print people_infos