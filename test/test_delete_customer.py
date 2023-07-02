import time

from selenium.webdriver.support import expected_conditions, wait

from pages.DeleteCustomer import DeleteCustomerPage
from pages.NewCustomerPage import NewCustomerPage

from faker import Faker


class Test2:

    def test_delete_customer(self, open_login_page):

        fake = Faker()

        login_page = open_login_page
        login_page.login_com_sucesso('mngr512504', 'qUqAdYs')
        login_page.click_menu_new_customer()

        new_customer_page = NewCustomerPage(login_page.driver)
        new_customer_page.preencher_formulario_customer(
            fake.name(),
            '10101997',
            'Rua Feliz da vida',
            'Joao Pessoa',
            'Paraiba',
            '456321',
            '83909138123',
            fake.email(),
            'Ohomemdeferro12'
        )

        new_customer_page.click_btn_submit_customer()
        customer_id = new_customer_page.get_customer_id()

        print(customer_id)

        delete_customer_page = DeleteCustomerPage(login_page.driver)
        delete_customer_page.click_menu_delete_customer()
        delete_customer_page.delete_customer_from_id(customer_id)

        alert = delete_customer_page.driver.switch_to.alert
        alert.accept()

        alert_ok = delete_customer_page.driver.switch_to.alert
        alert_ok.dismiss()

        time.sleep(5)
