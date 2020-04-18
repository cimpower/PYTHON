import requests
from bs4 import BeautifulSoup

headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36'}

def echo_N():
    URL = 'https://www.amazon.es/dp/B07SNPKX5Y'
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'lxml')
#buscamos la etuiqueta, cogemos texto y quitamos espacios
    title_text = soup.find(id="productTitle").get_text().strip()
    title = title_text[15:27]+ ' Negro'
    price = soup.find(id="priceblock_ourprice").get_text()
#para la disponibilidad compobamos si 'no stock', si falla busca 'stock'
    try:
        stock = soup.find('span',{'class':'a-size-medium a-color-state'}).get_text()
    except AttributeError:
        stock = soup.find('span',{'class':'a-size-medium a-color-success'}).get_text().strip()
    print(title)
    print(price)
    print(stock.strip())

def echo_B():
    URL = 'https://www.amazon.es/dp/B07SNPKX63'
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'lxml')
#buscamos la etuiqueta, cogemos texto y quitamos espacios
    title_text = soup.find(id="productTitle").get_text().strip()
    title = title_text[15:27]+ ' Blanco'
    price = soup.find(id="priceblock_ourprice").get_text()
#para la disponibilidad compobamos si 'no stock', si falla busca 'stock'
    try:
        stock = soup.find('span',{'class':'a-size-medium a-color-state'}).get_text().strip()
    except AttributeError:
        stock = soup.find('span',{'class':'a-size-medium a-color-success'}).get_text().strip()
    print(title)
    print(price)
    print(stock)

def USB():
    URL = 'https://www.amazon.es/dp/B07XRC3WXX'
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'lxml')
#buscamos la etuiqueta, cogemos texto y quitamos espacios
    title_text = soup.find(id="productTitle").get_text().strip()
    title = title_text[8:27]+ ' Blanco'
    price = soup.find(id="priceblock_ourprice").get_text()
#para la disponibilidad compobamos si 'no stock', si falla busca 'stock'
    try:
        stock = soup.find('span',{'class':'a-size-medium a-color-state'}).get_text().strip()
    except AttributeError:
        stock = soup.find('span',{'class':'a-size-medium a-color-success'}).get_text().strip()
    print(title)
    print(price)
    print(stock)


echo_N()
echo_B()
USB()