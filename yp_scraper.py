import requests

from lxml import html
from time import sleep


def scrape_yellow_pages(search_term, city, state):
    params = {'search_terms': search_term,
              'geo_location_terms': city + ', ' + state}
    base_url = "http://www.yellowpages.com/search?"
    businesses = []

    for url in [base_url + "&page=%s" % i for i in xrange(1, 4)]:
        try:
            page = requests.get(url, params=params)
        except:
            print "Unable to retrieve page %s of results" % (url[-1])
            continue

        dom_tree = html.fromstring(page.text)

        names = dom_tree.xpath('//a[@class="business-name"]/text()')

        businesses.extend(names)

        sleep(5)

    return businesses


if __name__ == "__main__":
    scrape_yellow_pages('cupcakes', 'Tuscon', 'AZ')
