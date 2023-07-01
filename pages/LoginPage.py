from selenium.webdriver.common.by import By

from pages.PageObject import PageObject


class LoginPage(PageObject):
    url_login = 'https://demo.guru99.com/v4/'
    login = 'uid'
    password = 'password'
    btn_login = 'btnLogin'

    btn_new_customer = '.menusubnav li:nth-child(2)'

    def __init__(self, browser):
        super(LoginPage, self).__init__(browser=browser)
        self.driver.get(self.url_login)

    def open_url(self):
        self.driver.get(self.url_login)

    def preacher_login(self, user_login, user_password):
        self.driver.find_element(By.NAME, self.login).send_keys(user_login)
        self.driver.find_element(By.NAME, self.password).send_keys(user_password)

    def click_btn_login(self):
        self.driver.find_element(By.NAME, self.btn_login).click()

    def login_com_sucesso(self, user_login, user_password):
        self.preacher_login(user_login, user_password)
        self.click_btn_login()

    def get_manger_id(self):
        manger_id = self.driver.find_element(By.CSS_SELECTOR, '.heading3 td').text
        return manger_id

    def click_menu_new_customer(self):
        self.driver.find_element(By.CSS_SELECTOR, self.btn_new_customer).click()
