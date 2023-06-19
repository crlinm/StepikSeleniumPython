import pytest

from .pages.product_page import ProductPage


@pytest.mark.parametrize('promo', [*range(7),
                                   pytest.param("7", marks=pytest.mark.xfail),
                                   *range(8, 10)])
def test_guest_can_add_product_to_basket(browser, promo):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo}"
    page = ProductPage(browser, link)
    page.open()
    print(browser.current_url)
    page.add_product_to_basket()
