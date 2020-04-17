from bs4 import BeautifulSoup as bs
import requests
import pandas as pd

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36"
LANGUAGE = "es-ES,es;q=0.9,en;q=0.8"

# url = "https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population"

def get_soup(url):
    """Constructs and returns a soup using the HTML content of `url` passed"""
    # initialize a session
    session = requests.Session()
    # set the User-Agent as a regular browser
    session.headers['User-Agent'] = USER_AGENT
    # request for english content (optional)
    session.headers['Accept-Language'] = LANGUAGE
    session.headers['Content-Language'] = LANGUAGE
    # make the request
    html = session.get(url)
    # return the soup
    return bs(html.content, "html.parser")

def get_all_lists(soup):
    """Extracts and returns all tables in a soup object"""
    return soup.find_all("ul","feature-list")

def get_table_headers():
    """Given a table soup, returns all the headers"""
    headers = ['VACIO','ORIGEN-DESTINO','HORARIO','PRECIO','VENDIDO','xxx']
    # for li in lis.find("li").find_all("span"):
    #     headers.append(li.text.strip())     
    #     #print(th) 
    return headers

def get_table_rows(lis):
    """Given a table, returns all its rows"""
    rows = []
    for li in lis.find_all("li"):
        cells = []
        # grab all td tags in this table row
        spans = li.find_all("span")
        for sp in spans:
            cells.append(sp.text.replace('\n', ' ').strip())
            #cells = " ".join(sp.split())
        rows.append(cells)
    return rows

def save_as_csv(lis_name, headers, rows):
    df = pd.DataFrame(rows, columns=headers)    #, index=False
    #df = df.droplevel('VACIO')
    df.to_csv(f"{lis_name}.csv")
    return df

def main(url):
    # get the soup
    soup = get_soup(url)
    # extract all the tables from the web page
    lists = get_all_lists(soup)
    print(f"[+] Found a total of {len(lists)} lists.")
    # print(lists)
    # iterate over all lists
    for i, lis in enumerate(lists, start=1):
        # get the table headers
        print(i)
        headers = get_table_headers()
        # get all the rows of the table
        rows = get_table_rows(lis)
        # save table as csv file
        lis_name = f"lista-{i}"
        print(f"[+] Saving {lis_name}")
        save_as_csv(lis_name, headers, rows)


if __name__ == "__main__":

    url = "https://www.truecalia.com/comprar-billetes/tren-ave-barcelona-madrid.html"
    main(url)

    #pueba prueba prueba
    