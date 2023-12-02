class Media:
    def __init__(self, id, title, genre, releaseYear, ageClassification):
        self.id = id
        self.title = title
        self.genre = genre
        self.releaseYear = releaseYear
        self.ageClassification = ageClassification

    def getAge(self):
        return self.ageClassification
    
    def getID(self):
        return self.id
    
    def getTitle(self):
        return self.title
    
class Serie(Media):
    def __init__(self, id, title, genre, releaseYear, ageClassification, seasons):
        super().__init__(id, title, genre, releaseYear, ageClassification)
        self.seasons = seasons

    def getInfos(self):
        infos = (f'{self.title}, Gênero: {self.genre}, Ano: {self.releaseYear}, Idade: +{self.ageClassification}, Temporadas: {self.seasons}')
        return infos

class Movie(Media):
    def __init__(self, id, title, genre, releaseYear, ageClassification, director, producer):
        super().__init__(id, title, genre, releaseYear, ageClassification)
        self.director = director
        self.producer = producer

    def getInfos(self):
        infos = (f'{self.title}, Gênero: {self.genre}, Ano: {self.releaseYear}, Idade: +{self.ageClassification}, Diretor: {self.director}, Produtor: {self.producer}')
        return infos

class Documentary(Media):
    def __init__(self, id, title, genre, releaseYear, ageClassification, theme):
        super().__init__(id, title, genre, releaseYear, ageClassification)
        self.theme = theme

    def getInfos(self):
        infos = (f'{self.title}, Gênero: {self.genre}, Ano: {self.releaseYear}, Idade: +{self.ageClassification}, Tema: {self.theme}')
        return infos

class Animation(Media):
    def __init__(self, id, title, genre, releaseYear, ageClassification, studio):
        super().__init__(id, title, genre, releaseYear, ageClassification)
        self.studio = studio

    def getInfos(self):
        infos = (f'{self.title}, Gênero: {self.genre}, Ano: {self.releaseYear}, Idade: +{self.ageClassification}, Estúdio: {self.studio}')
        return infos

class TVProgram(Media):
    def __init__(self, id, title, genre, releaseYear, ageClassification, episodesNumber):
        super().__init__(id, title, genre, releaseYear, ageClassification)
        self.episodesNumber = episodesNumber

    def getInfos(self):
        infos = (f'{self.title}, Gênero: {self.genre}, Ano: {self.releaseYear}, Idade: +{self.ageClassification}, Episódios: {self.episodesNumber}')
        return infos