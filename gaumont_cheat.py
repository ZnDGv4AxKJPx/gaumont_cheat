from selenium import webdriver
from selenium.webdriver import FirefoxProfile
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import time


profile = FirefoxProfile()
profile.set_preference("network.proxy.type", 1)
profile.set_preference("network.proxy.socks", "127.0.0.1")
profile.set_preference("network.proxy.socks_port", 9150)

while True:
    driver = webdriver.Firefox(firefox_profile=profile)
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://www.myip.ms/")
    print(driver.find_element_by_xpath('//*[@id="whois_table"]/tbody/tr[6]/td[2]/a').text)
    print(driver.find_element_by_xpath('//*[@id="whois_table"]/tbody/tr[1]/td[2]/div/b/a').text)
    time.sleep(5)
    driver.quit()
    for i in range(1, 60):
        time.sleep(1)
        print(i)


#while True:
# driver = webdriver.Firefox()
# driver.maximize_window()
# driver.implicitly_wait(10)
# driver.get("https://s.cinemaspathegaumont.com/#/C3351S201603/booking")
# places = ['O2', 'O4']
# to_hide = driver.find_element_by_xpath("/html/body/cgp-front-app/booking-component/booking-seating-component/div/div/div/booking-seating-validation-component/section")
# driver.execute_script("arguments[0].style.visibility='hidden'", to_hide)
# rows = driver.find_elements_by_xpath('//*[@id="plan"]/tbody/tr')
# for row in rows:
#     print(row)
#     for col in row.find_elements_by_xpath('td'):
#         print(col.find_element_by_xpath('tooltip-content/div/div[2]').get_attribute('innerText'))
#         for place in places:
#             if place+"\n" in col.find_element_by_xpath('tooltip-content/div/div[2]').get_attribute('innerText'):
#                 col.click()
# time.sleep(5)
# # break
# driver.quit()
#for i in range(1, 600):
#    time.sleep(1)
#    print(i)
