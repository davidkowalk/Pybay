from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as soup
from datetime import datetime
from datetime import timedelta

def load_auction(url):

    # dowload auction
    uclient = ureq(url)
    page_html = uclient.read()
    uclient.close()

    #parse html
    page_soup = soup(page_html, "html.parser")

    return page_soup


def get_price(soup):
    price = soup.find("span", {"id":"prcIsum_bidPrice"}).contents[0][4:]
    price = price.replace(".", "")
    return float(price.replace(",", "."))


#Handle dates
def get_end_date(soup):
    date_str = soup.find("span", {"class":"vi-tm-left"}).span.contents[0][1:]
    date_str += " " + soup.find("span", {"class":"endedDate"}).contents[0][:8]
    datetime_object = datetime.strptime(date_str, "%d. %b. %Y %H:%M:%S")
    #datetime_object = datetime.strptime(date_str, "%H:%M:%S")

    return datetime_object


def get_auction_ended(auction):
    pass


def push_bid(bid):
    pass
