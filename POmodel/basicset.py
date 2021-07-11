# -*- coding: utf-8 -*-
# username: huangqun
"""
BasePage提供公共方法的封装，即和页面逻辑无关的封装
比如解决driver初始化的问题
步骤三
1.浏览器初始化，完成后到po建模的文件中添加继承父类
"""
from pprint import pprint

import yaml
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

from weixintest.testcase.get_data import get_cookies


class BasicSet:
    # Chrome Options是一个配置chrome启动时属性的类
    # 定义为方法，继承后还需调用方法，直接重写__init__，继承时会直接重构？？
    # def startbrowser(self):
    # 四.2 初始页配置
    # 测试数据赋值，参数化处理到get_data中，写的不是很顺，根据yml文件的标签来取到标签下的列表传入
    # with open( '../datas/testdatas.yml' , encoding='utf-8' ) as f:
    #     data = yaml.safe_load( f )
    # seccess_data = data['seccess']
    # fail_data = data['fail']
    # fail_name_none = fail_data['name_none']
    # fail_account_none = fail_data['account_none']
    # fail_exist_account_id = fail_data['exist_account_id']
    # fail_exist_phone_num = fail_data['exist_phone_num']
    # fail_phone_num_form = fail_data['phone_num_form']
    # fail_phone_none = fail_data['phone_none']
    # cast_path = data['title']
    # pprint(data)
    # pprint( cast_path[1] )
    _get_url = ""

    def __init__(self , base_driver=None):
        if base_driver == None:
            chrome_opts = webdriver.ChromeOptions()
            # 设置调试器地址 (debugger_address)
            chrome_opts.debugging_address = "127.0.0.1:9222"
            # ActionChains(self.driver)报w3c错误
            chrome_opts.add_experimental_option( 'w3c' , False )
            self.driver = webdriver.Chrome( options=chrome_opts )
            self.driver.maximize_window()
            # 看了直播，可以用cookie登录跳过二维码扫描登录
            self.driver.get( 'https://work.weixin.qq.com/wework_admin/loginpage_wx' )  # 进入到网页中才能设置cookie
            cookies = get_cookies()
            for cookie in cookies:
                self.driver.add_cookie( cookie )
            # 起始页可配化
            # self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
            self.driver.get( self._get_url )
            # 暂时无法解决企业微信需要扫码登录的问题，这里采用显示等待，等到手动登录后出现企业微信的logo图标再进行下一步操作
            WebDriverWait( self.driver , 20 ) \
                .until( lambda driver: self.driver.find_element_by_id( 'menu_index' ) )

            # self.driver.implicitly_wait(20)
            # # 发现执行过程中打开了两次浏览器,链式调用时调了多次BasicSet的构造函数？？
            # 单例模式思想，调用一次后改变状态使调用跳过
        else:
            # 将self.driver 添加一个WebDriver对象注解， 解决类型提示的问题:注解报错。。。。？？\
            # from selenium.webdriver.chrome.webdriver import WebDriver
            # 注解本身没有任何的赋值作用，方便IDE 操作
            self.driver: WebDriver = base_driver
            # 完犊子。。。加了base_driver又多弹出一个：没有给子类返回self.driver
            # 至此完成url初始化，其中可优化配置起始页，将url变成可配置私有属性，在具体方法中再给定url

    # 四.3 操作模块化，优化定位元素的调用方式
    def find_eles(self , by , ele=None):
        # 不传ele时传入的结构为:(By.XPATH, '//*[@id="_hmt_click"]/div[1]/div[4]/div[2]/a[1]')是一个元组
        if ele is None:
            return self.driver.find_element( *by )
        # 传ele时传入的结构为:By.XPATH, '//*[@id="_hmt_click"]/div[1]/div[4]/div[2]/a[1]'
        else:
            return self.driver.find_element( by=by , value=ele )

# if __name__ == '__main__':
#     driver = webdriver.Chrome()
#     driver.implicitly_wait( 10 )
#     driver.get( 'https://work.weixin.qq.com/wework_admin/loginpage_wx' )  # 进入到网页中才能设置cookie
#     print( driver.get_cookies() )
#     cookies = [{'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False, 'value': '1688850260931747'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False, 'value': 'FaGlBL5ZHnPHumQP233mfXNsFjReeAd4zStshNSeK4WvKZIT9uAQxsZ-rMFraelVkGsJfqQMAATzRBUEXjQ_a05-qzCbfztDFn4MwgZG2SI-pMsRE07YMn1ouUlVI8pTnAj9fh33wjJcNR3XYimcS3OBjIiGsAf-GmRgDBkHGf_Y13FyQ0HnEfwtdOsUFdHNP4hi1glyUKl_oiEVz60Uo3DweJ2nGh_Hlh-hTpwX4T0RbRmq3Py5wyd7X_SaUx6N4_-nfhMJTfM5FBfByr76zA'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False, 'value': '1688850260931747'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False, 'value': '1970325019462757'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False, 'value': 'direct'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False, 'value': 'a9148616'}, {'domain': '.qq.com', 'expiry': 1626108323, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False, 'value': 'GA1.2.756599326.1626021910'}, {'domain': 'work.weixin.qq.com', 'expiry': 1626053447, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/', 'secure': False, 'value': '2jhc8qc'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False, 'value': '17621935912708638'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.cs_ind', 'path': '/', 'secure': False, 'value': ''}, {'domain': '.qq.com', 'expiry': 1626021970, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.work.weixin.qq.com', 'expiry': 1657557908, 'httpOnly': False, 'name': 'wwrtx.c_gdpr', 'path': '/', 'secure': False, 'value': '0'}, {'domain': '.qq.com', 'expiry': 1689093923, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.178072952.1626021910'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False, 'value': 'LAo1wDAGySzqOu1IOslU6ZE-yxXPeMeIEyy0cec4qquL7U_-qoACubLLj3j5BKfW'}, {'domain': '.work.weixin.qq.com', 'expiry': 1628613925, 'httpOnly': False, 'name': 'wwrtx.i18n_lan', 'path': '/', 'secure': False, 'value': 'zh'}]
#     for cookie in cookies:
#         driver.add_cookie( cookie )
#     driver.get( 'https://work.weixin.qq.com/wework_admin/frame#index' )
