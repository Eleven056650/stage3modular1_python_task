# -*- coding: utf-8 -*-
# username: huangqun
"""
步骤一
1.plantuml画出模块功能及时序关系
2.page Object阶段实现架构建模，只定义类名、方法名，具体实现先pass
3.方法结束后需return 指向时序的下一个类功能
步骤四
1.补充之前建模时pass的地方具体实现的代码
以往经验：
实现参数模块化抓取元素，日志管理（不在业务逻辑范围内，考虑并入basicset）
测试用例数据参数化
"""
import time

from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.by import By
from weixintest.POmodel.add_members_page import AddMembers
from weixintest.POmodel.address_list_page import AddressList
from weixintest.POmodel.basicset import BasicSet


class HomePage( BasicSet ):
    _goto_add_member = (By.XPATH , '//*[@id="_hmt_click"]/div[1]/div[4]/div[2]/a[1]')
    _goto_address_list = (By.ID , 'menu_contacts')
    _get_url = "https://work.weixin.qq.com/wework_admin/frame#index"
    _homepage = (By.ID , 'menu_index')
    _quit_button = (By.CSS_SELECTOR , '[node-type=cancel]')
    _div_alter = (By.CSS_SELECTOR , '[node-type=cancel]')

    def add_member_button(self):
        """
        1.首页点击添加成员按钮
        2.进入添加成员页面
        :return:
        """
        # 定位元素模块化，定位方式及定位元素提取出来作为两个参数，写入basicset的find_element方法中
        # self.driver.find_element(By.XPATH, '//*[@id="_hmt_click"]/div[1]/div[4]/div[2]/a[1]').click()
        self.driver.implicitly_wait( 2 )
        self.find_eles( self._goto_add_member ).click()
        return AddMembers( self.driver )

    def click_address_list(self):
        """
        1.首页点击通讯录页签
        2.进入通讯录页面
        :return:
        """
        self.driver.implicitly_wait( 2 )
        self.find_eles( self._goto_address_list ).click()
        return AddressList( self.driver )

    # 返回首页
    def turnback_homepage(self):
        self.find_eles( self._homepage ).click()
        time.sleep( 2 )
        try:
            div_alter = self.find_eles( self._div_alter )
            if div_alter is not None:
                self.find_eles( self._quit_button ).click()
        except:
            NoAlertPresentException
        return False
