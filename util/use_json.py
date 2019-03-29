#encoding = utf-8

import json
class user_json:
    #读取数据
    def read_data(self):
        with open("C:/Users/zhangjiaqi3/PycharmProjects/python_request2/dataconfig/data.json") as f:
            data = json.load(f)
            return data
    #根据关键字获取数据
    def get_data(self,key):
        #self.read_data()
        return self.read_data()[key]

if __name__ == "__main__":
    obj = user_json()
    str = obj.get_data("username")
    print(str)