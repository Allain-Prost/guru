from selenium.webdriver.common.by import By

from pages.PageObject import PageObject


class NewCustomerPage(PageObject):
    customer_name = 'name'
    date_of_birth = 'dob'
    address = 'addr'
    city = 'city'
    state = 'state'
    pin = 'pinno'
    mobile_number = 'telephoneno'
    email = 'emailid'
    password = 'password'
    btn_submit = 'sub'
    register_customer_sucess = "//*[@id='customer']//p[contains(.,'Customer Registered Successfully!!!')]"
    customer_id = "//*[@id='customer']//tr/td[contains(.,'Customer ID')]/../td[2]"

    def __init__(self, driver):
        super(NewCustomerPage, self).__init__(driver=driver)

    def preencher_formulario_customer(self, customer_name, date_of_birth, address, city, state, pin, mobile_number,
                                      email, password):
        self.driver.find_element(By.NAME, self.customer_name).send_keys(customer_name)
        self.driver.find_element(By.ID, self.date_of_birth).send_keys(date_of_birth)
        self.driver.find_element(By.NAME, self.address).send_keys(address)
        self.driver.find_element(By.NAME, self.city).send_keys(city)
        self.driver.find_element(By.NAME, self.state).send_keys(state)
        self.driver.find_element(By.NAME, self.pin).send_keys(pin)
        self.driver.find_element(By.NAME, self.mobile_number).send_keys(mobile_number)
        self.driver.find_element(By.NAME, self.email).send_keys(email)
        self.driver.find_element(By.NAME, self.password).send_keys(password)

    def click_btn_submit_customer(self):
        self.driver.find_element(By.NAME, self.btn_submit).click()

    def get_text_sucess(self):
        text_sucess = self.driver.find_element(By.XPATH, self.register_customer_sucess)
        return text_sucess

    def get_customer_id(self):
        customer_id = self.driver.find_element(By.XPATH, self.customer_id).text
        return customer_id
