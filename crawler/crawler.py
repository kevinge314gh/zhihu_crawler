__author__ = 'kevin'
import urllib2
import cookielib

from settings import ROOT_PATH,HEADERS,URL_PEOPLE

def get_html(self, url):
        cookie = cookielib.MozillaCookieJar()
        cookie.load('%s/data/cookie.txt'%ROOT_PATH, ignore_discard=True, ignore_expires=True)
        handlder = urllib2.HTTPCookieProcessor(cookie)
        opener = urllib2.build_opener(handlder, urllib2.HTTPHandler)
        urllib2.install_opener(opener)

        request = urllib2.Request(url = url, headers=HEADERS)
        response = urllib2.urlopen(request)
        html = response.read()
        f = open('%s/data/html.txt' % ROOT_PATH, 'w')
        f.write(html)
        f.close()
        return html

class crawler(object):


    def get_people_infos(self, p_name):
        url = URL_PEOPLE + p_name
        html = get_html(self, url)
        people_info = {}

        return people_info


    def get_followees(self, html):
        pass

    def get_followers(self, html):
        pass

    def get_answers(self, html):
        pass

    def get_posts(self, html):
        pass

    def get_posts(self,html):
        pass

    def get_collections(self, html):
        pass

    def get_logs(self, html):
        pass

    def get_columns_followed(self, html):
        pass

    def get_topics(self, html):
        pass




if __name__ == '__main__':
    crawler = crawler()
    html = crawler.get_html(url='http://www.zhihu.com/people/zhang-jia-wei')
    print html



