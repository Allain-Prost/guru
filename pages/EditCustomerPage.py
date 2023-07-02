from selenium.webdriver.common.by import By

from pages.PageObject import PageObject


class EditCustomerPage(PageObject):
    btn_edit_customer = '.menusubnav li:nth-child(3)'
    customer_id_edit = 'cusid'
    btn_submit = 'AccSubmit'
    address_edit = 'addr'
    btn_submit_edit = 'sub'

    def __init__(self, driver):
        super(EditCustomerPage, self).__init__(driver=driver)

    def click_menu_edit_customer(self):
        self.driver.find_element(By.CSS_SELECTOR, self.btn_edit_customer).click()

    def edit_customer_id(self, customer_id):
        self.driver.find_element(By.NAME, self.customer_id_edit).click()
        self.driver.find_element(By.NAME, self.customer_id_edit).send_keys(customer_id)
        self.driver.find_element(By.NAME, self.btn_submit).click()

    def edit_address_customer_id(self, new_address):
        self.driver.find_element(By.NAME, self.address_edit).click()
        self.driver.find_element(By.NAME, self.address_edit).clear()
        self.driver.find_element(By.NAME, self.address_edit).send_keys(new_address)
        self.driver.find_element(By.NAME, self.btn_submit_edit).click()
