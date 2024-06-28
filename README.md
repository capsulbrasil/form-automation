# Automation Script

This project automates the process of submitting data from Excel files to a web form using Selenium and threading.

## Requirements

Make sure you have the following installed:

- Python 3.7 or higher
- pip (Python package installer)

## Setup

1. **Clone the repository:**

    ```sh
    git clone https://github.com/your-repo/automation-script.git
    cd automation-script
    ```

2. **Create a virtual environment and activate it:**

    ```sh
    python -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages:**

    ```sh
    pip install -r requirements.txt
    ```

    The `requirements.txt` should contain:
    ```
    pandas
    selenium
    webdriver-manager
    ```

4. **Place your Excel files in the `data` directory:**

    The script expects the following files:
    - `data/LISTA01CSHB.xlsx`
    - `data/LISTA02CSHB.xlsx`
    - `data/LISTA03CSHB.xlsx`
    - `data/LISTA04CSHB.xlsx`
    - `data/LISTA05CSHB.xlsx`

## Running the Script

To run the automation script, use the following command:

```sh
python main.py
