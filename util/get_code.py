# coding=utf-8
from PIL import Image
from util.ShowapiRequest import ShowapiRequest
import time


class GetCode:
    def __init__(self,driver):
        self.driver = driver

    def get_code_image(self,file_name):
        self.driver.save_screenshot(file_name)   # 截取全屏，并保存在file_name路径下
        code_element = self.driver.find_element_by_id("getcode_num")
        # 获取验证码图片的坐标
        left = code_element.location['x']
        top = code_element.location['y']
        right = code_element.size['width']+left
        height = code_element.size['height']+top
        im = Image.open(file_name)
        img = im.crop((left,top,right,height))  # 按照坐标切割验证码图片块
        img.save(file_name)
        time.sleep(1)

    # 解析图片获取验证码
    def code_online(self,file_name):
        self.get_code_image(file_name)
        # 使用第三方解析工具解析图片验证码
        r = ShowapiRequest("http://route.showapi.com/184-4","62626","d61950be50dc4dbd9969f741b8e730f5" )
        r.addBodyPara("typeId", "35")
        r.addBodyPara("convert_to_jpg", "0")
        r.addFilePara("image", file_name) #文件上传时设置
        res = r.post()
        time.sleep(1)
        text = res.json()['showapi_res_body']
        #print(text)
        code = text['Result']
        return code   # 返回解析后的验证码信息
