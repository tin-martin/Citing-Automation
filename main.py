from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import sys
import time
from tqdm import tqdm
from selenium.common.exceptions import NoSuchElementException
driver = webdriver.Chrome()
options = Options()
options.headless = True



DRIVER_PATH = '/Users/martintin/Downloads/chromedriver 3'
driver = webdriver.Chrome()

links = []

while(True):
    link = input("")
    if (link == "start"):
        print("...starting")
        break
    links.append(link)

def check_for_create_an_acc():
    try:
        driver.find_element(By.XPATH,"/html/body/div[1]/div/div[10]/div[2]/div/div/div[1]/h2")
       # print("THERE IS A CReATE AN ACC DAMIIT")
        exit_button = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[10]/div[2]/button")
        exit_button.click()
    except NoSuchElementException:
        pass



for i in range(len(links)):
    driver.get('https://www.scribbr.com/apa-citation-generator/new/webpage/')
    link = links[i]
    check_for_create_an_acc()
#enters the site 
    element = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[9]/div[2]/div[1]/span/form/div/div[3]/div/div[1]/div/div/div/div/div/input')
    element.send_keys(link)
    element.send_keys(Keys.RETURN)

    try:
        driver.find_element(By.XPATH,"/html/body/div[1]/div/div[9]/div[2]/div[1]/span/form/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[2]")
        print("CANNOT SITE THIS RESOURCE: ",link)
        continue
    except NoSuchElementException:
        check_for_create_an_acc()
    
    check_for_create_an_acc()

    while(True):
        check_for_create_an_acc()
        try:
            button1 = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[9]/div[2]/div[1]/span/form/div/div[3]/div/div[1]/div/div/div/div/ol/li/div')
            button1.click()
            break
        except:
            pass
        
        check_for_create_an_acc()
    # Scroll
#click cite source
    while(True):
       
        try:
            button3 = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[9]/div[2]/div[1]/span/form/div/div[4]/div/button/div')
            button3.click()
            break
        except:
            check_for_create_an_acc()
            height = driver.execute_script("return document.documentElement.scrollHeight")
            driver.execute_script("window.scrollTo(0, {})".format(height+1)) 
    check_for_create_an_acc()
    
    try:
        driver.find_element(By.XPATH,"/html/body/div[1]/div/div[9]/div[2]/div[1]/span/form/div/div[3]")
        print("CANNOT SITE THIS RESOURCE: ",link)
        continue
    except NoSuchElementException:
        check_for_create_an_acc()
    check_for_create_an_acc()



    while(True):
       
        try:
            ##button2 = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[9]/div[2]/div[6]/div[2]/div/div[1]/div')
           ## button2.click()
            citing = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[9]/div[2]/div[6]/div[2]/div/div[1]/div').text
            print(citing)
            break
        except:
            check_for_create_an_acc()

    
 
    driver.execute_script('localStorage.clear();')
 
    
 
