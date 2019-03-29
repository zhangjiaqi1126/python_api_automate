##encoding = utf-8
import requests

class RunMethod:
    #定义get请求方法
    def get_main(self,url,data=None,header=None):
        res = None
        if header != None:
            res = requests.get(url,data,header)
        else:
            res = requests.get(url,data)
        return res.json()
    # 定义get请求方法
    def post_main(self,url,header=None,data=None):
        res = None
        if header != None:
            res = requests.post(url, data, header)
        else:
            res = requests.post(url,data)
        return res.json()

    def run_main(self,method,url, data=None, header=None):
        res = None
        if method == "post":
            res = self.post_main(url, data, header)
        else:
            res = self.post_main(url, data, header)
        return res
if __name__ == "__main__":
    test = RunMethod()
    print(test.run_main("get","https://www.apiopen.top/novelSearchApi?name=盗墓笔记").text)