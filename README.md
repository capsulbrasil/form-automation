# Form Automation

This repository contains a PJupyter script that automates filling out a web form using data from an Excel file. Automation is performed with the **Selenium** and **Pandas** libraries.

## Features

- Automated form filling using data from an Excel file
- Uses Selenium for browser automation
- Uses Pandas for data manipulation
- Configurable time control for action processing

## Requirements

- `python` 3.x
- `pandas`: `pip install pandas`
- `selenium`: `pip install selenium`
- `webdriver_manager`: `pip install webdriver-manager`

## Usage

1. Clone this repository:

```sh
git clone https://github.com/uisNikol4s/form_automation.git
```

2. Navigate to the project directory:

```sh
cd form_automation
```

3. Install the required libraries:

```sh
pip install -r requirements.txt
```

4. Place your Excel file in the `data` directory.

5. Run the script:

```sh
python automation.py
```

## Script Overview

- **WebDriver Configuration**: Configures and initializes the WebDriver for the Firefox browser.
- **Data Loading**: Reads data from an Excel file into a Pandas DataFrame.
- **Form Filling**: Iterates over each row of the DataFrame to fill and submit the form.
- **Time Control**: Ensures that the browser has enough time to process each action.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
