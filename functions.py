import hashlib
import time
from userClass import User
from tkinter import *
import customtkinter
import elements
import csv
from mediaClass import *
from profileClass import Profile

margin = 0

def hash(password):
    hash_obj = hashlib.sha256()
    hash_obj.update(password.encode('utf-8'))
    return hash_obj.hexdigest()

def loadDatabase():
    global users
    global profiles
    users = []
    profiles = []
    with open('database/users.csv', 'r', newline='') as csvFile:
        readerCsv = csv.DictReader(csvFile, delimiter=';')
        for row in readerCsv:
            name = row['name']
            password = row['password']
            subscription = row['subscription']
            usersListStr = row['usersList']
            usersList = [(x) for x in usersListStr.split(',')]
            user = User(name, password, subscription, usersList)
            users.append(user)
    csvFile.close()

    with open('database/profiles.csv', 'r', newline='') as csvFile:
        readerCsv = csv.DictReader(csvFile, delimiter=';')
        for row in readerCsv:
            name = row['name']
            age = row['age']
            favoritesStr = row['favorites']
            lastWatchedStr = row['lastWatched']
            favorites = [(x) for x in favoritesStr.split(',')]
            lastWatched = [(x) for x in lastWatchedStr.split(',')]
            masterAccount = row['masterAccount']
            id = row['id']
            profile = Profile(name, age, favorites, lastWatched, masterAccount, id)
            profiles.append(profile)
    csvFile.close()

def loadCatalog():
    global medias
    medias = []

    with open('database/catalog.csv', 'r', newline='', encoding='utf-8') as csvFile:
        readerCsv = csv.DictReader(csvFile, delimiter=';')

        for linha in readerCsv:
            mediaType = linha['type']
            del linha['type']
            instanceMedia = None

            if mediaType == 'Série':
                instanceMedia = Serie(id=linha['id'], title=linha['title'], genre=linha['genre'],
                                      releaseYear=linha['releaseYear'], ageClassification=linha['ageClassification'],
                                      seasons=linha['seasons'])
            elif mediaType == 'Filme':
                instanceMedia = Movie(id=linha['id'], title=linha['title'], genre=linha['genre'],
                                      releaseYear=linha['releaseYear'], ageClassification=linha['ageClassification'],
                                      director=linha.get('director', ''), producer=linha.get('producer', ''))
            elif mediaType == 'Documentário':
                instanceMedia = Documentary(id=linha['id'], title=linha['title'], genre=linha['genre'],
                                            releaseYear=linha['releaseYear'], ageClassification=linha['ageClassification'],
                                            theme=linha['theme'])
            elif mediaType == 'Animação':
                instanceMedia = Animation(id=linha['id'], title=linha['title'], genre=linha['genre'],
                                          releaseYear=linha['releaseYear'], ageClassification=linha['ageClassification'],
                                          studio=linha['studio'])
            elif mediaType == 'Programa de TV':
                instanceMedia = TVProgram(id=linha['id'], title=linha['title'], genre=linha['genre'],
                                          releaseYear=linha['releaseYear'], ageClassification=linha['ageClassification'],
                                          episodesNumber=linha['episodesNumber'])

            if instanceMedia:
                medias.append(instanceMedia)
 
def saveDatabase(users, profiles):
    with open('database/users.csv', 'w', newline='') as csvFile:
        keys = ['name', 'password', 'subscription', 'usersList']
        writerCsv = csv.DictWriter(csvFile, fieldnames=keys, delimiter=';')
        writerCsv.writeheader()
        for user in users:
            name = user.getUsername()
            password = user.getPassword()
            subscription = user.getSubscription()
            usersList = ','.join(str(profilec) for profilec in user.getUsersList())
            writerCsv.writerow({'name': name, 'password': password, 'subscription': subscription, 'usersList': usersList})
    csvFile.close()

    with open('database/profiles.csv', 'w', newline='') as csvFile:
        keys = ['name', 'age', 'favorites', 'lastWatched', 'masterAccount', 'id']
        writerCsv = csv.DictWriter(csvFile, fieldnames=keys, delimiter=';')
        writerCsv.writeheader()
        for profile in profiles:
            name = profile.getName()
            age = profile.getAge()
            favorites = ','.join(str(favorite) for favorite in profile.getFavorites())
            lastWatched = ','.join(str(media) for media in profile.getLastWatched())
            masterAccount = profile.getMasterAccount()
            id = profile.getID()
            writerCsv.writerow({'name': name, 'age': age, 'favorites': favorites, 'lastWatched': lastWatched, 'masterAccount': masterAccount, 'id': id})
    csvFile.close()

