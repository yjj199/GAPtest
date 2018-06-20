# coding=utf-8
import HTMLTestRunner
import os
import unittest
import time
import testsuits
from testsuits.exact_search import Search01
from testsuits.advanced_search import Search02
from testsuits.fuzzy_search import FuzzySezrch
from testsuits.logo_info import LogoInfo
from testsuits.page import Page
from testsuits.search_time import SearchTime
from testsuits.test_analysis import Analysis
from testsuits.test_toolbar import Toolbar
import screenshort
import time
import unittest
from farmework.browser_engine import BrowserEngine
from pageobjects.homepage import HomePage
from farmework.base_page import BasePage
from farmework.base_page import BasePage
from farmework.logger import Logger
import logging
import os.path
import time
import time
import unittest
from farmework.browser_engine import BrowserEngine
from pageobjects.homepage import HomePage
from farmework.base_page import BasePage
import time
import unittest
from farmework.browser_engine import BrowserEngine
from pageobjects.homepage import HomePage
from farmework.base_page import BasePage
import time
import unittest
from farmework.browser_engine import BrowserEngine
from pageobjects.homepage import HomePage
from farmework.base_page import BasePage
import time
import unittest
from farmework.browser_engine import BrowserEngine
from pageobjects.homepage import HomePage
from farmework.base_page import BasePage
import time
import unittest
from farmework.browser_engine import BrowserEngine
from pageobjects.homepage import HomePage
from farmework.base_page import BasePage
from farmework.base_page import BasePage
from farmework.logger import Logger
import time
import unittest
from farmework.browser_engine import BrowserEngine
from pageobjects.analysisPage import AnalysisPage
from pageobjects.homepage import HomePage
from farmework.base_page import BasePage



# 设置报告文件保存路径
report_path = os.path.dirname(os.path.abspath('.')) + '/testReport/'
# 获取系统当前时间
now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))

# 设置报告名称格式
HtmlFile = report_path + now + "HTMLtemplate.html"
fp = open(HtmlFile, "wb")

# 构建suite
suite = unittest.TestSuite()

# test_dir = os.path.dirname(os.path.abspath('.')) + '/testsuits/'
# suite = unittest.defaultTestLoader.discover(start_dir=test_dir,pattern='test*.py')

