'''
This class aims to initialize/end the web driver in order to prepare/finish test cases 

'''
import os
from selenium import webdriver

class DriverManager(object):
    def __init__(self, os, os_version, browser, browser_version):
        self._os = os
        self._os_version = os_version
        self._browser = browser
        self._browser_version = browser_version
        
    
    def create_driver(self, host='http://www.isentia.com'):
        # create driver environment
        desired_cap = {'os': self._os, 'os_version': self._os_version, 'browser': self._browser, 'browser_version': self._browser_version}
        #desired_cap = {'browser': 'Chrome', 'os': 'Windows', 'os_version': '8'}
        #desired_cap = {'browser': 'IE', 'browser_version': '10.0', 'os': 'Windows', 'os_version': '8'}
        #desired_cap = {'browser': 'Safari', 'os': 'OS X', 'os_version': 'Sierra'} 
        #desired_cap = {'realMobile': 'true', 'device': 'Samsung Galaxy S6', 'browserstack.appium_version': '1.4.16'}
        #desired_cap = {'browserName': 'iPhone', 'platform': 'MAC', 'device': 'iPhone 5'}
        #desired_cap = {'browserName': 'iPhone', 'platform': 'MAC', 'device': 'iPhone 5'}
        desired_cap['browserstack.debug'] = True
        desired_cap['browserstack.networkLogs'] = True
        self.driver = webdriver.Remote(command_executor='http://' + os.environ.get('BROSWERSTACK_USERNAME') + ':' + os.environ.get('BROWSERSTACK_AUTOMATE_KEY') + '@hub.browserstack.com:80/wd/hub',desired_capabilities=desired_cap)
        self.driver.get(host)
        self.driver.maximize_window()
        
        return self.driver
        
    def kill_driver(self):
        self.driver.quit()
        
        