def linesCSV():
    with open('database/profiles.csv', 'r') as csvFile:
        readerCsv = csv.reader(csvFile)
        linesNumber = len(list(readerCsv))
    return linesNumber

def createUser():
    lines = linesCSV()
    user = elements.userEntry.get()
    password = elements.passwordEntry.get()
    passVerify = elements.repeatPasswordEntry.get()
    if user == '':
        elements.dynamicText.configure(text='Escolha um nome de usuário!', text_color=elements.color_red)
        elements.dynamicText.place(relx=0.5, rely=0.82+margin, anchor=CENTER)
    elif password == '':
        elements.dynamicText.configure(text='Escolha uma senha!', text_color=elements.color_red)
        elements.dynamicText.place(relx=0.5, rely=0.82+margin, anchor=CENTER)
    elif password != passVerify:
        elements.dynamicText.configure(text='As senhas não coincidem!', text_color=elements.color_red)
        elements.dynamicText.place(relx=0.5, rely=0.82+margin, anchor=CENTER)
    elif verifyIfUserExists(user):
        elements.dynamicText.configure(text='Usuário já existe no sistema!', text_color=elements.color_red)
        elements.dynamicText.place(relx=0.5, rely=0.82+margin, anchor=CENTER)
    else:
        hashed = hash(password)
        newUser = User(user, hashed, 'Nenhum', [user])
        loadDatabase()
        users.append(newUser)
        profile = Profile(user, 999, [], [], user, lines)
        profiles.append(profile)
        saveDatabase(users, profiles)

        elements.dynamicText.configure(text='Usuário criado com sucesso!', text_color='mediumseagreen')
        elements.dynamicText.place(relx=0.5, rely=0.82+margin, anchor=CENTER)
        time.sleep(1)
        elements.dynamicText.configure(text='Retornando à tela de login...', text_color='royalblue')
        elements.dynamicText.place(relx=0.5, rely=0.82+margin, anchor=CENTER)
        time.sleep(1)
        homeScreen()

def verifyIfUserExists(user):
    with open('database/users.csv', 'r', newline='') as csvFile:
        readerCsv = csv.reader(csvFile, delimiter=';')
        for row in readerCsv:
            if row[0] == user:
                return True
    csvFile.close()
    return False

def login():
    global sessionUser
    def verifyLogin(user, hash):
        with open('database/users.csv', 'r', newline='') as csvFile:
            readerCsv = csv.reader(csvFile, delimiter=';')
            for row in readerCsv: 
                if row[0] == user and row[1] == hash:
                    return True
        csvFile.close()
        return False
    user = elements.userEntry.get()
    password = elements.passwordEntry.get()
    hashed = hash(password)
    elements.dynamicText.configure(text='Verificando o Login...', text_color='royalblue')
    elements.dynamicText.place(relx=0.5, rely=0.74+margin, anchor=CENTER)
    time.sleep(1)
    if verifyLogin(user, hashed):
        elements.dynamicText.configure(text='Login efetuado com sucesso!', text_color='mediumseagreen')
        time.sleep(1)
        loadDatabase()
        for i in range(len(users)):
            if users[i].getUsername() == user:
                sessionUser = users[i]
                connectedInterface()

    else:
        elements.dynamicText.configure(text='Credenciais inválidas!', text_color=elements.color_red)

def chooseTheme():
    theme = elements.switchTheme.get()
    if theme == 1:
        customtkinter.set_appearance_mode('light')
    else:
        customtkinter.set_appearance_mode('dark')

