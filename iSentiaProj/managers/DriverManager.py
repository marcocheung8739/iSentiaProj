'''
This class aims to initialize/end the web driver in order to prepare/finish test cases 

'''
import os
from selenium import webdriver

class DriverManager(object):
    def __init__(self, argv1, argv2, argv3, argv4, argv5, argv6):
        self._argv1 = argv1
        self._argv2 = argv2
        self._argv3 = argv3
        self._argv4 = argv4
        self._argv5 = argv5
        self._argv6 = argv6
        #print self._argv3, self._argv4, self._argv5
        
    
    def create_driver(self, host='http://www.isentia.com'):
        # create driver environment
        if self._argv1 == 'Web':
            desired_cap = {'os': self._argv2, 'os_version': self._argv3, 'browser': self._argv4, 'browser_version': self._argv5}
        else:
            
            desired_cap = {'device': self._argv3, 'realMobile': self._argv4, 'browserstack.appium_version': self._argv5}
        #desired_cap = {'browser': 'Chrome', 'os': 'Windows', 'os_version': '8'}
        #desired_cap = {'browser': 'IE', 'browser_version': '10.0', 'os': 'Windows', 'os_version': '8'}
        #desired_cap = {'browser': 'Safari', 'os': 'OS X', 'os_version': 'Sierra'} 
        
        #desired_cap = {'browserName': 'iPhone', 'platform': 'MAC', 'device': 'iPhone 5'}
        #desired_cap = {'browserName': 'iPhone', 'platform': 'MAC', 'device': 'iPhone 5'}
        desired_cap['browserstack.debug'] = True
        desired_cap['browserstack.networkLogs'] = True
        self.driver = webdriver.Remote(command_executor='http://' + os.environ.get('BROSWERSTACK_USERNAME') + ':' + os.environ.get('BROWSERSTACK_AUTOMATE_KEY') + '@hub.browserstack.com:80/wd/hub',desired_capabilities=desired_cap)
        self.driver.get(host)
        if self._argv1 == 'Web':
            self.driver.maximize_window()
        
        return self.driver
        
    def kill_driver(self):
        self.driver.quit()
        
        




