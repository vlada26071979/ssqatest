import pytest
from ssqatest.src.helpers.assertions import Ensure
from ssqatest.src.pages.HomePage import HomePage
from ssqatest.src.pages.ProductPage import ProductPage


@pytest.mark.usefixtures("init_driver")
class TestHomePage:

    @pytest.fixture(scope="class")
    def setup(self, request):
        request.cls.product_page = ProductPage(request.cls.driver)
        request.cls.home_page = HomePage(request.cls.driver)
        request.cls.home_page.go_to_home_page()

    @pytest.mark.smoke
    @pytest.mark.tcid01
    def test_verify_number_of_products_displayed(self, setup):
        expected_products_number = 16

        actual_products = self.home_page.get_all_product_elements()
        Ensure.is_equal(len(actual_products), expected_products_number, f"Unexpected number of products displayed, "
                                                                        f"Expected '{expected_products_number}' "
                                                                        f"but got '{len(actual_products)}")

    @pytest.mark.smoke
    @pytest.mark.tcid67
    def test_verify_heading_is_displayed(self, setup):
        expected_heading_text = "Shop"
        actual_heading_text = self.home_page.get_displayed_heading()

        Ensure.is_equal(actual_heading_text, expected_heading_text,
                        f"Wrong header displayed?! - Expected: {expected_heading_text} but got {actual_heading_text}")

    @pytest.mark.smoke
    @pytest.mark.tcid68
    def test_verify_header_menu_is_displayed(self, setup):
        expected_headers = ["Home", "Cart", "Checkout", "My account", "Sample Page"]
        actual_headers = self.home_page.get_displayed_headers()

        Ensure.is_equal(sorted(expected_headers), sorted(actual_headers))

    @pytest.mark.tcid203
    def test_verify_clicking_a_product_opens_the_product_details_page(self, setup):
        expected_product_title = "Beanie"

        self.home_page.click_beanie()
        actual_product_title = self.product_page.get_displayed_product_name()
        Ensure.is_equal(actual_product_title, expected_product_title)

    @pytest.mark.tcid204
    def test_verify_each_product_name_is_displayed(self, setup):
        expected_displayed_names = ["Album", "Beanie", "Beanie with Logo", "Belt", "Cap", "Hoodie", "Hoodie with Logo",
                                    "Hoodie with Zipper", "Logo Collection", "Long Sleeve Tee", "Polo", "Single",
                                    "Sunglasses", "T-Shirt", "T-Shirt with Logo", "V-Neck T-Shirt"]

        product_name_elements = self.home_page.get_all_product_name_elements()
        actual_displayed_names = [product.text for product in product_name_elements]

        Ensure.is_equal(actual_displayed_names, expected_displayed_names)

    @pytest.mark.tcid300
    def test_mouse_click(self,setup):
        self.home_page.click_beanie()
        breakpoint()



