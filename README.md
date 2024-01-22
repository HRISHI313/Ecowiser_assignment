# LinkedIn Scraper and API Integration

## Overview

This project is a Python-based LinkedIn scraper that automates the process of searching for LinkedIn profiles, extracting relevant information, and integrating with the LinkedIn API to retrieve additional data. The scraper uses Selenium for web automation and requests for API integration.

## Prerequisites

- Chrome Driver: Ensure you have the Chrome driver installed and provide its path in `chrome_driver_path`.
- LinkedIn Credentials: Enter your LinkedIn email and password in `mail` and `paswd` respectively.
- LinkedIn API Access: Obtain an access token and cookies for API requests and replace the placeholders in the script.

## Usage

1. Clone the repository:

    ```bash
    git clone https://github.com/your_username/linkedin-scraper.git
    cd linkedin-scraper
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the script:

    ```bash
    python linkedin_scraper.py
    ```

## Configuration

- **Chrome Driver Path**: Set the path to your Chrome driver in `chrome_driver_path`.
- **LinkedIn Credentials**: Provide your LinkedIn email and password in `mail` and `paswd`.
- **Search Name**: Set the name you want to search in `Search_name`.
- **API Access**: Replace the placeholders for access token and cookies with valid values.

## Output

The script will generate a CSV file named `profile.csv` containing the extracted LinkedIn profile information.

## LinkedIn API Integration

To use the LinkedIn API, make sure you have obtained the necessary access token and cookies. Replace the placeholders in the API integration section of the script.

```python
token = 'Enter the access token'
cookies = 'Enter the cookie that has been generated'

import requests

url = "https://api.linkedin.com/v2/userinfo"

payload = {}
headers = {
    'Authorization': f'Bearer {token}',
    'Cookie': f'{cookies}'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
