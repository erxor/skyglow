#sisselogimise kontroll
#hyperlinkide avamine
from tkinter import *
from tkinter import ttk
from twitter import *
from os.path import isfile
from tkinter import font
from textwrap import * 

tweets_home = []
tweets_me = []
tweets_at = []


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
          
     
def validateTextInputSize(event):#Loendur toodab mingit jama counteri järgi, kui see läheb alla 10, võiks kohe ilmuda
     arv = (140-(len(twiidikast.get('1.0',END))-1))
     loendur = ttk.Label(raam, text = ' '+str(arv), anchor = 'e')
     if arv > 99:
         loendur.configure(background = color1, foreground = "white")
         loendur.grid(column = 1, row = 5)
     elif arv < 100:
         if arv > -1:
             loendur.configure(background = color1, foreground = "white")
             loendur.grid(column = 1, row = 5)
         elif arv < 0:
             loendur.configure(background = color1, foreground = "red")
             loendur.grid(column = 1, row = 5)

     
def säutsumine():
    if len(twiidikast.get('1.0',END))-1 >140:
        #messagebox.showinfo("Viga!", message = "Twiit on liialt pikk. Maksimaalne lubatud pikkus on 140 tähemärki")
        pass
    else:
        twitter.statuses.update(status=twiidikast.get('1.0',END))
        twiidikast.delete('1.0', END)
        twiidikast.insert('1.0', 'Sisesta siia oma tweet...')
        twiidikast.tag_add('hall tekst', '1.0', 'end')
     
def kustuta_tekst(event):
    twiidikast.delete('1.0', END)
    twiidikast.configure(height = 5)


def parem_twiit(name, user, tweet, yasukoht):
        tweet = wrap(tweet, width = 50)
        if len(tweet) == 1:
             tweet = tweet[0]
        elif len(tweet) == 2:
             tweet = tweet[0]+'\n'+tweet[1]
        elif len(tweet) == 3:
             tweet = tweet[0]+'\n'+tweet[1]+'\n'+tweet[2]
        elif len(tweet) == 4:
             tweet = tweet[0]+'\n'+tweet[1]+'\n'+tweet[2]+'\n'+tweet[3]
        twiidiala.create_text(2,yasukoht, text = (name+'   '+"@"+user+"\n"+tweet+'\n'), anchor = 'w', font =("Segoe UI", 8), fill = "white")

def get_tweets_mina():
    c = 40
    twiidiala.delete(ALL)#teeme tahvli puhtaks
    scrollbar.set(0.0, 0.43529411764705883)#liigutame scrollbari üles
    twiidiala.yview('moveto', '0.0')#liigutame vaate üles
    for a in tweets_me:
        parem_twiit(a[0], a[1], a[2], c)
        c += 70

def get_tweets():
    c = 40
    twiidiala.delete(ALL)
    scrollbar.set(0.0, 0.43529411764705883)
    twiidiala.yview('moveto', '0.0')
    for a in tweets_home:
        parem_twiit(a[0], a[1], a[2], c)
        c += 70

def get_mentions():
    c = 40
    twiidiala.delete(ALL)
    scrollbar.set(0.0, 0.43529411764705883)
    twiidiala.yview('moveto', '0.0')
    for a in tweets_at:
        parem_twiit(a[0], a[1], a[2], c)
        c += 70
                
        
color1 = '#0B3A58'
#loob akna
raam = Tk()
raam.title("Skyglow")
raam.geometry("618x400")
raam.option_add("*Font", ("Segoe UI", 10))#font
paksFont = ("Times", 20, "bold")
#raam.resizable(width=FALSE, height=FALSE)

#loome taustapildi
taustapilt = Label(raam)
taustapilt.place(x=0, y=0)
taust = PhotoImage(file='taust.gif')
taustapilt['image'] = taust
taustapilt.config(padx=0, pady=0, bd=-2)

###loome scrollbari ja twiidiala
twiidiala = Canvas(raam, width = 304, height = 375)
twiidialataust_pilt = PhotoImage(file = "twiitidetaust.gif")
twiidiala.create_image(0,0, image =twiidialataust_pilt)
scrollbar = ttk.Scrollbar(twiidiala)
twiidiala.configure(yscrollcommand = scrollbar.set, scrollregion = (0,0,320,800), highlightthickness = 0)
twiidiala.configure(bg = color1)
twiidiala.place(x = 316, y = 25)
scrollbar.place(x = 285, y = 0, height = 375)
scrollbar.configure(command=twiidiala.yview)


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
#twiitide taustad
##twitterbox1 = Label(twiidiala)
##twitterbox1.place(x=0, y=0)
##twitterbox1_pilt = PhotoImage(file="tweet1.gif")
##twitterbox1['image'] = twitterbox1_pilt
##twitterbox1.config(bd=-2, padx = 0, pady=0)

refresh_home()
refresh_me()
refresh_at()
get_tweets()

twitterbox4 = Label(raam)
twitterbox4.place(x=316, y=0)
twitterbox4_pilt = PhotoImage(file="twitterbox4aylemine.gif")
twitterbox4['image'] = twitterbox4_pilt
twitterbox4.config(bd=-2, padx = 0, pady=0)

#loob nupud
nupp0 = ttk.Label(raam, text = '                        ')
nupp0.grid (column = 2, row=1)
nupp0.config(background = color1)
nupp0.lower()
nupp1 = Button(raam, text="Home", width = 9, bg = 'white',command = get_tweets)
nupp1.grid(column=3, row=1)
nupp2 = Button(raam, text="@", width = 9,command = get_mentions)
nupp2.grid(column=4, row=1)
nupp3 = Button(raam, text="Me", width = 9,command = get_tweets_mina)
nupp3.grid(column=5, row=1)
nupp4 = Button(raam, text="Refresh", width = 9, command = refresh)
nupp4.grid(column=6, row=1)
nupp5 = ttk.Button(raam, text="Säutsu", command = säutsumine)
nupp5.grid(column=1, row=5, pady=2, sticky = (E))

#säutsu sisestamine
twiidikast = Text(raam, width=30, height=1, wrap = 'word')
twiidikast.grid(column=1, row = 3)
twiidikast.insert('1.0','Sisesta siia oma tweet...')
twiidikast.bind('<1>', kustuta_tekst)
twiidikast.bind("<KeyRelease>", validateTextInputSize)
twiidikast.tag_add('hall tekst', '1.0', 'end')#algul tekst hall
twiidikast.tag_configure('hall tekst', foreground = 'gray')


#kasti alus ja ülemine osa
twiidialus = Label(raam)
twiidialus.grid(column=1, row = 4)
twiidialus.config(bd=-2, padx = 0, pady=0)
twiidialus_pilt = PhotoImage(file="raam_alus.gif")
twiidialus['image'] = twiidialus_pilt

twiidiylemine = Label(raam)
twiidiylemine.grid(column=1, row = 2)
twiidiylemine_pilt = PhotoImage(file="raam_ylemine.gif")
twiidiylemine['image'] = twiidiylemine_pilt
twiidiylemine.config(bd=-2, padx = 0, pady=0)


#logo osa
logo = Label(raam)
logo.place(x=0, y=243)
logopilt = PhotoImage(file='logo.gif')
logo['image'] = logopilt
logo.config(bd=-2, padx = 0, pady=0)
raam.mainloop()
