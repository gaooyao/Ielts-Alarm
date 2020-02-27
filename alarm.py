from playsound import playsound
import logging
import requests
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest

from config import ACCESS_KEY_Id, ACCESS_SECRET, AUTHORIZATION

logger = logging.getLogger("log")


def alarm(message):
    logger.info("警报已触发，开始播放提示音")

    """
    阿里云发送
    """
    client = AcsClient(ACCESS_KEY_Id, ACCESS_SECRET, 'cn-hangzhou')
    request = CommonRequest()
    request.set_accept_format('json')
    request.set_domain('dysmsapi.aliyuncs.com')
    request.set_method('POST')
    request.set_protocol_type('https')
    request.set_version('2017-05-25')
    request.set_action_name('SendSms')

    request.add_query_param('RegionId', "cn-hangzhou")
    request.add_query_param('PhoneNumbers', "13718336593")
    request.add_query_param('SignName', "KisPig网")
    request.add_query_param('TemplateCode', "SMS_184215625")
    request.add_query_param('TemplateParam', "{\"message\": \"" + message + "\"}")

    response = client.do_action(request)
    logger.info("通知短信已发送%s", response)

    """
    又拍云发送
    """
    # url = "https://sms-api.upyun.com/api/messages"
    # headers = {'Authorization': AUTHORIZATION}
    # data = {
    #     "mobile": phone_number,
    #     "template_id": "1",
    #     "vars": message
    # }
    # res = requests.post(url=url, data=data, headers=headers)
    # logger.info("通知短信已发送%s", res.text)
    while True:
        playsound('./others/alarm.mp3')
