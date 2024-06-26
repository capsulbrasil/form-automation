# function imports
from function import stopwatch

# lib imports
import time
import threading
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

# automation with selenium
def automation(df):
    # Integrating drivers
    service = Service(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service)  # Running on GeckoDriver (Firefox)
    driver.get('https://renopele.fun/api/')  # Web page on which Selenium will operate

    # Automation logic
    for index, row in df.iterrows():
        # Capturing insights
        email = str(row.iloc[0])
        numero = row.iloc[1]
        
        # Form input
        driver.find_element(By.XPATH, '//*[@id="form-field-email"]').send_keys(email)  # Email
        driver.find_element(By.XPATH, '//*[@id="form-field-message"]').send_keys(numero)  # Phone
        
        time.sleep(1)# Dramatic stop for click
        
        # Submit
        xpath = "//button[@class='elementor-button elementor-size-sm']/span/span[@class='elementor-button-text' and text()='Send']"
        button = driver.find_element(By.XPATH, xpath)
        button.click()  # Click
        
        time.sleep(1)# Dramatic stop to clear
        
        # Form cleaning
        driver.find_element(By.XPATH, '//*[@id="form-field-email"]').clear()
        driver.find_element(By.XPATH, '//*[@id="form-field-message"]').clear()
        
        time.sleep(1)# Dramatic pause to input
    driver.quit() # quit drivers

# Starting timer
threadStopwatch = threading.Thread(target=stopwatch)
threadStopwatch.daemon = True
threadStopwatch.start()

# Opening files - CSV or XLSX data
df1 = pd.read_csv('data/form.csv')
df2 = pd.read_csv('data/form.csv')
df3 = pd.read_csv('data/form.csv')
df4 = pd.read_csv('data/form.csv')
df5 = pd.read_csv('data/form.csv')

# Creating kernel for each process
thread1 = threading.Thread(target=automation, args=(df1,))
thread2 = threading.Thread(target=automation, args=(df2,))
thread3 = threading.Thread(target=automation, args=(df3,))
thread4 = threading.Thread(target=automation, args=(df4,))
thread5 = threading.Thread(target=automation, args=(df5,))

# Starting all threads - Ending threads
thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread5.start()
#==============
thread1.join()
thread2.join()
thread3.join()
thread4.join()
thread5.join()

print("Automation completed")
