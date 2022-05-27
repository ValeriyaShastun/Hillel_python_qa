from bs4 import BeautifulSoup
import requests

class GetPagesCount:

    def __init__(self, url):
        self.url = url

    def get_pages_count(self):
        """
        Will give quantity of pages which are available in the web page
        :param url: url of web page
        :return: pages' count
        """
        req = requests.get(self.url)
        soup = BeautifulSoup(req.content, 'html.parser')
        tag_with_next_page = soup.find("li", class_="next")
        count = 1
        while tag_with_next_page is not None:
            link_to_next_page = "https://quotes.toscrape.com" + tag_with_next_page.find("a").get("href")
            next_page_navigate = requests.get(link_to_next_page)
            soup = BeautifulSoup(next_page_navigate.content, 'html.parser')
            tag_with_next_page = soup.find("li", class_="next")
            count += 1
        return count


if __name__ == "__main__":
    url = "https://quotes.toscrape.com/"
    pages_count = GetPagesCount(url).get_pages_count()
    print(f"Total pages amount on website is {pages_count}")