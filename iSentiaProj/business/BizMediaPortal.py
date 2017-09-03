'''
This class creates a business layer responsible for dealing with test case logic & features (performed on media portal page)

'''

from api.MediaPortal import MediaPortal

class BizMediaPortal(object):
    def __init__(self):
        self._mediaportal = MediaPortal()
        
    # get all module elements
    def get_all_modules(self, driver):
        modules = []
        connect = self._mediaportal.get_module_connect(driver)
        news_analysis = self._mediaportal.get_module_newsAnalysis(driver)
        social = self._mediaportal.get_module_social(driver)
        modules.append(connect)
        modules.append(news_analysis)
        modules.append(social)
        
        return modules
    
    # get number of modules
    def get_num_of_modules(self, driver):
        modules_list = self._mediaportal.get_modules(driver)
        modules_num = len(modules_list)
        
        return modules_num
