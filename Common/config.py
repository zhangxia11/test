import os
import configparser




class GetConfig(object):
    def getConfig(self,section,key):
        config_file = os.path.dirname(os.getcwd()) + '\Config\config.ini'
        conf = configparser.ConfigParser()
        conf.read(config_file,encoding='utf-8')

        #读取配置文件中的内容
        return conf.get(section,key)



if __name__ == '__main__':
    getConf = GetConfig()
    print(getConf.getConfig('url','urlName'))