def homeScreen():
    clearhomeScreen()
    loadCatalog()

    elements.uniflixImageLabel.place(relx=0.5, rely=0.1+margin, anchor=CENTER)
    elements.user.place(relx=0.335, rely=0.24+margin, anchor=CENTER)
    elements.userEntry.place(relx=0.5, rely=0.3+margin, anchor=CENTER)
    elements.password.place(relx=0.335, rely=0.4+margin, anchor=CENTER)
    elements.passwordEntry.place(relx=0.5, rely=0.46+margin, anchor=CENTER)
    elements.buttonLogin.place(relx=0.6, rely=0.6+margin, anchor=CENTER)
    elements.buttonCreateAccountInterface.place(relx=0.4, rely=0.6+margin, anchor=CENTER)

    elements.switchTheme.place(relx=0.05, rely=0.9)
    elements.switchImageLabel.place(relx=0.12, rely=0.9)
    elements.credits.place(relx=0.65, rely=0.9)

def clearhomeScreen():
    elements.uniflixImageLabel.place_forget()
    elements.user.place_forget()
    elements.userEntry.place_forget()
    elements.password.place_forget()
    elements.passwordEntry.place_forget()
    elements.buttonLogin.place_forget()
    elements.buttonCreateAccountInterface.place_forget()
    elements.switchTheme.place_forget()
    elements.switchImageLabel.place_forget()
    elements.credits.place_forget()
    elements.repeatPassword.place_forget()
    elements.repeatPasswordEntry.place_forget()
    elements.buttonBackLogin.place_forget()
    elements.buttonCreateUser.place_forget()
    elements.dynamicText.place_forget()

def createUserInterface():
    clearhomeScreen()
    elements.uniflixImageLabel.place(relx=0.5, rely=0.1+margin, anchor=CENTER)
    elements.user.place(relx=0.335, rely=0.24+margin, anchor=CENTER)
    elements.userEntry.place(relx=0.5, rely=0.3+margin, anchor=CENTER)
    elements.password.place(relx=0.335, rely=0.4+margin, anchor=CENTER)
    elements.passwordEntry.place(relx=0.5, rely=0.46+margin, anchor=CENTER)
    elements.repeatPassword.place(relx=0.36, rely=0.56+margin, anchor=CENTER)
    elements.repeatPasswordEntry.place(relx=0.5, rely=0.62+margin, anchor=CENTER)
    elements.buttonCreateUser.place(relx=0.6, rely=0.72+margin, anchor=CENTER)
    elements.buttonBackLogin.place(relx=0.4, rely=0.72+margin, anchor=CENTER)

    elements.switchTheme.place(relx=0.05, rely=0.9)
    elements.switchImageLabel.place(relx=0.12, rely=0.9)
    elements.credits.place(relx=0.65, rely=0.9)

def clearConnectedInterface():
    elements.welcome.place_forget()
    elements.subscription.place_forget()
    elements.buttonChangeSubscription.place_forget()
    elements.buttonLogout.place_forget()
    elements.buttonConfirm.place_forget()
    elements.subscription.place_forget()
    elements.buttonBackConnected.place_forget()
    elements.checkNenhum.place_forget()
    elements.checkSimples.place_forget()
    elements.checkPremium.place_forget()
    elements.passwordSubscription.place_forget()
    elements.profile1Button.place_forget()
    elements.profile2Button.place_forget()
    elements.profile3Button.place_forget()
    elements.profile4Button.place_forget()
    elements.profile5Button.place_forget()
    elements.nameProfile1.place_forget()
    elements.nameProfile2.place_forget()
    elements.nameProfile3.place_forget()
    elements.nameProfile4.place_forget()
    elements.nameProfile5.place_forget()
    elements.manageProfilesButton.place_forget()
    elements.nameEntry.place_forget()
    elements.ageEntry.place_forget()
    elements.addProfileButton.place_forget()
    elements.buttonBackProfiles.place_forget()
    elements.removeProfileEntry.place_forget()
    elements.buttonRemoveProfile.place_forget()
    elements.mediaButton0.place_forget()
    elements.mediaButton2.place_forget()
    elements.mediaButton1.place_forget()
    elements.mediaButton3.place_forget()
    elements.mediaButton4.place_forget()
    elements.mediaButton5.place_forget()
    elements.mediaLabel0.place_forget()
    elements.mediaLabel1.place_forget()
    elements.mediaLabel2.place_forget()
    elements.mediaLabel3.place_forget()
    elements.mediaLabel4.place_forget()
    elements.mediaLabel5.place_forget()
    elements.infosLabel.place_forget()
    elements.progressBar.place_forget()
    elements.playButton.place_forget()
    elements.buttonBackMedias.place_forget()
    elements.stopButton.place_forget()
    elements.favoriteTrueButton.place_forget()
    elements.favoriteFalseButton.place_forget()
    elements.lastWatchedButton.place_forget()
    elements.favoritesButton.place_forget()
    elements.allMediasButton.place_forget()
    elements.dynamicText.place_forget()
    elements.searchButton.place_forget()
    elements.searchEntry.place_forget()

