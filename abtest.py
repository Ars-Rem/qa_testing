from selenium import webdriver
import unittest
#  import time


class ABTest(unittest.TestCase):

    def test_open(self):
        self.driver = webdriver.Chrome(r'C:\Users\Ars\Downloads\chromedriver_win32\chromedriver.exe')
        self.driver.maximize_window()
        self.driver.get('https://the-internet.herokuapp.com/abtest')
        #  link_ars_rem = driver.find_element_by_link_text('Elemental Selenium')
        link_ars_rem = self.driver.find_element_by_xpath('//*[contains(text(), "Elemental Selenium")]')
        link_ars_rem.click()
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[1])
        current_url = self.driver.current_url
        #  time.sleep(1)
        self.assertEqual('http://elementalselenium.com/', current_url)
        #  time.sleep(1)
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
