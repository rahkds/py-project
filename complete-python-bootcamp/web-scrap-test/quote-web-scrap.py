import requests
import bs4


base_url = "https://quotes.toscrape.com"


def getSoupRes(url):
    res = requests.get(url)
    soup = bs4.BeautifulSoup(res.text,"lxml")
    return soup

def getAuthors(url):
    author_set = set()
    soup = getSoupRes(url)
    authorSoup = soup.select('.quote')
    for elem in authorSoup:
        authorElem = elem.select('.author')
        if len(authorElem):
            author_set.add(authorElem[0].getText())
    return sorted(list(author_set))


def getQuotes(url):
    quotes = []
    soup = getSoupRes(url)
    authorSoup = soup.select('.quote .text')
    for elem in authorSoup:
        quotes.append(elem.getText())
    return quotes

def getTopTenTags(url):
    tags = []
    soup = getSoupRes(url)
    tagSoup = soup.select('.tag-item .tag')
    for elem in tagSoup:
        tags.append(elem.getText())
    return tags

def getAllAuthors():
    page_url = "https://quotes.toscrape.com/page/{page}/"
    counter = 1
    all_authors = []
    while True:
        url = page_url.format(page=counter)
        print(url)
        counter +=1
        authors = getAuthors(url)
        if len(authors):
            all_authors.extend(authors)
        else:
            break
    return set(all_authors)


print(getAllAuthors())
# print(getTopTenTags(base_url))
# print(getQuotes(base_url))
# print(getAuthors(base_url))