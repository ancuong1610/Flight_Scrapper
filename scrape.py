import time
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


def handle_cookie_consent(driver):
    try:
        # Wait for the button to be clickable
        button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH,
                                        "//button[@class='RxNS RxNS-mod-stretch RxNS-mod-variant-outline RxNS-mod-theme-base RxNS-mod-shape-default RxNS-mod-spacing-base RxNS-mod-size-small']"))
        )

        # Click the button
        button.click()
        print("Cookie consent button clicked successfully!")
    except TimeoutException:
        print("Timed out waiting for the cookie consent button to be clickable.")
    except Exception as e:
        print(f"Error: {e}")


def scroll_to_bottom(driver):
    # Scroll to the bottom of the page
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)  # Wait for scrolling to finish


def click_show_more(driver):
    while True:
        try:
            # Check if the "Show More" button exists
            show_more_button = driver.find_element(By.CLASS_NAME, 'ULvh-button.show-more-button')

            # Click the "Show More" button
            show_more_button.click()

            # Wait for a short time to allow new results to load
            time.sleep(2)

        except NoSuchElementException:
            # If the "Show More" button is not found, exit the loop
            break

        except Exception as e:
            print(f"Error: {e}")
            break


def scrape_kayak(origin, destination, outbound_date, return_date):
    gecko_driver_path = 'path/to/geckodriver'  # Specify the path to your GeckoDriver executable

    options = webdriver.FirefoxOptions()
    options.headless = False  # Run Firefox with a GUI

    driver = webdriver.Remote(
        command_executor='http://localhost:4444/wd/hub',
        options=options
    )
    url = f'https://www.cheapflights.com.au/flight-search/{origin}-{destination}/{outbound_date}/{return_date}?sort=bestflight_a'
    driver.get(url)

    # Handle cookie consent button
    handle_cookie_consent(driver)

    # Scroll to the bottom of the page to load more content
    scroll_to_bottom(driver)

    # Click "Show More" button to load all results
    #click_show_more(driver)

    flight_results = []

    try:
        # Wait for the page to load completely
        driver.implicitly_wait(10)

        # Find all elements with class `nrc6-wrapper`
        wrapper_elements = driver.find_elements(By.CLASS_NAME, 'nrc6-main')

        for wrapper in wrapper_elements:
            # Create a dictionary to store data for each row
            row_data = {}

            # Get the class name of the wrapper element
            row_data['Class'] = 'nrc6-main'

            # Find and store text data inside the wrapper element
            row_data['Text'] = wrapper.text.strip()

            # Find image elements inside the wrapper element
            image_elements = wrapper.find_elements(By.TAG_NAME, 'img')

            # Store the source URLs of images (if any)
            images = [img.get_attribute('src') for img in image_elements]
            row_data['Images'] = images

            # Append row data to flight_results list
            flight_results.append(row_data)

    except Exception as e:
        print(f"Error: {e}")

    finally:
        #driver.quit()
        print("done")

    return flight_results
