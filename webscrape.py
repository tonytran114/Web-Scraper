from bs4 import BeautifulSoup
import urllib.request
import requests


def main():
    # getting the Data
    url = "https://trends24.in/united-states/"
    page = requests.get(url)

    # making the Soup
    soup = BeautifulSoup(page.text, "html.parser")

    # getting data from trend cards
    '''
    Structure of data 
    ------------------
    Data is an array of trend_card arrays
    trend_card arrays are in the format ['timestamp', [trend1, trend1_count], [trend2, trend2_count], ...]

    '''
    data = []
    for body in soup.find_all('body'):
        for div in body.find_all('div', {'class': 'trend-card'})[1:5]:
            trend_card = []
            for h5 in div.find_all('h5'):
                trend_card.append(h5.text)
            for ol in div.find_all('ol', {'class': 'trend-card__list'}):
                for li in ol.find_all('li'):
                    for a in li.find_all('a'):
                        trend = a.text
                        tc = ''
                    for count in li.find_all('span', {'class': 'tweet-count'}):
                        tc = count.text
                    trend_card.append([trend, tc])

            data.append(trend_card)

    return data


# starts the process
if __name__ == '__main__':
    main()
