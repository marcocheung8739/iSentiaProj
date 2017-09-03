'''
This class plays the role of "main", which is the entrance to the entire framework
'''
import sys
from tests.TCMediaPortal import TCMediaPortal

class TestRunner(object):
    def __init__(self, os, os_version, browser, browser_version, host):
        self._os = os
        self._os_version = os_version
        self._browser = browser
        self._browser_version = browser_version
        self._host = host

    def run_tests(self):
        tcMediaPortal = TCMediaPortal(self._os, self._os_version, self._browser, self._browser_version, self._host)
        
        # start test1
        tcMediaPortal.test1()
        # start test2
        tcMediaPortal.test2()
        
        tcMediaPortal.finalize()
    '''
    def run_tests(self):

        tcMediaPortal = unittest.TestLoader().loadTestsFromTestCase(TCMediaPortal)
 
        # create a test suite combining search_text and home_page_test
        test_suite = unittest.TestSuite([tcMediaPortal])
 
        # run the suite
        unittest.TextTestRunner(verbosity=2).run(test_suite)
        '''
    
if __name__ == "__main__":
    test_runner = TestRunner(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
    test_runner.run_tests()
