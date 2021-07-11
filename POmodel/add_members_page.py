# -*- coding: utf-8 -*-
# username: huangqun
"""
步骤一
plantuml画出模块功能及时序关系
page Object阶段实现架构建模，只定义类名、方法名，具体实现先pass
方法结束后需return 指向时序的下一个类功能
步骤四
1.补充之前建模时pass的地方具体实现的代码
"""

from selenium.webdriver.common.by import By
from weixintest.POmodel.address_list_page import AddressList
from weixintest.POmodel.basicset import BasicSet


class AddMembers( BasicSet ):
    _user_name = (By.ID , 'username')
    _accountid = (By.ID , 'memberAdd_acctid')
    _phone = (By.NAME , 'mobile')
    _save_button = (By.CSS_SELECTOR , '.js_btn_save')

    def fill_in_member_information(self , name , id , tel):
        """
        1.填写成员信息
        2.点击保存按钮
        3.返回通讯录页面
        :return:
        """
        self.driver.implicitly_wait( 2 )
        self.find_eles( self._user_name ).send_keys( name )
        self.find_eles( self._accountid ).send_keys( id )
        self.find_eles( self._phone ).send_keys( tel )
        self.find_eles( self._save_button ).click()
        return AddressList( self.driver )
