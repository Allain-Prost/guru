from pages.NewAccountPage import NewAccountPage
from pages.NewCustomerPage import NewCustomerPage

from faker import Faker

from pages.WithdrawalPage import WithdrawalPage


class Test7:

    def test_withdrawal_successfully(self, open_login_page):

        fake = Faker()

        login_page = open_login_page
        login_page.login_com_sucesso('mngr512504', 'qUqAdYs')
        login_page.click_menu_new_customer()

        new_customer_page = NewCustomerPage(login_page.driver)
        new_customer_page.preencher_formulario_customer(
            fake.name(),
            '10101998',
            'Rua Feliz da vida',
            'Joao Pessoa',
            'Paraiba',
            '456321',
            '83909138123',
            fake.email(),
            'lasdad1031'
        )

        new_customer_page.click_btn_submit_customer()
        customer_id = new_customer_page.get_customer_id()

        new_account_page = NewAccountPage(login_page.driver)
        new_account_page.preencher_new_account_form(customer_id, 1000)
        account_id = new_account_page.get_account_id()

        withdrawal_page = WithdrawalPage(login_page.driver)
        withdrawal_page.preacher_amount_withdrawal_form(account_id, 10000, 'sacando 10000 reais')

        text_failure = withdrawal_page.get_text_failure()

        assert "Transaction Failed. Account Balance Low!!!" in text_failure
