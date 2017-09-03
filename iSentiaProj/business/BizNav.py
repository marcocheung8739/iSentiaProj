'''
This class creates a business layer responsible for dealing with test case logic & features (performed on navigation)

'''
from api.Nav import Nav
import time

class BizNav(object):
    def __init__(self):
        self._nav = Nav()
        
    def nav_to_mediaportal_page(self, driver, app):
        # for mobile application there is a drop down menu which needs to be dealt with
        if app == 'Mobile':
            self._nav.click_menu_link(driver)
            time.sleep(5)
        
        self._nav.click_products_services_link(driver)
        time.sleep(5)
        self._nav.click_mediaportal_link(driver)
        
    
