import unittest
import csv, xlrd
import time
from ddt import ddt, data, unpack
from selenium import webdriver
from selenium.webdriver.common.by import By

def get_dataCSV(filename):
    rows = []
    datafile = open(filename, "r")
    reader = csv.reader(datafile)
    next(reader, None)
    for row in reader:
        rows.append(row)
    return rows

'''def get_dataEXCEL(filename):
    rows = []
    book = xlrd.open_workbook(filename)
    sheet = book.sheet_by_index(0)
    for row_idx in range(1, sheet.nrows):
        rows.append(list(sheet.row_values(row_idx, 0, sheet.ncols)))
    return rows'''

@ddt
class UsingDDT(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.driver.get("https://prom.ua")

    '''def test1_login(self):
        inputLogin = self.driver.find_element(By.ID, "user-name")
        inputLogin.send_keys("standard_user")
        inputPass = self.driver.find_element(By.ID, "password")
        inputPass.send_keys("secret_sauce")
        btnLogin = self.driver.find_element(By.ID, "login-button")
        btnLogin.click()'''
    
    '''@data(["phones", 30], ["music", 30], ["military", 29])
    @unpack
    def test2_search(self, search_value, expected_count):
        search_box = self.driver.find_element(By.XPATH, "//input[@type='search' and @class='Dm7py']")
        search_box.clear()
        search_box.send_keys(search_value)
        search_box.submit()
        time.sleep(2)
        products = self.driver.find_elements(By.XPATH, "//a[@target='_self']")
        print(type(products))
        print("Found " + str(len(products)) + " products:")
        for product in products:
            print(product.get_attribute("title"))
        #self.assertAlmostEqual(expected_count, len(products), 0, "first and second are not almost equal")
        #self.assertAlmostEqual
        self.assertGreaterEqual(expected_count, len(products), "not greater or equal")'''
    
    @data(*get_dataCSV("GundechaProject\DataDDT.csv"))
    @unpack
    def test3_searchWith_CSV_File(self, search_value, expected_count):
        search_box = self.driver.find_element(By.XPATH, "//input[@type='search' and @class='Dm7py']")
        search_box.clear()
        search_box.send_keys(search_value)
        search_box.submit()
        time.sleep(2)
        products = self.driver.find_elements(By.XPATH, "//a[@target='_self']")
        expected_count = int(expected_count)
        print(len(products))
        if expected_count > 0:
            self.assertGreaterEqual(len(products), expected_count, "not greater or equal")
        else:
            msg = self.driver.find_element(By.XPATH, "//span[contains(text(), 'назву товару по-іншому')]")
            self.assertEqual("Спробуйте написати назву товару по-іншому, скоротити запит або перейдіть в категорію", msg.text)

    '''@data(*get_dataEXCEL("GundechaProject\DataDDT.xls"))
    @unpack
    def test3_searchWith_XLS_File(self, search_value, expected_count):
        search_box = self.driver.find_element(By.XPATH, "//input[@type='search' and @class='Dm7py']")
        search_box.clear()
        search_box.send_keys(search_value)
        search_box.submit()
        time.sleep(2)
        products = self.driver.find_elements(By.XPATH, "//a[@target='_self']")
        expected_count = int(expected_count)
        print(len(products))
        if expected_count > 0:
            self.assertGreaterEqual(len(products), expected_count, "not greater or equal")
        else:
            msg = self.driver.find_element(By.XPATH, "//span[contains(text(), 'назву товару по-іншому')]")
            self.assertEqual("Спробуйте написати назву товару по-іншому, скоротити запит або перейдіть в категорію", msg.text)'''

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)
