import unittest
import HtmlTestRunner
import os
from NewFile2_test import SearchTest
from PickMeTest import HomePageTest


search_tests = unittest.TestLoader().loadTestsFromTestCase(SearchTest)

home_page_tests = unittest.TestLoader().loadTestsFromTestCase(HomePageTest)

smoke_tests = unittest.TestSuite([search_tests, home_page_tests])

runner = HtmlTestRunner.HTMLTestRunner(
    verbosity=2, output='_reports', title='Test report', report_name='report',
    open_in_browser=True, description="HTMLTestReport", tested_by="Artem Marchenko",
    add_traceback=False
    )

runner.run(smoke_tests)