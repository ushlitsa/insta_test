import time

from selenium import webdriver
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.search_results_page import SearchResultPage

driver = webdriver.Chrome('E:/Studying/QAA/1/chromedriver_win32/chromedriver')
driver.implicitly_wait(5)

driver.get("https://www.instagram.com/accounts/login/")

login_page = LoginPage(driver)
login_page.enter_username("turgarom")
login_page.enter_password("123456qwe")
login_page.click_login()

main_page = MainPage(driver)
main_page.click_not_now_button()
main_page.type_in_search_field("fitness")
main_page.click_result_with_text("#fitness")

search_results_page = SearchResultPage(driver)

if search_results_page.get_follow_button_text():
    print ("Button appeared")

    driver.quit()
