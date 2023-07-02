from faker import Faker

from pages.EditCustomerPage import EditCustomerPage
from pages.NewCustomerPage import NewCustomerPage


class Test3:

    def test_delete_customer(self, open_login_page):

        fake = Faker()

        login_page = open_login_page
        login_page.login_com_sucesso('mngr512504', 'qUqAdYs')
        login_page.click_menu_new_customer()

        new_customer_page = NewCustomerPage(login_page.driver)
        new_customer_page.preencher_formulario_customer(
            fake.name(),
            '20111999',
            'Rua Me Edit Por Favor',
            'Sao Paulo',
            'Sao Paulo',
            '290505',
            '8390912313',
            fake.email(),
            'Ohomemdeferro15'
        )

        new_customer_page.click_btn_submit_customer()
        customer_id = new_customer_page.get_customer_id()

        print(customer_id)

        edit_customer_page = EditCustomerPage(login_page.driver)
        edit_customer_page.click_menu_edit_customer()
        edit_customer_page.edit_customer_id(customer_id)
        edit_customer_page.edit_address_customer_id('Novo endereço')

        alert = edit_customer_page.driver.switch_to.alert
        alert_text = alert.text
        alert.dismiss()

        assert "Customer editado com sucesso!" in alert_text
