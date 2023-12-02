from termcolor import colored
import functions

class User:
    def __init__(self, username, password, subscription, usersList):
        self.username = username
        self.password = password
        self.subscription = subscription
        self.usersList = usersList

    def getUsername(self):
        return self.username
    
    def getPassword(self):
        return self.password
    
    def getSubscription(self):
        return self.subscription
    
    def getUsersList(self):
        return self.usersList

    def removeProfile(self, name):
        self.usersList.remove(name)

    def removeProfileSub(self, subscription):
        if subscription == 'Nenhum':
            while len(self.usersList) > 1:
                self.usersList.pop(-1)
        if subscription == 'Simples':
            while len(self.usersList) > 3:
                self.usersList.pop(-1)
    
    def changePassword(self):
        newPass = input('Digite uma senha nova: ')
        self.password = newPass
        print(colored('Senha alterada com sucesso!', 'green'))
    
    def changeSubscription(self, newSub):
        self.subscription = newSub

    def addProfile(self, name):
        self.usersList.append(name)