'''
This class aims to collect all media portal related test cases
'''
import unittest
from managers.DriverManager import DriverManager
from business.BizNav import BizNav
from business.BizMediaPortal import BizMediaPortal
import time

class TCMediaPortal(unittest.TestCase):
    
    def __init__(self, os, os_version, browser, browser_version, host):
        self._os = os
        self._os_version = os_version
        self._browser = browser
        self._browser_version = browser_version
        self._host = host
        
        try:    
            self._driver_manager = DriverManager(self._os, self._os_version, self._browser, self._browser_version)
            if self._host == '':
                self._driver = self._driver_manager.create_driver()
            else:
                self._driver = self._driver_manager.create_driver(self._host)
            print 'Driver setup successful'
            
        except Exception:
            time_str = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
            self._driver.save_screenshot('err' + time_str + '.png')
            raise

    # verify module numbers
    def test1(self):
        
        try:
            # navigate to media portal page
            self._bizNav = BizNav()
            self._bizNav.nav_to_mediaportal_page(self._driver)
            
            # get web elements to test  
            self._bizMediaPortal = BizMediaPortal()
            num_of_modules = self._bizMediaPortal.get_num_of_modules(self._driver)
            
            #verify the number of modules displayed
            print 'number of modules in media portal page is ' + str(num_of_modules)
            #self.assertEqual(num_of_modules, 3, "the number of modules is not matching the expected result")

        except Exception:
            time_str = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
            self._driver.save_screenshot('err' + time_str + '.png')
            raise 
        
    # verify the module names
    def test2(self):
        try:
        #verify if module names are displayed
            self._bizMediaPortal = BizMediaPortal()
            modules = self._bizMediaPortal.get_all_modules(self._driver)
            self.assertTrue(modules[0].is_displayed(), 'Module name - Connect is not displayed')
            self.assertTrue(modules[1].is_displayed(), 'Module name - News And Analytics is not displayed')
            self.assertTrue(modules[2].is_displayed(), 'Module name - Social is not displayed')
            # get module names
            print 'all modules in media portal page: '
            for module in modules:
                print module.text
            
            # verify module names accuracy 
            self.assertEqual(modules[0].text, 'Connect', 'Module name - Connect is incorrect')
            self.assertEqual(modules[1].text, 'News and Analytics', 'Module name - News and Analytics is incorrect')
            self.assertEqual(modules[2].text, 'Social', 'Module name - Social is incorrect')
            
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
