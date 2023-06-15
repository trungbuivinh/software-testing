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

class TestTC2():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_tC2(self):
    # Test name: TC2
    # Step # | name | target | value
    # 1 | open | https://e-learning.hcmut.edu.vn/my/courses.php | 
    self.driver.get("https://e-learning.hcmut.edu.vn/my/courses.php")
    # 2 | clickAt | id=yui_3_17_2_1_1671380142966_59 | 
    self.driver.find_element(By.ID, "yui_3_17_2_1_1671380142966_59").click()
    # 3 | clickAt | css=#module-73914 .aalink | 
    self.driver.find_element(By.CSS_SELECTOR, "#module-73914 .aalink").click()
    # 4 | clickAt | linkText=COMPUTER NETWORKS (CO3093)_VIDEO | 
    self.driver.find_element(By.LINK_TEXT, "COMPUTER NETWORKS (CO3093)_VIDEO").click()
  