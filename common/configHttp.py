import requests
import json
from common.Log import logger

logger = logger


class RunMain():
    def send_post(self, url, data):  # 定义一个方法，传入需要的参数url和data
        # 参数必须按照url、data顺序传入
        if isinstance(data, str):
            result = requests.post(url=url, data=eval(data))  # 因为这里要封装post方法，所以这里的url和data值不能写死
        else:
            result = requests.post(url=url, json=data)
        #res = json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2)
        return result

    def send_get(self, url, data):
        # if isinstance(data, str):
        #     result = requests.get(url=url, data=eval(data))  # 因为这里要封装post方法，所以这里的url和data值不能写死
        # else:
        #     result = requests.get(url=url, data=data)
        # # res = json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2)
        result = requests.get(url, eval(data))
        return result

    def run_main(self, method, url=None, data=None):  # 定义一个run_main函数，通过传过来的method来进行不同的get或post请求

        if method == 'post':
            result = self.send_post(url, data)
            logger.info(str(result))
            return result
        elif method == 'get':
            result = self.send_get(url, data)
            logger.info(str(result))
            return result
        else:
            print("method值错误！！！", method)
            logger.info("method值错误！！！", method)

    # 获取json 数据转换为python可识别的字典数据，获取其中对应key的value
    def getJson(result, jsonType=None, value=None):
        print('获取的jsonType', jsonType)
        if jsonType is 'dump':
            res = json.dump(result, ensure_ascii=False, sort_keys=True, indent=2)
        elif jsonType is 'dumps':
            res = json.dumps(result)
        elif jsonType is 'loads':
            res = json.loads(result)
        else:
            return 'jsonType值错误'
        return res[value]

    def getValue(self, result, msg):        # 断言用
        res = result.json()
        return res[msg]


if __name__ == '__main__':  # 通过写死参数，来验证我们写的请求是否正确
    param = {
        'clientId': 'ut.usscity.com',
        'password': '123456',
        'userName': 'admin',
        'VerificationCode': '',
        'VerificationCodeKey': "f7dc3967-bfbc-4a0f-9e2d-4d6e403d10a1"
    }
    # test = requests.post('http://192.168.0.157:18005/oauth/token', param)
    # print(test.json())
    result = RunMain().run_main('post', 'http://192.168.0.157:18005/oauth/token', param)
    print(result.json())
    print(result.text)
    res = RunMain().getValue(result, 'msg')
    print(res)



    # param = {'type': 'zhongtong', 'postid': '3710374504275'}
    # # test = requests.post('http://www.kuaidi100.com/query', param)
    # # print(test.json())
    # result = RunMain().run_main('post', 'http://www.kuaidi100.com/query', param)
    # # result=RunMain.getJson(result.json(),'loads','message')
    # print(result.json())
    # res = RunMain().getValue(result, 'message')
    # print(res)
    # ress = RunMain().getJson(param)
    # print(ress)

    '''
    param={'type':'yuantong','postid':'906063787827863000'}
    result = RunMain().run_main('post', 'http://www.kuaidi100.com/query', param)
    #result=requests.post('http://www.kuaidi100.com/query', param)
    print(result.json())
    res=result.json()
    print(res['message'],result.text)'''
