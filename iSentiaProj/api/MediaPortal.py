'''
This module aims to summarize all api level operations such as sendkeys, click...performed on media portal page
'''
from objRepository.ObjMediaPortal import ObjMediaPortal

class MediaPortal(object):
    
    def __init__(self):
        self._objMediaPortal = ObjMediaPortal()
    
    # return all media portal name elements
    def get_module_connect(self, driver):
        self._mediaportal_module_connect = self._objMediaPortal.get_text_module_connect(driver)
        return self._mediaportal_module_connect
    
    def get_module_newsAnalysis(self, driver):
        self._mediaportal_module_newsAnalysis = self._objMediaPortal.get_text_module_newsAnalytics(driver)
        return self._mediaportal_module_newsAnalysis
        
    def get_module_social(self, driver):
        self._mediaportal_module_social = self._objMediaPortal.get_text_module_social(driver)
        return self._mediaportal_module_social
    
    def get_modules(self, driver):
        self._mediaportal_modules = self._objMediaPortal.get_modules(driver)
        return self._mediaportal_modules

