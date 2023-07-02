from selenium.webdriver.common.by import By

from pages.PageObject import PageObject


class NewAccountPage(PageObject):
    btn_new_account = '.menusubnav li:nth-child(5)'
    customer_id = "//input[@name='cusid']"
    account_type = "select[name='selaccount']"
    type_savings = "option[value='Savings']"
    initial_deposit = "input[name='inideposit']"
    btn_submit = "input[name='button2']"
    menssage_success = ".heading3"

    def __init__(self, driver):
        super(NewAccountPage, self).__init__(driver=driver)

    def click_menu_new_account(self):
        self.driver.find_element(By.CSS_SELECTOR, self.btn_new_account).click()

    def preencher_new_account_form(self, customer_id, initial_deposit):
        self.click_menu_new_account()
        self.driver.find_element(By.XPATH, self.customer_id).click()
        self.driver.find_element(By.XPATH, self.customer_id).send_keys(customer_id)
        self.driver.find_element(By.CSS_SELECTOR, self.account_type).click()
        self.driver.find_element(By.CSS_SELECTOR, self.type_savings).click()
        self.driver.find_element(By.CSS_SELECTOR, self.initial_deposit).click()
        self.driver.find_element(By.CSS_SELECTOR, self.initial_deposit).send_keys(initial_deposit)
        self.driver.find_element(By.CSS_SELECTOR, self.btn_submit).click()

    def get_text_sucess(self):
        text_sucess = self.driver.find_element(By.CSS_SELECTOR, self.menssage_success).text
        return text_sucess