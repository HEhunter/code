import requests
import readExcel
import unittest
import getpathInfo
from common import HTMLTestRunner
from common.configHttp import RunMain

reportPath=getpathInfo.get_resultpath()

class requestDemo:
    def run_main(self,url,params,method):
        if method is 'post':
            r=requests.post(url,data=params)
            return r
        if method is 'get':
            r=requests.get(url,params=params)
            return r
    def post_main(self,url,data):
        res=None
        res=requests.post(url=url,data=data)
        return res
    def get_main(self,url,data):
        res=None
        res=requests.get(url=url,data=data)
        return res

class unitDemo(unittest.TestCase):
    def tearDown(self):
        print('每个测试用例执行之后')
    def setUp(self):
        print('每个测试用例执行之前')

    @classmethod
    def setUpClass(self):
        print('必须使用 @ classmethod装饰器, 所有test运行完后运行一次')
    @classmethod
    def tearDownClass(self):
        print('必须使用@classmethod 装饰器,所有test运行前运行一次')

    def getRequests(self,url,data):
        result=requests.get(url,data)
        return result

    def test_a_run(self):
        #self.assertEqual(1,1)
        param = {'type': 'yuantong', 'postid': '806063787827863801'}
        result= RunMain().run_main('post','http://www.kuaidi100.com/query', param )
        res=RunMain().getValue(result,'message')
        value= self.assertEqual('ok', str(res))
        print(res,'结果：',value)
    def test_b_run(self):
        param = {'tel': '18109045175'}
        result = RunMain().run_main('get', 'https://tcc.taobao.com/cc/json/mobile_tel_segment.htm', param)
        #result=self.getRequests('https://tcc.taobao.com/cc/json/mobile_tel_segment.htm', param)
        print(result.text)
        if result.status_code == 200:
            self.assertIn("province:'四川'", result.text)
        else:
            print( '请求失败，响应码：',result.status_code)

#cls=readExcel().get_xls('userCase.xlsx', 'login')



if __name__ == '__main__':

    suite=unittest.TestSuite()
    suite.addTest(unitDemo('test_a_run'))
    suite.addTest(unitDemo('test_b_run'))
    runner=unittest.TestTestRunner()
    fp=open('res.html','wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title='api测试报告',tester='ZhaoJun')
    runner.run(suite)
    '''
    unittest.main()
    '''