def connectedInterface():
    clearConnectedInterface()
    clearhomeScreen()
    showProfiles()
    username = sessionUser.getUsername()
    subscription = sessionUser.getSubscription()

    elements.welcome.configure(text=(f'Olá, {username}!'))
    elements.welcome.place(relx=0.5, rely=0.1+margin, anchor=CENTER)

    if subscription == 'Nenhum':
        color = 'lightcyan3'
    elif subscription == 'Premium':
        color = 'lightgoldenrod1'
    else:
        color = 'cornflowerblue'

    elements.subscription.configure(text=(f'Plano atual: {subscription}'), fg_color=color, corner_radius=50)
    elements.subscription.place(relx=0.9, rely=0.84+margin, anchor=CENTER)
    elements.buttonChangeSubscription.place(relx=0.9, rely=0.9+margin, anchor=CENTER)
    elements.switchTheme.place(relx=0.05, rely=0.9)
    elements.switchImageLabel.place(relx=0.12, rely=0.9)
    elements.buttonLogout.place(relx=0.5, rely=0.9, anchor=CENTER)
    elements.manageProfilesButton.place(relx=0.5, rely=0.6, anchor=CENTER)

def changeSubscriptionInterface():
    clearConnectedInterface()
    elements.subscription.place(relx=0.5, rely=0.1+margin, anchor=CENTER)
    elements.checkNenhum.place(relx=0.492, rely=0.2+margin, anchor=CENTER)
    elements.checkSimples.place(relx=0.4833, rely=0.3+margin, anchor=CENTER)
    elements.checkPremium.place(relx=0.505, rely=0.4+margin, anchor=CENTER)
    elements.buttonConfirm.place(relx=0.6, rely=0.7, anchor=CENTER)
    elements.buttonBackConnected.place(relx=0.4, rely=0.7, anchor=CENTER)
    elements.passwordSubscription.place(relx=0.5, rely=0.5, anchor=CENTER)

