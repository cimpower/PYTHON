import requests
from bs4 import BeautifulSoup
import smtplib

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
    price_text = soup.find(id="priceblock_ourprice").get_text()
    price = float(price_text.replace( ",",".")[0:5])
#para la disponibilidad compobamos si 'no stock', si falla busca 'stock'
    try:
        stock = soup.find('span',{'class':'a-size-medium a-color-state'}).get_text().strip()
    except AttributeError:
        stock = soup.find('span',{'class':'a-size-medium a-color-success'}).get_text().strip()

    if(price < 15.00):
        email()

    print(title)
    print(price)
    print(stock)

def email():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('javiemg@gmail.com', 'efrgapvrokfxpjzj')

    asunto = 'Ha bajado el precio!'
    cuerpo = 'Aqui tienes el link'

    msg = f"Subjet: {asunto}\n\n{cuerpo}"
    server.sendmail(
        'javiemg@gmail.com',
        'j_moregon@hotmail.com',
        msg
    )
    print('Se ha enviado el email!')

    server.quit()
#pasar el prcio y el link como variables

USB()
echo_N()
echo_B()