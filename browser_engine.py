# coding = utf-8
import os.path
import time
from selenium import webdriver
from farmework.logger import Logger

logger = Logger(logger="browser_engine").getlog()


class BrowserEngine(object):
    dir = os.path.dirname(os.path.abspath('.'))  # 注意相对路径获取方法
    chrome_driver_path = dir + '/tools/chromedriver.exe'
    #chorme_parh = dir + '/tools/Chrome/Application/chrome.exe'

    #chrome_driver_path = "C:/ProgramData/Anaconda3/chromedriver.exe"

    def __init__(self, driver):
        self.driver = driver

        # read the browser type from config.ini file, return the driver

    def open_browser(self, driver):
        #chromedriver = "C:/Program Files/Python37/chromedriver.exe"
        #chromedriver = os.path.dirname(os.path.abspath('.')) + '/tools/chromedriver.exe/'
        #os.environ["webdriver.chrome.driver"] = chromedriver
        driver = webdriver.Chrome(self.chrome_driver_path)  # 打开浏览器
        logger.info("Starting Chrome browser.")
        driver.maximize_window()  # 窗口最大化
        logger.info("Maximize the current window.")
        driver.get("http://192.168.0.144:8080/#/login")
        logger.info("enter 68")
        driver.implicitly_wait(10)
        logger.info("Set implicitly wait 10 seconds.")
        return driver

    def quit_browser(self):
        logger.info("Now, Close and quit the browser.")
        self.driver.quit()