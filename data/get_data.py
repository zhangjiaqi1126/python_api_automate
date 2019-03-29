#coding:utf-8

from data import data_config
from util.use_excel import user_excel
from util.use_json import user_json

'''
利用封装好的excel方法，获取sheet表的每个单元格的内容
'''


class GetData:
    def __init__(self):

        self.use = user_excel()
        self.usejson = user_json
    #获取excel的行数，因为我们的用例是卸载excel里，所以行数就是用例数
    def get_case_lines(self):
        return self.use.get_lines()

    #获取是否执行
    def get_is_run(self,row):
        flag = None
        col = int(data_config.get_run())
        run_model = self.use.get_cell_value(row,col)
        if run_model == "yes":
            flag = True
        else:
            flag = None
        return flag

    #获取是否携带header
    def is_header(self,row):
        col = int(data_config.get_header())
        header = self.use.get_cell_value(row,col)
        if header != '':
            return header
        else:
            return None

    # 获取请求方式
    def get_request_method(self, row):
        col = int(data_config.get_run_way())
        requesr_way = self.use.get_cell_value(row,col)
        return requesr_way

    #获取url
    def get_request_url(self,row):
        col = int(data_config.get_url())
        url = self.use.get_cell_value(row,col)
        return url

    # 获取请求数据
    def get_request_data(self, row):
        col = int(data_config.get_data())
        data = self.use.get_cell_value(row, col)
        if data == '':
            return None
        return data

    #通过关键字获取请求数据
    def get_data_for_json(self, row):
        make_json = user_json()
        request_data = make_json.get_data(self.get_request_data(row))
        return request_data

    # 获取预期结果
    def get_expcet_data(self, row):
        col = int(data_config.get_expect())
        expect = self.use.get_cell_value(row,col)
        return expect

    # 写入数据
    def write_result(self, row, value):
        col = int(data_config.get_result())
        self.use.write_value(row, col, value)
if __name__=="__main__":
    file_name = "C:/Users/zhangjiaqi3/PycharmProjects/python_request2/dataconfig/test_data.xls"
    sheet_id = 0
    obj = user_excel(file_name,sheet_id)
    print(obj.get_lines())
