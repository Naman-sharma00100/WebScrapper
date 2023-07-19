from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import validators

def main():
    URL = input("Enter the link of the product:")
    if not validate_url(URL):
        print("Invalid URL. Please enter a valid URL.")
        return
    
    if "amazon" in URL:
        amazon_data = scrape_amazon(URL)
        print(amazon_data)
    elif "flipkart" in URL:
        flipkart_data = scrape_flipkart(URL)
        print(flipkart_data)
    else:
        print("Unsupported website. Only Amazon and Flipkart are supported.")

def validate_url(URL):
    return validators.url(URL) 

def scrape_amazon(URL):
    browser = webdriver.Chrome()
    browser.get(URL)
    browser.maximize_window()

        #Fetching the title and price of the product
    try:
        title = browser.find_element(By.ID,"productTitle")        
    except NoSuchElementException:
        title = ""
    
    try:
        price = browser.find_element(By.XPATH,"//*[@id='corePriceDisplay_desktop_feature_div']/div[1]/span[2]/span[2]/span[2]")
    except NoSuchElementException:
        price = ""

    amazon_data = "Title: "+title.text + "\n Price: "+price.text
    return amazon_data  


def scrape_flipkart(URL):
    browser = webdriver.Chrome()
    browser.get(URL)
    browser.maximize_window()

        #Fetching the title and price of the product
    try:
        title = browser.find_element(By.XPATH,"//*[@id='container']/div/div[3]/div[1]/div[2]/div[3]/div/div[1]/h1/span")        
    except NoSuchElementException:
        title = ""
    
    try:
        price = browser.find_element(By.XPATH,"//*[@id='container']/div/div[3]/div[1]/div[2]/div[3]/div/div[3]/div[1]/div/div[1]")
    except NoSuchElementException:
        price = ""

    flipkart_data = "Title: "+title.text + "\n Price: "+price.text
    return flipkart_data


if __name__ == "__main__":
    main()