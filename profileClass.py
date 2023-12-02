class Profile:
    def __init__(self, name, age, favorites, lastWatched, masterAccount, id):
        self.name = name
        self.age = age
        self.favorites = favorites
        self.lastWatched = lastWatched
        self.masterAccount = masterAccount
        self.id = id

    def addFavorite(self, media):
        if '' in self.favorites:
            self.favorites.remove('')

        self.favorites.insert(0, media)

    def removeFavorite(self, media):
        self.favorites.remove(media)
    
    def addLastWatched(self, media):
        if '' in self.lastWatched:
            self.lastWatched.remove('')

        if media in self.lastWatched:
            self.lastWatched.remove(media)

        if len(self.lastWatched) >= 3:
            self.lastWatched.insert(0, media)
            self.lastWatched.pop()
        else:
            self.lastWatched.insert(0, media)

    def removeLastWatched(self, media):
        self.lastWatched.remove(media)

    def getName(self):
        return self.name
    
    def getAge(self):
        return self.age
    
    def getFavorites(self):
        return self.favorites
    
    def getLastWatched(self):
        return self.lastWatched
    
    def getMasterAccount(self):
        return self.masterAccount
    
    def getID(self):
        return self.id