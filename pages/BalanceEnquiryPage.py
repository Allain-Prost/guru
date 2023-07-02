from selenium.webdriver.common.by import By

from pages.PageObject import PageObject


class BalanceEnquiryPage(PageObject):
    btn_balance_enquiry = '.menusubnav li:nth-child(12)'
    loc_customer_id = 'cusid'
    btn_submit = 'AccSubmit'

    def __init__(self, driver):
        super(BalanceEnquiryPage, self).__init__(driver=driver)

    def click_menu_balance_enquiry(self):
        self.driver.find_element(By.CSS_SELECTOR, self.btn_balance_enquiry).click()

    def heck_balance_passing_null_account_number(self, customer_id):
        self.driver.find_element(By.NAME, self.loc_customer_id).click()
        self.driver.find_element(By.NAME, self.loc_customer_id).send_keys(customer_id)
        self.driver.find_element(By.NAME, self.btn_submit).click()
