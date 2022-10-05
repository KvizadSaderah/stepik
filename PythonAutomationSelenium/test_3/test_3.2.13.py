from selenium import webdriver
import unittest


class TestAbs(unittest.TestCase):

    def test_link_1(self):

        browser = webdriver.Chrome()
        browser.implicitly_wait(10)
        browser.get("http://suninjuly.github.io/registration1.html")

        # Ваш код, который заполняет обязательные поля

        input1 = browser.find_element_by_xpath("//div[1]/form/div[1]/div[1]/input")
        input1_message = input1.get_attribute("placeholder")
        print(input1_message)
        if input1_message == "Input your first name":
            input1.send_keys("Ivan")

        input1 = browser.find_element_by_xpath("//div[1]/form/div[1]/div[2]/input")
        input2_message = input1.get_attribute("placeholder")
        print(input1_message)
        if input2_message == "Input your last name":
            input1.send_keys("Petrov")

        input1 = browser.find_element_by_xpath("//div[1]/form/div[1]/div[3]/input")
        input3_message = input1.get_attribute("placeholder")
        if input3_message == "Input your email":
            input1.send_keys("Ivan@petrov.rq")

        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        print(welcome_text_elt)
        print(welcome_text_elt.text)
        print(welcome_text)
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "Text is not equal")

    def test_link_2(self):
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/registration2.html")

        # Ваш код, который заполняет обязательные поля

        input1 = browser.find_element_by_xpath("//div[1]/form/div[1]/div[1]/input")
        input1_message = input1.get_attribute("placeholder")
        print(input1_message)
        if input1_message == "Input your first name":
            input1.send_keys("Ivan")

        input1 = browser.find_element_by_xpath("//div[1]/form/div[1]/div[2]/input")
        input2_message = input1.get_attribute("placeholder")
        print(input1_message)
        if input2_message == "Input your last name":
            input1.send_keys("Petrov")

        input1 = browser.find_element_by_xpath("//div[1]/form/div[1]/div[3]/input")
        input3_message = input1.get_attribute("placeholder")
        if input3_message == "Input your email":
            input1.send_keys("Ivan@petrov.rq")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "Text is not equal")


if __name__ == "__main__":
    unittest.main()
