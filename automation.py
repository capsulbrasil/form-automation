import time
import threading
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from function.stopWatch import stopWatch

def automation(df):
    """
    Perform automation using Selenium to process a DataFrame.
    
    Args:
    df (pd.DataFrame): DataFrame containing the data to be processed.
    
    This function iterates over the rows of the DataFrame, extracting the email and message
    fields and inputs them into a web form. After submitting the form, it clears the input
    fields before processing the next row.
    """
    service = Service(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service)
    driver.get('https://renopele.fun/api/')
    
    email_xpath = '//*[@id="form-field-email"]'
    message_xpath = '//*[@id="form-field-message"]'
    submit_xpath = "//button[@class='elementor-button elementor-size-sm']/span/span[@class='elementor-button-text' and text()='Send']"

    for index, row in df.iterrows():
        email = str(row.iloc[0])
        numero = row.iloc[1]
        
        driver.find_element(By.XPATH, email_xpath).send_keys(email)
        driver.find_element(By.XPATH, message_xpath).send_keys(numero)
        
        time.sleep(1)
        
        driver.find_element(By.XPATH, submit_xpath).click()
        
        time.sleep(1)
        
        driver.find_element(By.XPATH, email_xpath).clear()
        driver.find_element(By.XPATH, message_xpath).clear()
        
        time.sleep(1)
    
    driver.quit()

def start_thread():
    """
    Starts a series of threads to process the automation.
    
    This function reads multiple files into DataFrames and creates a thread
    for each DataFrame to process them concurrently using the automation function.
    """
    thread_stopwatch = threading.Thread(target=stopWatch)
    thread_stopwatch.daemon = True
    thread_stopwatch.start()

    file_paths = [
        'data/LISTA01CSHB.xlsx',
        'data/LISTA02CSHB.xlsx',
        'data/LISTA03CSHB.xlsx',
        'data/LISTA04CSHB.xlsx',
        'data/LISTA05CSHB.xlsx'
    ]
    
    dataframes = [pd.read_excel(path) for path in file_paths]
    
    threads = [threading.Thread(target=automation, args=(df,)) for df in dataframes]
    
    for thread in threads:
        thread.start()
    
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    start_thread()
