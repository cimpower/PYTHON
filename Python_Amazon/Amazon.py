import requests
from bs4 import BeautifulSoup
import smtplib
import csv

headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36'}

def item_1(old_price_item_1):
    URL = 'https://www.amazon.es/dp/B07SNPKX5Y'
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'lxml')
    title_text = soup.find(id="productTitle").get_text().strip() #buscamos la etiqueta, cogemos texto y quitamos espacios
    title = title_text[15:27]+ ' Negro'
    price_text = soup.find(id="priceblock_ourprice").get_text()
    price = float(price_text.replace( ",",".")[0:5])
    try: #para la disponibilidad compobamos si 'no stock', si falla busca 'stock'
        stock = soup.find('span',{'class':'a-size-medium a-color-state'}).get_text()
    except AttributeError:
        stock = soup.find('span',{'class':'a-size-medium a-color-success'}).get_text().strip()
    #Envio de email si el precio baja
    if(price < old_price_item_1): #Envio de email si el precio baja
        email(title,price,stock,URL)
    #Añadimos nueva informacion al log,txt
    csv_a(title,price,stock,URL)

def item_2(old_price_item_2):
    URL = 'https://www.amazon.es/dp/B07SNPKX63'
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'lxml')

    title_text = soup.find(id="productTitle").get_text().strip()#buscamos la etuiqueta, cogemos texto y quitamos espacios"""
    title = title_text[15:27]+ ' Blanco'
    price_text = soup.find(id="priceblock_ourprice").get_text()
    price = float(price_text.replace( ",",".")[0:5])
    try: #para la disponibilidad compobamos si 'no stock', si falla busca 'stock'
        stock = soup.find('span',{'class':'a-size-medium a-color-state'}).get_text().strip()
    except AttributeError:
        stock = soup.find('span',{'class':'a-size-medium a-color-success'}).get_text().strip()
    #Envio de email si el precio baja
    if(price < old_price_item_2): #Envio de email si el precio baja
        email(title,price,stock,URL)
    #Añadimos nueva informacion al log,txt
    csv_a(title,price,stock,URL)

def item_3(old_price_item_3): 
    URL = 'https://www.amazon.es/dp/B07XRC3WXX'
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'lxml')
    title_text = soup.find(id="productTitle").get_text().strip() #buscamos la etuiqueta, cogemos texto y quitamos espacios
    title = title_text[8:26]+ ': Blanco'
    price_text = soup.find(id="priceblock_ourprice").get_text()
    price = float(price_text.replace( ",",".")[0:5])
    #para la disponibilidad compobamos si 'no stock', si falla busca 'stock'
    try: 
        stock = soup.find('span',{'class':'a-size-medium a-color-state'}).get_text().strip()
    except AttributeError:
        stock = soup.find('span',{'class':'a-size-medium a-color-success'}).get_text().strip()
    #Envio de email si el precio baja
    if(price < old_price_item_3): 
        email(title,price,stock,URL)
    #Añadimos nueva informacion al log,txt
    csv_a(title,price,stock,URL)

def email(title,price,stock,URL):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('javiemg@gmail.com', 'efrgapvrokfxpjzj')

    asunto = 'Ha bajado el precio!'
    cuerpo = '{}\n{}\n{}\nAqui tienes el link -> {}'.format(title,price,stock,URL)
    print(cuerpo)
    msg = 'Subject: {}\n\n{}'.format(asunto, cuerpo)
    server.sendmail(
        'javiemg@gmail.com',
        'j_moregon@hotmail.com',
        msg
    )
    print('Se ha enviado el email!')

    server.quit()

def csv_r():
    with open("./Python_Amazon/log.csv", "r") as log:
        rows = csv.reader(log)
        for i,lista in enumerate(rows):
            if i == 1:
                old_price_item_1 = float(lista[1])
                #print (old_price_item_1)
            elif i == 2:
                old_price_item_2 = float(lista[1])
                #print(old_price_item_2)
            elif i == 3:
                old_price_item_3 = float(lista[1])
                #print(old_price_item_3)
    #print (old_price_item_1,old_price_item_2,old_price_item_3)            
    return old_price_item_1,old_price_item_2,old_price_item_3

def csv_w():
    with open('./Python_Amazon/log.csv','w') as log:
        row = csv.writer(log)
        row.writerow(['TITULO','PRECIO','STOCK','LINK'])

def csv_a(title,price,stock,URL):
    with open('./Python_Amazon/log.csv','a') as log:

        lista = [title,price,stock,URL]
        row = csv.writer(log)
        row.writerow(lista)

csv_r()
old_price_item_1,old_price_item_2,old_price_item_3 = csv_r()
csv_w()

item_1(old_price_item_1)
item_2(old_price_item_2)
item_3(old_price_item_3)