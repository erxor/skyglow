#sisselogimise kontroll
from tkinter import *
from tkinter import ttk
from twitter import *
from os.path import isfile
from tkinter import font
from textwrap import wrap 


tweets_home = []
tweets_me = []
tweets_at = []
search = []


def get_search():
     c = 40
     i=j=0
     twiidiala.delete(ALL)
     if len(search) == 0: #kui varem pole midagi otsitud, siis loome tausta
          for i in range(7):
               twiidiala.create_image(160,35+j, image =twiidialataust4)
               j += 60
     otsingukast.lift()
     scrollbar.set(0.0, 0.43529411764705883)
     scrollbari_pikkus=10 + len(search)*60
     twiidiala.config(scrollregion = (0,0,320,scrollbari_pikkus))
     twiidiala.yview('moveto', '0.0')
     for a in search:
          tweet = parem_twiit(a[0],a[1],a[2])
          twiidiala.create_image(160,35+i, image =twiidialataust4)
          tekst = twiidiala.create_text(5,40+i, anchor=W, text = tweet, fill=color2, font=("Segoe UI", 8))
          i += 60

     
def refresh_search(event):
     statuses = twitter.search.tweets(q=otsingukast.get())['statuses']
     säutsud = []
     for a in range(0,11):
          x = statuses[a]
          tweet = x['text'] #krabame dictist teksti
          user = (x['user'])['screen_name'] #krabame dicti subdictist username
          name = (x['user'])['name'] #lisaks usernamele võtaks silmale meeldivama nime ka
          säuts = [name, user, tweet]
          säutsud.insert(0, säuts)
     for i in säutsud:
          if i not in search:
               search.insert(0, i)
     säutsud = []
     get_search()
     otsingukast.lower()

     
def refresh_home():
     statuses = twitter.statuses.home_timeline()
     säutsud = []
     for a in range(0,15):
          x = statuses[a]
          tweet = x['text'] #krabame dictist teksti
          user = (x['user'])['screen_name'] #krabame dicti subdictist username
          name = (x['user'])['name'] #lisaks usernamele võtaks silmale meeldivama nime ka
          säuts = [name, user, tweet]
          säutsud.insert(0, säuts)
     for i in säutsud:
          if i not in tweets_home:
               tweets_home.insert(0, i)
     säutsud = []


def refresh_me():
     statuses = twitter.statuses.user_timeline()
     säutsud = []
     for a in range(0,15):
          x = statuses[a]
          tweet = x['text']
          user = (x['user'])['screen_name']
          name = (x['user'])['name']
          säuts = [name, user, tweet]
          säutsud.insert(0, säuts)
     for i in säutsud:
          if i not in tweets_me:
               tweets_me.insert(0, i)


def refresh_at():
     statuses = twitter.statuses.mentions_timeline()
     säutsud = []
     for a in range(0,15):
          x = statuses[a]
          tweet = x['text']
          user = (x['user'])['screen_name']
          name = (x['user'])['name']
          säuts = [name, user, tweet]
          säutsud.insert(0, säuts)
     for i in säutsud:
          if i not in tweets_at:
               tweets_at.insert(0, i)


def refresh():
     refresh_home()
     refresh_me()
     refresh_at()
     refresh_search()
          
     
def validateTextInputSize(event):#Loendur toodab mingit jama counteri järgi, kui see läheb alla 10, võiks kohe ilmuda
     arv = (140-(len(twiidikast.get('1.0',END))-1))
     loendur = ttk.Label(raam, text = ' '+str(arv))
     loendur.config(background = color1)
     loendur.grid(column=1, row = 5)
     if arv > -1:
          loendur.configure(background = color1, foreground = "white")
     if arv < 0:
          loendur.configure(foreground = "red")

     
def säutsumine():
    if len(twiidikast.get('1.0',END))-1 >140:
        pass
    else:
        twitter.statuses.update(status=twiidikast.get('1.0',END))
        twiidikast.delete('1.0', END)
        twiidikast.insert('1.0', 'Sisesta siia oma tweet...')
        twiidikast.tag_add('hall tekst', '1.0', 'end')

     
def kustuta_tekst(event):
    twiidikast.delete('1.0', END)
    twiidikast.configure(height = 5)


