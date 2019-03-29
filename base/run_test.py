#coding:utf-8
import  sys
#sys.path.append("C:/Users/zhangjiaqi3/PycharmProjects/python_api_automate")
from data.get_data import GetData
from base.run_method import RunMethod
from util.common_util import CommonUtil
from util.send_email import SendEmail
from util.log import *

class RunTest:
    def __init__(self):
        self.run_method = RunMethod()
        self.data = GetData()
        self.com_util = CommonUtil()
        self.send_mail = SendEmail()

    def go_on_run(self):
        res = None
        pass_count = []
        fail_count = []
        rows_count = self.data.get_case_lines()
        print(rows_count)
        for i in range(1,rows_count):
            #获取excel表格中的数据
            url = self.data.get_request_url(i)
            method = self.data.get_request_method(i)
            is_run = self.data.get_is_run(i)
            data = self.data.get_request_data(i)
            header = self.data.is_header(i)
            expect = self.data.get_expcet_data(i)
            print(url,method,is_run,data,header,expect)
            #判断是否执行
            if is_run:
                res = self.run_method.run_main(method,url,data,header)
                info(res)
                #print(res)
                #判断预期结果和实际结果
                if self.com_util.is_contain(expect,res['data']):
                    #如果通过就把行号写入定义的列表中
                    pass_count.append(i)
                    #在excel表中的实际结果中输入测试结果
                    self.data.write_result(i, "pass")
                    print("测试通过")
                else:
                    print("测试失败")
                    #把执行失败的行号写入定义的列表中
                    fail_count.append(i)

        print(len(pass_count))
        print(len(fail_count))
        self.send_mail.send_main(pass_count, fail_count)
        #return res




if __name__ =="__main__":

    run = RunTest()
    run.go_on_run()