# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestTestregistrashen():
  def setup_method(self, method):
    self.driver = webdriver.Firefox()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_testregistrashen(self):
    self.driver.get("https://petfriends.skillfactory.ru/")
    self.driver.set_window_size(1550, 878)
    self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
    self.driver.find_element(By.ID, "name").click()
    self.driver.find_element(By.ID, "name").send_keys("kola567")
    self.driver.find_element(By.ID, "email").click()
    self.driver.find_element(By.ID, "email").send_keys("kola@yandex.ru")
    self.driver.find_element(By.ID, "pass").click()
    self.driver.find_element(By.ID, "pass").send_keys("12345")
    self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
    self.driver.close()
  
