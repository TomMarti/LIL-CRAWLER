import requests

class Scraper:
    def __init__(self):
        self.name = "scraper"

    @staticmethod
    def scrape(url):
        r = None
        try:
            r = requests.get(url)
        except:
            return []
        if r.status_code == 200:
            return Scraper.parse(r.text)
        else:
            return []

    @staticmethod
    def parse(file):
        tofind = "href"
        filelenght = len(file) - 1
        res = [i for i in range(len(file)) if file.startswith(tofind, i)]
        newurls = []
        for element in res:
            ur = Scraper.get_url(file, element, filelenght)
            if len(ur) > 0 and ur[0] == "h":
                newurls.append(ur)
        return newurls

    @staticmethod
    def get_url(file, position, filelenght):
        url = ""
        stop = False
        i = 5 + position
        iplusun = ""
        while (not stop):
            url += iplusun
            try:
                iplusun = file[i + 1]
            except:
                return ""

            if iplusun != '"':
                i += 1
            else:
                stop = True
            if iplusun == '\'':
                stop = True
        return url
