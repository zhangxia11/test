from xlrd import open_workbook
import os



class read_excel():
    excel_path = os.path.dirname(os.getcwd()) + r'\Config\test.xlsx'
    def readExcel(self,sheet_name):
        cls = []
        file = open_workbook(self.excel_path)        #打开excel
        sheet = file.sheet_by_name(sheet_name)       #获取excel的sheet页
        nrows =  sheet.nrows            #获取sheet页的行数
        for i in range(nrows):
            if sheet.row_values(i)[0] != 'case_name':
                cls.append(sheet.row_values(i))
        return cls



if __name__ == '__main__':
    excel = read_excel().readExcel('test')
    print(excel)