# suite.addTest(Search01('test_exact_search_01'))
# suite.addTest(Search01('test_exact_search_02'))
# suite.addTest(Search01('test_exact_search_03'))
# suite.addTest(Search01('test_exact_search_04'))
# suite.addTest(Search01('test_exact_search_04'))
# suite.addTest(Search01('test_exact_search_05'))
# suite.addTest(Search01('test_exact_search_06'))
# suite.addTest(Search01('test_exact_search_07'))
# suite.addTest(Search01('test_exact_search_08'))
# suite.addTest(Search01('test_exact_search_09'))
# suite.addTest(Search01('test_exact_search_10'))
# suite.addTest(Search01('test_exact_search_11'))
# suite.addTest(Search01('test_exact_search_12'))
# suite.addTest(Search01('test_exact_search_13'))
# suite.addTest(Search01('test_exact_search_14'))
# suite.addTest(Search01('test_exact_search_15'))
# suite.addTest(Search01('test_exact_search_16'))
# suite.addTest(Search01('test_exact_search_17'))
# suite.addTest(Search01('test_exact_search_18'))
# suite.addTest(Search01('test_exact_search_20'))
# suite.addTest(Search01('test_exact_search_21'))
# suite.addTest(Search01('test_exact_search_22'))
# suite.addTest(Search01('test_exact_search_23'))
# suite.addTest(Search01('test_exact_search_25'))
# suite.addTest(Search01('test_exact_search_26'))
# suite.addTest(Search01('test_exact_search_28'))
# suite.addTest(Search01('test_exact_search_29'))
# #高级搜索
# suite.addTest(Search02('test_advanced_search_01'))
# suite.addTest(Search02('test_advanced_search_02'))
# suite.addTest(Search02('test_advanced_search_03'))
# suite.addTest(Search02('test_advanced_search_04'))
# suite.addTest(Search02('test_advanced_search_11'))
# suite.addTest(Search02('test_advanced_search_09'))
# suite.addTest(Search02('test_advanced_search_10'))
# suite.addTest(Search02('test_advanced_search_12'))
# suite.addTest(Search02('test_advanced_search_13'))
# suite.addTest(Search02('test_advanced_search_14'))
# suite.addTest(Search02('test_advanced_search_17'))
# suite.addTest(Search02('test_advanced_search_18'))
# suite.addTest(Search02('test_advanced_search_19'))
# suite.addTest(Search02('test_advanced_search_20'))
# suite.addTest(Search02('test_advanced_search_21'))
# suite.addTest(Search02('test_advanced_search_22'))
# suite.addTest(Search02('test_advanced_search_23'))
# suite.addTest(Search02('test_advanced_search_30'))
# suite.addTest(Search02('test_advanced_search_31'))
# suite.addTest(Search02('test_advanced_search_32'))
# suite.addTest(Search02('test_advanced_search_56'))
# suite.addTest(Search02('test_advanced_search_53'))
# suite.addTest(Search02('test_advanced_search_54'))
# suite.addTest(Search02('test_advanced_search_55'))
# suite.addTest(Search02('test_advanced_search_33'))
# suite.addTest(Search02('test_advanced_search_34'))
# suite.addTest(Search02('test_advanced_search_35'))
# suite.addTest(Search02('test_advanced_search_36'))
# suite.addTest(Search02('test_advanced_search_41'))
# suite.addTest(Search02('test_advanced_search_42'))
# suite.addTest(Search02('test_advanced_search_43'))
# suite.addTest(Search02('test_advanced_search_44'))
# suite.addTest(Search02('test_advanced_search_45'))
# suite.addTest(Search02('test_advanced_search_46'))
# suite.addTest(Search02('test_advanced_search_47'))
# suite.addTest(Search02('test_advanced_search_48'))
# suite.addTest(Search02('test_advanced_search_49'))
#页面跳转
# suite.addTest(Page('test_page_01'))
# suite.addTest(Page('test_page_02'))
# suite.addTest(Page('test_page_03'))
# suite.addTest(Page('test_page_04'))
# suite.addTest(Page('test_page_05'))
# suite.addTest(Page('test_page_06'))
# suite.addTest(Page('test_page_07'))
# suite.addTest(Page('test_page_08'))
# suite.addTest(Page('test_page_09'))
# suite.addTest(Page('test_page_10'))
# suite.addTest(Page('test_page_11'))
# suite.addTest(Page('test_page_12'))
# suite.addTest(Page('test_page_13'))
# suite.addTest(Page('test_page_14'))
# suite.addTest(Page('test_page_15'))
# suite.addTest(Page('test_page_16'))
# suite.addTest(Page('test_page_17'))
# suite.addTest(Page('test_page_18'))
# suite.addTest(Page('test_page_19'))
# suite.addTest(Page('test_page_20'))
# suite.addTest(Page('test_page_21'))
# suite.addTest(Page('test_page_22'))
#模糊搜索测试用例
# suite.addTest(FuzzySezrch("test_fuzzy_search_01"))
# suite.addTest(FuzzySezrch('test_fuzzy_search_02'))
# suite.addTest(FuzzySezrch('test_fuzzy_search_03'))
# suite.addTest(FuzzySezrch('test_fuzzy_search_04'))
# suite.addTest(FuzzySezrch('test_fuzzy_search_05'))
# suite.addTest(FuzzySezrch('test_fuzzy_search_06'))
# suite.addTest(FuzzySezrch('test_fuzzy_search_07'))

#图谱分析
# suite.addTest(Analysis("test_analysis_01"))
# suite.addTest(Toolbar("test_toolbar_36"))
#图谱分析界面工具栏
suite.addTest(Toolbar("test_toolbar_03_01"))

if __name__ == '__main__':
    # 初始化一个HTMLTestRunner实例对象，用来生成报告
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u"GAP化工测试报告", description=u"用例测试情况")
    # 开始执行测试套件
    runner.run(suite)
    fp.close()