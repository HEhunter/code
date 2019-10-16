import os
import unittest
import requests
from common.configHttp import RunMain
from ddt import ddt, data
import xlwt as xlwt
import getpathInfo  # 自己定义的内部类，该类返回项目的绝对路径
# 调用读Excel的第三方库xlrd
from xlrd import open_workbook

# 拿到该项目所在的绝对路径
path = getpathInfo.get_Path()


class readExcel():
    def __init__(self):
        self.sheet_name = None

    def excel_data_list(self, xls_name, sheetname):
        data_list = []
        xlsPath = os.path.join(path, "testFile", 'case', xls_name)
        wb = open_workbook(xlsPath)  # 打开excel
        sh = wb.sheet_by_name(sheetname)  # 定位工作表
        header = sh.row_values(0)  # 获取标题行的数据
        print(header)
        for i in range(1, sh.nrows):  # 跳过标题行，从第二行开始获取数据
            col_datas = dict(zip(sh.row_values(0), sh.row_values(i)))  # 将标题和每一行的数据，组装成字典
            print(col_datas)
            data_list.append(col_datas)  # 将字典添加到列表中 ，列表嵌套字典，相当于每个字典的元素都是一个列表（也就是一行数据）
        return data_list

    def get_test_data(self, data_list, case_id):
        '''
        :param data_list: 工作表的所有行数据
        :param case_id: 用例id，用来判断执行哪几条case。如果id=all ，那就执行所有用例；否则，执行列表参数中指定的用例
        :return:  返回最终要执行的测试用例
        '''
        if case_id == 'all':
            final_data = data_list
        else:
            final_data = []
            for item in data_list:
                if item['id'] in case_id:
                    final_data.append(item)
        return final_data

    def get_xls(self, xls_name, sheet_name):  # xls_name填写用例的Excel名称 sheet_name该Excel的sheet名称
        cls = []
        # 获取用例文件路径
        xlsPath = os.path.join(path, "testFile", 'case', xls_name)
        print(xlsPath + 'fdsfsd')
        file = open_workbook(xlsPath)  # 打开用例Excel
        sheet = file.sheet_by_name(sheet_name)  # 获得打开Excel的sheet
        # 获取这个sheet内容行数
        nrows = sheet.nrows
        for i in range(nrows):  # 根据行数做循环
            if sheet.row_values(i)[0] != u'case_name':  # 如果这个Excel的这个sheet的第i行的第一列不等于case_name那么我们把这行的数据添加到cls[]
                cls.append(sheet.row_values(i))
        return cls

    def writeExcel(self, xls_name, sheet_name, sheet_value):

        if self.sheet_name is not None:

            wb = xlwt.Workbook()
            sheet = wb.add_sheet(sheet_name)

            for i in range(len(sheet_value)):
                for j in range(len(sheet_value[i])):
                    sheet.write(i, j, sheet_value[i][j])

            wb.save(self.EXCEL_PATH)
            print("write date success!")
            return True
        else:
            return False


# test_data = readExcel().excel_data_list('userCase.xlsx', 'login')
test_data = readExcel().excel_data_list('demo2.xlsx', 'Sheet1')
#print(test_data)


@ddt
class testRegister(unittest.TestCase):
    def setUp(self):
        print("开始执行测试用例")

    def tearDown(self):
        print("测试用例执行完毕")

    @data(*test_data)
    def test_register(self, data_item):
        # 调用configHttp runmanin
        result = RunMain().run_main(data_item['method'], data_item['url'], data)
        message = RunMain().getValue(result, 'expectValue')
        try:
            print(message)
            self.assertEqual(data_item['msg'], message)
        except AssertionError as e:
            print('Failed')
            raise e

    # @data(*test_data)
    # def test_register(self, data_item):
    #     # 调用configHttp runmain
    #     print(data_item['method'], data_item['url'] + data_item['path'], data_item['params'])
    #     # data=eval(data_item['params'])   eval转换为字典型数据，不然系统识别不了
    #     result = RunMain().run_main(data_item['method'], data_item['url'] + data_item['path'], data)
    #     print(result.json())
    #     message = RunMain().getValue(result, 'message')
    #     try:
    #         print(message)
    #         self.assertEqual(data_item['msg'], message)
    #     except AssertionError as e:
    #         print('Failed')
    #         raise e


if __name__ == '__main__':  # 我们执行该文件测试一下是否可以正确获取Excel中的值
    '''
    test_data=readExcel().excel_data_list('userCase.xlsx', 'login')
    print('第一种方法：',test_data)
    cls=readExcel().get_xls('userCase.xlsx', 'login')
    print(readExcel().get_xls('userCase.xlsx', 'login'))
    for i in cls:
        for j in range(len(i)):
            print(i[j])
    '''
    unittest.main()
