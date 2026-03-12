import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()


class InputTesting(TestCase):

    BLOG_URL = "https://login.pwr.edu.pl/auth/realms/pwr.edu.pl/protocol/cas/login?service=https%3A%2F%2Fweb.usos.pwr.edu.pl%2Fkontroler.php%3F_action%3Dlogowaniecas%2Findex%26callback%3DK7YyNrVS0s%252FOzyspys9JLdIryCiwj09MLsnMz7PNSy0v1k9JTUsszSlRsgYA801cd74c64dd0c182745239265a2c1f773d396e1&locale=pl"
    INPUT_NAME = "username"
    CLEAR_BUTTON_ID = "clearForm"

    def test_input_and_clear(self):

        self.driver.get(self.BLOG_URL)

        try:
            login_box = self.driver.find_element(By.NAME, self.INPUT_NAME)
        except Exception:
            self.fail("Login input not found!")

        login_box.send_keys("test_user")

        value = login_box.get_attribute("value")

        self.assertEqual("test_user", value)

        button = self.driver.find_element(By.ID, self.CLEAR_BUTTON_ID)
        button.click()

        value_after = login_box.get_attribute("value")

        self.assertEqual("", value_after)


if __name__ == "__main__":
    unittest.main()