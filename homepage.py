# coding=utf-8
from farmework.base_page import BasePage
from farmework.logger import Logger
import time

logger = Logger(logger="homepage").getlog()
class HomePage(BasePage):
#搜索框和点击
    input_box = "xpath=>/html/body/div/div[3]/div/div[1]/div[1]/input"
    search_submit_btn = "xpath=>/html/body/div[1]/div[3]/div/div[1]/div[1]/span/i"
#筛选框
    button_1 = "xpath=>/html/body/div/div[3]/div/div[1]/div[1]/div[2]/label[1]/span[1]/span"
    button_2 = "xpath=>/html/body/div/div[3]/div/div[1]/div[1]/div[2]/label[2]/span[1]/span"
    button_3 = "xpath=>/html/body/div/div[3]/div/div[1]/div[1]/div[2]/label[3]/span[1]/span"
    button_4 = "xpath=>/html/body/div/div[3]/div/div[1]/div[1]/div[2]/label[4]/span[1]/span"
    button_5 = "xpath=>/html/body/div/div[3]/div/div[1]/div[1]/div[2]/label[5]/span[1]/span"
    #实体筛选框
    config_1 = 'xpath=>/html/body/div[1]/div[3]/div/div[3]/div/div/label[1]/span'
    config_2 = 'xpath=>/html/body/div[1]/div[3]/div/div[3]/div/div/label[2]/span'
    config_3 = 'xpath=>/html/body/div[1]/div[3]/div/div[3]/div/div/label[3]/span'
    config_4 = 'xpath=>/html/body/div[1]/div[3]/div/div[3]/div/div/label[4]/span'
    config_5 = 'xpath=>/html/body/div[1]/div[3]/div/div[3]/div/div/label[5]/span'
#搜索
    exact_search = "xpath=>/html/body/div/div[3]/div/div[1]/div[2]/div/label[1]/span"
    fuzzy_search = "xpath=>/html/body/div/div[3]/div/div[1]/div[2]/div/label[2]/span"
