import time

from pages.DeleteCustomerPage import DeleteCustomerPage
from pages.NewAccount import NewAccountPage
from pages.NewCustomerPage import NewCustomerPage

from faker import Faker


class Test4:

    def test_new_account(self, open_login_page):

        fake = Faker()

        login_page = open_login_page
        login_page.login_com_sucesso('mngr512504', 'qUqAdYs')
        login_page.click_menu_new_customer()

        new_customer_page = NewCustomerPage(login_page.driver)
        new_customer_page.preencher_formulario_customer(
            fake.name(),
            '10102000',
            'Rua nova conta',
            'Para',
            'Para',
            '45631321',
            '8390919938123',
            fake.email(),
            'Ohomemdeferro12'
        )

        new_customer_page.click_btn_submit_customer()
        customer_id = new_customer_page.get_customer_id()

        new_account_page = NewAccountPage(login_page.driver)
        new_account_page.preencher_new_account_form(customer_id, 1000)

        assert new_account_page.get_text_sucess(), 'Account não foi gerado com sucesso'


