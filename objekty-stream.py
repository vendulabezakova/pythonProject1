class Item:
    def __init__(self, name, genre):
        self.name = name
        self.genre = genre

    def getInfo(self):
        return f"{self.name} je žánr {self.genre}. "

class Movie(Item):
    def getCelkovaDelka(self):
        return self.delka


    def __init__(self, name, genre, length):
        self.name = name
        self.genre = genre
        self.length = length

    def getInfo(self):
        text = super().getInfo()
        text = text + f"{self.name} trvá {self.length} minut."
        return text

class Serial(Item):
    def getCelkovaDelka(self):
        return self.delka

    def __init__(self, name, genre, episodeNum, episodeLength):
        self.name = name
        self.genre = genre
        self.episodeNum = episodeNum
        self.episodeLength = episodeLength

    def getInfo(self):
        text = super().getInfo()
        text = text + f"Seriál má {self.episodeNum} dílů. Jedna epizoda trvá {self.episodeLength} minut."
        return text



biglebowski = Movie("Big Lebowski", "komedie", 120)
biglebowski.name = "Big Lebowski"
biglebowski.genre = "komedie"
biglebowski.length = 120

bojackhorseman = Serial("Bojack Horseman", "animovaná komedie", 120, 25)
bojackhorseman.name = "Bojack Horseman"
bojackhorseman.genre = "animovaná komedie"
bojackhorseman.episodeNum = 120
bojackhorseman.episodeLength = 20

print(biglebowski.getInfo())
print(bojackhorseman.getInfo())