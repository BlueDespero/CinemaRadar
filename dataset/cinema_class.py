import procedures

class Cinema():

    def __init__(self, city, name, url, type):
        self.city = city
        self.name = name
        self.url = url
        self.type = type
        self.procedure = procedures.searches_by_type[str(self.type)]

    def search(self, driver, title, date = 0):
        return self.procedure(self, driver, title, date)
