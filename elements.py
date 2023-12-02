from tkinter import *
import customtkinter
from PIL import Image
import threading

def command_chooseTheme():
    from functions import chooseTheme
    chooseTheme()

def command_login():
    from functions import login
    t1 = threading.Thread(target=login)
    t1.start()

def command_create_user():
    from functions import createUser
    t1 = threading.Thread(target=createUser)
    t1.start()

def command_create_user_interface():
    from functions import createUserInterface
    createUserInterface()

def command_back_login():
    from functions import homeScreen
    homeScreen()

def command_logout():
    from functions import logout
    logout()

def command_change_sub():
    from functions import changeSubscriptionInterface
    changeSubscriptionInterface()

def command_back_connected():
    from functions import connectedInterface
    connectedInterface()

def command_confirm():
    from functions import confirmSubscription
    confirmSubscription()

def command_manage_profile():
    from functions import manageProfiles
    manageProfiles()

def command_add_profile():
    from functions import addProfile
    addProfile()

def command_remove_profile():
    from functions import removeProfile
    removeProfile()

def command_back_medias():
    from functions import profileInterface
    profileInterface()

def play():
    from functions import play
    t1 = threading.Thread(target=play)
    t1.start()

def stop():
    from functions import stop
    stop()

def selectFavorite():
    from functions import favorite
    favorite()

def deselectFavorite():
    from functions import unfavorite
    unfavorite()

def command_last_watched():
    from functions import lastWatchedInterface
    lastWatchedInterface()

def command_favorites():
    from functions import favoritesInterface
    favoritesInterface()

def command_all_medias():
    from functions import profileInterface
    profileInterface()

def command_search():
    from functions import searchInterface
    searchInterface()

def command_close_ad():
    from functions import closeAd
    closeAd()

def button1():
    from functions import selectProfile
    selectProfile(1)
def button2():
    from functions import selectProfile
    selectProfile(2)
def button3():
    from functions import selectProfile
    selectProfile(3)
def button4():
    from functions import selectProfile
    selectProfile(4)
def button5():
    from functions import selectProfile
    selectProfile(5)


customtkinter.set_appearance_mode('dark')
root = customtkinter.CTk()
root.geometry('1280x720+300+170') #ALTERAR AQUI TAMANHO DA JANELA E POSIÇÃO // Largura x Altura x Horizontal x Vertical
#root.attributes('-topmost', True)
root.iconbitmap('graphicElements/icon.ico')
root.title('UNIFLIX')

    #Cores
color_red = '#d8141c'
color_red_dark = '#a20c12'
color_background = '#282424'

    #Fontes
fonteMinuscula = customtkinter.CTkFont('Montserrat', size=12, weight="bold")
fontePequena = customtkinter.CTkFont('Montserrat', size=13, weight="bold")
fonteMedia = customtkinter.CTkFont('Montserrat', size=14, weight="bold")
fonteGrande = customtkinter.CTkFont('Montserrat', size=15, weight="bold")
fonteGigante = customtkinter.CTkFont('Montserrat', size=17, weight="bold")
fontePropaganda=customtkinter.CTkFont('Montserrat', size=23, weight="bold")

    #Logo Uniflix
uniflixImage = customtkinter.CTkImage(dark_image=Image.open('graphicElements/Uniflixv6.png'),
                                      light_image=Image.open('graphicElements/Uniflixv6.png'),
                                      size=(320, 102))
uniflixImageLabel = customtkinter.CTkLabel(master=root, text=None, image=uniflixImage)

    #Botão Switch do tema
switchTheme = customtkinter.CTkSwitch(master=root,
                                      text='',
                                      command=command_chooseTheme,
                                      border_color='',
                                      border_width=0,
                                      switch_width=65,
                                      switch_height=30,
                                      progress_color='red')

switchImage = customtkinter.CTkImage(dark_image=Image.open('graphicElements/light.png'),
                                         light_image=Image.open('graphicElements/dark.png'),
                                         size=(30,30))
switchImageLabel = customtkinter.CTkLabel(master=root, text=None, image=switchImage)

    #Créditos
credits = customtkinter.CTkLabel(master=root,
                                 font=fonteGrande,
                                 text='Desenvolvido por: Felipe Torres e Pedro Webber',
                                 corner_radius=9)

    #Login
