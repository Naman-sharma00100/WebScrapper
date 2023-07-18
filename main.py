from bs4 import BeautifulSoup
import requests
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


proxies = {
    'http': 'http://numcys:Webscrap.123@unblock.oxylabs.io:60000',
    'https': 'http://numcys:Webscrap.123@unblock.oxylabs.io:60000',
}


def validate_url(URL):
    return validators.url(URL)


def scrape_amazon(URL):
    response = requests.request(
        'GET',
        URL,
        verify=False,  # Ignore the certificate
        proxies=proxies,
    )
    soup = BeautifulSoup(response.text,"html.parser")

    title = get_title_amazon(soup)
    price = get_price_amazon(soup)

    amazon_data = "Title: "+title + "\n Price: "+price
    return amazon_data  


def get_title_amazon(soup):
    try:
        title = soup.find("span", attrs={"id":'productTitle'})
        
        # Inner NavigatableString Object
        title_value = title.text

        # Title as a string value
        title_string = title_value.strip()

    except AttributeError:
        title_string = ""

    return title_string


# Function to extract Product Price
def get_price_amazon(soup):
    try:
        price = soup.find("span",attrs={"class":"a-price aok-align-center reinventPricePriceToPayMargin priceToPay"}).find("span",attrs={"class":"a-offscreen"}).string.strip()

    except AttributeError:
        price = ""

    return price


def scrape_flipkart(URL):
    HEADERS = ({'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36', 'Accept-Language': 'en-US, en;q=0.5'})
    response = requests.request(
        'GET',
        URL,
        verify=False,  # Ignore the certificate
        proxies=proxies,
        headers=HEADERS
    )
    soup = BeautifulSoup(response.text,"html.parser")
    # with open('result.html', 'w',encoding="utf-8") as f:
    #     f.write(response.text)
    title = get_title_flipkart(soup)
    price = get_price_flipkart(soup)
    flipkart_data = "Title: "+title + "\n Price: "+price

    return flipkart_data  # Replace this with the actual data you want to return from Flipkart.


def get_title_flipkart(soup):
    try:
        title = soup.find("span", attrs={"class":'B_NuCI'})

        # Inner NavigatableString Object
        title_value = title.text

        # Title as a string value
        title_string = title_value.strip()

    except AttributeError:
        title_string = ""

    return title_string


# Function to extract Product Price
def get_price_flipkart(soup):
    try:
        price = soup.find("div",attrs={"class":"_25b18c"}).find("div",attrs={"class":"_30jeq3 _16Jk6d"}).string.strip()

    except AttributeError:
        price = ""

    return price


if __name__ == "__main__":
    main()

