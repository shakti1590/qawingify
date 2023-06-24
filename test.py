import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPageTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://sakshingp.github.io/assignment/login.html")

    def tearDown(self):
        self.driver.quit()

    def test_login_valid_credentials(self):
        username = "valid_username"
        password = "valid_password"
        username_input = self.driver.find_element(By.ID, "username")
        password_input = self.driver.find_element(By.ID, "password")
        username_input.send_keys(username)
        password_input.send_keys(password)
        login_button = self.driver.find_element(By.XPATH, "/html/body/div/div/form/div[3]/button")
        login_button.click()
        WebDriverWait(self.driver, 10).until(EC.url_contains("home.html"))
        self.assertTrue("home.html" in self.driver.current_url)

class HomePageTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://sakshingp.github.io/assignment/home.html")
    def tearDown(self):
        self.driver.quit()
    def test_sort_transaction_table(self):
        amount_header = self.driver.find_element(By.XPATH, "/html/body/div/div[3]/div[2]/div/div/div[2]/div/div/table/thead/tr/th[5]")
        amount_header.click()
        transaction_amounts = self.driver.find_elements(By.XPATH, "//table[@id='transaction-table']//tr/td[5]")
        sorted_amounts = [float(amount.text.replace('$', ''))for amount in transaction_amounts]
        self.assertEqual(sorted_amounts, sorted(sorted_amounts))

if __name__ == "__main__":
    unittest.main()
