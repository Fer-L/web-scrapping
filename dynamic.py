from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.edge.service import Service

# Loads chrome driver
serv = Service('chromedriver.exe')
driver = webdriver.Chrome(service=serv)
driver.get('https://www.quadriframe.com.br/shop')
pageTitle = driver.title

# Finds all product cards
soup_file = driver.page_source
soup = bs(soup_file, "html.parser")
products = soup.find_all("div", class_="nm-shop-loop-title-price")
driver.quit()

if __name__ == '__main__':
    print(pageTitle)
    # Shows all products listed on the website, by name and price
    for product in products:
        title_element = product.find("a", class_="nm-shop-loop-title-link woocommerce-LoopProduct-link")
        price_element = product.find("span", class_="price")
        print(title_element.text)
        print(price_element.text)
        print()
    print(f'Total of products: {len(products)}')




