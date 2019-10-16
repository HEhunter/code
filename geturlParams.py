import readConfig as readConfig
from readExcel import readExcel

readconfig = readConfig.ReadConfig()

class geturlParams():# 定义一个方法，将从配置文件中读取的进行拼接
    def get_Url(self,path):
        new_url = readconfig.get_http('scheme') + '://' + readconfig.get_http('baseurl')+ path
        #logger.info('new_url'+new_url)
        return new_url

if __name__ == '__main__':# 验证拼接后的正确性
    cls = readExcel().get_xls('userCase.xlsx', 'login')
    path=cls[1][1]
    print(geturlParams().get_Url(path))

