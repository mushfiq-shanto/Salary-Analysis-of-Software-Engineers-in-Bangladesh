from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

# List to store information about companies
CompaniesInfo = []

# Function to extract and process company data from rows on the webpage
def get_data(Rows):
    for idx, Row in enumerate(Rows):
        try:
            # Extract company name, rating, and salary statistics using class name
            CompanyName = Row.find_element(By.CLASS_NAME, "css-1ikln7a").text  # Company name
            Rating = Row.find_element(By.CLASS_NAME, "css-h9sogr").text        # Company rating
            Salaries = Row.find_element(By.CLASS_NAME, "css-259095").text      # Number of salaries
            Median = Row.find_element(By.CLASS_NAME, "css-16zrpia").text       # Median salary
            
            # Box to contain all elements with the specified class as frequency, upper and lower ranges all share the class name
            Box = Row.find_elements(By.CLASS_NAME, "css-1in2cw4")

            # Set default values for Frequency, Lower, and Upper salary ranges
            Frequency, Lower, Upper = "N/A", "N/A", "N/A"

            # If the Box has sufficient elements, extract salary range information
            if len(Box) >= 4:
                Frequency = Box[1].text  # Frequency of salary disbursement
                Lower = Box[2].text      # Lower bound of the salary range
                Upper = Box[3].text      # Upper bound of the salary range

                # Sometimes the Upper & Lower ranges are close together so an extra '-' is added by website to create separation. This '-' takes up Box[3] and the Upper Range value is pushed to Box[4]
                if Upper.strip() == '-':
                    Upper = Box[4].text

            # Store extracted data in a dictionary
            CompanyData = {
                "Company": CompanyName,
                "Rating": Rating,
                "Salaries": Salaries,
                "Medians": Median,
                "Frequencies": Frequency,
                "Uppers": Upper,
                "Lowers": Lower
            }

            # Append the company data dictionary to the global CompaniesInfo list
            CompaniesInfo.append(CompanyData)
        
        except Exception as e:
            # Handle any exceptions during the data extraction process
            print(f"An error occurred while processing row {idx}: {e}")

# Main function to handle browser navigation and data collection from multiple pages
def main():
    # Function to handle retries for loading a webpage if it fails initially as Glassdoor sometimes denies get requests
    def retry_get(url, retries=3, initial_wait=10):
        wait = initial_wait
        driver = webdriver.Chrome()
        for attempt in range(retries):  # Try to load the page up to 'retries' times
            try:
                driver.get(url)  # Attempt to load the URL
                return driver    # If successful, return the driver instance
            except Exception:
                print(f"Error loading {url}, retrying in {wait} seconds...")
                time.sleep(wait)  # Wait before retrying
                wait *= 2         # Increase the wait time for the next attempt
        driver.quit()             # Quit the driver if all retries fail
        return None               # Return None if the page cannot be loaded

    try:
        # Loop through 20 pages of salary data
        for n in range(1, 21):  # Adjust the range for the number of pages to scrape
            url = f"https://www.glassdoor.com/Salaries/software-engineer-salary-SRCH_IM1237_KO0,17_IP{n}.htm"
            
            # Use retry_get function to attempt loading the page with retries
            driver = retry_get(url)
            if driver:  # If the page loaded successfully
                try:
                    time.sleep(5)  # Small delay to allow the page content to load

                    # Wait until the salary items are present on the page
                    WebDriverWait(driver, 20).until(
                        EC.presence_of_element_located((By.CLASS_NAME, "col-lg"))
                    )

                    # Locate the container that holds the salary entries
                    Items = driver.find_element(By.CLASS_NAME, "col-lg")

                    # Extract all individual rows (companies) from the container
                    Rows = Items.find_elements(By.CLASS_NAME, "py")

                    # Process each row to extract company data
                    get_data(Rows)
                    
                except Exception as e:
                    # Handle exceptions while processing the page
                    print(f"Error processing page {n}: {e}")
                
                # Close the driver and wait before loading the next page
                time.sleep(5)
                driver.quit()
                time.sleep(5)
            else:
                # Log a message if the page could not be loaded after retries
                print(f"Failed to load page {n} after retries.")
                
    except Exception as e:
        # Catch any errors that occur during the scraping process
        print(f"Error during scraping: {e}")

    # Convert the collected company data to a pandas DataFrame
    df = pd.DataFrame(CompaniesInfo)

    # Save the DataFrame to a CSV file
    df.to_csv("eng_salaries.csv", index=False)

    # Display the last 3 rows of the collected data as a sample
    print(df.tail(3))

    # Print the total number of companies scraped
    print(f"Total companies scraped: {len(CompaniesInfo)}")

# Entry point: execute the main function if this script is run directly
if __name__ == '__main__':
    main()