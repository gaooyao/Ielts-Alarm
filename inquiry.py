from selenium.webdriver.common.by import By
import time
import logging

logger = logging.getLogger("log")

WAIT_TIME_S = 0.2
WAIT_TIME_L = 1


def inquiry_april_ukvi(browser):
    """
    查询是否开放四月份UKVI考试
    """
    logger.info("开始查询是否开放四月份UKVI考试")
    browser.find_element(By.CSS_SELECTOR, "li:nth-child(14) > a").click()  # 点击UKVI考位查询
    time.sleep(WAIT_TIME_L)
    try:
        browser.find_element(By.ID, "2020-04")  # 查询四月份的是否开放
        logger.info("四月份UKVI考试报名已开放")
        return True  # 已开放
    except Exception as e:
        logger.info("四月份UKVI考试报名未开放")
        return False  # 未开放


def inquiry_april_remain(browser):
    """
    四月份剩余雅思预警
    """
    logger.info("开始查询四月份剩余雅思考位剩余情况")
    browser.find_element(By.CSS_SELECTOR, "li:nth-child(10) > a").click()
    time.sleep(WAIT_TIME_L)
    browser.find_element(By.ID, "2020-06").click()
    time.sleep(WAIT_TIME_S)
    browser.find_element(By.ID, "mvfSiteProvinces211").click()
    time.sleep(WAIT_TIME_S)
    browser.find_element(By.CSS_SELECTOR, ".myhomecon_bg").click()  # 点击空白处
    time.sleep(WAIT_TIME_S)
    browser.find_element(By.ID, "btnSearch").click()
    time.sleep(WAIT_TIME_L)
    element = browser.find_element(By.CSS_SELECTOR, ".table:nth-child(1) tr:nth-child(1) > td:nth-child(6)")
    if element.text != "有名额":
        logger.info("考点一已无名额")
        return True
    browser.find_element(By.CSS_SELECTOR, ".table:nth-child(1) tr:nth-child(2) > td:nth-child(6)")
    if element.text != "有名额":
        logger.info("考点二已无名额")
        return True
    logger.info("两个考点都有剩余")
    return False


def inquiry_march_ukvi(browser):
    """
    四月份雅思考试捡漏
    """
    logger.info("开始查询四月份雅思考试是否有剩余考位")
    browser.find_element(By.CSS_SELECTOR, "li:nth-child(10) > a").click()  # 点击雅思考位查询
    # browser.find_element(By.CSS_SELECTOR, "li:nth-child(14) > a").click()  # 点击UKVI考位查询
    time.sleep(WAIT_TIME_L)
    place_list = ["mvfSiteProvinces211", "mvfSiteProvinces212",
                  # "mvfSiteProvinces213", "mvfSiteProvinces214",
                  # "mvfSiteProvinces221", "mvfSiteProvinces222", "mvfSiteProvinces223", "mvfSiteProvinces231",
                  # "mvfSiteProvinces232", "mvfSiteProvinces233", "mvfSiteProvinces234", "mvfSiteProvinces235",
                  # "mvfSiteProvinces236", "mvfSiteProvinces237", "mvfSiteProvinces241", "mvfSiteProvinces242",
                  # "mvfSiteProvinces243", "mvfSiteProvinces244", "mvfSiteProvinces250", "mvfSiteProvinces251",
                  # "mvfSiteProvinces252", "mvfSiteProvinces253", "mvfSiteProvinces261"
                  ]
    for item in place_list:
        browser.find_element(By.ID, "2020-04").click()  # 点击月份选择框
        time.sleep(WAIT_TIME_S)
        browser.find_element(By.ID, item).click()  # 点击省份框
        time.sleep(WAIT_TIME_S)
        browser.find_element(By.CSS_SELECTOR, ".myhomecon_bg").click()  # 点击空白处
        time.sleep(WAIT_TIME_S)
        browser.find_element(By.ID, "btnSearch").click()  # 点击查询按钮
        time.sleep(WAIT_TIME_L)
        try:
            browser.find_element_by_xpath("//*[text()='有名额']")  # 有名额则返回True
            logger.info("省份" + item + "有剩余")
            return True
        except Exception as e:
            logger.info("省份" + item + "无剩余")
            browser.find_element(By.ID, "btnBackToSearch").click()  # 无名额则查询下一个省份
            time.sleep(WAIT_TIME_S)
    logger.info("四月份雅思考试暂无剩余考位")
    return False
