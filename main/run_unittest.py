#encoding = utf-8

import unittest
import  sys
sys.path.append("C:/Users/zhangjiaqi3/PycharmProjects/python_api_automate")
import HTMLTestRunner
from base.run_test import RunTest
from util.log import *

class Runmain(unittest.TestCase):
    def setUp(self):
        self.runtest = RunTest()
    def tearDown(self):
        pass
    def test_01(self):
        info("开始执行脚本")
        self.runtest.go_on_run()

        info("执行结束")


if __name__=="__main__":
    filename = "C:/Users/zhangjiaqi3/PycharmProjects/python_api_automate/report/TestReport.html"
    fp = open(filename,"wb")
    # 创建一个测试集合
    suit = unittest.TestSuite()
    # 添加测试用例（test_Baidu是类名）
    suit.addTest(Runmain("test_01"))
    # 添加所有以test开头的
    # suit.addTest(Runmain, "test")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'百度搜索测试报告', description=u'用例执行情况：')
    runner.run(suit)
    fp.close()
