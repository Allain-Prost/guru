from selenium.webdriver.common.by import By

from pages.PageObject import PageObject


class DeleteCustomerPage(PageObject):
    btn_delete_customer = '.menusubnav li:nth-child(4)'
    loc_customer_id = 'cusid'
    btn_submit = 'AccSubmit'

    def __init__(self, driver):
        super(DeleteCustomerPage, self).__init__(driver=driver)

    def click_menu_delete_customer(self):
        self.driver.find_element(By.CSS_SELECTOR, self.btn_delete_customer).click()

    def delete_customer_from_id(self, customer_id):
        self.driver.find_element(By.NAME, self.loc_customer_id).click()
        self.driver.find_element(By.NAME, self.loc_customer_id).send_keys(customer_id)
        self.driver.find_element(By.NAME, self.btn_submit).click()

    def get_text_alert(self):
        alert_text = self.driver.switch_to.alert.text
        return alert_text

    def accept_alert(self):
        return self.driver.switch_to.alert
