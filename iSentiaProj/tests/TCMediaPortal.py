'''
This class aims to collect all media portal related test cases
'''
import unittest
from managers.DriverManager import DriverManager
from business.BizNav import BizNav
from business.BizMediaPortal import BizMediaPortal
import time

class TCMediaPortal(unittest.TestCase):
    
    def __init__(self, argv1, argv2, argv3, argv4, argv5, argv6):
        self._argv1 = argv1
        self._argv2 = argv2
        self._argv3 = argv3
        self._argv4 = argv4
        self._argv5 = argv5
        self._argv6 = argv6
        
        try:    
            self._driver_manager = DriverManager(self._argv1, self._argv2, self._argv3, self._argv4, self._argv5, self._argv6)
            if self._argv6 == '':
                self._driver = self._driver_manager.create_driver()
            else:
                self._driver = self._driver_manager.create_driver(self._argv6)
            print 'Driver setup successful'
            print 'Test Environment: ' + self._argv2 + ' ' + self._argv3 + ' ' + self._argv4 + ' ' + self._argv5
            
        except Exception:
            time_str = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
            self._driver.save_screenshot('err' + time_str + '.png')
            raise

    # verify module numbers
    def test1(self, app):
        
        try:
            # navigate to media portal page
            self._bizNav = BizNav()
            self._bizNav.nav_to_mediaportal_page(self._driver, app)
            
            # get web elements to test  
            self._bizMediaPortal = BizMediaPortal()
            num_of_modules = self._bizMediaPortal.get_num_of_modules(self._driver)
            
            #verify the number of modules displayed
            print 'number of modules in media portal page is ' + str(num_of_modules)
            #self.assertTrue(num_of_modules == 3, "the number of modules is not matching the expected result")

        except Exception:
            time_str = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
            self._driver.save_screenshot('err' + time_str + '.png')
            raise 
        
    # verify the module names
    def test2(self):
        try:
            # verify module names accuracy 
            self._bizMediaPortal = BizMediaPortal()
            modules = self._bizMediaPortal.get_all_modules(self._driver)
            # get module names
            print 'all modules in media portal page: '
            for module in modules:
                print module.text
            
            self.assertTrue(modules[0].text == 'Connect', 'Module name - Connect is incorrect')
            self.assertTrue(modules[1].text == 'News and Analytics', 'Module name - News and Analytics is incorrect')
            self.assertTrue(modules[2].text == 'Social', 'Module name - Social is incorrect')
            
        except Exception:
            time_str = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
            self._driver.save_screenshot('err' + time_str + '.png')
            raise 
        
    def finalize(self):
        try:
            self._driver_manager.kill_driver()
            print 'Driver exits successful'
            
        except Exception:
            time_str = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
            self._driver.save_screenshot('err' + time_str + '.png')
            raise
