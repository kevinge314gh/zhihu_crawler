from crawler.crawler import crawler
from db.mongo import *
from db.connection import connect
from settings import MONGO_IP, MONGO_PORT


if __name__ == '__main__':
    # crawler = crawler()
    # cnn = connect(host=MONGO_IP, port=MONGO_PORT)
    # people_infos = crawler.get_people_infos('linan')
    # print save_people_infos(people_infos, cnn.zhihu_crawler)
    url = 'http://www.zhihu.com/node/ProfileFolloweesListV2'
    data = {
        'method':'next',
        'params':{"offset":20,"order_by":"created","hash_id":"f9de84865e3e8455a09af78bfe4d1da5"}
        '_xsrf':'327696efedfd4529121f81c7017cc593'
            }