def parem_twiit(name, user, tweet):
        tweet = wrap(tweet, width = 50)
        if len(tweet) == 1:
             tweet = tweet[0]
        elif len(tweet) == 2:
             tweet = tweet[0]+'\n'+tweet[1]
        elif len(tweet) == 3:
             tweet = tweet[0]+'\n'+tweet[1]+'\n'+tweet[2]
        elif len(tweet) == 4:
             tweet = tweet[0]+'\n'+tweet[1]+'\n'+tweet[2]+'\n'+tweet[3]
        return name+'   '+"@"+user+"\n"+tweet+'\n'


def get_tweets_mina():
    c = 40
    i = 0
    otsingukast.lower()
    twiidiala.delete(ALL)#teeme tahvli puhtaks
    scrollbar.set(0.0, 0.43529411764705883)#liigutame scrollbari üles
    scrollbari_pikkus=10 + len(tweets_me)*60
    twiidiala.config(scrollregion = (0,0,320,scrollbari_pikkus))
    twiidiala.yview('moveto', '0.0')#liigutame vaate üles
    for a in tweets_me:
          tweet = parem_twiit(a[0],a[1],a[2])
          twiidiala.create_image(160,35+i, image =twiidialataust3)
          tekst = twiidiala.create_text(5,40+i, anchor=W, text = tweet, fill="white", font=("Segoe UI", 8))
          i += 60


def get_tweets():
    c = 40
    i = 0
    if kontrollmuutuja ==1:
         otsingukast.lower()
    twiidiala.delete(ALL)
    scrollbar.set(0.0, 0.43529411764705883)
    scrollbari_pikkus=10+ len(tweets_home)*60
    twiidiala.config(scrollregion = (0,0,320,scrollbari_pikkus))
    twiidiala.yview('moveto', '0.0')
    for a in tweets_home:
          tweet = parem_twiit(a[0],a[1],a[2])
          twiidiala.create_image(160,35+i, image =twiidialataust1)
          tekst = twiidiala.create_text(5,40+i, anchor=W, text = tweet, fill=color1, font=("Segoe UI", 8))
          i += 60


def get_mentions():
    c = 40
    i = 0
    otsingukast.lower()
    twiidiala.delete(ALL)
    scrollbar.set(0.0, 0.43529411764705883)
    scrollbari_pikkus=10 + len(tweets_at)*60
    twiidiala.config(scrollregion = (0,0,320,scrollbari_pikkus))
    twiidiala.yview('moveto', '0.0')
    for a in tweets_at:
          tweet = parem_twiit(a[0],a[1],a[2])
          #label=Label(twiidiala, image=twiidialataust2,anchor=W, text=tweet,bd=0,padx=0, pady=0,fg='white',font=("Segoe UI", 8),justify=LEFT,compound=CENTER)
          #label.pack()
          #label.place(x=0,y=i)
          twiidiala.create_image(160,35+i, image =twiidialataust2)
          tekst = twiidiala.create_text(5,40+i, anchor=W, text = tweet, fill="white", font=("Segoe UI", 8))
          i += 60
                
        
color1 = '#0B3A58'
color2 = '#5aac8c'
#loob akna
raam = Tk()
raam.title("Skyglow")
raam.geometry("614x400")
raam.option_add("*Font", ("Segoe UI", 10))#font
paksFont = ("Times", 20, "bold")
#raam.resizable(width=FALSE, height=FALSE)


#loome taustapildi
taustapilt = Label(raam)
taustapilt.place(x=0, y=0)
taust = PhotoImage(file='selg.gif')
taustapilt['image'] = taust
taustapilt.config(padx=0, pady=0, bd=-2)


#loome scrollbari ja twiidiala
twiidiala = Canvas(width = 340, height = 380)
twiidialataust4= PhotoImage(file = "tweet4.gif")
twiidialataust3= PhotoImage(file = "tweet3.gif")
twiidialataust2= PhotoImage(file = "tweet2.gif")
twiidialataust1= PhotoImage(file = "tweet1.gif")
twiidiala.config(background=color1)
scrollbar = ttk.Scrollbar(twiidiala)
twiidiala.configure(yscrollcommand = scrollbar.set, scrollregion = (0,0,320,800), highlightthickness = 0)
twiidiala.place(x = 278, y = 20)
scrollbar.place(x = 320, y = 0, height = 380)
scrollbar.configure(command=twiidiala.yview)


