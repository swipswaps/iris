from targets.firefox.fx_testcase import *


class Test(FirefoxTest):
    def setUp(self):
        self.meta = 'Test_case example1'
        self.test_case_id = '123'
        self.test_suite_id = '345'

    def test_run(self):
        print(self.meta)
        mylogger.info("Testing logger")
        assert 1 == 1
