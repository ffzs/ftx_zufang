import json
import requests
import urllib.parse
import random
from config import *

class GaoDE_coordinater(object):
    def __init__(self):
        # self.ip_list = self.get_ip_list("ip_gaode.txt")
        # # print(self.ip_list)
        # self.headers = {
        #     'Referer': 'http://lbs.amap.com/console/show/picker',
        #     'User-Agent': random.choice(USER_AGENTS)
        # }
        pass

    def get_ip_list(self,file):
        file = open(file)
        ip_list =[]
        for line in file:
            try:
                ip_list.append(json.loads(line.strip()))
            except:
                pass
        return ip_list

    def spider(self,content,ip):
        try:
            headers = {
                'Referer': 'http://lbs.amap.com/console/show/picker',
                'User-Agent': random.choice(USER_AGENTS)
            }
            keyword =urllib.parse.quote(
                content)
            url = "http://restapi.amap.com/v3/place/text?s=rsv3&children=&key=8325164e247e15eea68b59e89200988b&page=1&offset=10&city=110000&language=zh_cn&callback=jsonp_297203_&platform=JS&logversion=2.0&sdkversion=1.3&appname=http%3A%2F%2Flbs.amap.com%2Fconsole%2Fshow%2Fpicker&csid=ED97034C-EC17-4196-842E-0590BEBB2DA4&keywords="+ keyword
            requset = requests.get(url=url, headers=headers,proxies=ip)
            result_a = requset.text
            # print(result_a)
            result_a = result_a.split("(", 1)[1][:-1]
            result_a = json.loads(result_a)

            if (result_a["info"]=="OK"):
                if result_a["pois"]:
                    return result_a["pois"][0]["location"]
            else:
                return ""
        except:
            return ""

if __name__ == '__main__':
    content = "北京风行在线技术有限公司"
    app = GaoDE_coordinater()
    ip ={"http": "http://101.37.23.221:80"}
    a = app.spider(content,ip)
    print(a)


