# coding=utf-8
import time
import unittest
from farmework.browser_engine import BrowserEngine
from pageobjects.analysisPage import AnalysisPage
from pageobjects.homepage import HomePage
from farmework.base_page import BasePage


class Toolbar(unittest.TestCase):
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


    def test_toolbar_01(self):#通过
        homepage=HomePage(self.driver)
        analysispage=AnalysisPage(self.driver)
        homepage.type_search("甲醛")#输入框中输入甲醛
        homepage.send_submit_btn()#点击搜索按钮
        homepage.click_config_2()#点击实体筛选框2（此处根据搜索结果来排列，当前化学品位于筛选框第2）
        homepage.click_choose_all()#点击勾选 所有 （当前化学品只有1条）
        homepage.click_analysis_button()#d点击进入图谱分析界面
        analysispage.click_save_photo()#点击保存图片
        BasePage.get_windows_img1(self)  # 调用基类截图方法

    def test_toolbar_02(self):
        homepage=HomePage(self.driver)
        analysispage=AnalysisPage(self.driver)
        homepage.type_search("甲醛")  # 输入框中输入甲醛
        homepage.send_submit_btn()  # 点击搜索按钮
        homepage.click_config_2()  # 点击实体筛选框2（此处根据搜索结果来排列，当前化学品位于筛选框第2）
        homepage.click_choose_all()  # 点击勾选 所有 （当前化学品只有1条）
        homepage.click_analysis_button()  # d点击进入图谱分析界面
        time.sleep(2)
        analysispage.click_choice()
        time.sleep(2)
        analysispage.acclick_node1()
        time.sleep(1)
        analysispage.acclick_node2()
        time.sleep(1)
        BasePage.get_windows_img1(self)



    def test_toolbar_03(self):
        homepage=HomePage(self.driver)
        analysispage=AnalysisPage(self.driver)
        homepage.type_search("甲醛")  # 输入框中输入甲醛
        homepage.send_submit_btn()  # 点击搜索按钮
        homepage.click_config_2()  # 点击实体筛选框2（此处根据搜索结果来排列，当前化学品位于筛选框第2）
        homepage.click_choose_all()  # 点击勾选 所有 （当前化学品只有1条）
        homepage.click_analysis_button()  # d点击进入图谱分析界面
        analysispage.click_choice()#点击工具栏 选择
        analysispage.acclick_node1()
        time.sleep(1)
        analysispage.acclick_node2()
        time.sleep(1)
        analysispage.acclick_node3()
        time.sleep(1)
        BasePage.get_windows_img1(self)#调用基类截图方法

    def test_toolbar_03_01(self):
        homepage = HomePage(self.driver)
        analysispage = AnalysisPage(self.driver)
        homepage.type_search("甲醛")  # 输入框中输入甲醛
        homepage.send_submit_btn()  # 点击搜索按钮
        homepage.click_config_2()  # 点击实体筛选框2（此处根据搜索结果来排列，当前化学品位于筛选框第2）
        homepage.click_choose_all()  # 点击勾选 所有 （当前化学品只有1条）
        homepage.click_analysis_button()  # d点击进入图谱分析界面
        analysispage.click_choice()  # 点击工具栏 选择
        analysispage.acclick_node1()
        time.sleep(1)
        analysispage.acclick_node2()
        time.sleep(1)
        analysispage.acclick_node3()
        time.sleep(1)
        analysispage.acclick_node4()
        time.sleep(1)
        analysispage.acclick_node1()
        time.sleep(1)
        analysispage.acclick_node2()
        time.sleep(1)
        analysispage.acclick_node3()
        time.sleep(1)
        analysispage.acclick_node4()
        BasePage.get_windows_img1(self)  # 调用基类截图方法


    def test_toolbar_04(self):
        homepage=HomePage(self.driver)
        analysispage=AnalysisPage(self.driver)
        homepage.type_search("甲醛")  # 输入框中输入甲醛
        homepage.send_submit_btn()  # 点击搜索按钮
        homepage.click_config_2()  # 点击实体筛选框2（此处根据搜索结果来排列，当前化学品位于筛选框第2）
        homepage.click_choose_all()  # 点击勾选 所有 （当前化学品只有1条）
        homepage.click_analysis_button()  # d点击进入图谱分析界面
        analysispage.click_kuang_xuan()
        #测试步骤待确定



    def test_toolbar_05(self):
        homepage=HomePage(self.driver)
        analysispage=AnalysisPage(self.driver)
        homepage.type_search("甲醛")  # 输入框中输入甲醛
        homepage.send_submit_btn()  # 点击搜索按钮
        homepage.click_config_2()  # 点击实体筛选框2（此处根据搜索结果来排列，当前化学品位于筛选框第2）
        homepage.click_choose_all()  # 点击勾选 所有 （当前化学品只有1条）
        homepage.click_analysis_button()  # d点击进入图谱分析界面
        analysispage.click_choice()  # 点击工具栏 选择
        # analysispage.click #点击 选择任意节点
        #任意选中3个节点甚至多个节点
        analysispage.click_kuang_xuan()
        #框选多个节点
        BasePage.get_windows_img1(self)  # 调用基类截图方法

    def test_toolbar_06(self):
        homepage=HomePage(self.driver)
        analysispage=AnalysisPage(self.driver)
        homepage.type_search("甲醛")  # 输入框中输入甲醛
        homepage.send_submit_btn()  # 点击搜索按钮
        homepage.click_config_2()  # 点击实体筛选框2（此处根据搜索结果来排列，当前化学品位于筛选框第2）
        homepage.click_choose_all()  # 点击勾选 所有 （当前化学品只有1条）
        homepage.click_analysis_button()  # d点击进入图谱分析界面
        analysispage.click_delete()#点击删除
        BasePage.get_windows_img1(self)  # 调用基类截图方法

    def test_toolbar_07(self):
        homepage = HomePage(self.driver)
        analysispage = AnalysisPage(self.driver)
        homepage.type_search("甲醛")  # 输入框中输入甲醛
        homepage.send_submit_btn()  # 点击搜索按钮
        homepage.click_config_2()  # 点击实体筛选框2（此处根据搜索结果来排列，当前化学品位于筛选框第2）
        homepage.click_choose_all()  # 点击勾选 所有 （当前化学品只有1条）
        homepage.click_analysis_button()  # d点击进入图谱分析界面
        analysispage.click_choice()#d点击选择
        analysispage.acclick_node1()#点击节点天然气
        analysispage.acclick_node2()
        analysispage.click_delete()#点击删除
        BasePage.get_windows_img1(self)  # 调用基类截图方法

    def test_toolbar_08(self):
        homepage = HomePage(self.driver)
        analysispage = AnalysisPage(self.driver)
        homepage.type_search("甲醛")  # 输入框中输入甲醛
        homepage.send_submit_btn()  # 点击搜索按钮
        homepage.click_config_2()  # 点击实体筛选框2（此处根据搜索结果来排列，当前化学品位于筛选框第2）
        homepage.click_choose_all()  # 点击勾选 所有 （当前化学品只有1条）
        homepage.click_analysis_button()  # d点击进入图谱分析界面
        analysispage.click_kuang_xuan()#点击框选 通过框选来删除
        # analysispage.click#选择任意节点
        analysispage.click_delete()
        BasePage.get_windows_img1(self)  # 调用基类截图方法


    def test_toolbar_09(self):
        homepage = HomePage(self.driver)
        analysispage = AnalysisPage(self.driver)
        homepage.type_search("甲醛")  # 输入框中输入甲醛
        homepage.send_submit_btn()  # 点击搜索按钮
        homepage.click_config_2()  # 点击实体筛选框2（此处根据搜索结果来排列，当前化学品位于筛选框第2）
        homepage.click_choose_all()  # 点击勾选 所有 （当前化学品只有1条）
        homepage.click_analysis_button()  # 点击进入图谱分析界面
        analysispage.click_choice()
        analysispage.acclick_node3()#x选择节点甲醇
        analysispage.acclick_node4()#选择节点 水
        analysispage.click_kuang_xuan()#点击框选
        # analysispage.click#选择任意节点
        analysispage.click_delete()
        BasePage.get_windows_img1(self)  # 调用基类截图方法


    def test_toolbar_10(self):
        homepage = HomePage(self.driver)
        analysispage = AnalysisPage(self.driver)
        homepage.type_search("甲醛")  # 输入框中输入甲醛
        homepage.send_submit_btn()  # 点击搜索按钮
        homepage.click_config_2()  # 点击实体筛选框2（此处根据搜索结果来排列，当前化学品位于筛选框第2）
        homepage.click_choose_all()  # 点击勾选 所有 （当前化学品只有1条）
        homepage.click_analysis_button()  # d点击进入图谱分析界面
        analysispage.click_qie_ge()#点击切割
        BasePage.get_windows_img1(self)  # 调用基类截图方法

    def test_toolbar_11(self):
        homepage = HomePage(self.driver)
        analysispage = AnalysisPage(self.driver)
        homepage.type_search("甲醛")  # 输入框中输入甲醛
        homepage.send_submit_btn()  # 点击搜索按钮
        homepage.click_config_2()  # 点击实体筛选框2（此处根据搜索结果来排列，当前化学品位于筛选框第2）
        homepage.click_choose_all()  # 点击勾选 所有 （当前化学品只有1条）
        homepage.click_analysis_button()  # d点击进入图谱分析界面
        analysispage.click_kuang_xuan()#点击框选
        # analysispage.click#框选任意节点
        analysispage.click_qie_ge()
        BasePage.get_windows_img1(self)  # 调用基类截图方法

    def test_toolbar_12(self):
        homepage = HomePage(self.driver)
        analysispage = AnalysisPage(self.driver)
        homepage.type_search("甲醛")  # 输入框中输入甲醛
        homepage.send_submit_btn()  # 点击搜索按钮
        homepage.click_config_2()  # 点击实体筛选框2（此处根据搜索结果来排列，当前化学品位于筛选框第2）
        homepage.click_choose_all()  # 点击勾选 所有 （当前化学品只有1条）
        homepage.click_analysis_button()  # d点击进入图谱分析界面
        analysispage.click_choice()
        analysispage.acclick_node1()
        analysispage.acclick_node2()#选择任意节点
        analysispage.click_kuang_xuan()  # 点击框选
        # analysispage.click#框选任意节点
        analysispage.click_qie_ge()
        BasePage.get_windows_img1(self)  # 调用基类截图方法

    def test_toolbar_13(self):
        homepage = HomePage(self.driver)
        analysispage = AnalysisPage(self.driver)
        homepage.type_search("甲醛")  # 输入框中输入甲醛
        homepage.send_submit_btn()  # 点击搜索按钮
        homepage.click_config_2()  # 点击实体筛选框2（此处根据搜索结果来排列，当前化学品位于筛选框第2）
        homepage.click_choose_all()  # 点击勾选 所有 （当前化学品只有1条）
        homepage.click_analysis_button()  # d点击进入图谱分析界面
        analysispage.click_choice()#点击选择
        analysispage.acclick_node2()
        analysispage.acclick_node4()
        analysispage.click_qie_ge()#点击切割
        BasePage.get_windows_img1(self)  # 调用基类截图方法

    def test_toolbar_14(self):
        homepage = HomePage(self.driver)
        analysispage = AnalysisPage(self.driver)
        homepage.type_search("甲醛")  # 输入框中输入甲醛
        homepage.send_submit_btn()  # 点击搜索按钮
        homepage.click_config_2()  # 点击实体筛选框2（此处根据搜索结果来排列，当前化学品位于筛选框第2）
        homepage.click_choose_all()  # 点击勾选 所有 （当前化学品只有1条）
        homepage.click_analysis_button()  # d点击进入图谱分析界面
        analysispage.click_choice()#点击节点选择
        analysispage.acclick_node1()#点击节点天然气
        analysispage.acclick_node2()#点击节点空气
        analysispage.click_delete()#点击删除
        analysispage.click_rework()#点击撤销
        BasePage.get_windows_img1(self)  # 调用基类截图方法

    def test_toolbar_15(self):
        homepage = HomePage(self.driver)
        analysispage = AnalysisPage(self.driver)
        homepage.type_search("甲醛")  # 输入框中输入甲醛
        homepage.send_submit_btn()  # 点击搜索按钮
        homepage.click_config_2()  # 点击实体筛选框2（此处根据搜索结果来排列，当前化学品位于筛选框第2）
        homepage.click_choose_all()  # 点击勾选 所有 （当前化学品只有1条）
        homepage.click_analysis_button()  # d点击进入图谱分析界面
        analysispage.click_kuang_xuan()
        # analysispage.click#框选任意节点
        analysispage.click_delete()
        analysispage.click_rework()
        BasePage.get_windows_img1(self)  # 调用基类截图方法

    def test_toolbar_16(self):
        homepage = HomePage(self.driver)
        analysispage = AnalysisPage(self.driver)
        homepage.type_search("甲醛")  # 输入框中输入甲醛
        homepage.send_submit_btn()  # 点击搜索按钮
        homepage.click_config_2()  # 点击实体筛选框2（此处根据搜索结果来排列，当前化学品位于筛选框第2）
        homepage.click_choose_all()  # 点击勾选 所有 （当前化学品只有1条）
        homepage.click_analysis_button()  # d点击进入图谱分析界面
        analysispage.click_choice()#点击节点选择
        analysispage.acclick_node1()#点击节点天然气
        analysispage.acclick_node2()#点击节点空气
        analysispage.click_path_analysis()#路径分析  默认最短路径 深度为2
        analysispage.click_confirm()#点击确定
        analysispage.click_rework()#点击撤销
        BasePage.get_windows_img1(self)  # 调用基类截图方法

    def test_toolbar_17(self):
        homepage = HomePage(self.driver)
        analysispage = AnalysisPage(self.driver)
        homepage.type_search("甲醛")  # 输入框中输入甲醛
        homepage.send_submit_btn()  # 点击搜索按钮
        homepage.click_config_2()  # 点击实体筛选框2（此处根据搜索结果来排列，当前化学品位于筛选框第2）
        homepage.click_choose_all()  # 点击勾选 所有 （当前化学品只有1条）
        homepage.click_analysis_button()  # d点击进入图谱分析界面
        analysispage.click_choice()#点击节点选择
        analysispage.acclick_node1()#点击节点天然气
        analysispage.acclick_node2()#点击节点空气
        analysispage.click_reaction()#反应链分析
        analysispage.click_rework()#点击撤销
        BasePage.get_windows_img1(self)  # 调用基类截图方法

    def test_toolbar_18(self):
        homepage = HomePage(self.driver)
        analysispage = AnalysisPage(self.driver)
        homepage.type_search("甲醛")  # 输入框中输入甲醛
        homepage.send_submit_btn()  # 点击搜索按钮
        homepage.click_config_2()  # 点击实体筛选框2（此处根据搜索结果来排列，当前化学品位于筛选框第2）
        homepage.click_choose_all()  # 点击勾选 所有 （当前化学品只有1条）
        homepage.click_analysis_button()  # d点击进入图谱分析界面
        analysispage.click_choice()#点击节点选择
        analysispage.acclick_node1()#点击节点天然气
        analysispage.acclick_node2()#点击节点空气
        analysispage.click_delete()
        time.sleep(2)
        analysispage.acclick_node3()
        analysispage.click_qie_ge()
        analysispage.click_rework()
        analysispage.click_rework()#多步骤多撤销
        time.sleep(2)
        BasePage.get_windows_img1(self)  # 调用基类截图方法

    def test_toolbar_19(self):
        homepage = HomePage(self.driver)
        analysispage = AnalysisPage(self.driver)
        homepage.type_search("甲醛")  # 输入框中输入甲醛
        homepage.send_submit_btn()  # 点击搜索按钮
        homepage.click_config_2()  # 点击实体筛选框2（此处根据搜索结果来排列，当前化学品位于筛选框第2）
        homepage.click_choose_all()  # 点击勾选 所有 （当前化学品只有1条）
        homepage.click_analysis_button()  # d点击进入图谱分析界面
        analysispage.click_filter()
        time.sleep(3)
        analysispage.click_entity_1()#过滤化学品
        time.sleep(3)
        analysispage.click_rework()#撤销
        BasePage.get_windows_img1(self)  # 调用基类截图方法


    def test_toolbar_20(self):#添加实体再撤销
        homepage = HomePage(self.driver)
        analysispage = AnalysisPage(self.driver)
        homepage.type_search("甲醛")  # 输入框中输入甲醛
        homepage.send_submit_btn()  # 点击搜索按钮
        homepage.click_config_2()  # 点击实体筛选框2（此处根据搜索结果来排列，当前化学品位于筛选框第2）
        homepage.click_choose_all()  # 点击勾选 所有 （当前化学品只有1条）
        homepage.click_analysis_button()  # d点击进入图谱分析界面
        analysispage.click_add_shiti()
        analysispage.type_addshiti_input("甲醛")
        analysispage.click_addshiti_search()
        time.sleep(3)
        analysispage.click_dangye()
        analysispage.click_add_analysis()
        time.sleep(3)
        analysispage.click_rework()
        BasePage.get_windows_img1(self)  # 调用基类截图方法

    def test_toolbar_21(self):
        homepage = HomePage(self.driver)
        analysispage = AnalysisPage(self.driver)
        homepage.type_search("甲醛")  # 输入框中输入甲醛
        homepage.send_submit_btn()  # 点击搜索按钮
        homepage.click_config_2()  # 点击实体筛选框2（此处根据搜索结果来排列，当前化学品位于筛选框第2）
        homepage.click_choose_all()  # 点击勾选 所有 （当前化学品只有1条）
        homepage.click_analysis_button()  # d点击进入图谱分析界面
        analysispage.click_rework()#直接点击撤销
        BasePage.get_windows_img1(self)  # 调用基类截图方法


    def test_toolbar_22(self):
        homepage = HomePage(self.driver)
        analysispage = AnalysisPage(self.driver)
        homepage.type_search("甲醛")  # 输入框中输入甲醛
        homepage.send_submit_btn()  # 点击搜索按钮
        homepage.click_config_2()  # 点击实体筛选框2（此处根据搜索结果来排列，当前化学品位于筛选框第2）
        homepage.click_choose_all()  # 点击勾选 所有 （当前化学品只有1条）
        homepage.click_analysis_button()  # d点击进入图谱分析界面
        analysispage.click_filter()#点击过滤
        analysispage.click_entity_1()#过滤化学品
        BasePage.get_windows_img1(self)  # 调用基类截图方法

    def test_toolbar_23(self):
        homepage = HomePage(self.driver)
        analysispage = AnalysisPage(self.driver)
        homepage.type_search("甲醛")  # 输入框中输入甲醛
        homepage.send_submit_btn()  # 点击搜索按钮
        homepage.click_config_2()  # 点击实体筛选框2（此处根据搜索结果来排列，当前化学品位于筛选框第2）
        homepage.click_choose_all()  # 点击勾选 所有 （当前化学品只有1条）
        homepage.click_analysis_button()  # d点击进入图谱分析界面
        analysispage.click_filter()
        time.sleep(5)
        analysispage.click_entity_2()
        time.sleep(2)
        BasePage.get_windows_img1(self)  # 调用基类截图方法

    def test_toolbar_24(self):
        homepage = HomePage(self.driver)
        analysispage = AnalysisPage(self.driver)
        homepage.type_search("甲醛")  # 输入框中输入甲醛
        homepage.send_submit_btn()  # 点击搜索按钮
        homepage.click_config_2()  # 点击实体筛选框2（此处根据搜索结果来排列，当前化学品位于筛选框第2）
        homepage.click_choose_all()  # 点击勾选 所有 （当前化学品只有1条）
        homepage.click_analysis_button()  # d点击进入图谱分析界面
        analysispage.click_filter()#点击过滤
        time.sleep(5)
        analysispage.click_entity_3()
        time.sleep(3)
        BasePage.get_windows_img1(self)  # 调用基类截图方法

    def test_toolbar_25(self):
        homepage = HomePage(self.driver)
        analysispage = AnalysisPage(self.driver)
        homepage.type_search("甲醛")  # 输入框中输入甲醛
        homepage.send_submit_btn()  # 点击搜索按钮
        homepage.click_config_2()  # 点击实体筛选框2（此处根据搜索结果来排列，当前化学品位于筛选框第2）
        homepage.click_choose_all()  # 点击勾选 所有 （当前化学品只有1条）
        homepage.click_analysis_button()  # d点击进入图谱分析界面
        analysispage.click_filter()
        time.sleep(5)
        analysispage.click_entity_4()
        time.sleep(3)
        BasePage.get_windows_img1(self)  # 调用基类截图方法

    def test_toolbar_26(self):
        homepage = HomePage(self.driver)
        analysispage = AnalysisPage(self.driver)
        homepage.type_search("甲醛")  # 输入框中输入甲醛
        homepage.send_submit_btn()  # 点击搜索按钮
        homepage.click_config_2()  # 点击实体筛选框2（此处根据搜索结果来排列，当前化学品位于筛选框第2）
        homepage.click_choose_all()  # 点击勾选 所有 （当前化学品只有1条）
        homepage.click_analysis_button()  # d点击进入图谱分析界面
        analysispage.click_filter()
        time.sleep(3)
        analysispage.click_entity_5()
        time.sleep(3)
        BasePage.get_windows_img1(self)  # 调用基类截图方法

    def test_toolbar_27(self):
        homepage = HomePage(self.driver)
        analysispage = AnalysisPage(self.driver)
        homepage.type_search("甲醛")  # 输入框中输入甲醛
        homepage.send_submit_btn()  # 点击搜索按钮
        homepage.click_config_2()  # 点击实体筛选框2（此处根据搜索结果来排列，当前化学品位于筛选框第2）
        homepage.click_choose_all()  # 点击勾选 所有 （当前化学品只有1条）
        homepage.click_analysis_button()  # d点击进入图谱分析界面
        analysispage.click_filter()
        analysispage.click_entity_6()
        BasePage.get_windows_img1(self)  # 调用基类截图方法

    def test_toolbar_28(self):
        homepage = HomePage(self.driver)
        analysispage = AnalysisPage(self.driver)
        homepage.type_search("甲醛")  # 输入框中输入甲醛
        homepage.send_submit_btn()  # 点击搜索按钮
        homepage.click_config_2()  # 点击实体筛选框2（此处根据搜索结果来排列，当前化学品位于筛选框第2）
        homepage.click_choose_all()  # 点击勾选 所有 （当前化学品只有1条）
        homepage.click_analysis_button()  # d点击进入图谱分析界面
        analysispage.click_filter()
        time.sleep(3)
        analysispage.click_relation_1()#关系类别1
        BasePage.get_windows_img1(self)  # 调用基类截图方法

    def test_toolbar_29(self):
        homepage = HomePage(self.driver)
        analysispage = AnalysisPage(self.driver)
        homepage.type_search("甲醛")  # 输入框中输入甲醛
        homepage.send_submit_btn()  # 点击搜索按钮
        homepage.click_config_2()  # 点击实体筛选框2（此处根据搜索结果来排列，当前化学品位于筛选框第2）
        homepage.click_choose_all()  # 点击勾选 所有 （当前化学品只有1条）
        homepage.click_analysis_button()  # d点击进入图谱分析界面
        analysispage.click_filter()
        analysispage.click_relation_2()
        BasePage.get_windows_img1(self)  # 调用基类截图方法

    def test_toolbar_30(self):
        homepage = HomePage(self.driver)
        analysispage = AnalysisPage(self.driver)
        homepage.type_search("甲醛")  # 输入框中输入甲醛
        homepage.send_submit_btn()  # 点击搜索按钮
        homepage.click_config_2()  # 点击实体筛选框2（此处根据搜索结果来排列，当前化学品位于筛选框第2）
        homepage.click_choose_all()  # 点击勾选 所有 （当前化学品只有1条）
        homepage.click_analysis_button()  # d点击进入图谱分析界面
        analysispage.click_filter()
        analysispage.click_relation_3()
        BasePage.get_windows_img1(self)  # 调用基类截图方法

    def test_toolbar_31(self):
        homepage = HomePage(self.driver)
        analysispage = AnalysisPage(self.driver)
        homepage.type_search("甲醛")  # 输入框中输入甲醛
        homepage.send_submit_btn()  # 点击搜索按钮
        homepage.click_config_2()  # 点击实体筛选框2（此处根据搜索结果来排列，当前化学品位于筛选框第2）
        homepage.click_choose_all()  # 点击勾选 所有 （当前化学品只有1条）
        homepage.click_analysis_button()  # d点击进入图谱分析界面
        analysispage.click_filter()
        analysispage.click_relation_4()
        BasePage.get_windows_img1(self)  # 调用基类截图方法

    def test_toolbar_32(self):
        homepage = HomePage(self.driver)
        analysispage = AnalysisPage(self.driver)
        homepage.type_search("甲醛")  # 输入框中输入甲醛
        homepage.send_submit_btn()  # 点击搜索按钮
        homepage.click_config_2()  # 点击实体筛选框2（此处根据搜索结果来排列，当前化学品位于筛选框第2）
        homepage.click_choose_all()  # 点击勾选 所有 （当前化学品只有1条）
        homepage.click_analysis_button()  # d点击进入图谱分析界面
        analysispage.click_filter()#d点击过滤
        analysispage.click_entity_1()#点击化学品
        time.sleep(3)
        analysispage.click_entity_1()#取消过滤化学品
        analysispage.click_rework()#点击撤销
        analysispage.click_rework()#点击撤销
        BasePage.get_windows_img1(self)  # 调用基类截图方法


    def test_toolbar_33(self):
        homepage = HomePage(self.driver)
        analysispage = AnalysisPage(self.driver)
        homepage.type_search("甲醛")  # 输入框中输入甲醛
        homepage.send_submit_btn()  # 点击搜索按钮
        homepage.click_config_2()  # 点击实体筛选框2（此处根据搜索结果来排列，当前化学品位于筛选框第2）
        homepage.click_choose_all()  # 点击勾选 所有 （当前化学品只有1条）
        homepage.click_analysis_button()  # d点击进入图谱分析界面
        analysispage.click_filter()#点击过滤
        analysispage.click_entity_1()#化学品
        analysispage.click_rework()#点击撤销
        analysispage.click_entity_1()#点击化学品
        time.sleep(3)
        BasePage.get_windows_img1(self)  # 调用基类截图方法

    def test_toolbar_34(self):
        homepage = HomePage(self.driver)
        analysispage = AnalysisPage(self.driver)
        homepage.type_search("甲醛")  # 输入框中输入甲醛
        homepage.send_submit_btn()  # 点击搜索按钮
        homepage.click_config_2()  # 点击实体筛选框2（此处根据搜索结果来排列，当前化学品位于筛选框第2）
        homepage.click_choose_all()  # 点击勾选 所有 （当前化学品只有1条）
        homepage.click_analysis_button()  # d点击进入图谱分析界面
        analysispage.click_filter()#点击过滤
        analysispage.click_entity_3()
        analysispage.click_entity_3()
        time.sleep(3)
        BasePage.get_windows_img1(self)  # 调用基类截图方法

    def test_toolbar_35(self):
        homepage = HomePage(self.driver)
        analysispage = AnalysisPage(self.driver)
        homepage.type_search("甲醛")  # 输入框中输入甲醛
        homepage.send_submit_btn()  # 点击搜索按钮
        homepage.click_config_2()  # 点击实体筛选框2（此处根据搜索结果来排列，当前化学品位于筛选框第2）
        homepage.click_choose_all()  # 点击勾选 所有 （当前化学品只有1条）
        homepage.click_analysis_button()  # d点击进入图谱分析界面
        time.sleep(3)
        analysispage.click_choice()
        analysispage.acclick_node1()
        analysispage.click_delete()#点击删除
        time.sleep(1)
        analysispage.click_filter()#点击过滤
        analysispage.click_entity_1()#化学品
        time.sleep(2)
        analysispage.click_entity_1()#先删除节点，然后过滤掉化学品，然后取消过滤
        BasePage.get_windows_img1(self)  # 调用基类截图方法



    def test_toolbar_36(self):
        homepage = HomePage(self.driver)
        analysispage = AnalysisPage(self.driver)
        homepage.type_search("甲醛")  # 输入框中输入甲醛
        homepage.send_submit_btn()  # 点击搜索按钮
        homepage.click_config_2()  # 点击实体筛选框2（此处根据搜索结果来排列，当前化学品位于筛选框第2）
        homepage.click_choose_all()  # 点击勾选 所有 （当前化学品只有1条）
        homepage.click_analysis_button()  # d点击进入图谱分析界面
        time.sleep(3)
        analysispage.click_choice()
        analysispage.acclick_node3()
        time.sleep(1)
        analysispage.click_qie_ge()
        analysispage.click_filter()
        analysispage.click_entity_1()
        analysispage.click_entity_1()#先删除节点，然后过滤掉化学品，然后取消过滤
        BasePage.get_windows_img1(self)  # 调用基类截图方法


    def test_toolbar_37(self):
        homepage = HomePage(self.driver)
        analysispage = AnalysisPage(self.driver)
        homepage.type_search("甲醛")  # 输入框中输入甲醛
        homepage.send_submit_btn()  # 点击搜索按钮
        homepage.click_config_2()  # 点击实体筛选框2（此处根据搜索结果来排列，当前化学品位于筛选框第2）
        homepage.click_choose_all()  # 点击勾选 所有 （当前化学品只有1条）
        homepage.click_analysis_button()  # d点击进入图谱分析界面
        time.sleep(3)
        analysispage.click_add_shiti()
        analysispage.type_addshiti_input("甲醇")
        analysispage.click_addshiti_search()
        time.sleep(3)
        analysispage.click_marquee_1()
        analysispage.click_add_analysis()
        BasePage.get_windows_img1(self)  # 调用基类截图方法


    def test_toolbar_38(self):
        homepage = HomePage(self.driver)
        analysispage = AnalysisPage(self.driver)
        homepage.type_search("甲醛")  # 输入框中输入甲醛
        homepage.send_submit_btn()  # 点击搜索按钮
        homepage.click_config_2()  # 点击实体筛选框2（此处根据搜索结果来排列，当前化学品位于筛选框第2）
        homepage.click_choose_all()  # 点击勾选 所有 （当前化学品只有1条）
        homepage.click_analysis_button()  # d点击进入图谱分析界面
        time.sleep(3)
        analysispage.click_add_shiti()
        # analysispage.type_addshiti_input("甲醇")化学品中文名+英文名
        analysispage.click_addshiti_search()
        time.sleep(3)
        analysispage.click_marquee_2()
        analysispage.click_add_analysis()
        BasePage.get_windows_img1(self)  # 调用基类截图方法

    def test_toolbar_39(self):
        homepage = HomePage(self.driver)
        analysispage = AnalysisPage(self.driver)
        homepage.type_search("甲醛")  # 输入框中输入甲醛
        homepage.send_submit_btn()  # 点击搜索按钮
        homepage.click_config_2()  # 点击实体筛选框2（此处根据搜索结果来排列，当前化学品位于筛选框第2）
        homepage.click_choose_all()  # 点击勾选 所有 （当前化学品只有1条）
        homepage.click_analysis_button()  # d点击进入图谱分析界面
        time.sleep(3)
        analysispage.click_add_shiti()
        # analysispage.type_addshiti_input("")英文名
        analysispage.click_addshiti_search()
        time.sleep(3)
        analysispage.click_marquee_2()
        analysispage.click_add_analysis()
        BasePage.get_windows_img1(self)  # 调用基类截图方法


    def test_toolbar_40(self):
        homepage = HomePage(self.driver)
        analysispage = AnalysisPage(self.driver)
        homepage.type_search("甲醛")  # 输入框中输入甲醛
        homepage.send_submit_btn()  # 点击搜索按钮
        homepage.click_config_2()  # 点击实体筛选框2（此处根据搜索结果来排列，当前化学品位于筛选框第2）
        homepage.click_choose_all()  # 点击勾选 所有 （当前化学品只有1条）
        homepage.click_analysis_button()  # d点击进入图谱分析界面
        time.sleep(3)
        analysispage.click_add_shiti()
        analysispage.type_addshiti_input("12345")
        time.sleep(3)
        analysispage.click_addshiti_search()
        BasePage.get_windows_img1(self)  # 调用基类截图方法


    def test_toolbar_41(self):
        homepage = HomePage(self.driver)
        analysispage = AnalysisPage(self.driver)
        homepage.type_search("甲醛")  # 输入框中输入甲醛
        homepage.send_submit_btn()  # 点击搜索按钮
        homepage.click_config_2()  # 点击实体筛选框2（此处根据搜索结果来排列，当前化学品位于筛选框第2）
        homepage.click_choose_all()  # 点击勾选 所有 （当前化学品只有1条）
        homepage.click_analysis_button()  # d点击进入图谱分析界面
        time.sleep(3)
        analysispage.click_add_shiti()
        analysispage.type_addshiti_input("152.4566")
        time.sleep(3)
        analysispage.click_addshiti_search()
        BasePage.get_windows_img1(self)  # 调用基类截图方法


    def test_toolbar_42(self):
        homepage = HomePage(self.driver)
        analysispage = AnalysisPage(self.driver)
        homepage.type_search("甲醛")  # 输入框中输入甲醛
        homepage.send_submit_btn()  # 点击搜索按钮
        homepage.click_config_2()  # 点击实体筛选框2（此处根据搜索结果来排列，当前化学品位于筛选框第2）
        homepage.click_choose_all()  # 点击勾选 所有 （当前化学品只有1条）
        homepage.click_analysis_button()  # d点击进入图谱分析界面
        time.sleep(3)
        analysispage.click_add_shiti()
        analysispage.type_addshiti_input("asguosiagn")#无效字母
        time.sleep(3)
        analysispage.click_addshiti_search()
        BasePage.get_windows_img1(self)  # 调用基类截图方法

    def test_toolbar_43(self):
        homepage = HomePage(self.driver)
        analysispage = AnalysisPage(self.driver)
        homepage.type_search("甲醛")  # 输入框中输入甲醛
        homepage.send_submit_btn()  # 点击搜索按钮
        homepage.click_config_2()  # 点击实体筛选框2（此处根据搜索结果来排列，当前化学品位于筛选框第2）
        homepage.click_choose_all()  # 点击勾选 所有 （当前化学品只有1条）
        homepage.click_analysis_button()  # d点击进入图谱分析界面
        time.sleep(3)
        analysispage.click_add_shiti()
        analysispage.type_addshiti_input("@#￥！%")#特殊符号
        time.sleep(3)
        analysispage.click_addshiti_search()
        BasePage.get_windows_img1(self)  # 调用基类截图方法


    def test_toolbar_44(self):
        homepage = HomePage(self.driver)
        analysispage = AnalysisPage(self.driver)
        homepage.type_search("甲醛")  # 输入框中输入甲醛
        homepage.send_submit_btn()  # 点击搜索按钮
        homepage.click_config_2()  # 点击实体筛选框2（此处根据搜索结果来排列，当前化学品位于筛选框第2）
        homepage.click_choose_all()  # 点击勾选 所有 （当前化学品只有1条）
        homepage.click_analysis_button()  # d点击进入图谱分析界面
        time.sleep(3)
        analysispage.click_add_shiti()
        analysispage.type_addshiti_input("")#输入为空
        time.sleep(3)
        analysispage.click_addshiti_search()
        BasePage.get_windows_img1(self)  # 调用基类截图方法


    def test_toolbar_45(self):
        homepage = HomePage(self.driver)
        analysispage = AnalysisPage(self.driver)
        homepage.type_search("甲醛")  # 输入框中输入甲醛
        homepage.send_submit_btn()  # 点击搜索按钮
        homepage.click_config_2()  # 点击实体筛选框2（此处根据搜索结果来排列，当前化学品位于筛选框第2）
        homepage.click_choose_all()  # 点击勾选 所有 （当前化学品只有1条）
        homepage.click_analysis_button()  # d点击进入图谱分析界面
        time.sleep(3)
        analysispage.click_add_shiti()
        analysispage.type_addshiti_input("aslgduoi2134liuon@##$%")#字母加数字加特殊符号
        time.sleep(3)
        analysispage.click_addshiti_search()
        analysispage.click_addshiti_close()#g关闭按钮
        BasePage.get_windows_img1(self)  # 调用基类截图方法

    def test_toolbar_46(self):
        homepage = HomePage(self.driver)
        analysispage = AnalysisPage(self.driver)
        homepage.type_search("甲醛")  # 输入框中输入甲醛
        homepage.send_submit_btn()  # 点击搜索按钮
        homepage.click_config_2()  # 点击实体筛选框2（此处根据搜索结果来排列，当前化学品位于筛选框第2）
        homepage.click_choose_all()  # 点击勾选 所有 （当前化学品只有1条）
        homepage.click_analysis_button()  # d点击进入图谱分析界面
        time.sleep(3)
        analysispage.click_add_shiti()
        analysispage.type_addshiti_input("甲醇")
        analysispage.click_addshiti_search()
        time.sleep(3)
        analysispage.click_marquee_1()#勾选选框1
        analysispage.click_marquee_2()#勾选选框2
        time.sleep(3)
        analysispage.click_nextpage()#单击下一页
        time.sleep(3)
        analysispage.click_marquee_3()#点击选框3
        analysispage.click_marquee_4()#点击选框4
        time.sleep(3)
        analysispage.click_onpage()#点击上一页
        time.sleep(3)
        analysispage.click_add_analysis()#添加分析
        BasePage.get_windows_img1(self)  # 调用基类截图方法


    def test_toolbar_47(self):
        homepage = HomePage(self.driver)
        analysispage = AnalysisPage(self.driver)
        homepage.type_search("甲醛")  # 输入框中输入甲醛
        homepage.send_submit_btn()  # 点击搜索按钮
        homepage.click_config_2()  # 点击实体筛选框2（此处根据搜索结果来排列，当前化学品位于筛选框第2）
        homepage.click_choose_all()  # 点击勾选 所有 （当前化学品只有1条）
        homepage.click_analysis_button()  # d点击进入图谱分析界面
        time.sleep(3)
        analysispage.click_add_shiti()
        analysispage.type_addshiti_input("甲醇")
        time.sleep(3)
        analysispage.click_addshiti_search()
        time.sleep(1)
        analysispage.type_inputpage1("4")
        analysispage.enter_confirm()#敲击键盘enter
        time.sleep(2)
        analysispage.click_marquee_3()#勾选选框3
        analysispage.click_add_analysis()#添加分析
        BasePage.get_windows_img1(self)  # 调用基类截图方法

    def test_toolbar_48(self):
        homepage = HomePage(self.driver)
        analysispage = AnalysisPage(self.driver)
        homepage.type_search("甲醛")  # 输入框中输入甲醛
        homepage.send_submit_btn()  # 点击搜索按钮
        homepage.click_config_2()  # 点击实体筛选框2（此处根据搜索结果来排列，当前化学品位于筛选框第2）
        homepage.click_choose_all()  # 点击勾选 所有 （当前化学品只有1条）
        homepage.click_analysis_button()  # d点击进入图谱分析界面
        analysispage.click_choice()
        time.sleep(3)
        analysispage.acclick_node1()
        analysispage.acclick_node2()
        analysispage.click_path_analysis()#点击路径分析
        analysispage.click_confirm()#点击确认按钮  默认是最短路径，深度为2
        BasePage.get_windows_img1(self)  # 调用基类截图方法


    def test_toolbar_49(self):
        homepage = HomePage(self.driver)
        analysispage = AnalysisPage(self.driver)
        homepage.type_search("甲醛")  # 输入框中输入甲醛
        homepage.send_submit_btn()  # 点击搜索按钮
        homepage.click_config_2()  # 点击实体筛选框2（此处根据搜索结果来排列，当前化学品位于筛选框第2）
        homepage.click_choose_all()  # 点击勾选 所有 （当前化学品只有1条）
        homepage.click_analysis_button()  # d点击进入图谱分析界面
        analysispage.click_choice()
        time.sleep(3)
        analysispage.acclick_node1()
        analysispage.acclick_node2()
        analysispage.click_path_analysis()
        time.sleep(3)
        analysispage.type_inputpath("1")
        analysispage.click_confirm()  # 点击确定按钮
        BasePage.get_windows_img1(self)  # 调用基类截图方法

    def test_toolbar_50(self):
        homepage = HomePage(self.driver)
        analysispage = AnalysisPage(self.driver)
        homepage.type_search("甲醛")  # 输入框中输入甲醛
        homepage.send_submit_btn()  # 点击搜索按钮
        homepage.click_config_2()  # 点击实体筛选框2（此处根据搜索结果来排列，当前化学品位于筛选框第2）
        homepage.click_choose_all()  # 点击勾选 所有 （当前化学品只有1条）
        homepage.click_analysis_button()  # d点击进入图谱分析界面
        analysispage.click_choice()
        time.sleep(3)
        analysispage.acclick_node1()
        analysispage.acclick_node2()
        analysispage.click_path_analysis()
        analysispage.type_inputpath("9")
        analysispage.click_confirm()  # 点击确定按钮
        BasePage.get_windows_img1(self)  # 调用基类截图方法



    def test_toolbar_51(self):
        homepage = HomePage(self.driver)
        analysispage = AnalysisPage(self.driver)
        homepage.type_search("甲醛")  # 输入框中输入甲醛
        homepage.send_submit_btn()  # 点击搜索按钮
        homepage.click_config_2()  # 点击实体筛选框2（此处根据搜索结果来排列，当前化学品位于筛选框第2）
        homepage.click_choose_all()  # 点击勾选 所有 （当前化学品只有1条）
        homepage.click_analysis_button()  # d点击进入图谱分析界面
        analysispage.click_choice()
        time.sleep(3)
        analysispage.acclick_node3()
        analysispage.acclick_node4()
        analysispage.click_path_analysis()
        analysispage.type_inputpath("8")
        analysispage.click_confirm()  # 点击确定按钮
        BasePage.get_windows_img1(self)  # 调用基类截图方法

    def test_toolbar_52(self):
        homepage = HomePage(self.driver)
        analysispage = AnalysisPage(self.driver)
        homepage.type_search("甲醛")  # 输入框中输入甲醛
        homepage.send_submit_btn()  # 点击搜索按钮
        homepage.click_config_2()  # 点击实体筛选框2（此处根据搜索结果来排列，当前化学品位于筛选框第2）
        homepage.click_choose_all()  # 点击勾选 所有 （当前化学品只有1条）
        homepage.click_analysis_button()  # d点击进入图谱分析界面
        analysispage.click_choice()
        time.sleep(3)
        analysispage.acclick_node1()
        analysispage.acclick_node2()
        analysispage.click_path_analysis()
        analysispage.click_allpath()
        analysispage.type_inputpath("2")
        analysispage.click_confirm()  # 点击确定按钮
        BasePage.get_windows_img1(self)  # 调用基类截图方法

    def test_toolbar_53(self):
        homepage = HomePage(self.driver)
        analysispage = AnalysisPage(self.driver)
        homepage.type_search("甲醛")  # 输入框中输入甲醛
        homepage.send_submit_btn()  # 点击搜索按钮
        homepage.click_config_2()  # 点击实体筛选框2（此处根据搜索结果来排列，当前化学品位于筛选框第2）
        homepage.click_choose_all()  # 点击勾选 所有 （当前化学品只有1条）
        homepage.click_analysis_button()  # d点击进入图谱分析界面
        analysispage.click_choice()
        time.sleep(3)
        analysispage.acclick_node1()
        analysispage.acclick_node2()
        analysispage.click_path_analysis()
        analysispage.click_allpath()
        analysispage.type_inputpath("9")
        analysispage.click_confirm()  # 点击确定按钮
        time.sleep(5)#加载时间
        BasePage.get_windows_img1(self)  # 调用基类截图方法


    def test_toolbar_54(self):
        homepage = HomePage(self.driver)
        analysispage = AnalysisPage(self.driver)
        homepage.type_search("甲醛")  # 输入框中输入甲醛
        homepage.send_submit_btn()  # 点击搜索按钮
        homepage.click_config_2()  # 点击实体筛选框2（此处根据搜索结果来排列，当前化学品位于筛选框第2）
        homepage.click_choose_all()  # 点击勾选 所有 （当前化学品只有1条）
        homepage.click_analysis_button()  # d点击进入图谱分析界面
        analysispage.click_choice()
        time.sleep(3)
        analysispage.acclick_node1()
        analysispage.acclick_node2()
        analysispage.click_path_analysis()
        analysispage.click_allpath()#所有路径
        analysispage.type_inputpath("8")
        analysispage.click_confirm()  # 点击确定按钮
        time.sleep(5)
        BasePage.get_windows_img1(self)  # 调用基类截图方法

    def test_toolbar_55(self):
        homepage = HomePage(self.driver)
        analysispage = AnalysisPage(self.driver)
        homepage.type_search("甲醛")  # 输入框中输入甲醛
        homepage.send_submit_btn()  # 点击搜索按钮
        homepage.click_config_2()  # 点击实体筛选框2（此处根据搜索结果来排列，当前化学品位于筛选框第2）
        homepage.click_choose_all()  # 点击勾选 所有 （当前化学品只有1条）
        homepage.click_analysis_button()  # d点击进入图谱分析界面
        analysispage.click_choice()
        time.sleep(3)
        analysispage.acclick_node1()
        analysispage.acclick_node2()
        analysispage.click_path_analysis()
        analysispage.click_allpath()#所有路径
        analysispage.type_inputpath("1")
        analysispage.click_confirm()  # 点击确定按钮
        time.sleep(2)
        BasePage.get_windows_img1(self)  # 调用基类截图方法

    def test_toolbar_56(self):
        homepage = HomePage(self.driver)
        analysispage = AnalysisPage(self.driver)
        homepage.type_search("甲醛")  # 输入框中输入甲醛
        homepage.send_submit_btn()  # 点击搜索按钮
        homepage.click_config_2()  # 点击实体筛选框2（此处根据搜索结果来排列，当前化学品位于筛选框第2）
        homepage.click_choose_all()  # 点击勾选 所有 （当前化学品只有1条）
        homepage.click_analysis_button()  # d点击进入图谱分析界面
        analysispage.click_choice()
        time.sleep(3)
        analysispage.acclick_node1()
        analysispage.click_path_analysis()#默认是最短路径，深度为2,
        analysispage.click_confirm()  # 点击确定按钮
        BasePage.get_windows_img1(self)  # 调用基类截图方法

    def test_toolbar_57(self):
        homepage = HomePage(self.driver)
        analysispage = AnalysisPage(self.driver)
        homepage.type_search("甲醛")  # 输入框中输入甲醛
        homepage.send_submit_btn()  # 点击搜索按钮
        homepage.click_config_2()  # 点击实体筛选框2（此处根据搜索结果来排列，当前化学品位于筛选框第2）
        homepage.click_choose_all()  # 点击勾选 所有 （当前化学品只有1条）
        homepage.click_analysis_button()  # d点击进入图谱分析界面
        analysispage.click_choice()
        time.sleep(3)
        analysispage.acclick_node2()
        analysispage.click_path_analysis()  # 默认是最短路径，深度为2,
        analysispage.click_cancel()#d点击取消按钮
        BasePage.get_windows_img1(self)  # 调用基类截图方法

    def test_toolbar_58(self):
        homepage = HomePage(self.driver)
        analysispage = AnalysisPage(self.driver)
        homepage.type_search("甲醛")  # 输入框中输入甲醛
        homepage.send_submit_btn()  # 点击搜索按钮
        homepage.click_config_2()  # 点击实体筛选框2（此处根据搜索结果来排列，当前化学品位于筛选框第2）
        homepage.click_choose_all()  # 点击勾选 所有 （当前化学品只有1条）
        homepage.click_analysis_button()  # d点击进入图谱分析界面
        analysispage.click_choice()
        time.sleep(3)
        analysispage.acclick_node1()
        analysispage.acclick_node2()#多节点进行路径分析
        analysispage.acclick_node3()
        analysispage.click_path_analysis()  # 默认是最短路径，深度为2,
        analysispage.click_confirm()#点击确定按钮
        BasePage.get_windows_img1(self)  # 调用基类截图方法


    def test_toolbar_59(self):
        homepage = HomePage(self.driver)
        analysispage = AnalysisPage(self.driver)
        homepage.type_search("甲醛")  # 输入框中输入甲醛
        homepage.send_submit_btn()  # 点击搜索按钮
        homepage.click_config_2()  # 点击实体筛选框2（此处根据搜索结果来排列，当前化学品位于筛选框第2）
        homepage.click_choose_all()  # 点击勾选 所有 （当前化学品只有1条）
        homepage.click_analysis_button()  # d点击进入图谱分析界面
        analysispage.click_choice()
        time.sleep(3)
        analysispage.acclick_node1()
        analysispage.acclick_node2()
        analysispage.click_reaction()#反应链分析
        BasePage.get_windows_img1(self)  # 调用基类截图方法

    def test_toolbar_60(self):
        homepage = HomePage(self.driver)
        analysispage = AnalysisPage(self.driver)
        homepage.type_search("甲醛")  # 输入框中输入甲醛
        homepage.send_submit_btn()  # 点击搜索按钮
        homepage.click_config_2()  # 点击实体筛选框2（此处根据搜索结果来排列，当前化学品位于筛选框第2）
        homepage.click_choose_all()  # 点击勾选 所有 （当前化学品只有1条）
        homepage.click_analysis_button()  # d点击进入图谱分析界面
        analysispage.click_choice()
        time.sleep(3)
        analysispage.acclick_node1()#单节点进行反应链分析
        analysispage.click_reaction()
        BasePage.get_windows_img1(self)  # 调用基类截图方法

    def test_toolbar_61(self):
        homepage = HomePage(self.driver)
        analysispage = AnalysisPage(self.driver)
        homepage.type_search("甲醛")  # 输入框中输入甲醛
        homepage.send_submit_btn()  # 点击搜索按钮
        homepage.click_config_2()  # 点击实体筛选框2（此处根据搜索结果来排列，当前化学品位于筛选框第2）
        homepage.click_choose_all()  # 点击勾选 所有 （当前化学品只有1条）
        homepage.click_analysis_button()  # d点击进入图谱分析界面
        analysispage.click_choice()
        time.sleep(3)
        analysispage.acclick_node1()
        analysispage.acclick_node2()
        analysispage.acclick_node3()#多节点反应链分析
        analysispage.click_reaction()
        BasePage.get_windows_img1(self)  # 调用基类截图方法


    def test_toolbar_62(self):
        homepage = HomePage(self.driver)
        analysispage = AnalysisPage(self.driver)
        homepage.type_search("甲醛")  # 输入框中输入甲醛
        homepage.send_submit_btn()  # 点击搜索按钮
        homepage.click_config_2()  # 点击实体筛选框2（此处根据搜索结果来排列，当前化学品位于筛选框第2）
        homepage.click_choose_all()  # 点击勾选 所有 （当前化学品只有1条）
        homepage.click_analysis_button()  # d点击进入图谱分析界面
        analysispage.click_choice()
        time.sleep(3)
        analysispage.acclick_node1()#单节点进行反应链分析  天然气节点
        analysispage.acclick_node4()# 水节点 不同类型节点进行反应链分析
        analysispage.click_reaction()
        BasePage.get_windows_img1(self)  # 调用基类截图方法

    def test_toolbar_63(self):
        homepage = HomePage(self.driver)
        analysispage = AnalysisPage(self.driver)
        homepage.type_search("甲醛")  # 输入框中输入甲醛
        homepage.send_submit_btn()  # 点击搜索按钮
        homepage.click_config_2()  # 点击实体筛选框2（此处根据搜索结果来排列，当前化学品位于筛选框第2）
        homepage.click_choose_all()  # 点击勾选 所有 （当前化学品只有1条）
        homepage.click_analysis_button()  # d点击进入图谱分析界面
        analysispage.click_fullscreen()#点击全屏
        BasePage.get_windows_img1(self)  # 调用基类截图方法

    def test_toolbar_64(self):
        homepage = HomePage(self.driver)
        analysispage = AnalysisPage(self.driver)
        homepage.type_search("甲醛")  # 输入框中输入甲醛
        homepage.send_submit_btn()  # 点击搜索按钮
        homepage.click_config_2()  # 点击实体筛选框2（此处根据搜索结果来排列，当前化学品位于筛选框第2）
        homepage.click_choose_all()  # 点击勾选 所有 （当前化学品只有1条）
        homepage.click_analysis_button()  # d点击进入图谱分析界面
        analysispage.click_center()#点击居中
        BasePage.get_windows_img1(self)  # 调用基类截图方法

    def test_toolbar_65(self):
        homepage = HomePage(self.driver)
        analysispage = AnalysisPage(self.driver)
        homepage.type_search("甲醇")  # 输入框中输入甲醛
        homepage.send_submit_btn()  # 点击搜索按钮
        homepage.click_config_2()  # 点击实体筛选框2（此处根据搜索结果来排列，当前化学品位于筛选框第2）
        homepage.click_choose_all()  # 点击勾选 所有 （当前化学品只有1条）
        homepage.click_analysis_button()  # d点击进入图谱分析界面
        analysispage.type_search_place("甲醇")
        analysispage.click_search_button()
        BasePage.get_windows_img1(self)  # 调用基类截图方法

    def test_toolbar_66(self):
        homepage = HomePage(self.driver)
        analysispage = AnalysisPage(self.driver)
        homepage.type_search("甲醇")  # 输入框中输入甲醛
        homepage.send_submit_btn()  # 点击搜索按钮
        homepage.click_config_2()  # 点击实体筛选框2（此处根据搜索结果来排列，当前化学品位于筛选框第2）
        homepage.click_choose_all()  # 点击勾选 所有 （当前化学品只有1条）
        homepage.click_analysis_button()  # d点击进入图谱分析界面
        # analysispage.type_search_place("甲醇")#化学品中文名+英文名
        analysispage.click_search_button()
        BasePage.get_windows_img1(self)  # 调用基类截图方法

    def test_toolbar_67(self):
        homepage = HomePage(self.driver)
        analysispage = AnalysisPage(self.driver)
        homepage.type_search("甲醇")  # 输入框中输入甲醛
        homepage.send_submit_btn()  # 点击搜索按钮
        homepage.click_config_2()  # 点击实体筛选框2（此处根据搜索结果来排列，当前化学品位于筛选框第2）
        homepage.click_choose_all()  # 点击勾选 所有 （当前化学品只有1条）
        homepage.click_analysis_button()  # d点击进入图谱分析界面
        # analysispage.type_search_place("甲醇")#化学品英文名
        analysispage.click_search_button()
        BasePage.get_windows_img1(self)  # 调用基类截图方法

    def test_toolbar_68(self):
        homepage = HomePage(self.driver)
        analysispage = AnalysisPage(self.driver)
        homepage.type_search("甲醇")  # 输入框中输入甲醛
        homepage.send_submit_btn()  # 点击搜索按钮
        homepage.click_config_2()  # 点击实体筛选框2（此处根据搜索结果来排列，当前化学品位于筛选框第2）
        homepage.click_choose_all()  # 点击勾选 所有 （当前化学品只有1条）
        homepage.click_analysis_button()  # d点击进入图谱分析界面
        analysispage.type_search_place("1234")
        analysispage.click_search_button()
        BasePage.get_windows_img1(self)  # 调用基类截图方法

    def test_toolbar_69(self):
        homepage = HomePage(self.driver)
        analysispage = AnalysisPage(self.driver)
        homepage.type_search("甲醇")  # 输入框中输入甲醛
        homepage.send_submit_btn()  # 点击搜索按钮
        homepage.click_config_2()  # 点击实体筛选框2（此处根据搜索结果来排列，当前化学品位于筛选框第2）
        homepage.click_choose_all()  # 点击勾选 所有 （当前化学品只有1条）
        homepage.click_analysis_button()  # d点击进入图谱分析界面
        analysispage.type_search_place("152.36")
        analysispage.click_search_button()
        BasePage.get_windows_img1(self)  # 调用基类截图方法

    def test_toolbar_70(self):
        homepage = HomePage(self.driver)
        analysispage = AnalysisPage(self.driver)
        homepage.type_search("甲醇")  # 输入框中输入甲醛
        homepage.send_submit_btn()  # 点击搜索按钮
        homepage.click_config_2()  # 点击实体筛选框2（此处根据搜索结果来排列，当前化学品位于筛选框第2）
        homepage.click_choose_all()  # 点击勾选 所有 （当前化学品只有1条）
        homepage.click_analysis_button()  # d点击进入图谱分析界面
        analysispage.type_search_place("sdgkjuasoidgu")
        analysispage.click_search_button()
        BasePage.get_windows_img1(self)  # 调用基类截图方法

    def test_toolbar_71(self):
        homepage = HomePage(self.driver)
        analysispage = AnalysisPage(self.driver)
        homepage.type_search("甲醇")  # 输入框中输入甲醛
        homepage.send_submit_btn()  # 点击搜索按钮
        homepage.click_config_2()  # 点击实体筛选框2（此处根据搜索结果来排列，当前化学品位于筛选框第2）
        homepage.click_choose_all()  # 点击勾选 所有 （当前化学品只有1条）
        homepage.click_analysis_button()  # d点击进入图谱分析界面
        analysispage.type_search_place("!@#$$%")
        analysispage.click_search_button()
        BasePage.get_windows_img1(self)  # 调用基类截图方法

    def test_toolbar_72(self):
        homepage = HomePage(self.driver)
        analysispage = AnalysisPage(self.driver)
        homepage.type_search("甲醛")  # 输入框中输入甲醛
        homepage.send_submit_btn()  # 点击搜索按钮
        homepage.click_config_2()  # 点击实体筛选框2（此处根据搜索结果来排列，当前化学品位于筛选框第2）
        homepage.click_choose_all()  # 点击勾选 所有 （当前化学品只有1条）
        homepage.click_analysis_button()  # d点击进入图谱分析界面
        analysispage.click_filter()#点击过滤
        analysispage.click_entity_1()#化学品
        analysispage.type_search_place("甲醛")#过滤后搜索
        analysispage.click_search_button()
        BasePage.get_windows_img1(self)  # 调用基类截图方法

    def test_toolbar_73(self):
        homepage = HomePage(self.driver)
        analysispage = AnalysisPage(self.driver)
        homepage.type_search("甲醛")  # 输入框中输入甲醛
        homepage.send_submit_btn()  # 点击搜索按钮
        homepage.click_config_2()  # 点击实体筛选框2（此处根据搜索结果来排列，当前化学品位于筛选框第2）
        homepage.click_choose_all()  # 点击勾选 所有 （当前化学品只有1条）
        homepage.click_analysis_button()  # d点击进入图谱分析界面
        analysispage.click_choice()
        analysispage.acclick_node1()
        analysispage.acclick_node2()
        analysispage.click_qie_ge()
        analysispage.type_search_place("甲醛")#过滤后搜索
        analysispage.click_search_button()
        BasePage.get_windows_img1(self)  # 调用基类截图方法

    def test_toolbar_74(self):
        homepage = HomePage(self.driver)
        analysispage = AnalysisPage(self.driver)
        homepage.type_search("甲醛")  # 输入框中输入甲醛
        homepage.send_submit_btn()  # 点击搜索按钮
        homepage.click_config_2()  # 点击实体筛选框2（此处根据搜索结果来排列，当前化学品位于筛选框第2）
        homepage.click_choose_all()  # 点击勾选 所有 （当前化学品只有1条）
        homepage.click_analysis_button()  # d点击进入图谱分析界面
        analysispage.click_choice()
        analysispage.acclick_node1()
        analysispage.acclick_node2()
        analysispage.click_delete()
        analysispage.type_search_place("天然气")
        analysispage.click_search_button()
        BasePage.get_windows_img1(self)  # 调用基类截图方法

if __name__ == '__main__':
    unittest.main()