from selenium import webdriver
import time


driver = webdriver.Chrome(r'C:\Users\Ars\Downloads\chromedriver_win32\chromedriver.exe')
driver.get("http://www.youtube.com/")
searchInput = driver.find_element_by_id("search")
searchInput.send_keys("кипелов")
searchButton = driver.find_element_by_id("search-icon-legacy")
print(type(searchButton))

searchButton.click()
time.sleep(5)
#refuse = driver.find_element_by_css_selector('ytp-id-56')
refuse = driver.find_element_by_xpath("//*[contains(text(), 'Кипелов - Концерт с симфоническим оркестром')]")
print(type(refuse))
refuse.click()
time.sleep(10)
#adblock = driver.find_elements_by_xpath("//*[contains(text(), 'Пропустить рекламу')]")
#print(type(adblock))
#adblock.click()

end = "0:10"
#endOfSong = driver.find_element_by_xpath("//*[@class='ytp-time-duration']").getText()

'''# save main_window
main_window = driver.current_window_handle

# obtain url of gmail on the home page of Google
addr = driver.find_element_by_xpath('//*[@id="gbw"]/div/div/div[1]/div[1]/a').get_attribute("href")

# open new blank tab
driver.execute_script("window.open();")

# switch to the new window which is second in window_handles array
driver.switch_to_window(driver.window_handles[1])

# open successfully and close
driver.get(addr)
driver.close()

# back to the main window
driver.switch_to_window(main_window)
driver.get(addr)
'''