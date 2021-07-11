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
# from weixintest.POmodel.add_members_page import AddMembers # 这里会报循环导入的错误，写进方法里避免
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from weixintest.POmodel.basicset import BasicSet


class AddressList( BasicSet ):
    # 类属性私有化，封装在类内部，避免外部读取，提高代码可读性
    _add_button = (By.LINK_TEXT , '添加成员')
    _get_url = "https://work.weixin.qq.com/wework_admin/frame#contacts"

    def add_member_button(self):
        from weixintest.POmodel.add_members_page import AddMembers

        """
        1.通讯录界面点击添加成员按钮
        2.进入添加成员界面
        :return:
        """
        self.driver.implicitly_wait( 2 )
        self.find_eles( self._add_button ).click()
        # a = self.find_eles( self._add_button )
        # action = ActionChains(self.driver)
        # action.click(a).perform()

        return AddMembers( self.driver )

    def get_member_information(self):
        """
        1.通讯录界面获取成员列表信息
        2.用于断言，断言不写在方法中
        :return:
        """
        self.driver.implicitly_wait( 2 )
        # 找到一条数据中的名字元素
        # 四.1 find_elements  返回的不只是一个元素
        ele = self.driver.find_elements( By.CSS_SELECTOR , '.member_colRight_memberTable_td:nth-child(2)' )
        name_list = [i.text for i in ele]
        return name_list
