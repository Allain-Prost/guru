from selenium.webdriver.common.by import By

from pages.PageObject import PageObject


class BalanceEnquiryPage(PageObject):
    btn_balance_enquiry = '.menusubnav li:nth-child(12)'
    account_id = "//input[@name='accountno']"
    btn_submit = "//input[@name='AccSubmit']"

    def __init__(self, driver):
        super(BalanceEnquiryPage, self).__init__(driver=driver)

    def click_menu_balance_enquiry(self):
        self.driver.find_element(By.CSS_SELECTOR, self.btn_balance_enquiry).click()

    def click_btn_submit(self):
        self.driver.find_element(By.XPATH, self.btn_submit).click()

    def heck_balance_passing_null_account_number(self, customer_id):
        self.driver.find_element(By.XPATH, self.account_id).click()
        self.driver.find_element(By.XPATH, self.account_id).send_keys(customer_id)
        self.driver.find_element(By.XPATH, self.btn_submit).click()

    def get_text_alert(self):
        alert_text = self.driver.switch_to.alert.text
        return alert_text

    def accept_alert(self):
        alert = self.driver.switch_to.alert.text
        return alert
