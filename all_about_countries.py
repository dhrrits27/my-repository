class India():
    def capital(self):
        print("new delhi is the capital of india")

    def language(spread):
        print("hindi is the most widespread language of india")

    def type(self):
        print("india is a developing country")

class USA():
    def capital(self):
        print("washington is the capital of USA")

    def language(self):
        print("english is the most widespread language of USA")

    def type(self):
        print("USA is a developed country")

obj_ind=India()
obj_usa=USA()


for country in (obj_ind, obj_usa):
    country.capital()
    country.language()
    country.type()
