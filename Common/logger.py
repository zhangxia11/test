import logging
import time
import os

class Logger(object):
    def __init__(self,logger_name):
        #创建logger logger_name为参数，可设置为项目名称，日志中会打印出来，好识别
        self.logger = logging.getLogger(logger_name)
        self.logger.setLevel(logging.INFO)

        # 生成log文件名，以时间命名
        time1 = time.strftime('%Y%m%d', time.localtime())
        #print(time1)
        filepath_info = os.path.dirname(os.getcwd()) + '\logs\\' + time1 + '.log'
        filepath_error = os.path.dirname(os.getcwd()) + '\logs\\' + time1 + '_error' + '.log'
        #print(filepath_info)

        # 生成处理器 将infolog 发送至file
        fh = logging.FileHandler(filepath_info)
        fh.setLevel(logging.INFO)

        # 生成处理器 将errorlog 发送至file,若不加，error和info会打印到同一个日志？
        eh = logging.FileHandler(filepath_error)
        eh.setLevel(logging.ERROR)

        # 生成处理器将log 输出至控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)



        # 设置内容格式 时间-日志器名称-日志级别-日志内容
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        # 设置error内容格式 时间-日志器名称-日志级别-文件名-日志行号-日志内容
        formatter_error = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(module)s  - %(lineno)s - %(message)s')

        #设置日志显示格式
        fh.setFormatter(formatter)
        eh.setFormatter(formatter_error)
        ch.setFormatter(formatter)

        # 给logger添加handler
        self.logger.addHandler(fh)
        self.logger.addHandler(eh)
        self.logger.addHandler(ch)

    def GetLog(self):
        return self.logger