user = customtkinter.CTkLabel(master=root, font=fonteGigante, text='Usuário:')
userEntry = customtkinter.CTkEntry(master=root,width=500, height=40, corner_radius=30, font=fonteMedia)

password = customtkinter.CTkLabel(master=root, font=fonteGigante, text='Senha:')
passwordEntry = customtkinter.CTkEntry(master=root,width=500, height=40, corner_radius=30, show='*', font=fonteMedia)

buttonLogin = customtkinter.CTkButton(master=root,
                                      text='Entrar',
                                      width=240,
                                      height=40,
                                      fg_color=color_red,
                                      corner_radius=30,
                                      font=fonteGigante,
                                      hover_color=color_red_dark,
                                      command=command_login)

buttonCreateAccountInterface = customtkinter.CTkButton(master=root,
                                              text='Criar conta',
                                              width=240, height=40,
                                              fg_color='grey30',
                                              corner_radius=30,
                                              font=fonteGigante,
                                              hover_color='grey20',
                                              command=command_create_user_interface)
repeatPassword = customtkinter.CTkLabel(master=root, font=fonteGigante, text='Repita a senha:')
repeatPasswordEntry = customtkinter.CTkEntry(master=root,width=500, height=40, corner_radius=30, font=fonteMedia, show='*')

    #Texto dinâmico
dynamicText = customtkinter.CTkLabel(master=root, font=fonteGigante)

#Botão que de fato cria a conta do usuário
buttonCreateUser = customtkinter.CTkButton(master=root,
                                      text='Criar conta',
                                      width=240,
                                      height=40,
                                      fg_color=color_red,
                                      corner_radius=30,
                                      font=fonteGigante,
                                      hover_color=color_red_dark,
                                      command=command_create_user)

buttonBackLogin = customtkinter.CTkButton(master=root,
                                      text='Fazer Login',
                                      width=240,
                                      height=40,
                                      fg_color='grey30',
                                      corner_radius=30,
                                      font=fonteGigante,
                                      hover_color='grey20',
                                      command=command_back_login)

    #ELEMENTOS LOGADO
welcome = customtkinter.CTkLabel(master=root, font=fonteGigante)
subscription = customtkinter.CTkLabel(master=root, font=fonteGigante, width = 200, text_color='black')
buttonChangeSubscription = customtkinter.CTkButton(master=root,
                                      text='Alterar Plano',
                                      width=200,
                                      height=40,
                                      fg_color='grey30',
                                      corner_radius=30,
                                      font=fonteGigante,
                                      hover_color='grey20',
                                      command=command_change_sub)



buttonLogout = customtkinter.CTkButton(master=root,
                                      text='Sair',
                                      width=200,
                                      height=40,
                                      fg_color='grey30',
                                      corner_radius=30,
                                      font=fonteGigante,
                                      hover_color='grey20',
                                      command=command_logout)

buttonConfirm = customtkinter.CTkButton(master=root,
                                      text='Confirmar escolha',
                                      width=200,
                                      height=40,
                                      fg_color=color_red,
                                      corner_radius=30,
                                      font=fonteGigante,
                                      hover_color=color_red_dark,
                                      command=command_confirm)

buttonBackConnected = customtkinter.CTkButton(master=root,
                                      text='Voltar',
                                      width=200,
                                      height=40,
                                      fg_color='grey30',
                                      corner_radius=30,
                                      font=fonteGigante,
                                      hover_color='grey20',
                                      command=command_back_connected)

nenhumVar = customtkinter.StringVar(value='check')
simplesVar = customtkinter.StringVar(value='check')
premiumVar = customtkinter.StringVar(value='check')

checkNenhum = customtkinter.CTkRadioButton(master=root, text=' Nenhum plano: R$ 0,00 - Nenhuma funcionalidade', font=fonteGigante, value=1, variable=nenhumVar, state='normal')
checkSimples = customtkinter.CTkRadioButton(master=root, text=' Plano Simples: R$ 29,90 - 3 perfis + Propagandas', font=fonteGigante, value=1, variable=simplesVar, state='normal')
checkPremium = customtkinter.CTkRadioButton(master=root, text=' Plano Premium: R$ 49,90 - 5 perfis + Zero propagandas', font=fonteGigante, value=1, variable=premiumVar, state='normal')

