# Web Form Filling Automation with Selenium and Pandas

This document describes a Python script that automates the filling of a web form using data from an Excel file. The automation is performed using the Selenium and Pandas libraries.

## Requirements

- Python 3.x
- Python Libraries:
  - `time`: Standard Python library for timing operations.
  - `pandas`: Library for data manipulation. Installation: `pip install pandas`.
  - `selenium`: Library for web browser automation. Installation: `pip install selenium`.
  - `webdriver_manager`: Library to manage browser drivers. Installation: `pip install webdriver-manager`.

## Script Description

The script starts by importing the necessary libraries:

```python
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
It then initializes the Firefox browser driver using GeckoDriver:

service = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)
driver.get('https://renopele.fun/api/')
The script reads data from an Excel file (data/test.xlsx) into a Pandas DataFrame:

df = pd.read_excel('data/test.xlsx')
print(df)  # Display the DataFrame
Next, the script iterates over each row in the DataFrame, filling and submitting the form with the extracted data:

for index, row in df.iterrows():
    numero = str(row.iloc[0])  # Extracts the first value of the row and converts to string
    email = row.iloc[1]  # Extracts the second value of the row

    # Fill in the form fields
    driver.find_element(By.XPATH, '//*[@id="form-field-email"]').send_keys(email)
    driver.find_element(By.XPATH, '//*[@id="form-field-message"]').send_keys(numero)

    time.sleep(1)  # Wait for 1 second to ensure the fields are filled

    # Locate and click the send button
    xpath = "//button[@class='elementor-button elementor-size-sm']/span/span[@class='elementor-button-text' and text()='Send']"
    button = driver.find_element(By.XPATH, xpath)
    button.click()

    time.sleep(1)  # Wait for 1 second to ensure the form is submitted

    # Clear the form fields
    driver.find_element(By.XPATH, '//*[@id="form-field-email"]').clear()
    driver.find_element(By.XPATH, '//*[@id="form-field-message"]').clear()

    time.sleep(1)  # Wait for 1 second before proceeding to the next iteration
```

### Script Functionality
The script provides an efficient solution for automating web form filling, particularly useful for repetitive tasks involving large volumes of data. The use of libraries like Selenium and Pandas makes the process robust and flexible, allowing for easy adaptation as needed.

WebDriver Setup: Configures and initializes the WebDriver for the Firefox browser, using GeckoDriverManager to automatically install the necessary driver.

Data Loading: Reads the Excel file containing the data to be used for filling the form.

Iteration and Form Filling: For each row in the DataFrame, the script:

Extracts the relevant column values (numero and email).

Fills the web form fields with the extracted values.

Clicks the form's submit button.

Clears the form fields for the next iteration.

*Timing Control* Uses time.sleep(1) to ensure the browser has sufficient time to process each action.
