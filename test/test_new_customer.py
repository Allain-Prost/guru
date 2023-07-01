from pages.NewCustomerPage import NewCustomerPage


class Test:

    def test_new_customer(self, open_login_page):
        login_page = open_login_page
        login_page.login_com_sucesso('mngr512504', 'qUqAdYs')
        login_page.click_menu_new_customer()

        new_customer_page = NewCustomerPage(login_page.driver)
        new_customer_page.preencher_formulario_customer(
            'CarlosTest',
            '10101997',
            'Rua Feliz da vida',
            'Joao Pessoa',
            'Paraiba',
            '456321',
            '839912312313',
            'cgggds1231110@gmail.com',
            'Ohomemdeferro12'
        )

        new_customer_page.click_btn_submit_customer()

        assert new_customer_page.get_text_sucess(), 'Mensagem de sucesso não encontrado'
        assert new_customer_page.get_customer_id(), 'Customer ID não foi criado com sucesso'
