'''
This class plays the role of "main", which is the entrance to the entire framework
'''
import sys
from tests.TCMediaPortal import TCMediaPortal

class TestRunner(object):
    def __init__(self, argv1, argv2, argv3, argv4, argv5, argv6):
        if(argv1 != 'Web' and argv1 != 'Mobile'):
            print 'No Application is sepcified. Testing has to be performed on either web application or mobile application'
            exit
        else:
            self._argv1 = argv1
            self._argv2 = argv2
            self._argv3 = argv3
            self._argv4 = argv4
            self._argv5 = argv5
            self._argv6 = argv6

    def run_tests(self):
        tcMediaPortal = TCMediaPortal(self._argv1, self._argv2, self._argv3, self._argv4, self._argv5, self._argv6)
        
        # start test1
        tcMediaPortal.test1(self._argv1)
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
    
    test_runner = TestRunner(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6])
    test_runner.run_tests()