#高级搜索
    advanced_search= "xpath=>/html/body/div[1]/div[3]/div/div[1]/div[2]/button"
    #实体
    box_1 = "css_selector=>.high_extra-label > div:nth-child(2) > div:nth-child(1)"
    box_1_1 = "xpath=>/html/body/div[3]/div[1]/div[1]/ul/li[1]/span"
    box_1_2 = "xpath=>/html/body/div[3]/div[1]/div[1]/ul/li[2]/span"
    box_1_3 = "xpath=>/html/body/div[3]/div[1]/div[1]/ul/li[3]/span"
    box_1_4 = "xpath=>/html/body/div[3]/div[1]/div[1]/ul/li[4]"
    box_1_5 = "xpath=>/html/body/div[3]/div[1]/div[1]/ul/li[5]"
    #属性拉框
    box_2 = "xpath=>/html/body/div[2]/div[1]/div[2]/div/div/div[2]/div[1]/input"
    box_2_1 = "xpath=>/html/body/div[4]/div[1]/div[1]/ul/li[1]"
    box_2_2 = "xpath=>/html/body/div[4]/div[1]/div[1]/ul/li[2]"
    box_2_3 = "xpath=>/html/body/div[4]/div[1]/div[1]/ul/li[3]"
    box_2_4 = "xpath=>/html/body/div[4]/div[1]/div[1]/ul/li[4]"
    box_2_5 = "xpath=>/html/body/div[4]/div[1]/div[1]/ul/li[5]"
    box_2_6 = "xpath=>/html/body/div[4]/div[1]/div[1]/ul/li[6]"
    #属性关系
    box_3 = "xpath=>/html/body/div[2]/div[1]/div[2]/div/div/div[3]/div[1]/input"
    box_3_1 = "xpath=>/html/body/div[5]/div[1]/div[1]/ul/li[1]"
    box_3_2 = "xpath=>/html/body/div[5]/div[1]/div[1]/ul/li[2]"
    box_3_3 = "xpath=>/html/body/div[5]/div[1]/div[1]/ul/li[3]"
    box_3_4 = "xpath=>/html/body/div[5]/div[1]/div[1]/ul/li[4]"
    #属性关联值
    box_4 = "xpath=>/html/body/div[2]/div[1]/div[2]/div/div/div[4]/input"
    #确认-重置-增加-与或-取消
    confirm = "xpath=>/html/body/div[2]/div[1]/div[3]/div[1]/button"
    retry = 'xpath=>/html/body/div[2]/div[1]/div[3]/div[2]/button'
    add_proprety = "xpath=>/html/body/div[2]/div[1]/div[2]/div/div/span[1]"
    an_d = 'xpath=>/html/body/div[2]/div[1]/div[2]/div/div[2]/div[1]/div[1]/div[2]/input'
    o_r = 'xpath=>/html/body/div[2]/div[1]/div[2]/div/div[2]/div[1]/div[2]/div[2]/input'
    delete = 'xpath=>/html/body/div[2]/div[1]/div[2]/div/div[2]/span[2]'
    box_5 = 'xpath=>/html/body/div[2]/div[1]/div[2]/div/div[2]/div[2]/div[1]/input'
    box_5_1 = 'xpath=>/html/body/div[6]/div[1]/div[1]/ul/li[1]/span'
    box_6 = 'xpath=>/html/body/div[2]/div[1]/div[2]/div/div[2]/div[3]/div[1]/input'
    box_6_1 = 'xpath=>/html/body/div[7]/div[1]/div[1]/ul/li[1]'
    box_7 = 'xpath=>/html/body/div[2]/div[1]/div[2]/div/div[2]/div[4]/input'
    box_8 = 'xpath=>/html/body/div[2]/div[1]/div[2]/div/div[3]/div[2]/div[1]/input'
    box_8_2 = 'xpath=>/html/body/div[8]/div[1]/div[1]/ul/li[2]/span'
    box_9 = 'xpath=>/html/body/div[2]/div[1]/div[2]/div/div[3]/div[3]/div[1]/input'
    box_9_1 = 'xpath=>/html/body/div[9]/div[1]/div[1]/ul/li[1]/span'
    box_10 = 'xpath=>/html/body/div[2]/div[1]/div[2]/div/div[3]/div[4]/input'
    add_proprety_2 = 'xpath=>/html/body/div[2]/div[1]/div[2]/div/div[2]/span[1]'
    delete_2 = 'xpath=>/html/body/div[2]/div[1]/div[2]/div/div[3]/span[2]'
#选择结果
    #选框
    choose_all = 'xpath=>/html/body/div[1]/div[3]/div/div[4]/div[1]/div/label[1]/span'
    choose_1 = 'xpath=>/html/body/div[1]/div[3]/div/div[4]/div[2]/div[1]/div/div[1]/label/span[1]/span'
    choose_2 = 'xpath=>/html/body/div[1]/div[3]/div/div[4]/div[2]/div[2]/div/div[1]/label/span[1]/span'
    choose_3 = 'xpath=>/html/body/div[1]/div[3]/div/div[4]/div[2]/div[3]/div/div[1]/label/span[1]/span'
    choose_4 = 'xpath=>/html/body/div[1]/div[3]/div/div[4]/div[2]/div[4]/div/div[1]/label/span[1]/span'
    choose_5 = 'xpath=>/html/body/div[1]/div[3]/div/div[4]/div[2]/div[5]/div/div[1]/label/span[1]/span'
    choose_6 = 'xpath=>/html/body/div[1]/div[3]/div/div[4]/div[2]/div[6]/div/div[1]/label/span[1]/span'
    #页面
    path_2 = 'xpath=>/html/body/div[1]/div[3]/div/div[4]/div[3]/div/ul/li[2]'
    path_some = 'xpath=>/html/body/div[1]/div[3]/div/div[4]/div[3]/div/ul/li[7]'
    path_input = 'css_selector=>div.task-container:nth-child(4) > div:nth-child(3) > div:nth-child(1) > span:nth-child(5) > div:nth-child(1) > input:nth-child(1)'
    path_next = 'xpath=>/html/body/div[1]/div[3]/div/div[4]/div[3]/div/button[2]'
    path_last = 'xpath=>/html/body/div[1]/div[3]/div/div[4]/div[3]/div/button[1]'
