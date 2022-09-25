class Chapter:
    def __init__(self, title, subtitle):
        self.title = title
        self.subtitle = subtitle

    def chap_org(self):
        print("The title: ",self.title, "and its subtitle: ", self.subtitle) 


class Book:
    def __init__(self, name, pageNum ,titles):
        self.name = name
        self.pageName = pageNum
        self.titles = titles

    def result(self):
        print(self.titles.chap_org())

chapter1 = Chapter('Genuis love', 'part1')
book1 = Book('revence', 512, chapter1)
book1.result()