#encoding = utf-8

import xlrd
from xlutils.copy import copy
class user_excel:
    def __init__(self,file_name=None,sheet_id=None):
        if file_name:
            self.file_name =file_name
            self.sheet_id = sheet_id
        else:
            self.file_name = "C:/Users/zhangjiaqi3/PycharmProjects/python_api_automate/data_file/test_data.xls"
            self.sheet_id = 0
        #self.data_file = self.get_data()

    #获取数据
    def get_data(self):
        data = xlrd.open_workbook(self.file_name)
        tables = data.sheets()[self.sheet_id]
        return tables

    #获取单元格的行数
    def get_lines(self):
        tables = self.get_data()
        return tables.nrows
    #获取单元格内容
    def get_cell_value(self,row,col):
        tables = self.get_data()
        return tables.cell_value(row,col)

    #写入数据
    def write_value(self,row,col,value):
        # 打开excel表
        read_data = xlrd.open_workbook("C:/Users/zhangjiaqi3/PycharmProjects/python_api_automate/data_file/test_data.xls")
        # 将xlrd对象拷贝转化为xlwt对象
        write_data = copy(read_data)
        # 获取要写入数据的sheet表
        sheet_data = write_data.get_sheet(0)
        # 写入数据
        sheet_data.write(row, col, value)
        # 保存
        write_data.save("C:/Users/zhangjiaqi3/PycharmProjects/python_api_automate/data_file/test_data.xls")


if __name__=="__main__":
    file_name = "C:/Users/zhangjiaqi3/PycharmProjects/python_request2/dataconfig/test_data.xls"
    sheet_id = 0
    obj = user_excel(file_name,sheet_id)
    print(obj.get_lines())