#进入分析
    analysis_button = 'xpath=>/html/body/div[1]/div[3]/div/div[4]/div[1]/div/button'
#图谱分析



#搜索点击
    #搜索框



    def type_search(self, text):
        self.type(self.input_box, text)
        logger.info("搜索框输入")
    #清除搜索框
    def clear_search(self):
        self.clear(self.input_box)
        logger.info('清空搜索框')
    #模糊搜索
    def click_fuzzy_search(self):
        self.click(self.fuzzy_search)
        logger.info("点击模糊搜索")
    #精确搜索
    def click_exact_search(self):
        self.click(self.exact_search)
        logger.info('点击精确搜索')
    #搜索
    def send_submit_btn(self):
        self.click(self.search_submit_btn)
        time.sleep(1)
        logger.info("点击搜索按钮")
#高级搜索
    def click_advaced_search(self):
        self.click(self.advanced_search)
        time.sleep(1)
        logger.info('点击高级搜索')
    #实体
    def click_box_1(self):
        self.click(self.box_1)
        time.sleep(1)
        logger.info("点击实体下拉框")
    def click_box_1_1(self):
        self.click(self.box_1_1)
        logger.info('选择实体化学品')
    def click_box_1_2(self):
        self.click(self.box_1_2)
        logger.info('选择实体化工企业')

    def click_box_1_3(self):
        self.click(self.box_1_3)
        logger.info('选择实体重大危险源')
    def click_box_1_4(self):
        self.click(self.box_1_4)
    def click_box_1_5(self):
        self.click(self.box_1_5)
        logger.info('选择实体法律法规')
    #属性
    def click_box_2(self):
        time.sleep(1)
        self.click(self.box_2)
        time.sleep(1)
        logger.info('点击属性下拉框')
    def click_box_2_1(self):
        self.click(self.box_2_1)
        logger.info('选择属性1')
    def click_box_2_2(self):
        self.click(self.box_2_2)
        logger.info('选择属性2')
    def click_box_2_3(self):
        self.click(self.box_2_3)
        logger.info('选择属性3')
    def click_box_2_4(self):
        self.click(self.box_2_4)
        logger.info('选择属性4')
    def click_box_2_5(self):
        self.click(self.box_2_5)
        logger.info('选择属性5')
    def click_box_2_6(self):
        self.click(self.box_2_6)
        logger.info('选择属性6')
    def click_box_5(self):
        time.sleep(1)
        self.click(self.box_5)
        time.sleep(1)
        logger.info('点击新增属性框5')
    def click_box_5_1(self):
        self.click(self.box_5_1)
        logger.info('选择属性法律法规')
    def click_box_6(self):
        time.sleep(1)
        self.click(self.box_6)
        time.sleep(1)
        logger.info('点击新增属性框6')
    def click_box_6_1(self):
        self.click(self.box_6_1)
        logger.info('选择关系包含')
    def type_box_7(self,text):
        time.sleep(1)
        time.sleep(1)
        self.type(self.box_7,text)
        logger.info('新增输入框输入')
    def click_add_proprety(self):
        self.click(self.add_proprety)
        logger.info('添加新条件1')
    def click_add_proprety_2(self):
        self.click(self.add_proprety_2)
        logger.info('添加新条件2')
    def click_an_d(self):
        self.click(self.an_d)
        logger.info('选择关系与')
    def click_o_r(self):
        self.click(self.o_r)
        logger.info('选择关系或')
    def click_delete(self):
        self.click(self.delete)
        logger.info('删除属性1')
    def click_delete_2(self):
        self.click(self.delete_2)
        logger.info('删除属性2')
    def click_box_8(self):
        time.sleep(1)
        self.click(self.box_8)
        time.sleep(1)
        logger.info('点击选框8')
    def click_box_8_2(self):
        self.click(self.box_8_2)
        logger.info('选择属性发布部门')
    def click_box_9(self):
        time.sleep(1)
        self.click(self.box_9)
        time.sleep(1)
        logger.info('点击选框9')
    def click_box_9_1(self):
        self.click(self.box_9_1)
        logger.info('选择关系包含')
    def type_box_10(self,text):
        time.sleep(1)
        self.type(self.box_10,text)
        time.sleep(1)
        logger.info('新增关系3输入')

    #关系
    def click_box_3(self):
        time.sleep(1)
        self.click(self.box_3)
        time.sleep(1)
        logger.info('点击关系下拉框')
    def click_box_3_1(self):
        self.click(self.box_3_1)
        logger.info('选择关系1')
    def click_box_3_2(self):
        self.click(self.box_3_2)
        logger.info('选择关系2')
    def click_box_3_3(self):
        self.click(self.box_3_3)
    def click_box_3_4(self):
        self.click(self.box_3_4)
    '''
    条件增加
    '''
    #输入内容
    def type_box_4(self, text):
        time.sleep(1)
        self.type(self.box_4,text)
        time.sleep(1)
        logger.info("关系值输入")
    #确认-重置
    def click_confirm(self):
        time.sleep(1)
        self.click(self.confirm)
        logger.info('点击确认')
    def click_retry(self):
        self.click(self.retry)
        logger.info('重置')

