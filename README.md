
# Flight Scrapper

Flight Scrapper is a Python script that automatically navigates to flight booking websites to retrieve and compare flight prices from various airlines, helping you find the cheapest options.

## Features

- Scrapes flight data from [Cheapflights.com](https://www.cheapflights.com.au/)
- Uses Selenium for web automation and Pandas for data manipulation
- Asks for user input in the terminal for flight search parameters
- Outputs the scraped data to a CSV file (`flight_data.csv`)

## Prerequisites

- Python 3.x
- Firefox browser
- [GeckoDriver](https://github.com/mozilla/geckodriver/releases) (for Selenium, not needed if you already have Firefox installed)

## Setup Guide
```markdown
1. **Clone the repository:**

    ```sh
    git clone https://github.com/ancuong1610/Flight_Scrapper.git
    cd Flight_Scrapper
    ```

2. **Create a virtual environment (optional but recommended):**

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Download and install GeckoDriver:**

    - Download the appropriate version of GeckoDriver from the [releases page](https://github.com/mozilla/geckodriver/releases).
    - Extract the downloaded file and place the `geckodriver` executable in a directory that is in your system's PATH, or specify the path in the script.
    - **Note:** If you already have Firefox browser installed, there is no need to install GeckoDriver separately.
```

You will be prompted to enter the following details:

- Origin airport code (e.g., FRA)
- Destination airport code (e.g., HAN)
- Outbound date (YYYY-MM-DD)
- Return date (YYYY-MM-DD)

The script will then navigate to Cheapflights.com, perform the search, and scrape the flight data. The results will be saved in a file named `flight_data.csv`.

## Example

```sh
$ python flight_scraper.py
Enter origin airport code: FRA
Enter destination airport code: HAN
Enter outbound date (YYYY-MM-DD): 2024-11-20
Enter return date (YYYY-MM-DD): 2024-12-20
```

After running the above commands, you will find the `flight_data.csv` file with the scraped flight data.

## Code Overview

### handle_cookie_consent(driver)

Handles cookie consent pop-ups on the website.

### scroll_to_bottom(driver)

Scrolls to the bottom of the page to load more content.

### click_show_more(driver)

Continuously clicks the "Show More" button to load all available flight results.

### scrape_flights(origin, destination, outbound_date, return_date)

Main function that performs the web scraping and returns the flight data.

### main()

Handles user input and calls the `scrape_flights` function. Displays the results and saves them to a CSV file.

## Notes

- Ensure you have the Firefox browser installed.
- Adjust the GeckoDriver path in the script if it's not in your system's PATH.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## Acknowledgements

- [Selenium](https://www.selenium.dev/)
- [Pandas](https://pandas.pydata.org/)
- [Tabulate](https://pypi.org/project/tabulate/)

---

#Happy scraping!