def confirmSubscription():
    def getRad():
        nenhum = elements.nenhumVar.get()
        simples = elements.simplesVar.get()
        premium = elements.premiumVar.get()
        return nenhum,simples,premium
    nenhum,simples,premium = getRad()
    profilesSize = len(sessionUser.getUsersList())

    password = elements.passwordSubscription.get()
    hashed = hash(password)
    if sessionUser.getPassword() == hashed:
        if nenhum == '1' and simples != '1' and premium != '1':
            elements.dynamicText.configure(text='Plano alterado para: Nenhum', text_color='mediumseagreen')
            elements.dynamicText.place(relx=0.5, rely=0.6+margin, anchor=CENTER)
            sessionUser.changeSubscription('Nenhum')
            elements.subscription.configure(text='Plano atual: Nenhum', fg_color='lightcyan3')
            elements.subscription.place(relx=0.5, rely=0.1+margin, anchor=CENTER)
            if profilesSize > 1:
                sessionUser.removeProfileSub('Nenhum')
        elif simples == '1' and nenhum != '1' and premium != '1':
            elements.dynamicText.configure(text='Plano alterado para: Simples', text_color='mediumseagreen')
            elements.dynamicText.place(relx=0.5, rely=0.6+margin, anchor=CENTER)
            sessionUser.changeSubscription('Simples')
            elements.subscription.configure(text='Plano atual: Simples', fg_color='cornflowerblue')
            elements.subscription.place(relx=0.5, rely=0.1+margin, anchor=CENTER)
            if profilesSize > 3:
                sessionUser.removeProfileSub('Simples')
        elif premium == '1' and nenhum != '1' and simples != '1':
            elements.dynamicText.configure(text='Plano alterado para: Premium', text_color='mediumseagreen')
            elements.dynamicText.place(relx=0.5, rely=0.6+margin, anchor=CENTER)
            sessionUser.changeSubscription('Premium')
            elements.subscription.configure(text='Plano atual: Premium', fg_color='lightgoldenrod1')
            elements.subscription.place(relx=0.5, rely=0.1+margin, anchor=CENTER)
        else:
            elements.dynamicText.configure(text='Escolha apenas um plano', text_color=elements.color_red)
            elements.dynamicText.place(relx=0.5, rely=0.6+margin, anchor=CENTER)
    else:
        elements.dynamicText.configure(text='Senha incorreta', text_color=elements.color_red)
        elements.dynamicText.place(relx=0.5, rely=0.6+margin, anchor=CENTER)
    elements.checkNenhum.deselect()
    elements.checkSimples.deselect()
    elements.checkPremium.deselect()
    saveDatabase(users, profiles)

def logout():
    clearConnectedInterface()
    homeScreen()

def showProfiles():
    usersList = sessionUser.getUsersList()
    profileNumber = len(usersList)
    subscription = sessionUser.getSubscription()
    if profileNumber > 3 and subscription == 'Simples' or subscription == 'Nenhum':
        pass
    if profileNumber == 1:
        elements.profile1Button.place(relx=0.5, rely=0.4, anchor=CENTER)
        elements.nameProfile1.configure(text=usersList[0])
        elements.nameProfile1.place(relx=0.5, rely=0.5, anchor=CENTER)
    if profileNumber == 2:
        elements.profile1Button.place(relx=0.45, rely=0.4, anchor=CENTER)
        elements.nameProfile1.configure(text=usersList[0])
        elements.nameProfile1.place(relx=0.45, rely=0.5, anchor=CENTER)

        elements.profile2Button.place(relx=0.55, rely=0.4, anchor=CENTER)
        elements.nameProfile2.configure(text=usersList[1])
        elements.nameProfile2.place(relx=0.55, rely=0.5, anchor=CENTER)
    if profileNumber == 3:
        elements.profile1Button.place(relx=0.4, rely=0.4, anchor=CENTER)
        elements.nameProfile1.configure(text=usersList[0])
        elements.nameProfile1.place(relx=0.4, rely=0.5, anchor=CENTER)

        elements.profile2Button.place(relx=0.5, rely=0.4, anchor=CENTER)
        elements.nameProfile2.configure(text=usersList[1])
        elements.nameProfile2.place(relx=0.5, rely=0.5, anchor=CENTER)

        elements.profile3Button.place(relx=0.6, rely=0.4, anchor=CENTER)
        elements.nameProfile3.configure(text=usersList[2])
        elements.nameProfile3.place(relx=0.6, rely=0.5, anchor=CENTER)
    if profileNumber == 4:
        elements.profile1Button.place(relx=0.35, rely=0.4, anchor=CENTER)
        elements.nameProfile1.configure(text=usersList[0])
        elements.nameProfile1.place(relx=0.35, rely=0.5, anchor=CENTER)

        elements.profile2Button.place(relx=0.45, rely=0.4, anchor=CENTER)
        elements.nameProfile2.configure(text=usersList[1])
        elements.nameProfile2.place(relx=0.45, rely=0.5, anchor=CENTER)

        elements.profile3Button.place(relx=0.55, rely=0.4, anchor=CENTER)
        elements.nameProfile3.configure(text=usersList[2])
        elements.nameProfile3.place(relx=0.55, rely=0.5, anchor=CENTER)

        elements.profile4Button.place(relx=0.65, rely=0.4, anchor=CENTER)
        elements.nameProfile4.configure(text=usersList[3])
        elements.nameProfile4.place(relx=0.65, rely=0.5, anchor=CENTER)
    if profileNumber == 5:
        elements.profile1Button.place(relx=0.3, rely=0.4, anchor=CENTER)
        elements.nameProfile1.configure(text=usersList[0])
        elements.nameProfile1.place(relx=0.3, rely=0.5, anchor=CENTER)

        elements.profile2Button.place(relx=0.4, rely=0.4, anchor=CENTER)
        elements.nameProfile2.configure(text=usersList[1])
        elements.nameProfile2.place(relx=0.4, rely=0.5, anchor=CENTER)

        elements.profile3Button.place(relx=0.5, rely=0.4, anchor=CENTER)
        elements.nameProfile3.configure(text=usersList[2])
        elements.nameProfile3.place(relx=0.5, rely=0.5, anchor=CENTER)

        elements.profile4Button.place(relx=0.6, rely=0.4, anchor=CENTER)
        elements.nameProfile4.configure(text=usersList[3])
        elements.nameProfile4.place(relx=0.6, rely=0.5, anchor=CENTER)

        elements.profile5Button.place(relx=0.7, rely=0.4, anchor=CENTER)
        elements.nameProfile5.configure(text=usersList[4])
        elements.nameProfile5.place(relx=0.7, rely=0.5, anchor=CENTER)

