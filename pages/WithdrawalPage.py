from selenium.webdriver.common.by import By

from pages.PageObject import PageObject


class WithdrawalPage(PageObject):
    btn_withdrawal = '.menusubnav li:nth-child(9)'
    account = "input[name='accountno']"
    amount = "input[name='ammount']"
    description = "input[name='desc']"
    btn_submit = "input[name='AccSubmit']"
    menssage_success = ".heading3"

    def __init__(self, driver):
        super(WithdrawalPage, self).__init__(driver=driver)

    def click_menu_withdrawal(self):
        self.driver.find_element(By.CSS_SELECTOR, self.btn_withdrawal).click()

    def preacher_amount_withdrawal_form(self, account_no, amount, description):
        self.click_menu_withdrawal()
        self.driver.find_element(By.CSS_SELECTOR, self.account).click()
        self.driver.find_element(By.CSS_SELECTOR, self.account).send_keys(account_no)

        self.driver.find_element(By.CSS_SELECTOR, self.amount).click()
        self.driver.find_element(By.CSS_SELECTOR, self.amount).send_keys(amount)

        self.driver.find_element(By.CSS_SELECTOR, self.description).click()
        self.driver.find_element(By.CSS_SELECTOR, self.description).send_keys(description)

        self.driver.find_element(By.CSS_SELECTOR, self.btn_submit).click()


    def get_text_success(self):
        text_success = self.driver.find_element(By.CSS_SELECTOR, self.menssage_success).text
        return text_success

    def get_text_failure(self):
        alert_text = self.driver.switch_to.alert.text
        return alert_text

