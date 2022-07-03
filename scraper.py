import requests
from bs4 import BeautifulSoup
from pprint import pprint

res = requests.get('https://news.ycombinator.com/news')
soup = BeautifulSoup(res.text, 'html.parser')
links = soup.select('.titlelink')
subtexts = soup.select('.subtext')

def sorted_by_votes(hnlist):
    return sorted(hnlist, key= lambda k: k['votes'], reverse=True)

def create_custom_hn(links, subtexts):
    hn = []
    for idx, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None)
        vote = subtexts[idx].select(".score")
        if len(vote):
            points = int(vote[0].getText().replace(" points", " "))
            if points > 99:
                hn.append({'title' : title, "link" : href, "votes" : points})
    return sorted_by_votes(hn)

if __name__ == '__main__':
    pprint(create_custom_hn(links, subtexts))