def manageProfilesInterface():
    clearConnectedInterface()
    showProfiles()
    elements.removeProfileEntry.place(relx=0.5, rely=0.2, anchor=CENTER)
    elements.buttonRemoveProfile.place(relx=0.5, rely=0.25, anchor=CENTER)
    elements.nameEntry.place(relx=0.5, rely=0.6, anchor=CENTER)
    elements.ageEntry.place(relx=0.5, rely=0.65, anchor=CENTER)
    elements.addProfileButton.place(relx=0.5, rely=0.7, anchor=CENTER)
    elements.buttonBackProfiles.place(relx=0.9, rely=0.9, anchor=CENTER)

def manageProfiles():
    manageProfilesInterface()

def addProfile():
    id = linesCSV()
    name = elements.nameEntry.get()
    age = elements.ageEntry.get()
    usersList = sessionUser.getUsersList()
    profileNumber = len(usersList)
    if not age.isdigit():
        elements.dynamicText.configure(text='Insira uma idade válida', text_color=elements.color_red)
        elements.dynamicText.place(relx=0.5, rely=0.9, anchor=CENTER)
    elif sessionUser.getSubscription() == 'Nenhum':
        elements.dynamicText.configure(text='Seu plano não permite adicionar usuários.', text_color=elements.color_red)
        elements.dynamicText.place(relx=0.5, rely=0.9, anchor=CENTER)
    elif sessionUser.getSubscription() == 'Simples' and profileNumber >= 3:
        elements.dynamicText.configure(text='Seu plano não permite adicionar mais usuários.', text_color=elements.color_red)
        elements.dynamicText.place(relx=0.5, rely=0.9, anchor=CENTER)
    elif sessionUser.getSubscription() == 'Premium' and profileNumber >= 5:
        elements.dynamicText.configure(text='Seu plano não permite adicionar mais usuários.', text_color=elements.color_red)
        elements.dynamicText.place(relx=0.5, rely=0.9, anchor=CENTER)
    elif name in usersList:
        elements.dynamicText.configure(text='Nome de perfil já existe.', text_color=elements.color_red)
        elements.dynamicText.place(relx=0.5, rely=0.9, anchor=CENTER)
    else:
        sessionUser.addProfile(name)
        manageProfilesInterface()
        profile = Profile(name, age, [],[], sessionUser.getUsername(), id)
        profiles.append(profile)
        saveDatabase(users, profiles)
        elements.dynamicText.configure(text='Perfil adicionado com sucesso!', text_color='mediumseagreen')
        elements.dynamicText.place(relx=0.5, rely=0.9, anchor=CENTER)