passwordSubscription = customtkinter.CTkEntry(master=root,width=500, height=40, corner_radius=30, show='*', font=fonteMedia, placeholder_text='Senha')

    #Possibilidades de perfis
profile1 = customtkinter.CTkImage(dark_image=Image.open('graphicElements/profilePictureDark.png'),
                                         light_image=Image.open('graphicElements/profilePictureLight.png'),
                                         size=(80,80))
profile2 = customtkinter.CTkImage(dark_image=Image.open('graphicElements/profilePictureDark.png'),
                                         light_image=Image.open('graphicElements/profilePictureLight.png'),
                                         size=(80,80))
profile3 = customtkinter.CTkImage(dark_image=Image.open('graphicElements/profilePictureDark.png'),
                                         light_image=Image.open('graphicElements/profilePictureLight.png'),
                                         size=(80,80))
profile4 = customtkinter.CTkImage(dark_image=Image.open('graphicElements/profilePictureDark.png'),
                                         light_image=Image.open('graphicElements/profilePictureLight.png'),
                                         size=(80,80))
profile5 = customtkinter.CTkImage(dark_image=Image.open('graphicElements/profilePictureDark.png'),
                                         light_image=Image.open('graphicElements/profilePictureLight.png'),
                                         size=(80,80))
profile1Button = customtkinter.CTkButton(master=root, text=None, fg_color='transparent', border_width=0, hover=False, image=profile1, width=30, height=30, command=button1)
profile2Button = customtkinter.CTkButton(master=root, text=None, fg_color='transparent', border_width=0, hover=False, image=profile2, width=30, height=30, command=button2)
profile3Button = customtkinter.CTkButton(master=root, text=None, fg_color='transparent', border_width=0, hover=False, image=profile3, width=30, height=30, command=button3)
profile4Button = customtkinter.CTkButton(master=root, text=None, fg_color='transparent', border_width=0, hover=False, image=profile4, width=30, height=30, command=button4)
profile5Button = customtkinter.CTkButton(master=root, text=None, fg_color='transparent', border_width=0, hover=False, image=profile5, width=30, height=30, command=button5)

nameProfile1 = customtkinter.CTkLabel(master=root, text='', font=fonteGrande)
nameProfile2 = customtkinter.CTkLabel(master=root, text='', font=fonteGrande)
nameProfile3 = customtkinter.CTkLabel(master=root, text='', font=fonteGrande)
nameProfile4 = customtkinter.CTkLabel(master=root, text='', font=fonteGrande)
nameProfile5 = customtkinter.CTkLabel(master=root, text='', font=fonteGrande)

manageProfilesButton = customtkinter.CTkButton(master=root,
                                           text='Gerenciar Perfis',
                                           font=fonteGigante,
                                           fg_color=color_red,
                                           hover_color=color_red_dark,
                                           corner_radius=100,
                                           command=command_manage_profile)
addProfileButton = customtkinter.CTkButton(master=root,
                                           text='Adicionar perfil',
                                           font=fonteGrande,
                                           fg_color='mediumseagreen',
                                           hover_color='olivedrab4',
                                           corner_radius=100,
                                           command=command_add_profile)
nameEntry = customtkinter.CTkEntry(master=root, font=fonteGrande, corner_radius=100, placeholder_text='Nome', width=200)
ageEntry = customtkinter.CTkEntry(master=root, font=fonteGrande, corner_radius=100, placeholder_text='Idade', width=200)
buttonBackProfiles = customtkinter.CTkButton(master=root,
                                            font=fonteGigante,
                                            corner_radius=100,
                                            text='Voltar',
                                            command=command_back_connected,
                                            fg_color='grey30',
                                            hover_color='grey20')

    #Remover Perfis
removeProfileEntry = customtkinter.CTkEntry(master=root, font=fonteGrande, corner_radius=100, placeholder_text='Perfil', width=200)
buttonRemoveProfile = customtkinter.CTkButton(master=root,
                                              text='Remover perfil',
                                              fg_color=color_red,
                                              hover_color=color_red_dark,
                                              corner_radius=100,
                                              command=command_remove_profile,
                                              font=fonteGrande)

    #Media
def media(id):
    from functions import mediaInterface
    mediaInterface(id)

strangerThingsImage = customtkinter.CTkImage(dark_image=Image.open('graphicElements/StrangerThings.png'),
                                         light_image=Image.open('graphicElements/StrangerThings.png'),
                                         size=(320,180))
