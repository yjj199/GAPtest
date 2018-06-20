# coding=utf-8
import time
import unittest
# from selenium.webdriver.common.action_chains import ActionChains
from farmework.browser_engine import BrowserEngine
from pageobjects.analysisPage import AnalysisPage
from pageobjects.homepage import HomePage
from farmework.base_page import BasePage
# from selenium import webdriver


class Ring(unittest.TestCase):
    @classmethod
    def setUp(self):
        """
        测试固件的setUp()的代码，主要是测试的前提准备工作
        :return:
        """
        browse = BrowserEngine(self)
        self.driver = browse.open_browser(self)
        BasePage.login(self)

    @classmethod
    def tearDown(self):
        """
        测试结束后的操作，这里基本上都是关闭浏览器
        :return:
        """
        self.driver.quit()




    def test_toolbar_01(self):
        homepage=HomePage(self.driver)
        analysispage=AnalysisPage(self.driver)
        homepage.type_search("甲醛")  # 输入框中输入甲醛5t6
        homepage.send_submit_btn()  # 点击搜索按钮
        homepage.click_config_2()  # 点击实体筛选框2（此处根据搜索结果来排列，当前化学品位于筛选框第2）
        homepage.click_choose_all()  # 点击勾选 所有 （当前化学品只有1条）
        homepage.click_analysis_button()  # d点击进入图谱分析界面
        analysispage.right_click_node()
        time.sleep(1)
        # huagong=(self.driver).find_elements_by_link_text('化工企业')
        # webdriver.ActionChains(self.driver).move_to_element(huagong)
        analysispage.ac()
        time.sleep(3)
        # shaixuan=(self.driver).find_element_by_class_name('secondPiePath')
        # shaixuan.click()
        # analysispage.move_el_ring_huagong()
        # time.sleep(1)
        # analysispage.click_huagong_shaixuan()
        BasePage.get_windows_img1(self)  # 调用基类截图方法


    def test_toolbar_02(self):
        homepage=HomePage(self.driver)
        analysispage=AnalysisPage(self.driver)
        homepage.type_search("甲醛")  # 输入框中输入甲醛5t6
        homepage.send_submit_btn()  # 点击搜索按钮
        homepage.click_config_2()  # 点击实体筛选框2（此处根据搜索结果来排列，当前化学品位于筛选框第2）
        homepage.click_choose_all()  # 点击勾选 所有 （当前化学品只有1条）
        homepage.click_analysis_button()  # d点击进入图谱分析界面
        analysispage.right_click_node()
        time.sleep(1)
        analysispage.move_el_huanxing_huagong()
        # analysispage.click_#点击化工企业显示
        BasePage.get_windows_img1(self)  # 调用基类截图方法


    def test_toolbar_03(self):
        homepage=HomePage(self.driver)
        analysispage=AnalysisPage(self.driver)
        homepage.type_search("甲醛")  # 输入框中输入甲醛
        homepage.send_submit_btn()  # 点击搜索按钮
        homepage.click_config_2()  # 点击实体筛选框2（此处根据搜索结果来排列，当前化学品位于筛选框第2）
        homepage.click_choose_all()  # 点击勾选 所有 （当前化学品只有1条）
        homepage.click_analysis_button()  # d点击进入图谱分析界面
        analysispage.right_click_node()
        time.sleep(1)
        analysispage.move_el_huanxing_huagong()#移动至化工企业
        analysispage.click_shaixuan1()#点击筛选
        analysispage.click_province()#点击下拉列表
        analysispage.click_province_1()#点击北京
        #市区默认
        analysispage.click_size()#点击企业规模下拉列表
        analysispage.click_size_1()#其他
        analysispage.click_sx_relation()#点击关系下拉列表
        analysispage.click_sx_relation_1()#关系原料
        analysispage.click_chemical_sxbutton()#点击筛选按钮
        BasePage.get_windows_img1(self)  # 调用基类截图方法

    def test_toolbar_04(self):
        homepage=HomePage(self.driver)
        analysispage=AnalysisPage(self.driver)
        homepage.type_search("甲醛")  # 输入框中输入甲醛
        homepage.send_submit_btn()  # 点击搜索按钮
        homepage.click_config_2()  # 点击实体筛选框2（此处根据搜索结果来排列，当前化学品位于筛选框第2）
        homepage.click_choose_all()  # 点击勾选 所有 （当前化学品只有1条）
        homepage.click_analysis_button()  # d点击进入图谱分析界面
        analysispage.right_click_node()
        time.sleep(1)
        analysispage.move_el_huanxing_huagong()
        time.sleep(1)
        analysispage.click_shaixuan1()
        analysispage.click_province()
        analysispage.click_province_2()#点击天津
        analysispage.click_size()
        analysispage.click_size_2()#点击微型企业
        analysispage.click_sx_relation()
        analysispage.click_sx_relation_2()#点击关系 进口
        analysispage.click_chemical_sxbutton()
        BasePage.get_windows_img1(self)  # 调用基类截图方法


    def test_toolbar_05(self):
        homepage=HomePage(self.driver)
        analysispage=AnalysisPage(self.driver)
        homepage.type_search("甲醛")  # 输入框中输入甲醛
        homepage.send_submit_btn()  # 点击搜索按钮
        homepage.click_config_2()  # 点击实体筛选框2（此处根据搜索结果来排列，当前化学品位于筛选框第2）
        homepage.click_choose_all()  # 点击勾选 所有 （当前化学品只有1条）
        homepage.click_analysis_button()  # d点击进入图谱分析界面
        analysispage.right_click_node()
        time.sleep(1)
        analysispage.move_el_huanxing_huagong()
        time.sleep(1)
        analysispage.click_shaixuan1()
        analysispage.click_province()
        analysispage.click_province_3()#点击湖北
        analysispage.click_size()
        analysispage.click_size_3()#点击小型企业
        analysispage.click_sx_relation()
        analysispage.click_sx_relation_3()#点击关系中间产品
        analysispage.click_chemical_sxbutton()
        BasePage.get_windows_img1(self)  # 调用基类截图方法

    def test_toolbar_06(self):
        homepage=HomePage(self.driver)
        analysispage=AnalysisPage(self.driver)
        homepage.type_search("甲醛")  # 输入框中输入甲醛
        homepage.send_submit_btn()  # 点击搜索按钮
        homepage.click_config_2()  # 点击实体筛选框2（此处根据搜索结果来排列，当前化学品位于筛选框第2）
        homepage.click_choose_all()  # 点击勾选 所有 （当前化学品只有1条）
        homepage.click_analysis_button()  # d点击进入图谱分析界面
        analysispage.right_click_node()
        time.sleep(1)
        analysispage.move_el_huanxing_huagong()
        time.sleep(1)
        analysispage.click_shaixuan1()
        analysispage.click_province()
        analysispage.click_province_4()#贵州
        analysispage.click_city()
        analysispage.click_city_3()#荆门
        analysispage.click_size()
        analysispage.click_size_4()#规模中型企业
        analysispage.click_sx_relation()
        analysispage.click_sx_relation_4()#关系产品
        analysispage.click_chemical_sxbutton()
        BasePage.get_windows_img1(self)  # 调用基类截图方法

    def test_toolbar_07(self):
        homepage=HomePage(self.driver)
        analysispage=AnalysisPage(self.driver)
        homepage.type_search("甲醛")  # 输入框中输入甲醛
        homepage.send_submit_btn()  # 点击搜索按钮
        homepage.click_config_2()  # 点击实体筛选框2（此处根据搜索结果来排列，当前化学品位于筛选框第2）
        homepage.click_choose_all()  # 点击勾选 所有 （当前化学品只有1条）
        homepage.click_analysis_button()  # d点击进入图谱分析界面
        analysispage.right_click_node()
        time.sleep(1)
        analysispage.move_el_huanxing_huagong()
        time.sleep(1)
        analysispage.click_shaixuan1()
        analysispage.click_province()
        analysispage.click_province_5()#台湾
        analysispage.click_city()
        analysispage.click_city_4()#城市遵义
        analysispage.click_size()
        analysispage.click_size_5()#大型企业
        analysispage.click_sx_relation()
        analysispage.click_sx_relation_1()#各个控件的有效数据组合，优化用例
        analysispage.click_chemical_sxbutton()
        BasePage.get_windows_img1(self)  # 调用基类截图方法

    def test_toolbar_08(self):
        homepage=HomePage(self.driver)
        analysispage=AnalysisPage(self.driver)
        homepage.type_search("甲醛")  # 输入框中输入甲醛
        homepage.send_submit_btn()  # 点击搜索按钮
        homepage.click_config_2()  # 点击实体筛选框2（此处根据搜索结果来排列，当前化学品位于筛选框第2）
        homepage.click_choose_all()  # 点击勾选 所有 （当前化学品只有1条）
        homepage.click_analysis_button()  # d点击进入图谱分析界面
        analysispage.right_click_node()
        time.sleep(1)
        analysispage.move_el_huanxing_huagong()
        time.sleep(1)
        analysispage.click_shaixuan1()
        analysispage.click_province()
        analysispage.click_province_5()
        analysispage.click_city()
        analysispage.click_city_5()
        analysispage.click_size()
        analysispage.click_size_3()
        analysispage.click_sx_relation()
        analysispage.click_sx_relation_2()
        analysispage.click_chemical_sxbutton()
        BasePage.get_windows_img1(self)  # 调用基类截图方法

    def test_toolbar_09(self):
        homepage=HomePage(self.driver)
        analysispage=AnalysisPage(self.driver)
        homepage.type_search("甲醛")  # 输入框中输入甲醛
        homepage.send_submit_btn()  # 点击搜索按钮
        homepage.click_config_2()  # 点击实体筛选框2（此处根据搜索结果来排列，当前化学品位于筛选框第2）
        homepage.click_choose_all()  # 点击勾选 所有 （当前化学品只有1条）
        homepage.click_analysis_button()  # d点击进入图谱分析界面
        analysispage.right_click_node()
        time.sleep(1)
        analysispage.move_el_huanxing_huagong()
        time.sleep(1)
        analysispage.click_shaixuan1()
        analysispage.click_chemical_qxbutton()#点击取消按钮
        BasePage.get_windows_img1(self)  # 调用基类截图方法


    def test_toolbar_10(self):
        homepage=HomePage(self.driver)
        analysispage=AnalysisPage(self.driver)
        homepage.type_search("甲醛")  # 输入框中输入甲醛
        homepage.send_submit_btn()  # 点击搜索按钮
        homepage.click_config_2()  # 点击实体筛选框2（此处根据搜索结果来排列，当前化学品位于筛选框第2）
        homepage.click_choose_all()  # 点击勾选 所有 （当前化学品只有1条）
        homepage.click_analysis_button()  # d点击进入图谱分析界面
        # analysispage.移动到重大危险源
        #        点击显示按钮
        BasePage.get_windows_img1(self)  # 调用基类截图方法

    def test_toolbar_11(self):
        homepage=HomePage(self.driver)
        analysispage=AnalysisPage(self.driver)
        homepage.type_search("甲醛")  # 输入框中输入甲醛
        homepage.send_submit_btn()  # 点击搜索按钮
        homepage.click_config_2()  # 点击实体筛选框2（此处根据搜索结果来排列，当前化学品位于筛选框第2）
        homepage.click_choose_all()  # 点击勾选 所有 （当前化学品只有1条）
        homepage.click_analysis_button()  # d点击进入图谱分析界面
        #移动到环形菜单 重大危险源
        #点击重大危险源 筛选
        analysispage.click_dangerous()
        analysispage.click_dangerous_1()
        # analysispage.click_dangerous_sxbutton()#点击筛选按钮
        BasePage.get_windows_img1(self)  # 调用基类截图方法

    def test_toolbar_12(self):
        homepage=HomePage(self.driver)
        analysispage=AnalysisPage(self.driver)
        homepage.type_search("甲醛")  # 输入框中输入甲醛
        homepage.send_submit_btn()  # 点击搜索按钮
        homepage.click_config_2()  # 点击实体筛选框2（此处根据搜索结果来排列，当前化学品位于筛选框第2）
        homepage.click_choose_all()  # 点击勾选 所有 （当前化学品只有1条）
        homepage.click_analysis_button()  # d点击进入图谱分析界面
        #移动到环形菜单 重大危险源
        #点击重大危险源 筛选
        analysispage.click_dangerous()
        analysispage.click_dangerous_2()#危险等级 2
        # analysispage.click_dangerous_sxbutton()#点击筛选按钮
        BasePage.get_windows_img1(self)  # 调用基类截图方法

    def test_toolbar_13(self):
        homepage=HomePage(self.driver)
        analysispage=AnalysisPage(self.driver)
        homepage.type_search("甲醛")  # 输入框中输入甲醛
        homepage.send_submit_btn()  # 点击搜索按钮
        homepage.click_config_2()  # 点击实体筛选框2（此处根据搜索结果来排列，当前化学品位于筛选框第2）
        homepage.click_choose_all()  # 点击勾选 所有 （当前化学品只有1条）
        homepage.click_analysis_button()  # d点击进入图谱分析界面
        #移动到环形菜单 重大危险源
        #点击重大危险源 筛选
        analysispage.click_dangerous()
        analysispage.click_dangerous_3()
        # analysispage.click_dangerous_sxbutton()#点击筛选按钮
        BasePage.get_windows_img1(self)  # 调用基类截图方法

    def test_toolbar_14(self):
        homepage=HomePage(self.driver)
        analysispage=AnalysisPage(self.driver)
        homepage.type_search("甲醛")  # 输入框中输入甲醛
        homepage.send_submit_btn()  # 点击搜索按钮
        homepage.click_config_2()  # 点击实体筛选框2（此处根据搜索结果来排列，当前化学品位于筛选框第2）
        homepage.click_choose_all()  # 点击勾选 所有 （当前化学品只有1条）
        homepage.click_analysis_button()  # d点击进入图谱分析界面
        #移动到环形菜单 重大危险源
        #点击重大危险源 筛选
        analysispage.click_dangerous()
        analysispage.click_dangerous_4()
        # analysispage.click_dangerous_sxbutton()#点击筛选按钮
        BasePage.get_windows_img1(self)  # 调用基类截图方法

    def test_toolbar_15(self):
        homepage=HomePage(self.driver)
        analysispage=AnalysisPage(self.driver)
        homepage.type_search("甲醛")  # 输入框中输入甲醛
        homepage.send_submit_btn()  # 点击搜索按钮
        homepage.click_config_2()  # 点击实体筛选框2（此处根据搜索结果来排列，当前化学品位于筛选框第2）
        homepage.click_choose_all()  # 点击勾选 所有 （当前化学品只有1条）
        homepage.click_analysis_button()  # d点击进入图谱分析界面
        #移动到环形菜单 重大危险源
        #点击重大危险源 筛选
        analysispage.click_dangerous()
        analysispage.click_dangerous_1()
        # analysispage.click_dangerous_qxbutton()#点击筛选按钮
        BasePage.get_windows_img1(self)  # 调用基类截图方法


    def test_toolbar_16(self):
        homepage=HomePage(self.driver)
        analysispage=AnalysisPage(self.driver)
        homepage.type_search("甲醛")  # 输入框中输入甲醛
        homepage.send_submit_btn()  # 点击搜索按钮
        homepage.click_config_2()  # 点击实体筛选框2（此处根据搜索结果来排列，当前化学品位于筛选框第2）
        homepage.click_choose_all()  # 点击勾选 所有 （当前化学品只有1条）
        homepage.click_analysis_button()  # d点击进入图谱分析界面
        #移动到环形菜单 事故信息
        #点击事故信息 显示
        BasePage.get_windows_img1(self)  # 调用基类截图方法

    def test_toolbar_17(self):
        homepage=HomePage(self.driver)
        analysispage=AnalysisPage(self.driver)
        homepage.type_search("甲醛")  # 输入框中输入甲醛
        homepage.send_submit_btn()  # 点击搜索按钮
        homepage.click_config_2()  # 点击实体筛选框2（此处根据搜索结果来排列，当前化学品位于筛选框第2）
        homepage.click_choose_all()  # 点击勾选 所有 （当前化学品只有1条）
        homepage.click_analysis_button()  # d点击进入图谱分析界面
        #移动到环形菜单 事故信息
        #点击事故信息 筛选
        analysispage.click_accident()
        analysispage.click_accident_1()#事故类型 火灾
        #点击事故信息 筛选按钮 进行筛选
        BasePage.get_windows_img1(self)  # 调用基类截图方法

    def test_toolbar_18(self):
        homepage=HomePage(self.driver)
        analysispage=AnalysisPage(self.driver)
        homepage.type_search("甲醛")  # 输入框中输入甲醛
        homepage.send_submit_btn()  # 点击搜索按钮
        homepage.click_config_2()  # 点击实体筛选框2（此处根据搜索结果来排列，当前化学品位于筛选框第2）
        homepage.click_choose_all()  # 点击勾选 所有 （当前化学品只有1条）
        homepage.click_analysis_button()  # d点击进入图谱分析界面
        #移动到环形菜单 事故信息
        #点击事故信息 筛选
        analysispage.click_accident()
        analysispage.click_accident_2()#事故类型 泄露
        #点击事故信息 筛选按钮 进行筛选
        BasePage.get_windows_img1(self)  # 调用基类截图方法


    def test_toolbar_19(self):
        homepage=HomePage(self.driver)
        analysispage=AnalysisPage(self.driver)
        homepage.type_search("甲醛")  # 输入框中输入甲醛
        homepage.send_submit_btn()  # 点击搜索按钮
        homepage.click_config_2()  # 点击实体筛选框2（此处根据搜索结果来排列，当前化学品位于筛选框第2）
        homepage.click_choose_all()  # 点击勾选 所有 （当前化学品只有1条）
        homepage.click_analysis_button()  # d点击进入图谱分析界面
        #移动到环形菜单 事故信息
        #点击事故信息 筛选
        analysispage.click_accident()
        analysispage.click_accident_3()#事故类型 爆炸
        #点击事故信息 筛选按钮 进行筛选
        BasePage.get_windows_img1(self)  # 调用基类截图方法


    def test_toolbar_20(self):
        homepage=HomePage(self.driver)
        analysispage=AnalysisPage(self.driver)
        homepage.type_search("甲醛")  # 输入框中输入甲醛
        homepage.send_submit_btn()  # 点击搜索按钮
        homepage.click_config_2()  # 点击实体筛选框2（此处根据搜索结果来排列，当前化学品位于筛选框第2）
        homepage.click_choose_all()  # 点击勾选 所有 （当前化学品只有1条）
        homepage.click_analysis_button()  # d点击进入图谱分析界面
        #移动到环形菜单 事故信息
        #点击事故信息 筛选
        analysispage.click_accident()
        analysispage.click_accident_4()#事故类型 其他
        #点击事故信息 筛选按钮 进行筛选
        BasePage.get_windows_img1(self)  # 调用基类截图方法

    def test_toolbar_21(self):
        homepage=HomePage(self.driver)
        analysispage=AnalysisPage(self.driver)
        homepage.type_search("甲醛")  # 输入框中输入甲醛
        homepage.send_submit_btn()  # 点击搜索按钮
        homepage.click_config_2()  # 点击实体筛选框2（此处根据搜索结果来排列，当前化学品位于筛选框第2）
        homepage.click_choose_all()  # 点击勾选 所有 （当前化学品只有1条）
        homepage.click_analysis_button()  # d点击进入图谱分析界面
        #移动到环形菜单 事故信息
        #点击事故信息 筛选
        analysispage.click_accident()
        analysispage.click_accident_5()#事故类型 中毒
        #点击事故信息 筛选按钮 进行筛选
        BasePage.get_windows_img1(self)  # 调用基类截图方法

    def test_toolbar_22(self):
        homepage=HomePage(self.driver)
        analysispage=AnalysisPage(self.driver)
        homepage.type_search("甲醛")  # 输入框中输入甲醛
        homepage.send_submit_btn()  # 点击搜索按钮
        homepage.click_config_2()  # 点击实体筛选框2（此处根据搜索结果来排列，当前化学品位于筛选框第2）
        homepage.click_choose_all()  # 点击勾选 所有 （当前化学品只有1条）
        homepage.click_analysis_button()  # d点击进入图谱分析界面
        #移动到环形菜单 事故信息
        #点击事故信息 筛选
        analysispage.click_accident()
        analysispage.click_accident_3()#事故类型 爆炸
        #点击事故信息 取消  按钮
        BasePage.get_windows_img1(self)  # 调用基类截图方法


    def test_toolbar_23(self):
        homepage=HomePage(self.driver)
        analysispage=AnalysisPage(self.driver)
        homepage.type_search("甲醛")  # 输入框中输入甲醛
        homepage.send_submit_btn()  # 点击搜索按钮
        homepage.click_config_2()  # 点击实体筛选框2（此处根据搜索结果来排列，当前化学品位于筛选框第2）
        homepage.click_choose_all()  # 点击勾选 所有 （当前化学品只有1条）
        homepage.click_analysis_button()  # d点击进入图谱分析界面
        #移动到化学反应
        #点击反应物
        BasePage.get_windows_img1(self)  # 调用基类截图方法


    def test_toolbar_24(self):
        homepage=HomePage(self.driver)
        analysispage=AnalysisPage(self.driver)
        homepage.type_search("甲醛")  # 输入框中输入甲醛
        homepage.send_submit_btn()  # 点击搜索按钮
        homepage.click_config_2()  # 点击实体筛选框2（此处根据搜索结果来排列，当前化学品位于筛选框第2）
        homepage.click_choose_all()  # 点击勾选 所有 （当前化学品只有1条）
        homepage.click_analysis_button()  # d点击进入图谱分析界面
        #移动到化学反应
        #点击生成物
        BasePage.get_windows_img1(self)  # 调用基类截图方法


    def test_toolbar_25(self):
        homepage=HomePage(self.driver)
        analysispage=AnalysisPage(self.driver)
        homepage.type_search("甲醛")  # 输入框中输入甲醛
        homepage.send_submit_btn()  # 点击搜索按钮
        homepage.click_config_2()  # 点击实体筛选框2（此处根据搜索结果来排列，当前化学品位于筛选框第2）
        homepage.click_choose_all()  # 点击勾选 所有 （当前化学品只有1条）
        homepage.click_analysis_button()  # d点击进入图谱分析界面
        analysispage.acclick_node()#点击甲醛节点
        analysispage.click_details()#点击 查看详情
        time.sleep(2)
        analysispage.click_fallback()#点击回退
        BasePage.get_windows_img1(self)  # 调用基类截图方法

    def test_toolbar_26(self):
        homepage=HomePage(self.driver)
        analysispage=AnalysisPage(self.driver)
        homepage.type_search("甲醛")  # 输入框中输入甲醛
        homepage.send_submit_btn()  # 点击搜索按钮
        homepage.click_config_2()  # 点击实体筛选框2（此处根据搜索结果来排列，当前化学品位于筛选框第2）
        homepage.click_choose_all()  # 点击勾选 所有 （当前化学品只有1条）
        homepage.click_analysis_button()  # d点击进入图谱分析界面
        analysispage.acclick_node()#点击甲醛节点
        analysispage.click_directory()#点击所属目录
        BasePage.get_windows_img1(self)  # 调用基类截图方法

    def test_toolbar_27(self):
        homepage=HomePage(self.driver)
        analysispage=AnalysisPage(self.driver)
        homepage.type_search("甲醛")  # 输入框中输入甲醛
        homepage.send_submit_btn()  # 点击搜索按钮
        homepage.click_config_2()  # 点击实体筛选框2（此处根据搜索结果来排列，当前化学品位于筛选框第2）
        homepage.click_choose_all()  # 点击勾选 所有 （当前化学品只有1条）
        homepage.click_analysis_button()  # d点击进入图谱分析界面
        analysispage.acclick_node()#点击甲醛节点
        analysispage.click_standard()#点击法律法规
        BasePage.get_windows_img1(self)  # 调用基类截图方法

    def test_toolbar_28(self):
        homepage=HomePage(self.driver)
        analysispage=AnalysisPage(self.driver)
        homepage.type_search("甲醛")  # 输入框中输入甲醛
        homepage.send_submit_btn()  # 点击搜索按钮
        homepage.click_config_2()  # 点击实体筛选框2（此处根据搜索结果来排列，当前化学品位于筛选框第2）
        homepage.click_choose_all()  # 点击勾选 所有 （当前化学品只有1条）
        homepage.click_analysis_button()  # d点击进入图谱分析界面
        analysispage.click_back()#点击收回
        BasePage.get_windows_img1(self)  # 调用基类截图方法

    def test_toolbar_29(self):
        homepage=HomePage(self.driver)
        analysispage=AnalysisPage(self.driver)
        homepage.type_search("甲醛")  # 输入框中输入甲醛
        homepage.send_submit_btn()  # 点击搜索按钮
        homepage.click_config_2()  # 点击实体筛选框2（此处根据搜索结果来排列，当前化学品位于筛选框第2）
        homepage.click_choose_all()  # 点击勾选 所有 （当前化学品只有1条）
        homepage.click_analysis_button()  # d点击进入图谱分析界面
        analysispage.click_back()#点击收回
        time.sleep(3)
        analysispage.click_back_1()#展开属性框
        time.sleep(3)
        BasePage.get_windows_img1(self)  # 调用基类截图方法

    def test_toolbar_30(self):
        homepage=HomePage(self.driver)
        analysispage=AnalysisPage(self.driver)
        homepage.type_search("甲醛")  # 输入框中输入甲醛
        homepage.send_submit_btn()  # 点击搜索按钮
        homepage.click_config_2()  # 点击实体筛选框2（此处根据搜索结果来排列，当前化学品位于筛选框第2）
        homepage.click_choose_all()  # 点击勾选 所有 （当前化学品只有1条）
        homepage.click_analysis_button()  # d点击进入图谱分析界面
        analysispage.click_fullscreen()#点击全屏
        time.sleep(2)
        BasePage.get_windows_img1(self)  # 调用基类截图方法

    def test_toolbar_31(self):
        homepage=HomePage(self.driver)
        analysispage=AnalysisPage(self.driver)
        homepage.type_search("甲醛")  # 输入框中输入甲醛
        homepage.send_submit_btn()  # 点击搜索按钮
        homepage.click_config_2()  # 点击实体筛选框2（此处根据搜索结果来排列，当前化学品位于筛选框第2）
        homepage.click_choose_all()  # 点击勾选 所有 （当前化学品只有1条）
        homepage.click_analysis_button()  # d点击进入图谱分析界面
        analysispage.click_center()#点击居中
        time.sleep(2)
        BasePage.get_windows_img1(self)  # 调用基类截图方法

    def test_toolbar_32(self):
        homepage=HomePage(self.driver)
        analysispage=AnalysisPage(self.driver)
        homepage.type_search("甲醛")  # 输入框中输入甲醛
        homepage.send_submit_btn()  # 点击搜索按钮
        homepage.click_config_2()  # 点击实体筛选框2（此处根据搜索结果来排列，当前化学品位于筛选框第2）
        homepage.click_choose_all()  # 点击勾选 所有 （当前化学品只有1条）
        homepage.click_analysis_button()  # d点击进入图谱分析界面
        analysispage.click_theme()
        analysispage.click_theme_1()
        BasePage.get_windows_img1(self)  # 调用基类截图方法


    def test_toolbar_33(self):
        homepage=HomePage(self.driver)
        analysispage=AnalysisPage(self.driver)
        homepage.type_search("甲醛")  # 输入框中输入甲醛
        homepage.send_submit_btn()  # 点击搜索按钮
        homepage.click_config_2()  # 点击实体筛选框2（此处根据搜索结果来排列，当前化学品位于筛选框第2）
        homepage.click_choose_all()  # 点击勾选 所有 （当前化学品只有1条）
        homepage.click_analysis_button()  # d点击进入图谱分析界面
        analysispage.click_theme()
        analysispage.click_theme_2()
        BasePage.get_windows_img1(self)  # 调用基类截图方法


    def test_toolbar_34(self):
        homepage=HomePage(self.driver)
        analysispage=AnalysisPage(self.driver)
        homepage.type_search("甲醛")  # 输入框中输入甲醛
        homepage.send_submit_btn()  # 点击搜索按钮
        homepage.click_config_2()  # 点击实体筛选框2（此处根据搜索结果来排列，当前化学品位于筛选框第2）
        homepage.click_choose_all()  # 点击勾选 所有 （当前化学品只有1条）
        homepage.click_analysis_button()  # d点击进入图谱分析界面
        analysispage.click_theme()
        analysispage.click_theme_3()
        BasePage.get_windows_img1(self)  # 调用基类截图方法

    def test_toolbar_35(self):
        homepage=HomePage(self.driver)
        analysispage=AnalysisPage(self.driver)
        homepage.type_search("甲醛")  # 输入框中输入甲醛
        homepage.send_submit_btn()  # 点击搜索按钮
        homepage.click_config_2()  # 点击实体筛选框2（此处根据搜索结果来排列，当前化学品位于筛选框第2）
        homepage.click_choose_all()  # 点击勾选 所有 （当前化学品只有1条）
        homepage.click_analysis_button()  # d点击进入图谱分析界面
        # analysispage.点击筛选 关闭按钮
        BasePage.get_windows_img1(self)  # 调用基类截图方法

































if __name__ == '__main__':
    unittest.main()