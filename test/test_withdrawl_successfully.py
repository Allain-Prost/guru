from pages.NewAccountPage import NewAccountPage
from pages.NewCustomerPage import NewCustomerPage

from faker import Faker

from pages.WithdrawalPage import WithdrawalPage


class Test6:

    def test_withdrawal_successfully(self, open_login_page):

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
        customer_id = new_customer_page.get_customer_id()

        new_account_page = NewAccountPage(login_page.driver)
        new_account_page.preencher_new_account_form(customer_id, 100000)
        account_id = new_account_page.get_account_id()

        withdrawal_page = WithdrawalPage(login_page.driver)
        withdrawal_page.preacher_amount_withdrawal_form(account_id, 100, 'sacando 100 reais')

        text_success = withdrawal_page.get_text_success()

        assert "Transaction details of Withdrawal for Account " + account_id in text_success
