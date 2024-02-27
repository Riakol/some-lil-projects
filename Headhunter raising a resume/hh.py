import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class HH:
    def __init__(self) -> None:
        self.resume = '/html/body/div[4]/div/div[2]/div[1]/div/div/div/div[1]/a'
        self.prolongation = '/html/body/div[5]/div/div[3]/div[1]/div/div/div[1]/div[5]/div/div/div[6]/div/div[1]/button'
        self.extension_line = '/html/body/div[5]/div/div[3]/div[1]/div/div/div[1]/div[5]/div/div/div[2]/div'
        self.btn_name = '//*[@id="HH-React-Root"]/div/div[3]/div[1]/div/div/div[1]/div[5]/div/div/div[6]/div/div[1]/div/button'

    def edited_time(self, seconds):
        """edits seconds into hours and minutes"""
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        return f'{hours}h:{minutes}m'
    
    def send_btn(self, driver, value):
        """searches for the button by xpath then clicks on it"""
        any_btn = driver.find_element(by=By.XPATH, value=value)
        any_btn.send_keys(Keys.ENTER)
        time.sleep(3)

    def fill_field(self, driver, value, field):
        """searches for a field by xpath then fills it in"""
        any_field = driver.find_element(by=By.XPATH, value=field)
        any_field.send_keys(value)
