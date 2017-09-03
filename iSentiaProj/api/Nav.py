'''
This module aims to summarize all api level operations such as sendkeys, click...performed on navigation
'''
from objRepository.ObjNav import ObjNav

class Nav(object):
    
    def __init__(self):
        self._objNav = ObjNav()
        
    def click_menu_link(self, driver):
        link_menu = self._objNav.get_link_menu(driver)
        link_menu.click()
    
    def click_products_services_link(self, driver):
        
        link_products_services = self._objNav.get_link_products_services(driver)
        link_products_services.click()
    
    def click_mediaportal_link(self, driver):
        link_mediaportal = self._objNav.get_link_mediaportal(driver)
        link_mediaportal.click()
        
    