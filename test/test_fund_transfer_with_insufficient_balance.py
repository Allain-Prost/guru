import time

from pages.FundTransferPage import FundTransferPage
from pages.NewAccountPage import NewAccountPage
from pages.NewCustomerPage import NewCustomerPage

from faker import Faker


class Test9:

    def test_fund_transfer_successfully(self, open_login_page):

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
            'loucoucoasd213'
        )

        new_customer_page.click_btn_submit_customer()
        customer_id_a = new_customer_page.get_customer_id()

        login_page.click_menu_new_customer()
        new_account_page = NewAccountPage(login_page.driver)
        new_account_page.preencher_new_account_form(customer_id_a, 3000)
        account_id_a = new_account_page.get_account_id()

        new_account_page.click_menu_new_customer()
        new_customer_page = NewCustomerPage(login_page.driver)
        new_customer_page.preencher_formulario_customer(
            fake.name(),
            '10101997',
            'Rua Feliz da teste',
            'Joao Pessoaa',
            'Paraiba',
            '456321',
            '83909128123',
            fake.email(),
            'louc11asd213'
        )

        new_customer_page.click_btn_submit_customer()
        customer_id_b = new_customer_page.get_customer_id()

        login_page.click_menu_new_customer()
        new_account_page = NewAccountPage(login_page.driver)
        new_account_page.preencher_new_account_form(customer_id_b, 2000)
        account_id_b = new_account_page.get_account_id()

        fund_transfer_page = FundTransferPage(login_page.driver)
        fund_transfer_page.preacher_fund_transfer(account_id_a, account_id_b, 50000, "transferindo 50000 reais")

        text_failure = fund_transfer_page.get_text_failure()

        assert "Transfer Failed. Account Balance low!!" in text_failure

        time.sleep(2)
