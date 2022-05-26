from bs4 import BeautifulSoup
import requests


url = "https://quotes.toscrape.com/"
req = requests.get(url)

soup = BeautifulSoup(req.content, 'html.parser')
tag_with_next_page = soup.find("li", class_="next")
count = 1
while tag_with_next_page is not None:
    link_to_next_page = "https://quotes.toscrape.com" + tag_with_next_page.find("a").get("href")
    next_page_navigate = requests.get(link_to_next_page)
    soup = BeautifulSoup(next_page_navigate.content, 'html.parser')
    tag_with_next_page = soup.find("li", class_="next")
    count += 1

print(f"Total pages amount on website is {count}")
