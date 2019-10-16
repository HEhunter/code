from common.configHttp import RunMain
import readExcel
import paramunittest
import unittest
import common.Log
import json

# getZone=readExcel.readExcel().excel_data_list('userCase.xlsx','getZone')
Sheet1 = readExcel.readExcel().excel_data_list('demo1.xlsx', 'Sheet1')
log = common.Log.logger


@paramunittest.parametrized(*Sheet1)
class testZone(unittest.TestCase):
    def setParameters(self, caseNmber, caseType, caseName, priority, url, method, header, purpose, params, expectValue,
                      actualvalue, resultValue):
        self.caseNmber = caseNmber
        self.caseType = caseType
        self.caseName = caseName
        self.priority = priority
        self.url = url
        self.method = method
        self.header = header
        self.purpose = purpose
        self.params = params
        self.expectValue = str(expectValue)
        self.actualvalue = actualvalue
        self.resultValue = resultValue

    # @paramunittest.parametrized(*getZone)
    # class testZone(unittest.TestCase):
    #     def setParameters(self,casename,method,path,url,params,msg):
    #         self.casename=casename
    #         self.method=method
    #         self.path=path
    #         self.url=url
    #         self.params=params
    #         self.msg=msg

    def testcheckResult(self):
        self.checkResult()

    def checkResult(self):
        result = RunMain().run_main(self.method, self.url, json.dumps(self.params))

        if result.status_code == 200:
            # print('测试通过')
            # print(self.expectValue)
            # print(type(self.expectValue))
            # print(result.json())
            # print(type(result.json()))
            if self.expectValue in json.dumps(result.json()):
                print('测试通过')
                log.info('断言失败:' + '实际输出=' + result.text + 'expectValue=' + self.expectValue)
            # if self.assertIn(self.expectValue, result.json()) is False:
            #     log.info('断言失败:' + '实际输出=' + result.text + 'expectValue=' + self.expectValue)
        else:
            print('请求失败，响应码：', result.status_code)


if __name__ == '__main__':
    unittest.main()
