from selenium.webdriver.common.by import By

from pages.PageObject import PageObject


class FundTransferPage(PageObject):
    btn_fund_transfer = '.menusubnav li:nth-child(10)'
    loc_payers_account_no = "input[name='payersaccount']"
    loc_payees_account_no = "input[name='payeeaccount']"
    loc_amount = "input[name='ammount']"
    loc_description = "input[name='desc']"
    menssage_success = ".heading3"
    btn_submit = "input[name='AccSubmit']"
    from_account_number = "//*[@class='layout']//tr/td/table//td[contains(.,'From Account Number')]/../td[2]"
    to_account_number = "//*[@class='layout']//tr/td/table//td[contains(.,'To Account Number')]/../td[2]"
    amount = "//*[@class='layout']//tr/td/table//td[contains(.,'Amount')]/../td[2]"

    def __init__(self, driver):
        super(FundTransferPage, self).__init__(driver=driver)

    def click_menu_fund_transfer(self):
        self.driver.find_element(By.CSS_SELECTOR, self.btn_fund_transfer).click()

    def preacher_fund_transfer(self, payers_account_no, payees_account_no, amount, description):
        self.click_menu_fund_transfer()
        self.driver.find_element(By.CSS_SELECTOR, self.loc_payers_account_no).click()
        self.driver.find_element(By.CSS_SELECTOR, self.loc_payers_account_no).send_keys(payers_account_no)

        self.driver.find_element(By.CSS_SELECTOR, self.loc_payees_account_no).click()
        self.driver.find_element(By.CSS_SELECTOR, self.loc_payees_account_no).send_keys(payees_account_no)

        self.driver.find_element(By.CSS_SELECTOR, self.loc_amount).click()
        self.driver.find_element(By.CSS_SELECTOR, self.loc_amount).send_keys(amount)

        self.driver.find_element(By.CSS_SELECTOR, self.loc_description).click()
        self.driver.find_element(By.CSS_SELECTOR, self.loc_description).send_keys(description)

        self.driver.find_element(By.CSS_SELECTOR, self.btn_submit).click()

    def get_from_account_number(self):
        from_account_number = self.driver.find_element(By.XPATH, self.from_account_number).text
        return from_account_number

    def get_to_account_number(self):
        to_account_number = self.driver.find_element(By.XPATH, self.to_account_number).text
        return to_account_number

    def get_amount(self):
        amount = self.driver.find_element(By.XPATH, self.amount).text
        return amount

    def get_text_failure(self):
        alert_text = self.driver.switch_to.alert.text
        return alert_text