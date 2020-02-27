# coding = utf-8
from inquiry import inquiry_march_ukvi, inquiry_april_remain, inquiry_april_ukvi
from alarm import alarm
from login_site import login_by_window, login_by_command
from selenium import webdriver
import logging
from logger_init import log_init
import datetime
import time
from selenium.webdriver.firefox.options import Options

log_init()  # 初始化log
logger = logging.getLogger()

num = 0  # 已刷新次数
show_window = False  # 是否显示浏览器窗口

# if __name__ == "__main__":
#     alarm("test")

if __name__ == "__main__":
    if show_window:
        # 设置浏览器有界面模式
        browser = webdriver.Firefox()  # 初始化浏览器引擎
    else:
        # 设置浏览器无界面模式
        browser_options = Options()
        browser_options.add_argument('--headless')
        browser = webdriver.Firefox(firefox_options=browser_options)

    logger.info("浏览器初始化成功")

    browser.get("http://ielts.neea.cn")  # 打开雅思官网
    time.sleep(2)

    element = browser.find_element_by_id('btn_log_goto')  # 点击用户登录按钮
    element.click()
    time.sleep(2)
    if show_window:
        login_by_window(browser)
    else:
        login_by_command(browser)

    # 登陆成功
    start_time = datetime.datetime.now()
    while True:  # 开始循环查询
        last_time = (datetime.datetime.now() - start_time).seconds
        logger.info("*********************   上轮用时%d秒     *********************",
                    last_time)
        start_time = datetime.datetime.now()
        num = num + 1
        logger.info("*********************   开始第%d遍查询   *********************", num)
        try:
            if num != 1 and last_time == 0:
                try:
                    browser.find_element(By.CSS_SELECTOR, "#rightRange > #dialog .btn").click()
                    browser.find_element(By.ID, "btnBackToSearch").click()
                    time.sleep(1)
                except Exception as e:
                    continue
            if inquiry_april_ukvi(browser):  # 查询4月份UKVI是否开放
                alarm("4UKVIOK")
            # if inquiry_april_remain(browser):  # 4月份普通雅思考试考位预警
            #     alarm("4月份普通雅思考位剩余不多")
            # if inquiry_april_ukvi(browser):  # 4月份雅思捡漏
            #     alarm("4月份普通雅思考位有剩余")
        except Exception as e:
            logger.error(e.args)
            continue
        time.sleep(2)