FriendsImage = customtkinter.CTkImage(dark_image=Image.open('graphicElements/Friends.png'),
                                         light_image=Image.open('graphicElements/Friends.png'),
                                         size=(320,180))
breakingBadImage = customtkinter.CTkImage(dark_image=Image.open('graphicElements/BreakingBad.png'),
                                         light_image=Image.open('graphicElements/BreakingBad.png'),
                                         size=(320,180))
PulpFictionImage = customtkinter.CTkImage(dark_image=Image.open('graphicElements/PulpFiction.png'),
                                         light_image=Image.open('graphicElements/PulpFiction.png'),
                                         size=(320,180))
PlanetEarth2Image = customtkinter.CTkImage(dark_image=Image.open('graphicElements/PlanetEarth2.png'),
                                         light_image=Image.open('graphicElements/PlanetEarth2.png'),
                                         size=(320,180))
ToyStoryImage = customtkinter.CTkImage(dark_image=Image.open('graphicElements/ToyStory.png'),
                                         light_image=Image.open('graphicElements/ToyStory.png'),
                                         size=(320,180))
mediaButton0 = customtkinter.CTkButton(master=root, text=None, image=strangerThingsImage, border_width=0 , fg_color='transparent', hover=False, command=lambda: media(0))
mediaButton1 = customtkinter.CTkButton(master=root, text=None, image=FriendsImage, border_width=0 , fg_color='transparent', hover=False, command=lambda: media(1))
mediaButton2 = customtkinter.CTkButton(master=root, text=None, image=breakingBadImage, border_width=0 , fg_color='transparent', hover=False, command=lambda: media(2))
mediaButton3 = customtkinter.CTkButton(master=root, text=None, image=PulpFictionImage, border_width=0 , fg_color='transparent', hover=False, command=lambda: media(3))
mediaButton4 = customtkinter.CTkButton(master=root, text=None, image=PlanetEarth2Image, border_width=0 , fg_color='transparent', hover=False, command=lambda: media(4))
mediaButton5 = customtkinter.CTkButton(master=root, text=None, image=ToyStoryImage, border_width=0 , fg_color='transparent', hover=False, command=lambda: media(5))

strangerThingsImageSized = customtkinter.CTkImage(dark_image=Image.open('graphicElements/StrangerThings.png'),
                                         light_image=Image.open('graphicElements/StrangerThings.png'),
                                         size=(640,360))
FriendsImageSized = customtkinter.CTkImage(dark_image=Image.open('graphicElements/Friends.png'),
                                         light_image=Image.open('graphicElements/Friends.png'),
                                         size=(640,360))
breakingBadImageSized = customtkinter.CTkImage(dark_image=Image.open('graphicElements/BreakingBad.png'),
                                         light_image=Image.open('graphicElements/BreakingBad.png'),
                                         size=(640,360))
PulpFictionImageSized = customtkinter.CTkImage(dark_image=Image.open('graphicElements/PulpFiction.png'),
                                         light_image=Image.open('graphicElements/PulpFiction.png'),
                                         size=(640,360))
PlanetEarth2ImageSized = customtkinter.CTkImage(dark_image=Image.open('graphicElements/PlanetEarth2.png'),
                                         light_image=Image.open('graphicElements/PlanetEarth2.png'),
                                         size=(640,360))
ToyStoryImageSized = customtkinter.CTkImage(dark_image=Image.open('graphicElements/ToyStory.png'),
                                         light_image=Image.open('graphicElements/ToyStory.png'),
                                         size=(640,360))

mediaLabel0 = customtkinter.CTkLabel(master=root, text=None, image=strangerThingsImageSized)
mediaLabel1 = customtkinter.CTkLabel(master=root, text=None, image=FriendsImageSized)
mediaLabel2 = customtkinter.CTkLabel(master=root, text=None, image=breakingBadImageSized)
mediaLabel3 = customtkinter.CTkLabel(master=root, text=None, image=PulpFictionImageSized)
mediaLabel4 = customtkinter.CTkLabel(master=root, text=None, image=PlanetEarth2ImageSized)
mediaLabel5 = customtkinter.CTkLabel(master=root, text=None, image=ToyStoryImageSized)

