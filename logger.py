# coding=utf-8
import logging


def log_init():
    logger = logging.getLogger("log")
    logger.setLevel(level=logging.INFO)
    fmt = '%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'
    formatter = logging.Formatter(fmt)
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    console.setFormatter(formatter)

    # handler = logging.FileHandler("log.log")
    # handler.setLevel(logging.INFO)
    # handler.setFormatter(formatter)
    # logger.addHandler(handler)   #是否把log保存到文件

    logger.addHandler(console)
    logger.info("log初始化成功")