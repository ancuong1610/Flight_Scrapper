
# Flight Scrapper

Flight Scrapper is a Python script that automatically navigates to flight booking websites to retrieve and compare flight prices from various airlines, helping you find the cheapest options.

## Features

- Scrapes flight data from [Cheapflights.com](https://www.cheapflights.com.au/)
- Uses Selenium for web automation and Pandas for data manipulation
- Asks for user input in the localhost website for flight search parameters
- Outputs the scraped data in the website

## Prerequisites

- Python 3.x
- Docker Application
- Firefox
- Pycharm IDE

## Setup Guide
```markdown
1. **Clone the repository:**

    git clone https://github.com/ancuong1610/Flight_Scrapper.git
    cd Flight_Scrapper

2. **Create a virtual environment (optional but recommended):**

    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. **Install the required packages (go to Pycharm Project terminal):**

    docker-compose build
    docker-compose up

4. **Run the application:**

    python app.py 

    - Go to link: http://127.0.0.1:5002
```

You will be prompted to enter the following details:

- Origin airport code (e.g., FRA)
- Destination airport code (e.g., HAN)
- Outbound date (YYYY-MM-DD)
- Return date (YYYY-MM-DD)

The script will then navigate to Cheapflights.com, perform the search, and scrape the flight data. The results will be displayed under the search box.

## Example



## Code Overview

### handle_cookie_consent(driver)

Handles cookie consent pop-ups on the website.

### scroll_to_bottom(driver)

Scrolls to the bottom of the page to load more content.

### click_show_more(driver)

Continuously clicks the "Show More" button to load all available flight results.

### scrape_flights(origin, destination, outbound_date, return_date)

Main function that performs the web scraping and returns the flight data.

### app.py

Handles user input and calls the `scrape_flights` function. Displays the results.

Example:

![Screenshot 2024-05-21 at 12 41 10](https://github.com/ancuong1610/Flight_Scrapper/assets/66347972/4bd7f6e5-0d8d-4737-8b6d-2b78d7d9d9bb)


## Notes

- Ensure you have the Firefox browser and Docker installed.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

---

# Happy scraping!

