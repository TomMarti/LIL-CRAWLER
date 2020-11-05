from src.file.File import File
from src.parser.scraper import Scraper


class Crawler:
    def __init__(self):
        self.todo = File("./data/todo.txt")
        self.done = File("./data/done.txt")

    def crawl(self):
        while(True):
            if self.todo.is_empty():
                break
            print("Start new crawl")
            url = self.todo.pop()
            print("scrape url: {}".format(url))
            links = Scraper.scrape(url)
            print(links)
            for link in links:
                self.todo.add(link)
            self.done.add(url)
            print("save files")
            self.todo.save()
            self.done.save()