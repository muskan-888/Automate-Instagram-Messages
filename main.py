from selenium import webdriver
import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

# you can take any valid username 
audience = [ 'elonofficiall'] 
message = "You are doing a great job"

#main class

class bot:
    def __init__(self,username,password,audience,message):
        self.username=username
        self.password=password
        self.audience=audience
        self.message=message
         
        #initialise base_url
        self.base_url= 'https://www.instagram.com/'
        
        #opening google chrome
        self.bot=driver
        
        #initailse the login function
        self.login()
    
    def login(self):
        self.bot.get(self.base_url) 
  
        enter_username = WebDriverWait(self.bot, 20).until( 
            expected_conditions.presence_of_element_located((By.NAME, 'username'))) 
        enter_username.send_keys(self.username) 
        enter_password = WebDriverWait(self.bot, 20).until( 
            expected_conditions.presence_of_element_located((By.NAME, 'password'))) 
        enter_password.send_keys(self.password) 
        enter_password.send_keys(Keys.RETURN) 
        time.sleep(5) 
  
        # first pop-up 
        self.bot.find_element_by_xpath( 
            '//html/body/div[4]/div/div/div/div[3]/button[2]').click() 
        
        time.sleep(3) 
  
        # 2nd pop-up 
        #self.bot.find_element_by_xpath( 
        #   '/html/body/div[4]/div/div/div/div[3]/button[2]').click() 
        #time.sleep(4) 
  
        # direct button 
        self.bot.find_element_by_xpath( 
            '//a[@class="xWeGp"]/*[name()="svg"][@aria-label="Direct"]').click() 
        
        time.sleep(3) 
  
        # clicks on pencil icon 
        self.bot.find_element_by_xpath( 
            '//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div/div[3]/div/button').click() 
        time.sleep(2) 
        for i in audience: 
  
            # enter the username 
            self.bot.find_element_by_xpath( 
                '/html/body/div[4]/div/div/div[2]/div[1]/div/div[2]/input').send_keys(i) 
            time.sleep(2) 
  
            # click on the username 
            self.bot.find_element_by_xpath( 
                '/html/body/div[4]/div/div/div[2]/div[2]/div').click() 
            time.sleep(2) 
  
            # next button 
            self.bot.find_element_by_xpath( 
                '/html/body/div[4]/div/div/div[1]/div/div[2]/div/button').click() 
            time.sleep(2) 
  
            # click on message area 
            send = self.bot.find_element_by_xpath( 
                '/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea') 
  
            # types message
            self.message="You are doing a great job"
            send.send_keys(self.message) 
            time.sleep(1) 
  
            # send message 
            send.send_keys(Keys.RETURN) 
            time.sleep(2) 
  
            # clicks on direct option or pencl icon 
            self.bot.find_element_by_xpath( 
                '/html/body/div[1]/section/div/div[2]/div/div/div[1]/div[1]/div/div[3]/button').click() 
            time.sleep(2) 
  
def init(): 
    bot('muskan_sh888', 'muskan@8', audience, message) 
  
    # when our program ends it will show "done". 
    input("DONE") 
  
  
# calling the function 
if __name__== '__main__':
    init() 


         