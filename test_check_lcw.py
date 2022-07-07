import unittest

from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class TestCheckLcw(unittest.TestCase):
    CATEGORY_1 = (By.XPATH, '//a[contains(text(), "DİĞER MARKALAR")]')
    CATEGORY_2 = (By.XPATH, '//img[@alt="Sepette İndirim Markalı Ürünler - Kadın"]')
    CATEGORY_PAGE_CONTROL = (By.TAG_NAME, 'h3')
    PRODUCT_PAGE = (By.CLASS_NAME, 'product-card__product-info')
    PRODUCT_PAGE_CONTROL = (By.CLASS_NAME, 'add-to-cart-container')
    ADD_TO_CART = (By.CLASS_NAME, 'add-to-cart-container')
    CART_PAGE = (By.ID, 'shopping-cart')
    CART_PAGE_CONTROL = (By.TAG_NAME, 'h1')
    CART_COUNT = (By.CSS_SELECTOR, '.badge-circle:last-child')
    RETURN_HOMEPAGE = (By.CSS_SELECTOR, '.header__middle__left .main-header-logo')

    base_url = 'https://www.lcwaikiki.com/tr-TR/TR'
    control_message = 'Seçili Ürünlerde Sepette İndirim Kozmetik'
    cart_count_control = '1'
    cart_page_control_message = 'SİPARİŞ ÖZETİ'

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.get(self.base_url)
        self.driver.implicitly_wait(10)

    def test_check_lcw(self):
        self.base_url == self.driver.current_url
        self.driver.find_element(*self.CATEGORY_1).click()
        self.driver.find_element(*self.CATEGORY_2).click()
        self.assertEqual(self.control_message, self.driver.find_element(*self.CATEGORY_PAGE_CONTROL).text)
        self.driver.find_elements(*self.PRODUCT_PAGE)[1].click()
        self.assertTrue(self.driver.find_element(*self.PRODUCT_PAGE_CONTROL))
        self.driver.find_element(*self.ADD_TO_CART).click()
        self.assertIn(self.cart_count_control, self.driver.find_element(*self.CART_COUNT).text)
        self.driver.find_element(*self.CART_PAGE).click()
        self.assertEqual(self.cart_page_control_message, self.driver.find_element(*self.CART_PAGE_CONTROL).text)
        self.driver.find_element(*self.RETURN_HOMEPAGE).click()
        self.assertTrue(self.driver.find_element(*self.RETURN_HOMEPAGE))

    def tearDown(self):
        self.driver.quit()
