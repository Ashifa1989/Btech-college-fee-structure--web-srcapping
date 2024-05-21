**Project Description**
This project is a web scraping tool designed to extract fee structures for B.Tech courses from various colleges listed on the Collegedunia website. The tool utilizes Selenium WebDriver for automated browsing and data extraction, and it saves the collected data into CSV files for further analysis.

**Features**
Scrapes B.Tech fee structure details from Collegedunia.
Handles dynamic web content loading using Selenium WebDriver.
Saves scraped data into CSV files.
Handles pagination and scrolls through dynamically loaded content.
Retries on failures to ensure data collection completeness.
Requirements
Python 3.x
Selenium
Pandas
Microsoft Edge WebDriver
Installation
Clone the repository:


git clone https://github.com/yourusername/btech-fee-structure-scraper.git  # Replace `yourusername` with your GitHub username
cd btech-fee-structure-scraper
Install the required Python packages:

pip install selenium pandas
Download and install Microsoft Edge WebDriver:

Ensure that you have Microsoft Edge installed.
Download the appropriate version of the Edge WebDriver from here.
Make sure the WebDriver executable is in your system's PATH.

**Usage**
Prepare the input CSV file:

Ensure you have a CSV file with the list of colleges you want to scrape, formatted as follows:

College Name,College URL/Link
Example:
Example College,https://collegedunia.com/university/example-college

**Run the script:**
python b_tech_fee_structure.py 

**Output:**
The script will generate two CSV files:
data_list.csv containing the scraped fee structures. 
no_data_list.csv containing the colleges for which data could not be scraped. 

**Script Details**
**load_webpage_and_save_data(driver)**
Purpose: Loads the main B.Tech colleges page on Collegedunia and scrolls through the page to gather links and names of all listed colleges. Saves the data into a CSV file.
**find_the_page_to_process(driver, college_link)**
Purpose: Given a college's main page link, navigates to the B.Tech course page and gathers all relevant links for fee structure extraction.
**btech_fee_structure(driver, name, links)**
Purpose: Extracts fee structure details from each provided link and compiles the data into a DataFrame.
**main()**
Purpose: The main function to read input data, initiate the scraping process, and save the output to CSV files.

**Contributing**
Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.