#筛选
    def click_button_1(self):
        self.click(self.button_1)
        logger.info("点击筛选按钮1")
    def click_button_2(self):
        self.click(self.button_2)
        logger.info("点击筛选按钮2")
    def click_button_3(self):
        self.click(self.button_3)
        logger.info("点击筛选按钮3")
    def click_button_4(self):
        self.click(self.button_4)
        logger.info("点击筛选按钮4")
    def click_button_5(self):
        self.click(self.button_5)
        logger.info("点击筛选按钮5")
#实体筛选
    def click_config_1(self):
        self.click(self.config_1)
        logger.info("点击实体筛选按钮1")
        time.sleep(1)
    def click_config_2(self):
        self.click(self.config_2)
        logger.info("点击实体筛选按钮2")
        time.sleep(1)
    def click_config_3(self):
        self.click(self.config_3)
        logger.info("点击实体筛选按钮3")
        time.sleep(1)
    def click_config_4(self):
        self.click(self.config_4)
        logger.info("点击实体筛选按钮4")
        time.sleep(1)
    def click_config_5(self):
        self.click(self.config_5)
        logger.info("点击实体筛选按钮5")
        time.sleep(1)
#选择结果
    #选框
    def click_choose_all(self):
        self.click(self.choose_all)
        logger.info("勾选全部")
    def click_choose_1(self):
        self.click(self.choose_1)
        logger.info("勾选选框1")
    def click_choose_2(self):
        self.click(self.choose_2)
        logger.info("勾选选框2")
    def click_choose_3(self):
        self.click(self.choose_3)
        logger.info("勾选选框3")
    def click_choose_4(self):
        self.click(self.choose_4)
        logger.info("勾选选框4")
    def click_choose_5(self):
        self.click(self.choose_5)
        logger.info("勾选选框5")
    def click_choose_6(self):
        self.click(self.choose_6)
        logger.info('勾选选框6')
#进入图谱分析
    def click_analysis_button(self):
        self.click(self.analysis_button)
        time.sleep(1)
        logger.info("点击图谱分析按钮")
#选择页面
    def click_path_2(self):
        self.click(self.path_2)
        time.sleep(1)
        logger.info("跳转页面2")
    def click_path_some(self):
        self.click(self.path_some)
        time.sleep(1)
        logger.info("跳转页面。。。")
    def click_path_next(self):
        self.click(self.path_next)
        time.sleep(1)
        logger.info('点击下一页')
    def click_path_last(self):
        self.click(self.path_last)
        time.sleep(1)
        logger.info('点击上一页')
    #输入页数
    def type_path_input(self,text):
        self.type(self.path_input, text)
        logger.info("输入页数")


    #确认
    def enter_confirm(self):
        self.enter(self.path_input)
        time.sleep(1)
        logger.info("敲击enter")