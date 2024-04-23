from lesson4.pages.base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    def header(self):
        return self.is_visible((By.XPATH, '/html/body/h1'))
    
    def start_button(self):
        self.is_visible((By.XPATH, '//*[@id="startTest"]')).click()
        return self
    
    def login_field(self):
        self.is_visible((By.XPATH, '//*[@id="login"]')).send_keys("login")
        return self
    
    def password_field(self):
        self.is_visible((By.XPATH, '//*[@id="password"]')).send_keys("password")
        return self
    
    def checkbox(self):
        self.is_visible((By.XPATH, '//*[@id="agree"]')).click()
        return self
    
    def register_button(self):
        self.is_visible((By.XPATH, '//*[@id="register"]')).click()
        return self
    
    def loader(self):
        return self.is_visible((By.XPATH, '//*[@id="loader"]'))
        
    def success_msg(self):
        return self.is_visible((By.XPATH, '//*[@id="successMessage"]'))
    