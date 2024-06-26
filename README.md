# Python Script Documentation

## This project automates web form submission using Selenium and multiple threads. It reads data from CSV files, fills in email and phone fields in a specific form, and submits the information. The project uses Firefox with GeckoDriver, manages multiple parallel executions for efficiency, and includes a stopwatch to monitor execution time. At the end, all processes are synchronized and the browser is closed.

## Function Imports
- `stopwatch` function from `function`

## Library Imports
- `time`
- `threading`
- `pandas as pd`
- `selenium.webdriver` and related modules:
  - `webdriver`
  - `webdriver.common.by.By`
  - `webdriver.firefox.service.Service`
- `webdriver_manager.firefox`:
  - `GeckoDriverManager`

## Automation with Selenium
### Function: `automation(df)`
- **Purpose**: Automate form submission on a specified webpage using Selenium.
- **Parameters**: `df` - A DataFrame containing data to be submitted.

### Steps:
1. **Driver Setup**:
   - Initialize `GeckoDriver` (Firefox).
   - Navigate to the target URL: `https://renopele.fun/api/`.

2. **Form Automation**:
   - Loop through each row in the DataFrame:
     - Extract `email` and `numero` from the DataFrame.
     - Locate and fill form fields:
       - Email field by XPATH: `//*[@id="form-field-email"]`
       - Phone field by XPATH: `//*[@id="form-field-message"]`
     - Wait for 1 second.
     - Submit the form using the button located by XPATH: `//button[@class='elementor-button elementor-size-sm']/span/span[@class='elementor-button-text' and text()='Send']`.
     - Clear form fields.
     - Wait for 1 second.
   - Close the driver.

## Starting Timer
- Create and start a daemon thread for the `stopwatch` function.

## Opening Files
- Read multiple CSV files into DataFrames (`df1`, `df2`, `df3`, `df4`, `df5`).

## Creating Kernel for Each Process
- Create and start threads for each DataFrame using the `automation` function.
- Join threads to ensure all processes complete.

## Completion
- Print "Automation completed" after all threads finish.
