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

class TestCoursesearch():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_bV001(self):
    self.driver.get("https://e-learning.hcmut.edu.vn/")
    self.driver.set_window_size(536, 866)
    self.driver.find_element(By.LINK_TEXT, "Log in").click()
    self.driver.find_element(By.LINK_TEXT, "Teachers and Students of HCMUT").click()
    self.driver.find_element(By.ID, "username").send_keys("trung.bui2405")
    self.driver.find_element(By.ID, "password").send_keys("abcxyz")
    self.driver.find_element(By.NAME, "submit").click()
    self.driver.find_element(By.CSS_SELECTOR, ".nav-item:nth-child(5) > .nav-link").click()
    self.driver.find_element(By.CSS_SELECTOR, ".btn-primary > .icon").click()
  
  def test_bV002(self):
    self.driver.get("https://e-learning.hcmut.edu.vn/")
    self.driver.set_window_size(1722, 1034)
    element = self.driver.find_element(By.LINK_TEXT, "Log in")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.LINK_TEXT, "Log in").click()
    self.driver.find_element(By.LINK_TEXT, "Teachers and Students of HCMUT").click()
    self.driver.find_element(By.ID, "username").send_keys("trung.bui2405")
    self.driver.find_element(By.ID, "password").send_keys("abcxyz")
    self.driver.find_element(By.ID, "username").click()
    self.driver.find_element(By.CSS_SELECTOR, ".row:nth-child(3)").click()
    self.driver.find_element(By.ID, "password").click()
    self.driver.find_element(By.ID, "cas").click()
    self.driver.find_element(By.NAME, "submit").click()
    self.driver.find_element(By.CSS_SELECTOR, ".nav-item:nth-child(5) > .nav-link").click()
    self.driver.find_element(By.ID, "searchinput-639d7f0729054639d7f07257163").click()
    self.driver.find_element(By.ID, "searchinput-639d7f0729054639d7f07257163").send_keys("P")
    self.driver.find_element(By.CSS_SELECTOR, ".search-icon").click()
  
  def test_bV003(self):
    self.driver.get("https://e-learning.hcmut.edu.vn/")
    self.driver.set_window_size(1722, 1034)
    self.driver.find_element(By.LINK_TEXT, "Log in").click()
    self.driver.find_element(By.LINK_TEXT, "Teachers and Students of HCMUT").click()
    self.driver.find_element(By.ID, "username").send_keys("trung.bui2405")
    self.driver.find_element(By.ID, "password").send_keys("abcxyz")
    self.driver.find_element(By.ID, "username").click()
    self.driver.find_element(By.CSS_SELECTOR, ".row:nth-child(2) > .fl-label").click()
    self.driver.find_element(By.ID, "password").click()
    self.driver.find_element(By.CSS_SELECTOR, ".btn-row").click()
    self.driver.find_element(By.NAME, "submit").click()
    self.driver.find_element(By.CSS_SELECTOR, ".nav-item:nth-child(5) > .nav-link").click()
    self.driver.find_element(By.ID, "searchinput-639d7f6a36c31639d7f6a336f03").click()
    self.driver.find_element(By.ID, "searchinput-639d7f6a36c31639d7f6a336f03").send_keys("PR")
    self.driver.find_element(By.CSS_SELECTOR, ".btn-primary > .icon").click()
  
  def test_bV004(self):
    self.driver.get("https://e-learning.hcmut.edu.vn/")
    self.driver.set_window_size(1722, 1034)
    self.driver.find_element(By.LINK_TEXT, "Log in").click()
    self.driver.find_element(By.LINK_TEXT, "Teachers and Students of HCMUT").click()
    self.driver.find_element(By.ID, "username").send_keys("trung.bui2405")
    self.driver.find_element(By.ID, "password").send_keys("abcxyz")
    self.driver.find_element(By.ID, "username").click()
    self.driver.find_element(By.CSS_SELECTOR, ".row:nth-child(3) > .fl-label").click()
    self.driver.find_element(By.ID, "password").click()
    self.driver.find_element(By.NAME, "submit").click()
    self.driver.find_element(By.CSS_SELECTOR, ".nav-item:nth-child(5) > .nav-link").click()
    self.driver.find_element(By.ID, "searchinput-639d81ace43e9639d81ace08223").click()
    self.driver.find_element(By.ID, "searchinput-639d81ace43e9639d81ace08223").send_keys("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")
    self.driver.find_element(By.CSS_SELECTOR, ".btn-primary > .icon").click()
  
  def test_bV005(self):
    self.driver.get("https://e-learning.hcmut.edu.vn/")
    self.driver.set_window_size(1722, 1034)
    self.driver.find_element(By.LINK_TEXT, "Log in").click()
    self.driver.find_element(By.LINK_TEXT, "Teachers and Students of HCMUT").click()
    self.driver.find_element(By.ID, "username").send_keys("trung.bui2405")
    self.driver.find_element(By.ID, "password").send_keys("abcxyz")
    self.driver.find_element(By.ID, "username").click()
    self.driver.find_element(By.CSS_SELECTOR, ".row:nth-child(3) > .fl-label").click()
    self.driver.find_element(By.ID, "password").click()
    self.driver.find_element(By.NAME, "submit").click()
    self.driver.find_element(By.CSS_SELECTOR, ".nav-item:nth-child(5) > .nav-link").click()
    self.driver.find_element(By.ID, "searchinput-639d824d3f5d9639d824d3be523").click()
    self.driver.find_element(By.ID, "searchinput-639d824d3f5d9639d824d3be523").send_keys("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")
    self.driver.find_element(By.CSS_SELECTOR, ".btn-primary > .icon").click()
  
  def test_bV006(self):
    self.driver.get("https://e-learning.hcmut.edu.vn/")
    self.driver.set_window_size(1722, 1034)
    self.driver.find_element(By.LINK_TEXT, "Log in").click()
    self.driver.find_element(By.LINK_TEXT, "Teachers and Students of HCMUT").click()
    self.driver.find_element(By.ID, "username").send_keys("trung.bui2405")
    self.driver.find_element(By.ID, "password").send_keys("abcxyz")
    self.driver.find_element(By.ID, "username").click()
    self.driver.find_element(By.ID, "password").click()
    self.driver.find_element(By.NAME, "submit").click()
    self.driver.find_element(By.CSS_SELECTOR, ".nav-item:nth-child(5) > .nav-link").click()
    self.driver.find_element(By.ID, "searchinput-639d82d3eceed639d82d3e98273").click()
    self.driver.find_element(By.ID, "searchinput-639d82d3eceed639d82d3e98273").send_keys("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")
    self.driver.find_element(By.CSS_SELECTOR, ".search-icon").click()
  
  def test_bV007(self):
    self.driver.get("https://e-learning.hcmut.edu.vn/")
    self.driver.set_window_size(1460, 866)
    self.driver.find_element(By.LINK_TEXT, "Log in").click()
    self.driver.find_element(By.LINK_TEXT, "Teachers and Students of HCMUT").click()
    self.driver.find_element(By.ID, "username").send_keys("trung.bui2405")
    self.driver.find_element(By.ID, "password").send_keys("quachcncu2001")
    self.driver.find_element(By.ID, "username").click()
    self.driver.find_element(By.ID, "password").click()
    self.driver.find_element(By.NAME, "submit").click()
    self.driver.find_element(By.ID, "username").send_keys("trung.bui2405")
    self.driver.find_element(By.ID, "password").send_keys("abcxyz")
    self.driver.find_element(By.NAME, "submit").click()
    self.driver.find_element(By.CSS_SELECTOR, ".nav-item:nth-child(5) > .nav-link").click()
    self.driver.find_element(By.ID, "searchinput-639d83aa7ce72639d83aa79b623").click()
    self.driver.find_element(By.ID, "searchinput-639d83aa7ce72639d83aa79b623").send_keys("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")
    self.driver.find_element(By.CSS_SELECTOR, ".search-icon").click()
  
  def test_eCP001(self):
    self.driver.get("https://e-learning.hcmut.edu.vn/")
    self.driver.set_window_size(536, 866)
    self.driver.find_element(By.LINK_TEXT, "Log in").click()
    self.driver.find_element(By.LINK_TEXT, "Teachers and Students of HCMUT").click()
    self.driver.find_element(By.ID, "username").send_keys("trung.bui2405")
    self.driver.find_element(By.ID, "password").send_keys("abcxyz")
    self.driver.find_element(By.NAME, "submit").click()
    self.driver.find_element(By.CSS_SELECTOR, ".nav-item:nth-child(5) > .nav-link").click()
    self.driver.find_element(By.CSS_SELECTOR, ".btn-primary > .icon").click()
  
  def test_eCP002(self):
    self.driver.get("https://e-learning.hcmut.edu.vn/")
    self.driver.set_window_size(1722, 1034)
    element = self.driver.find_element(By.LINK_TEXT, "Log in")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.LINK_TEXT, "Log in").click()
    self.driver.find_element(By.LINK_TEXT, "Teachers and Students of HCMUT").click()
    self.driver.find_element(By.ID, "username").send_keys("trung.bui2405")
    self.driver.find_element(By.ID, "password").send_keys("abcxyz")
    self.driver.find_element(By.NAME, "submit").click()
    self.driver.find_element(By.CSS_SELECTOR, ".nav-item:nth-child(5) > .nav-link").click()
    self.driver.find_element(By.ID, "searchinput-639d850ed049a639d850eccd653").click()
    self.driver.find_element(By.ID, "searchinput-639d850ed049a639d850eccd653").send_keys("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")
    self.driver.find_element(By.CSS_SELECTOR, ".btn-primary > .icon").click()
  
  def test_eCP003(self):
    self.driver.get("https://e-learning.hcmut.edu.vn/")
    self.driver.set_window_size(1460, 866)
    self.driver.find_element(By.LINK_TEXT, "Log in").click()
    self.driver.find_element(By.LINK_TEXT, "Teachers and Students of HCMUT").click()
    self.driver.find_element(By.ID, "username").send_keys("trung.bui2405")
    self.driver.find_element(By.ID, "password").send_keys("abcxyz")
    self.driver.find_element(By.ID, "username").click()
    self.driver.find_element(By.ID, "password").click()
    self.driver.find_element(By.NAME, "submit").click()
    self.driver.find_element(By.ID, "username").send_keys("trung.bui2405")
    self.driver.find_element(By.ID, "password").send_keys("quachcncu2001")
    self.driver.find_element(By.NAME, "submit").click()
    self.driver.find_element(By.CSS_SELECTOR, ".nav-item:nth-child(5) > .nav-link").click()
    self.driver.find_element(By.ID, "searchinput-639d83aa7ce72639d83aa79b623").click()
    self.driver.find_element(By.ID, "searchinput-639d83aa7ce72639d83aa79b623").send_keys("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")
    self.driver.find_element(By.CSS_SELECTOR, ".search-icon").click()
  
  def test_dT001(self):
    self.driver.get("https://e-learning.hcmut.edu.vn/")
    self.driver.set_window_size(536, 866)
    self.driver.find_element(By.LINK_TEXT, "Log in").click()
    self.driver.find_element(By.LINK_TEXT, "Teachers and Students of HCMUT").click()
    self.driver.find_element(By.ID, "username").send_keys("trung.bui2405")
    self.driver.find_element(By.ID, "password").send_keys("abcxyz")
    self.driver.find_element(By.NAME, "submit").click()
    self.driver.find_element(By.CSS_SELECTOR, ".nav-item:nth-child(5) > .nav-link").click()
    self.driver.find_element(By.CSS_SELECTOR, ".btn-primary > .icon").click()
  
  def test_dT002(self):
    self.driver.get("https://e-learning.hcmut.edu.vn/")
    self.driver.set_window_size(1722, 1034)
    self.driver.find_element(By.LINK_TEXT, "Log in").click()
    self.driver.find_element(By.LINK_TEXT, "Teachers and Students of HCMUT").click()
    self.driver.find_element(By.ID, "username").send_keys("trung.bui2405")
    self.driver.find_element(By.ID, "password").send_keys("abcxyz")
    self.driver.find_element(By.ID, "username").click()
    self.driver.find_element(By.CSS_SELECTOR, ".row:nth-child(3) > .fl-label").click()
    self.driver.find_element(By.ID, "password").click()
    self.driver.find_element(By.NAME, "submit").click()
    self.driver.find_element(By.CSS_SELECTOR, ".nav-item:nth-child(5) > .nav-link").click()
    self.driver.find_element(By.ID, "searchinput-639d81ace43e9639d81ace08223").click()
    self.driver.find_element(By.ID, "searchinput-639d81ace43e9639d81ace08223").send_keys("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")
    self.driver.find_element(By.CSS_SELECTOR, ".btn-primary > .icon").click()
  