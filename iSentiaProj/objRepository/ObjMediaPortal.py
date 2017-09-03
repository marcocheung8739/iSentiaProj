'''
Object Repository for media portal page - this file aims to manipulate media portal elements 
'''
import os
from objRepository.LocMediaPortal import LocMediaPortal
from utils.FileReader import *
from api.BasicOperations import *
from managers.LocationManager import LocationManager

class ObjMediaPortal(object):
    
    def __init__(self):
        file_reader = FileReader()
        file_path = os.path.abspath('mediaportal.properties')
        prop = file_reader.read_file(file_path)
        
        #initialize instances for basic operations and location manager
        self._basic_operations = BasicOperations()
        self._location_manager = LocationManager()
        
        #initialize locations of media portal elements
        self._locMediaPortal = LocMediaPortal()
        self._locMediaPortal.set_loc_textArea_module_connect(prop['loc_textarea_moduleConnect'])
        self._locMediaPortal.set_loc_textArea_module_newsAnalytics(prop['loc_textarea_moduleNewsAnalytics'])
        self._locMediaPortal.set_loc_textArea_module_social(prop['loc_textarea_moduleSocial'])
        self._locMediaPortal.set_loc_modules(prop['num_of_modules'])
        
    # return "element location + locator"
    def get_text_module_connect(self, driver):
        
        element_location_locator = self._basic_operations.element(self._locMediaPortal.get_loc_textArea_module_connect())
        text_module_connect = self._location_manager.element_locator(element_location_locator[1], element_location_locator[0], driver)
        
        return text_module_connect
    
    def get_text_module_newsAnalytics(self, driver):
        
        element_location_locator = self._basic_operations.element(self._locMediaPortal.get_loc_textArea_module_newsAnalytics())
        text_module_newsAnalytics = self._location_manager.element_locator(element_location_locator[1], element_location_locator[0], driver)
        
        return text_module_newsAnalytics
    
    def get_text_module_social(self, driver):
        
        element_location_locator = self._basic_operations.element(self._locMediaPortal.get_loc_textArea_module_social())
        text_module_social = self._location_manager.element_locator(element_location_locator[1], element_location_locator[0], driver)

        return text_module_social
    
    def get_modules(self, driver):
        
        element_location_locator = self._basic_operations.element(self._locMediaPortal.get_loc_modules())
        modules = self._location_manager.elements_locator(element_location_locator[1], element_location_locator[0], driver)
        
        return modules
    
    