def removeProfile():
    profile = elements.removeProfileEntry.get()
    profilesList = sessionUser.getUsersList()
    if profile in profilesList:
        sessionUser.removeProfile(profile)
        elements.dynamicText.configure(text='Perfil Removido com sucesso', text_color='mediumseagreen')
        elements.dynamicText.place(relx=0.5, rely=0.9, anchor=CENTER)
        manageProfilesInterface()
        saveDatabase(users, profiles)
    else:
        elements.dynamicText.configure(text='Perfil não existe', text_color=elements.color_red)
        elements.dynamicText.place(relx=0.5, rely=0.9, anchor=CENTER)

def selectProfile(number):
    global sessionProfile
    masterAccount = sessionUser.getUsername()
    list = sessionUser.getUsersList()
    profile = list[number-1]
    with open('database/profiles.csv', 'r', newline='') as csvFile:
        csvReader = csv.DictReader(csvFile, delimiter=';')

        for row in csvReader:
            if 'name' in row and 'masterAccount' in row and row['name'] == profile and row['masterAccount'] == masterAccount:
                id = row['id']
                break
 
    csvFile.close()
    sessionProfile = profiles[int(id)-1]
    profileInterface()

def showMedias(profileMedias):
    IDs = []
    localPlace = 0.2
    vertical = 0.4
    counter = 0

    mediasButtons = [
        elements.mediaButton0,
        elements.mediaButton1,
        elements.mediaButton2,
        elements.mediaButton3,
        elements.mediaButton4,
        elements.mediaButton5
    ]

    for media in profileMedias:
        idStr = media.getID()
        id = int(idStr)
        IDs.append(id)
    
    for id in IDs:
        mediasButtons[id].place(relx=localPlace, rely=vertical, ancho=CENTER)
        localPlace += 0.3
        if localPlace > 0.8:
            localPlace = 0.2
            vertical = 0.7
        counter += 1
        if counter == len(profileMedias):
            break

def profileInterface():
    clearConnectedInterface()
    name = sessionProfile.getName()
    elements.welcome.configure(text=(f'Olá, {name}!'))
    elements.buttonBackConnected.place(relx=0.88, rely=0.92, anchor=CENTER)
    elements.welcome.place(relx=0.5, rely=0.1+margin, anchor=CENTER)
    elements.lastWatchedButton.place(relx=0.48, rely=0.92, anchor=CENTER)
    elements.favoritesButton.place(relx=0.68, rely=0.92, anchor=CENTER)
    elements.allMediasButton.place(relx=0.28, rely=0.92, anchor=CENTER)
    elements.searchButton.place(relx=0.085, rely=0.2, anchor=CENTER)
    elements.searchEntry.place(relx=0.27, rely=0.2, anchor=CENTER)

    profileMedias = []
    for x in medias:
        profileAgeStr = sessionProfile.getAge()
        ageStr = x.getAge()
        profileAge = int(profileAgeStr)
        age = int(ageStr)
        if profileAge >= age:
            profileMedias.append(x)

    showMedias(profileMedias)

def stop():
    elements.playButton.place(relx=0.5, rely=0.71, anchor=CENTER)
    elements.progressBar.stop()
    elements.stopButton.place_forget()

def closeAd():
    elements.adLabel.place_forget()
    elements.closeButton.place_forget()

