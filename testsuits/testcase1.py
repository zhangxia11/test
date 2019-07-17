import unittest
from Common.httpRequest import HttpRequest
from Common.config import GetConfig
import json
from Common.logger import Logger
from Common.read_excel import read_excel
import paramunittest





# header1 = {'Content-Type': 'application/json;charset=UTF-8', 'X-token': 'msswebe7fc57abcd914b60a375d2fabeee6cb9'}
# #header_json = json.dumps(header)
# #
# data = {"account": "zhangxia{{$timestamp}}", "password": "9c310f1e41974e097811ab3ab9334fe9", "nickName": "中心",
#              "status": "1"}
# data_json1 = json.dumps(data)


url1 = GetConfig().getConfig('url','urlName')
excel = read_excel().readExcel('test')



@paramunittest.parametrized(*excel)
class TestApi(unittest.TestCase):
    myLogger = Logger('ApiTest').GetLog()
    def setParameters(self,case_name,path,query,method,header):
        self.case_name = case_name
        self.path = path
        self.query = query
        self.method = method
        self.header = header

    @classmethod
    def setUpClass(cls):
        #做前提工作
        print("-----------START----------------")


    @classmethod
    def tearDownClass(cls):
        #做结束工作
        print("-------接口测试结束-------，请查看报告")


    # def test_print(self):
    #     print(self.case_name)
    #     print(self.path)
    #     print(type(self.query))
    #     print(self.method)
    #     print(type(self.header))





    def test_api1(self):
        '''测试1'''
        #req = HttpRequest().send('post', url, data_json, header)
        data_json = json.loads(self.query)
        data_json = json.dumps(data_json)
        #header = json.loads(self.header)
        url = url1 + self.path
        print(url)
        print(self.method)
        print(data_json)
        print(type(data_json))
        req = HttpRequest().send(self.method,url,data_json,eval(self.header))
        print(req)



        #在使用try except 时, 捕获了assert函数产生的AssertionError异常, 导致异常没有上抛, 这时只需要在后面加上raise 就可以再次把它抛出。
        try:
            self.assertEqual(req[1]['code'],'200','测试失败，code码不符合预期')
        except AssertionError as e:
            #self.myLogger.error(format(e))
            raise
            #print('test fail：%s',format(e))






if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run()