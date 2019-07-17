import requests
from logger import Logger
import json
from config import GetConfig



myLogger = Logger('ApiTest').GetLog()

class HttpRequest(object):
    def send_get(self,url,params=None,headers=None):
        try:
            r = requests.get(url, params=params, headers=headers)
            #myLogger.info("请求的内容如下： %s" % params)
            status_code = r.status_code   #获取返回的状态码
            reponse_json = r.json()    # 响应内容，json类型转化成python数据类型
            return status_code,reponse_json   #返回响应码 响应内容
        except Exception as e:
            myLogger.error("请求失败：",format(e))



    def send_post(self, url, params=None, headers=None):
        try:
            r = requests.post(url, data=params, headers=headers)
            #myLogger.info("请求的内容如下： %s" % params)
            status_code = r.status_code  # 获取返回的状态码
            reponse_json = r.json()  # 响应内容，json类型转化成python数据类型
            return status_code, reponse_json  # 返回响应码 响应内容
        except Exception as e:
            myLogger.error("请求失败：", format(e))



    def post_json(self, url, data=None, headers=None):
        '''封装post方法，并用json格式传值，return响应码和响应内容'''
        try:
            data = json.dumps(data).encode('utf-8')  # python数据类型转化为json数据类型
            r = requests.post(url, data=data, headers=headers)
            log1.info("请求的内容：%s" % data)
            status_code = r.status_code  # 获取返回的状态码
            log1.info("获取返回的状态码:%d" % status_code)
            response = r.json()  # 响应内容，json类型转化成python数据类型
            log1.info("响应内容：%s" % response)
            return status_code, response  # 返回响应码，响应内容
        except BaseException as e:
            myLogger.error("请求失败！", exc_info=1)


    def getDict(self,res,key):
        ''' 遍历嵌套字典，得到想要的value
                    dict1所需遍历的字典
                    obj 所需value的键'''
        for k,v in res.items():
            if k == key:
                return v
            else:
                if type(v) is dict: #如果value还是字典
                    re = self.getDict(v,key)   #递归
                    if re is not None:
                        return re


    def send(self, type, url, params=None, headers=None):
        res = None
        if(type == "get"):
            res = self.send_get(url, params, headers)
        elif(type == "post"):
            res = self.send_post(url, params, headers)
        else:
            print("method输入错误！")
        return res



#
# if __name__ == '__main__':
#     req = HttpRequest()
#     url1 = GetConfig().getConfig('url','urlName')
#     url = url1 + '/api/account/account/add'
#     print(url)
#     header = {'Content-Type': 'application/json;charset=UTF-8', 'X-token': 'msswebe7fc57abcd914b60a375d2fabeee6cb9'}
#     # header_json = json.dumps(header)
#
#     data = {"account": "zhangxia{{$timestamp}}", "password": "9c310f1e41974e097811ab3ab9334fe9", "nickName": "中心",
#             "status": "1"}
#     data = json.dumps(data)
#     res = req.send('post',url,data,header)
#     print(res)
#     print(data)








