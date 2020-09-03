import requests
from bs4 import BeautifulSoup
from pprint import pprint


def get_soup_res(url, page=0):
    if page > 0:
        res = requests.get(f'{url}?p={page}')
    else:
        res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    return soup


def sort_news_by_votes(news):
    return sorted(news, key=lambda k: k['vote'], reverse=True)


def create_custom_hn(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None)
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 99:
                hn.append({'title': title, 'link': href, 'vote': points})

    return sort_news_by_votes(hn)


def create_multipage_hn(url, pages=1):
    hn = []
    if pages < 1:
        raise ValueError('pages have to be greater than or equal to 1')
    for page in range(pages):
        soup = get_soup_res(url, page + 1)
        link = soup.select('.storylink')
        subtext = soup.select('.subtext')
        hn.extend(create_custom_hn(link, subtext))
    return hn


def main():
    web_url = 'https://news.ycombinator.com/news'
    compiled_hn = create_multipage_hn(web_url, 2)
    pprint(compiled_hn)
    return 0


if __name__ == "__main__":
    main()
