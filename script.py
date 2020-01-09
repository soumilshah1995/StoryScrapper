__Author__ = "Soumil Nitin Shah"
__Version__ = "0.0.1"
__Email__ = "soushah@my.bridgeport.edu"
__Website__ = "https://soumilshah.herokuapp.com"

try:
    import requests
    from bs4 import BeautifulSoup
    import pandas as pd

except Exception as e:
    print("Some modules are Missing {}".format(e))


class Request(object):

    def __init__(self):
        self.url = 'https://www.short-story.me/'
        self.headers = {
            'Accept-Encoding': 'gzip, deflate, sdch',
            'Accept-Language': 'en-US,en;q=0.8',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Referer': 'http://www.wikipedia.org/',
            'Connection': 'keep-alive',}

    @property
    def get(self):
        try:
            r =requests.get(self.url, self.headers)
            return r.text
        except Exception as e:
            print("Failed to Make Response ")


class HashMap(object):
    def __init__(self):
        self.data = {
            'Title':[],
            'Image':[],
            'Links':[],
            'Summary':[]

        }


class Scrapper(object):

    def __init__(self):
        self.request = Request()
        self.hashmap = HashMap()

    def getJokes(self):


        soup = BeautifulSoup(self.request.get, 'html.parser')

        for x in  soup.findAll('div', class_="allmode-wrapper"):
            links = x.find('a')
            baseURL = 'https://www.short-story.me/'
            NewLinks = baseURL + links["href"]

            heading = x.find('h3', class_='allmode-title').text


            ImageURL = x.find('img')
            ImageUrlLinks =  baseURL + ImageURL["src"]

            summary = x.find('div', class_='allmode-text').text
            self.hashmap.data['Title'].append(heading)
            self.hashmap.data['Image'].append(ImageUrlLinks)
            self.hashmap.data['Links'].append(NewLinks)
            self.hashmap.data['Summary'].append(summary)

        df = pd.DataFrame(data=self.hashmap.data)
        return df


if __name__ == "__main__":
    obj = Scrapper()
    df = obj.getJokes()
    print(df)
