from pages.BalanceEnquiryPage import BalanceEnquiryPage


class Test5:

    def test_balance_enquiry(self, open_login_page):

        login_page = open_login_page
        login_page.login_com_sucesso('mngr512504', 'qUqAdYs')

        balance_enquiry_page = BalanceEnquiryPage(login_page.driver)
        balance_enquiry_page.click_menu_balance_enquiry()
        balance_enquiry_page.click_btn_submit()

        alert_text = balance_enquiry_page.get_text_alert()

        assert "Please fill all fields" in alert_text
