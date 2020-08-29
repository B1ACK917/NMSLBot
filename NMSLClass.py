from bs4 import BeautifulSoup
import requests
import time
import threading
import random
import json


class NMSL:
    def __init__(self, default_type='嘴臭', server='https://s.nmsl8.club/'):
        self.Server = server
        self.NMSLURL = 'https://s.nmsl8.club/getloveword?type={}'
        self.Header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36',
        }
        self.TypeDict = {'嘴甜': 1, '嘴臭': 2}
        self.Type = self.TypeDict[default_type]
        self.Target = self.NMSLURL.format(self.Type)
        self.NMSLList = []
        self.MIN = 200
        self.NowHolding = 300
        self.update_text(300)
        threading.Thread(target=self.check_need_update).start()
        while True:
            if len(self.NMSLList) >= 100:
                break
            else:
                print('\rInitializing... {}%'.format(len(self.NMSLList)/3), end='', flush=True)
                time.sleep(1)
        print('\rInitialize Succeed', end='', flush=True)

    def __update_text(self):
        Respond = requests.get(self.Target, headers=self.Header)
        self.NMSLList.append(json.loads(Respond.content)['content'])

    def update_text(self, num):
        for i in range(num):
            threading.Thread(target=self.__update_text).start()



    def check_need_update(self):
        while True:
            time.sleep(3)
            if self.NowHolding < self.MIN:
                threading.Thread(target=self.update_text, args=(100,)).start()
                self.NowHolding += 100

    def get(self):
        index = random.randint(0, len(self.NMSLList) - 1)
        NMSLStr = self.NMSLList[index]
        self.NMSLList.pop(index)
        return NMSLStr


if __name__ == '__main__':
    a = NMSL()
    for i in range(10):
        print(a.get())
        time.sleep(3)