def play():
    adCounter = 0.2

    subscription = sessionUser.getSubscription()
    if subscription == 'Simples':
        watch = True
        ad = True
    elif subscription =='Premium':
        watch = True
        ad = False
    else:
        watch = False
        ad = True

    if ad == True and watch == True:
        elements.progressBar.start()
        elements.playButton.place_forget()
        elements.stopButton.place(relx=0.5, rely=0.71, anchor=CENTER)
        setLastWatched()
        while adCounter < 0.3:
            time.sleep(0.5)
            mediaProgress = elements.progressBar.get()
            if mediaProgress >= adCounter:
                adCounter += 1
                elements.adLabel.place(relx=0.5, rely=0.5, anchor=CENTER)
                elements.closeButton.place(relx=0.8, rely=0.5, anchor=CENTER)
                
    elif ad == False and watch == True:
        elements.progressBar.start()
        elements.playButton.place_forget()
        elements.stopButton.place(relx=0.5, rely=0.71, anchor=CENTER)
        setLastWatched()
    else:
        elements.dynamicText.configure(text='Seu plano não permite visualizar mídias', text_color=elements.color_red)
        elements.dynamicText.place(relx=0.5, rely=0.8, anchor=CENTER)

def mediaInterface(id):
    global mediaSelected
    mediaSelected = medias[id].getTitle()

    clearConnectedInterface()
    mediasLabels = [
        elements.mediaLabel0,
        elements.mediaLabel1,
        elements.mediaLabel2,
        elements.mediaLabel3,
        elements.mediaLabel4,
        elements.mediaLabel5
    ]
    mediasLabels[id].place(relx=0.5, rely=0.3, anchor=CENTER)
    elements.buttonBackMedias.place(relx=0.9, rely=0.9, anchor=CENTER)

    infos = medias[id].getInfos()
    elements.infosLabel.configure(text=infos)
    elements.infosLabel.place(relx=0.5, rely=0.85, anchor=CENTER)
    elements.playButton.place(relx=0.5, rely=0.71, anchor=CENTER)
    elements.progressBar.set(0)
    elements.progressBar.place(relx=0.5, rely=0.6, anchor=CENTER)
    
    favorites = sessionProfile.getFavorites()
    if mediaSelected not in favorites:
        elements.favoriteFalseButton.place(relx=0.6, rely=0.71, anchor=CENTER)
    else:
        elements.favoriteTrueButton.place(relx=0.6, rely=0.71, anchor=CENTER)

def favorite():
    sessionProfile.addFavorite(mediaSelected)

    elements.favoriteFalseButton.place_forget()
    elements.favoriteTrueButton.place(relx=0.6, rely=0.71, anchor=CENTER)
    saveDatabase(users, profiles)

def unfavorite():
    sessionProfile.removeFavorite(mediaSelected)

    elements.favoriteTrueButton.place_forget()
    elements.favoriteFalseButton.place(relx=0.6, rely=0.71, anchor=CENTER)
    saveDatabase(users, profiles)

def setLastWatched():
    sessionProfile.addLastWatched(mediaSelected)
    saveDatabase(users, profiles)

def clearMedias():
    elements.mediaButton0.place_forget()
    elements.mediaButton1.place_forget()
    elements.mediaButton2.place_forget()
    elements.mediaButton3.place_forget()
    elements.mediaButton4.place_forget()
    elements.mediaButton5.place_forget()
    elements.dynamicText.place_forget()

def setMedias(type):
    clearMedias()
    if type == 'lastWatched':
        titles = sessionProfile.getLastWatched()
    elif type == 'favorites':
        titles = sessionProfile.getFavorites()
    elif type == 'search':
        titles = [elements.searchEntry.get()]
    Objects = []
    counterType = 0
    counterMedias = 0
    while len(Objects) != len(titles) and '' not in titles:
        if medias[counterMedias].getTitle() == titles[counterType]:
            Objects.append(medias[counterMedias])
            counterType += 1
            counterMedias = -1
        if counterMedias+1 == len(medias):
            elements.dynamicText.configure(text='Não foi encontrada nenhuma mídia com este título.', text_color=elements.color_red)
            elements.dynamicText.place(relx=0.62, rely=0.2, anchor=CENTER)
            break
        counterMedias += 1

    showMedias(Objects)

def lastWatchedInterface():
    clearMedias()
    setMedias('lastWatched')

def favoritesInterface():
    clearMedias()
    setMedias('favorites')

def searchInterface():
    clearMedias()
    setMedias('search')
