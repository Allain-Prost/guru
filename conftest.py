import pytest

from pages.LoginPage import LoginPage
from pages.NewCustomerPage import NewCustomerPage


def pytest_addoption(parser):
    parser.addoption("--browser", default='chrome', help='Browser to run the tests.')


@pytest.fixture()
def open_login_page_all_browser(all_browser):
    login_page = LoginPage(browser=all_browser)
    yield login_page


@pytest.fixture()
def open_login_page(request):
    select_browser = request.config.getoption("--browser").lower()
    login_page = LoginPage(browser=select_browser)
    yield login_page


