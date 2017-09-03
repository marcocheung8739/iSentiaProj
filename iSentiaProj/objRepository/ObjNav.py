'''
Object Repository for navigation bar - this file aims to manipulate nav elements 
'''
import os
from objRepository.LocNav import *
from utils.FileReader import *
from api.BasicOperations import *
from managers.LocationManager import LocationManager

class ObjNav(object):
    
    def __init__(self):
        file_reader = FileReader()
        file_path = os.path.abspath('navigation.properties')
        prop = file_reader.read_file(file_path)
        
        #initialize instances for basic operations and location manager
        self._basic_operations = BasicOperations()
        self._location_manager = LocationManager()
        
        #initialize locations of navigation elements
        self._locNav = LocNav()
        self._locNav.set_loc_link_products_services(prop['loc_link_productsServices'])
        self._locNav.set_loc_link_mediaportal(prop['loc_link_mediaPortal'])
        
    def get_link_products_services(self, driver):   
        # return "element location + locator"
        element_location_locator = self._basic_operations.element(self._locNav.get_loc_link_products_services())
        link_products_services = self._location_manager.element_locator(element_location_locator[1], element_location_locator[0], driver)
        
        return link_products_services
    
    def get_link_mediaportal(self, driver):
        
        element_location_locator = self._basic_operations.element(self._locNav.get_loc_link_mediaportal())
        link_mediaportal = self._location_manager.element_locator(element_location_locator[1], element_location_locator[0], driver)
        
        return link_mediaportal


        

