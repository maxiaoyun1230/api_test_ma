#coding:utf-8
#测试用例

import unittest
import sys
import requests
sys.path.append("..")#
from config import config as cf
from lib.read_excel import get_case_data

class TestUserLogin(unittest.TestCase):
    def test_user_login_normal(self):
        case_data=get_case_data("test_user_data.xlsx",
                                "TestUserLogin,"
                                "test_user_login_normal")
        url=case_data[1]
        data=case_data[3]
        expect_res= case_data[4]
        data_dict=json.loads(data)
        res=requests.post(url=url,data=data_dict)
        self.assertAlmostEqual(expect_res,res.text)

