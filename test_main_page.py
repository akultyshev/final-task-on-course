from selenium.webdriver.common.by import By


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    browser.get(link)
    login_link_elt = browser.find_element(By.CSS_SELECTOR, "#login_link")
    login_link_elt.click()
