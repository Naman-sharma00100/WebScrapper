## Product Information Web Scraper

This Python script is a web scraper designed to extract product information from the provided URL. It supports scraping from Amazon and Flipkart websites.

### Requirements

To run this script, you need to have the following installed:

- Python 3.x
- BeautifulSoup library
- Requests library
- Validators library

You can install the required libraries using `pip`. For example:

- pip install beautifulsoup4 or pip install bs4
- pip install requests
- pip install validators


### How to Use

1. Make sure you have the required libraries installed as mentioned above.

2. Run the script by executing `python main.py` in the terminal or command prompt.

3. When prompted, enter the URL of the product you want to scrape.

4. The script will validate the URL and determine whether it is from Amazon or Flipkart.

5. If the URL is valid and recognized as either Amazon or Flipkart, the script will extract the product's title and price information.

### Important Note

1. The script uses proxies to access the URLs. The provided proxies may not work if they are not authorized or if the service is not available. Ensure you have appropriate and authorized proxies in the `proxies` dictionary or remove the proxy configuration if not needed.

2. The script ignores SSL certificate verification. It's generally not recommended to disable SSL certificate verification as it poses security risks. 
   

### Function Descriptions

1. `main()`: The main function that starts the script execution. It takes the product URL as input, validates it, and calls the appropriate scraping function based on the website.

2. `validate_url(URL)`: A function that checks whether the given URL is valid using the `validators` library.

3. `scrape_amazon(URL)`: A function that performs web scraping for Amazon products. It extracts the title and price of the product from the provided Amazon URL.

4. `get_title_amazon(soup)`: A helper function to extract the product title from the BeautifulSoup object of the Amazon page.

5. `get_price_amazon(soup)`: A helper function to extract the product price from the BeautifulSoup object of the Amazon page.

6. `scrape_flipkart(URL)`: A function that performs web scraping for Flipkart products. It extracts the title and price of the product from the provided Flipkart URL.

7. `get_title_flipkart(soup)`: A helper function to extract the product title from the BeautifulSoup object of the Flipkart page.

8. `get_price_flipkart(soup)`: A helper function to extract the product price from the BeautifulSoup object of the Flipkart page.


### Disclaimer

Web scraping can be subject to legal and ethical considerations. Ensure that you have the right to access and scrape the target website's data. Always review and comply with the website's terms of service and robots.txt file before scraping any data.
