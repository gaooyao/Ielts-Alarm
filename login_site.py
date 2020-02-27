import time
from PIL import Image
import pytesseract
import requests
from io import BytesIO
import logging

from config import USER_NAME,PASSWORD
logger = logging.getLogger("log")


def login_by_window(browser):
    """
    通过页面登陆雅思报名系统
    :param browser: browserHandler
    :return: browserHandler
    """
    logger.info("官网已打开，开始登陆")
    while True:  # 登录
        element = browser.find_element_by_id('userId')  # 输入用户名
        element.clear()
        element.send_keys(USER_NAME)
        element = browser.find_element_by_id('userPwd')  # 输入密码
        element.clear()
        element.send_keys(PASSWORD)
        element = browser.find_element_by_id('loginForm')  # 加载验证码
        element.click()
        time.sleep(2)
        element = browser.find_element_by_id('chkImg')  # 获取验证码
        element.click()
        time.sleep(2)
        imageObject = Image.open(BytesIO(requests.get(element.get_attribute("src")).content))
        string = pytesseract.image_to_string(imageObject)
        element = browser.find_element_by_id('checkImageCode')  # 输入验证码
        element.clear()
        element.send_keys(string)
        time.sleep(10)
        element = browser.find_element_by_id('btn_log_goto')  # 点击登录按钮
        element.click()
        time.sleep(2)
        try:
            browser.find_element_by_id("breadcrumbRange")
            logger.info("登陆成功")
            return browser
        except Exception as e:
            logger.info("登陆失败")
            continue


def login_by_command(browser):
    """
    通过命令行登陆雅思报名系统
    :param browser: browserHandler
    :return: browserHandler
    """
    logger.info("官网已打开，开始登陆")
    while True:  # 登录
        element = browser.find_element_by_id('userId')  # 输入用户名
        element.clear()
        element.send_keys(USER_NAME)
        element = browser.find_element_by_id('userPwd')  # 输入密码
        element.clear()
        element.send_keys(PASSWORD)
        element = browser.find_element_by_id('loginForm')  # 加载验证码
        element.click()
        time.sleep(2)
        element = browser.find_element_by_id('chkImg')  # 获取验证码
        element.click()
        time.sleep(2)
        imageObject = Image.open(BytesIO(requests.get(element.get_attribute("src")).content))

        imageObject.show()
        string = input("please enter the code: ")

        element = browser.find_element_by_id('checkImageCode')  # 输入验证码
        element.clear()
        element.send_keys(string)
        time.sleep(1)
        element = browser.find_element_by_id('btn_log_goto')  # 点击登录按钮
        element.click()
        time.sleep(2)
        try:
            browser.find_element_by_id("breadcrumbRange")
            logger.info("登陆成功")
            return browser
        except Exception as e:
            logger.info("登陆失败")
            continue
