import time
from selenium import webdriver
import datetime
import os 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InstagramBot : 
    def __init__(self , username , password , amount , hashtag ) : 
        self.username  = username 
        self.password = password 
        self.amount = amount 
        self.hashtag = hashtag  
        self.driver = webdriver.Chrome(('./Desktop/chromedriver'))
        time.sleep(1) 
        self.login()
        time.sleep(3) 
        self.explore_hashtags()
        time.sleep(3) 
        self.like_posts()
    def login(self) : 
        self.driver.get("https://www.instagram.com/accounts/login ")
        time.sleep(3) 

  #      WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[contains(text(),"Log in with Facebook")]')))
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[5]/button').click()
 

        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[contains(text(),"Log In")]')))
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.NAME, "email")))
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.NAME, "pass")))
        self.driver.find_element_by_name('email').send_keys(self.username)
        self.driver.find_element_by_name('pass').send_keys(self.password)
        self.driver.find_element_by_xpath('//*[contains(text(),"Log In")]').click()
        time.sleep(2) 

        self.driver.find_element_by_xpath('//*[@id="u_0_z"]/div[1]/div/div/div[3]/button[1]').click()
    def explore_hashtags(self):
        self.driver.get("https://www.instagram.com/"+self.hashtag)
    def like_posts(self):
        self.driver.find_element_by_class_name('_9AhH0').click()
        i = 1
        while i <= self.amount : 
            time.sleep(2)
            self.driver.find_element_by_class_name('fr66n').click()
            self.driver.find_element_by_class_name('coreSpriteRightPaginationArrow').click()
           
            i += 1 



instagram = InstagramBot("your facebook email", "your password" , "number of likes ", "the person you want to look for ")
 