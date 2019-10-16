import os
import time

nowTime = time.strftime("%Y-%m-%d", time.localtime())
print(nowTime)


def get_Path():
    path = os.path.split(os.path.realpath(__file__))[0]
    print(path)
    return path


def get_resultpath():
    path = get_Path()
    resultpath = os.path.join(path, 'result')
    print(resultpath)
    resultpath = os.path.join(resultpath, nowTime)
    if os.path.exists(resultpath):
        return resultpath
    else:
        os.mkdir(resultpath)  # 路径不存在则创建
        return resultpath


def set_reportPath():
    reportPath = get_resultpath()
    reportName = 'report.' + nowTime + '.html'
    resultPath = os.path.join(reportPath, reportName)
    return resultPath


if __name__ == '__main__':  # 执行该文件，测试下是否OK
    print('测试路径是否OK,路径为：', get_Path())
    print('测试路径是否OK,路径为：', get_resultpath())
    print('测试报告的路径：' + set_reportPath())