buttonBackMedias = customtkinter.CTkButton(master=root,
                                      text='Voltar',
                                      width=200,
                                      height=40,
                                      fg_color='grey30',
                                      corner_radius=30,
                                      font=fonteGigante,
                                      hover_color='grey20',
                                      command=command_back_medias)

infosLabel = customtkinter.CTkLabel(master=root, font=fonteGigante)

playButtonImage = customtkinter.CTkImage(dark_image=Image.open('graphicElements/PlayButtonDark.png'),
                                         light_image=Image.open('graphicElements/PlayButtonLight.png'),
                                         size=(80,80))
playButton = customtkinter.CTkButton(master=root, text=None, fg_color='transparent', border_width=0, hover=False, image=playButtonImage, width=30, height=30, command=play)

stopButtonImage = customtkinter.CTkImage(dark_image=Image.open('graphicElements/StopButtonDark.png'),
                                         light_image=Image.open('graphicElements/StopButtonLight.png'),
                                         size=(80,80))
stopButton = customtkinter.CTkButton(master=root, text=None, fg_color='transparent', border_width=0, hover=False, image=stopButtonImage, width=30, height=30, command=stop)


progressBar = customtkinter.CTkProgressBar(master=root, width=640, progress_color=color_red, determinate_speed=0.05)

    #Favorito
favoriteFalseImage = customtkinter.CTkImage(dark_image=Image.open('graphicElements/HeartDark.png'),
                                         light_image=Image.open('graphicElements/HeartLight.png'),
                                         size=(50,50))
favoriteFalseButton = customtkinter.CTkButton(master=root, text=None, fg_color='transparent', border_width=0, hover=False, image=favoriteFalseImage, width=30, height=30, command=selectFavorite)

favoriteTrueImage = customtkinter.CTkImage(dark_image=Image.open('graphicElements/RedHeart.png'),
                                         light_image=Image.open('graphicElements/RedHeart.png'),
                                         size=(50,50))
favoriteTrueButton = customtkinter.CTkButton(master=root, text=None, fg_color='transparent', border_width=0, hover=False, image=favoriteTrueImage, width=30, height=30, command=deselectFavorite)

    #Últimos Assistidos
lastWatchedButton = customtkinter.CTkButton(master=root,
                                      text='Últimos Assistidos',
                                      width=200,
                                      height=40,
                                      fg_color=color_red,
                                      corner_radius=30,
                                      font=fonteGigante,
                                      hover_color=color_red_dark,
                                      command=command_last_watched)

    #Favoritos
favoritesButton = customtkinter.CTkButton(master=root,
                                      text='Favoritos',
                                      width=200,
                                      height=40,
                                      fg_color=color_red,
                                      corner_radius=30,
                                      font=fonteGigante,
                                      hover_color=color_red_dark,
                                      command=command_favorites)

    #Todas as mídias
allMediasButton = customtkinter.CTkButton(master=root,
                                      text='Todas mídias',
                                      width=200,
                                      height=40,
                                      fg_color=color_red,
                                      corner_radius=30,
                                      font=fonteGigante,
                                      hover_color=color_red_dark,
                                      command=command_all_medias)
searchImage = customtkinter.CTkImage(dark_image=Image.open('graphicElements/searchDark.png'),
                                light_image=Image.open('graphicElements/searchLight.png'),
                                size=(30,30))
searchButton = customtkinter.CTkButton(master=root,
                                      width=20,
                                      height=20,
                                      text=None,
                                      border_width=0,
                                      fg_color='transparent',
                                      corner_radius=30,
                                      hover=False,
                                      image=searchImage,
                                      command=command_search)
searchEntry = customtkinter.CTkEntry(master=root, font=fonteGrande, corner_radius=100, placeholder_text='Pesquisar título', width=400)

    #Propaganda
adLabel = customtkinter.CTkLabel(master=root, font=fontePropaganda, text='PROPAGANDA: Curso de segurança da informação UNISINOS')

closeImage = customtkinter.CTkImage(dark_image=Image.open('graphicElements/close.png'),
                                light_image=Image.open('graphicElements/close.png'),
                                size=(20,20))
closeButton = customtkinter.CTkButton(master=root,
                                      width=20,
                                      height=20,
                                      text=None,
                                      border_width=0,
                                      fg_color='transparent',
                                      corner_radius=30,
                                      hover=False,
                                      image=closeImage,
                                      command=command_close_ad)
