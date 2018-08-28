from selenium import webdriver
import time

while True:
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get("https://s.cinemaspathegaumont.com/#/C3351S201274/booking")
    places = ['I1', 'I2', 'I3', 'I4']
    rows = driver.find_elements_by_xpath('//*[@id="plan"]/tbody/tr')
    for row in rows:
        print(row)
        for col in row.find_elements_by_xpath('td'):
            print(col.find_element_by_xpath('tooltip-content/div/div[2]').get_attribute('innerText'))
            for place in places:
                if place+"\n" in col.find_element_by_xpath('tooltip-content/div/div[2]').get_attribute('innerText'):
                    col.click()
    time.sleep(5)
    # break
    driver.quit()
    for i in range(1, 600):
        time.sleep(1)
        print(i)