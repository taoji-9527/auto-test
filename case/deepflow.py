# coding=utf-8
import ddt
import unittest
import sys
sys.path.append('E:\\Teacher\\Imooc\\SeleniumPython')
import traceback
from business.register_business import RegisterBusiness
from selenium import webdriver
import HtmlTestRunner
from util.excel_util import ExcelUtil
import os
from log.user_log import UserLog
import time
ex = ExcelUtil()
data = ex.get_data()
log = UserLog()
logger = log.get_log()
file_name = "E:/Teacher/Imooc/SeleniumPython/Image/test001.png"
# 邮箱、用户名、密码、验证码、错误信息定位元素、错误提示信息





