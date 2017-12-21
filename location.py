import json
import threading
import time
import pymongo
from Gaode import GaoDE_coordinater
from config import *
import random

client = pymongo.MongoClient(FANG_URL,connect=False)
db=client[FANG_DB]


def save_to_mongo(result):
    if db[FANGL_TABLE].insert(result):
        print('存储到MongoDB成功', result)
        return True
    return False

def get_ip_text(file):
    file = open(file)
    ip_list =[]
    for line in file:
        try:
            ip_list.append(json.loads(line.strip()))
        except:
            pass
    return ip_list

def main(line,ip_list):
    address = line.split(",")[3]
    name =address .split("-")[-1]
    location = address.split("-")[0].strip()
    number = line.split(",")[4]
    ip = random.choice(ip_list)
    try:
        coordinater = GaoDE_coordinater.spider(0, name, ip)
        print(coordinater)
        lon = coordinater.split(",")[0]
        lat = coordinater.split(",")[1]

        # with open("4.txt","a",encoding="utf-8") as f:
        #     total = lon+","+lat+","+address+","+number
        #     f.write(total+"\n")
        #     f.close()
        total = {
            "name": address,
            "number": number,
            "lat": lat,
            "lon": lon,
            "location":location
        }
        save_to_mongo(total)
        with open("ftx_.txt", "a") as file:
            file.write(json.dumps(ip) + "\n")
            file.close()
        # time.sleep(1)
    except Exception as e:
        print(e,str(ip)+"不可用++++++++剩余ip："+str(len(ip_list)))
        if ip in ip_list:
            ip_list.remove(ip)
        main(line,ip_list)
        # if ip in ip_list:
        #     ip_list.remove(ip)
        # main(line, ip_list)
    else:
        print(str(ip) + "可用###剩余ip数：" + str(len(ip_list)) )


if __name__ == '__main__':
    ip_list = get_ip_text("ftx_ip.txt")
    # print(ip_lsit)
    # ip_list = [{"http": "http://125.45.87.12:9999"},{"http": "http://111.40.84.73:9797"}]
    file = open("zufang2.txt",encoding="utf-8")
    address_list,number_list=[],[]
    for line in file:
        line = line.strip()
        print(line)
        t1 = threading.Thread(target=main,args=(line,ip_list))
        t1.start()
        time.sleep(1)
    time.sleep(10000000)
        # main(line,ip_list)




