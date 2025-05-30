import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class TestWebPage(unittest.TestCase):
    def setUp(self):
        """
        Inicjalizacja testu - uruchomienie przeglądarki Chrome
        """
        self.service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=self.service)

    def test_page_heading(self):
        """
        Test sprawdzający obecność (assertIsNotNone) i zawartość (assertEqual) nagłówka na stronie
        """
        # Given
        self.driver.get('https://tgadek.bitbucket.io/app/portfolio/prod/index.html')

        # When
        heading = self.driver.find_element(By.TAG_NAME, 'h2')

        # Then
        self.assertIsNotNone(heading)
        self.assertEqual(heading.text, "Profesjonalne Rozwiązania IT dla Twojej Firmy")

    def test_title(self):
        """
        Test sprawdzający obecność (assertIsNotNone) i zawartość (assertEqual) tytułu strony
        """
        # Given
        self.driver.get('https://tgadek.bitbucket.io/app/portfolio/prod/portfolio.html')

        # When
        heading = self.driver.find_element(By.TAG_NAME, 'h1')

        # Then
        self.assertIsNotNone(heading)
        self.assertEqual(heading.text, "IT Design")

    def test_footer(self):
        """
        Test sprawdzający obecność (assertIsNotNone) i zawartość (assertEqual) stopki na stronie
        """
        # Given
        self.driver.get('https://tgadek.bitbucket.io/app/portfolio/prod/experience.html')

        # When
        footer = self.driver.find_element(By.CSS_SELECTOR, 'footer > p')

        # Then
        self.assertIsNotNone(footer)
        self.assertEqual(footer.text, "© 2024 IT Design. Wszystkie prawa zastrzeżone.")

    def test_photo(self):
        """
        Test sprawdzający obecność (assertIsNotNone) i atrybut src zdjęcia na stronie
        """
        # Given
        self.driver.get('https://tgadek.bitbucket.io/app/portfolio/prod/team.html')

        # When
        photo = self.driver.find_element(By.CSS_SELECTOR, 'img[alt="Grafik IT Design"]')

        # Then
        self.assertIsNotNone(photo)
        self.assertEqual(photo.get_attribute('src'), 'https://tgadek.bitbucket.io/app/portfolio/prod/img/graphic-designer.jpg')

    def test_font_size(self):
        """
        Test sprawdzający obecność (assertIsNotNone) i wartość atrybutu font-size na stronie
        """
        # Given
        self.driver.get('https://tgadek.bitbucket.io/app/portfolio/prod/experience.html')

        # When
        element = self.driver.find_element(By.CSS_SELECTOR, 'div.experience > p')

        # Then
        self.assertIsNotNone(element)
        font_size = element.value_of_css_property('font-size')
        self.assertEqual(font_size, '18px')

    def tearDown(self):
        """
        Zakończenie testu - zamknięcie przeglądarki
        """
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
