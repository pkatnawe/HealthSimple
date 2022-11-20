from requests_html import HTMLSession
from bs4 import BeautifulSoup
import requests

headers = {
    'User-Agent' :'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:106.0) Gecko/20100101 Firefox/106.0'
}
def main(string):
    url = 'http://www.webmd.com/diet/health-benefits-' + string
    response = requests.get(url, headers=headers)
    print(response.content)
    soup = BeautifulSoup(response.content, 'html.parser')
    elements = soup.find_all(class_= "article-page active-page")
    print(f"Elements: {len(elements)}")
    for element in elements:
        print(element.text)
    

if __name__ == '__main__':
    main('apples')
    
