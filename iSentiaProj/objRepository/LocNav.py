'''
Created on 30Aug.,2017

@author: marcoc
'''

class LocNav(object): 
    def set_loc_link_menu(self, loc_link_menu):
        self._loc_link_menu = loc_link_menu
    
    def get_loc_link_menu(self):
        return self._loc_link_menu
    
    def set_loc_link_products_services(self, loc_link_products_services):
        self._loc_link_products_services = loc_link_products_services
        
    def get_loc_link_products_services(self):
        return self._loc_link_products_services
        
    def set_loc_link_mediaportal(self, loc_link_mediaportal):
        self._loc_link_mediaportal = loc_link_mediaportal
        
    def get_loc_link_mediaportal(self):
        return self._loc_link_mediaportal