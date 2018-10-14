#coding:utf-8
#"数据库操作"
import pymysql
import sys
sys.path.append("..")#提升包搜索路径到项目路径

from config import config as cf #从config文件夹中读取config重命名为cf

#获取连接方法
def get_conn():
    conn=pymysql.connect(host=cf.db_host,
                         port=cf.db_port,
                         user=cf.db_user,
                         password=cf.db_password,
                         db=cf.db,
                         charset='utf8')

#查询操作
def db_query(sql):
    conn=get_conn()
    cur=conn.cursor()
    cur.execute(sql)
    result=cur.fetcall()
    cf.logging.debug(sql)#debug小写表示方法
    cf.logging.debug(result)#DBBUG大写表示数字
    cur.close()
    conn.close()


    return result
#修改操作
def db_change(sql):
    conn=get_conn()
    cur=conn.cursor()
    try:
        cur.execute(sql)
        conn.commit()
    except Exception as e:
        conn.rollback()
        cf.logging.error(str(e))
    finally:
        cur.close()
        conn.close()

if __name__=="__main__":
    result=db_query("select * from user where name='张三'")
    print(result)