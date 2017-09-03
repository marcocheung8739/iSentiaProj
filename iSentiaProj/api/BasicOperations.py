class BasicOperations(object):
    
    # split the "location  locator" pair from properties file
    def element(self, location):
        element_location_locator = location.split('\t')
        
        return element_location_locator
        
