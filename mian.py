from crawler.crawler import crawler
from db.mongo import *
from db.connection import connect


if __name__ == '__main__':
    crawler = crawler()
    cnn = connect(host='172.16.77.53', port=27017)
    people_infos = crawler.get_people_infos('zhouyuan')
    print save_people_infos(people_infos, cnn.zhihu_crawler)
