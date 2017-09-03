'''
Created on 30Aug.,2017

@author: marcoc
'''

class LocationManager(object): 
       
    def element_locator(self, locator, location, driver):
        if locator == 'id':
            self._webelement = driver.find_element_by_id(location)
            
        elif locator == 'name':
            self._webelement = driver.find_element_by_name(location)
            
        elif locator == 'className':
            self._webelement = driver.find_element_by_class_name(location)
        
        elif locator == 'tagName':
            self._webelement = driver.find_element_by_tag_name(location)
        
        elif locator == 'linkText':
            self._webelement = driver.find_element_by_link_text(location)
        
        elif locator == 'partialLinkText':
            self._webelement = driver.find_element_by_partial_link_text(location)
        
        elif locator == 'cssSelector':
            self._webelement = driver.find_element_by_css_selector(location)
        
        elif locator == 'xpath':
            self._webelement = driver.find_element_by_xpath(location)
        
        else:
            print "No locator exists for this element, please check"  
        
        return self._webelement
    
    def elements_locator(self, locator, location, driver):
        if locator == 'id':
            self._webelements = driver.find_elements_by_id(location)
            
        elif locator == 'name':
            self._webelements = driver.find_elements_by_name(location)
            
        elif locator == 'className':
            self._webelements = driver.find_elements_by_class_name(location)
        
        elif locator == 'tagName':
            self._webelements = driver.find_elements_by_tag_name(location)
        
        elif locator == 'linkText':
            self._webelements = driver.find_elements_by_link_text(location)
        
        elif locator == 'partialLinkText':
            self._webelements = driver.find_elements_by_partial_link_text(location)
        
        elif locator == 'cssSelector':
            self._webelements = driver.find_elements_by_css_selector(location)
        
        elif locator == 'xpath':
            self._webelements = driver.find_elements_by_xpath(location)
        
        else:
            print "No locator exists for this element, please check"  
        
        return self._webelements