#twitteri jama
CONSUMER_KEY = "OyremhLVargLoqBAG2PZwQ" #voldemari consumer key
CONSUMER_SECRET = "25GrCT1ItNRnHmMQc4QRD1qUpm8jvY1HTzsaYHqLCBE" #voldemari consumer secret
kasutajanimi = "erx0r" #kasutajanimi
if not isfile(kasutajanimi+'.txt'): #kui vastavat faili veel pole siis loob selle
    oauth_dance('voldemar', 'OyremhLVargLoqBAG2PZwQ', '25GrCT1ItNRnHmMQc4QRD1qUpm8jvY1HTzsaYHqLCBE',kasutajanimi+'.txt')
f=open(kasutajanimi+'.txt') #avab faili ja võtab sealt oauth info
oauth_token = f.readline().strip()
oauth_secret = f.readline().strip()
f.close()
twitter = Twitter(auth=OAuth(oauth_token, oauth_secret, CONSUMER_KEY, CONSUMER_SECRET)) #logib twitterisse


#küsime tweete
kontrollmuutuja = 0
refresh_home()
refresh_me()
refresh_at()
get_tweets()


#loob nupud
nupp1_taust = PhotoImage(file="nupp1.gif")
nupp2_taust = PhotoImage(file="nupp2.gif")
nupp3_taust = PhotoImage(file="nupp3.gif")
nupp4_taust = PhotoImage(file="nupp4.gif")

nupp0 = Label(raam)
nupp0.config(width= 8)
nupp0.grid (column = 2, row=1)
nupp0.lower()

nupp1 = Button(raam, command = get_tweets)
nupp2 = Button(raam, command = get_mentions)
nupp3 = Button(raam, command = get_tweets_mina)
nupp4 = Button(raam, command = get_search)
nupp5 = Button(raam, text="Säutsu", command = säutsumine)

nupp1.grid(column=3, row=1)
nupp2.grid(column=4, row=1)
nupp3.grid(column=5, row=1)
nupp4.grid(column=6, row=1)
nupp5.grid(column=1, row=5, pady=2, sticky = (E))

nupp1.config(image=nupp1_taust, width = 80, height = 20, bd = 0, highlightthickness=0)
nupp2.config(image=nupp2_taust, width = 80, height = 20, bd = 0, highlightthickness=0)
nupp3.config(image=nupp3_taust, width = 80, height = 20, bd = 0, highlightthickness=0)
nupp4.config(image=nupp4_taust, width = 80, height = 20, bd = 0, highlightthickness=0)


#säutsu sisestamine
twiidikast = Text(raam, width=30, height=1, wrap = 'word')
twiidikast.grid(column=1, row = 3)
twiidikast.insert('1.0','Sisesta siia oma tweet...')
twiidikast.bind('<1>', kustuta_tekst)
twiidikast.bind("<KeyPress>", validateTextInputSize)
twiidikast.tag_add('hall tekst', '1.0', 'end')#algul tekst hall
twiidikast.tag_configure('hall tekst', foreground = 'gray')


#kasti alus ja ülemine osa
twiidialus = Label(raam)
twiidialus.grid(column=1, row = 4)
twiidialus.config(bd=-2, padx = 0, pady=0)
twiidialus_pilt = PhotoImage(file="raam_bots.gif")
twiidialus['image'] = twiidialus_pilt

twiidiylemine = Label(raam)
twiidiylemine.grid(column=1, row = 2)
twiidiylemine_pilt = PhotoImage(file="raam_topp.gif")
twiidiylemine['image'] = twiidiylemine_pilt
twiidiylemine.config(bd=-2, padx = 0, pady=0)


#peidetud otsingukaust
otsingukast = Entry(raam)
otsingukast.place(x=300, y=40)
otsingukast.bind("<Return>", refresh_search)
otsingukast.lower()
kontrollmuutuja = 1

#logo osa
logo = Label(raam)
logo.place(x=0, y=243)
logopilt = PhotoImage(file='logo.gif')
logo['image'] = logopilt
logo.config(bd=-2, padx = 0, pady=0)
raam.mainloop()
