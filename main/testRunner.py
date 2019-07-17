import unittest
import HTMLTestRunnerCN
import HTMLTestRunner
import os
import time

#discover()，一次性加载一个路径下的所有测试用例（不管多少包，多少测试类），其参数可以是包名，也可以是文件夹名称
suite = unittest.TestLoader().discover('testsuits')


if __name__ == '__main__':
    #runner = unittest.TextTestRunner()

    #now = time.strftime("%Y-%m-%d %H_%M_%S", time.localtime())
    now = time.strftime("%Y-%m-%d %H", time.localtime())
    report_path = os.path.dirname(os.getcwd()) + r'\testReport\\' + now + '.html'
    with open(report_path,'wb') as fp:
        # runner = HTMLTestRunnerCN.HTMLTestReportCN(stream=fp,
        #                                            title='xxx接口自动化测试报告',
        #                                            description='报告中描述部分',
        #                                            tester='测试者')
        # runner.run(suite)
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'测试报告', description=u'用例执行详情：')
        runner.run(suite)

