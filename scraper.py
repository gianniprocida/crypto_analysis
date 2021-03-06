import os
import time

import requests
from bs4 import BeautifulSoup as bs
import re




def scraping_pricing_data(url,num):


    # Load the web page content
    r = requests.get(url, verify=False)

    # Beautiful soup object
    soup = bs(r.content, "html.parser")

    files = []

    # Parsing for the links (daily prices)


    for item in soup.find_all('a'):
     if re.sub(r'\s+','',item.get_text())=='[Daily]':
        link=item.get('href')
        name=link.split('/')[-1]
        files.append(link.split('/'))
        if len(files) < num:
         print(f"Downloading {name} ...")
         with open (name,'wb') as file:
            try:
             resp = requests.get(link,
                                verify=False, timeout=5)
             file.write(resp.content)
            except requests.exceptions.ConnectionError:
             print("Site not reachable",link)
        else:
           pass
    print("Download completed")





