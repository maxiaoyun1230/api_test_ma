#coding:utf-8
'''项目配置文件'''


import os
import logging
#项目路径
prj_path=os.path.dirname(os.path.dirname(os.path.abspath(_file_)))
#当前文件的绝对路径

data_path=os.path.join(prj_path,'data')
testcase_path = os.path.join(prj_path, 'testcase')

report_file=os.path.join(prj_path,'report','report.html')
log_file=os.path.join(prj_path,'log','log.txt')
#日志配置
logging.basicConfig(level=logging.DEBUG,  # log level
                    format='[%(asctime)s] %(levelname)s [%(funcName)s: %(filename)s, %(lineno)d] %(message)s',  # log格式
                    datefmt='%Y-%m-%d %H:%M:%S',  # 日期格式
                    filename=log_file,  # 日志输出文件
                    filemode='a')  # 追加模式

#c:/api_test/data

#配置数据库
db_host='115.28.108.130'
db_port=3306
db_user='test'
db_password='123456'
db='api_test'


#邮件配置
smtp_server='smtp.sina.com'#smtp服务器地址
smtp_user='test_results@sina.com'
smtp_passwrod='hanzhichao123'
subject='接口测试邮件'#邮件主题
sender=smtp_user#邮件发送人
receiver='superhin@126.com'#邮件接收人
is_send_email=False#是否发送邮件开关

if __name__=="__main__":

    print(report_file)