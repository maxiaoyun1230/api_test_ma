#coding:utf-8
#读取excel 数据
import xlrd
import os
import sys
sys.path.append("..")
from config import config as cf
#从excel中获取一行用例的数据
#data——flie:数据文件，sheet 所在表明，case_name用例名称
def get_case_data(data_file,sheet,case_name):
    data_file_path=os.path.join(cf.data_path,data_file)
    wb = xlrd.open_wookbook(data_file_path)#打开excel
    sh = wb.sheet_by_name(sheet)
    for i in range(1,sh.nrows):#开闭合区间，前闭后开
        if sh.cell(i,0).value==case_name:
            return sh.row_values(i)

if __name__=="__main__":
    r=get_case_data("test_uesr_data.xlsx,""TestUserLogin","test_user_login_normal")
    print(r)

