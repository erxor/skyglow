#username ja muud asjad paika? modi akna suurust
#sisselogimise kontroll
#voldemari enda font
#twiitide pikkus
#hyperlinkide avamine
#s = ttk.Separator(parent, orient=HORIZONTAL)
from tkinter import *
from tkinter import ttk
from twitter import *
from os.path import isfile

def säutsumine():
    #twitter.statuses.update(status=twiidikast.get('1.0',END))
    twiidikast.delete('1.0', END)
    twiidikast.insert('1.0', 'Sisesta siia oma tweet...')
    twiidikast.tag_add('hall tekst', '1.0', 'end')

def kustuta_tekst(lambimuutuja):
    twiidikast.delete('1.0', END)
    twiidikast.configure(height = 5)

def twiit(a,b,c):
    twiit = ttk.Label(raam, wraplength = 290,text = a)
    twiit.place(x = b, y = c)

def get_tweets_mina():
    c = 50
    i = 0
    statuses = twitter.statuses.user_timeline()
    for a in range(0,5):
        x = statuses[a]
        tweet = x['text']
        user = (x['user'])['screen_name']
        name = (x['user'])['name']
        b = 320
        twiit(i*"\n"+name+'   '+"@"+user+"\n"+tweet+'\n', b, c)
        i = 1
        c += 60

def get_tweets():
    c = 50
    i = 0
    statuses = twitter.statuses.home_timeline()
    for a in range(0,5):
        x = statuses[a]
        tweet = x['text'] #krabame dictist teksti
        user = (x['user'])['screen_name'] #krabame dicti subdictist username
        name = (x['user'])['name'] #lisaks usernamele võtaks silmale meeldivama nime ka
        b = 320
        twiit(i*"\n"+name+'   '+"@"+user+"\n"+tweet+'\n', b, c) #prindime välja
        i = 1
        c += 60

def get_mentions():
    c = 50
    i = 0
    statuses = twitter.statuses.mentions_timeline()
    for a in range(0,5):
        x = statuses[a]
        tweet = x['text']
        user = (x['user'])['screen_name']
        name = (x['user'])['name']
        b = 320
        twiit(i*"\n"+name+'   '+"@"+user+"\n"+tweet+'\n', b, c)
        i = 1
        c += 60
                
        
def delete_tweets():
    c = 50
    for a in range(0,5):
        b= 320
        twiit("\n"+" "+140*" "+"\n"+140*" "+'\n',b, c)
        c += 60
        
def replace_tweets():
    delete_tweets()
    get_tweets()

def replace_mentions():
    delete_tweets()
    get_mentions()

def replace_tweets_mina():
    delete_tweets()
    get_tweets_mina()

#loob akna
raam = Tk()
raam.title("Voldemar")
raam.geometry("620x420")

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

get_tweets()

#loob nupud
nupp1 = ttk.Button(raam, text="Home", command = replace_tweets)
nupp1.grid(column=3, row=1, pady=5)
nupp2 = ttk.Button(raam, text="@", command = replace_mentions)
nupp2.grid(column=4, row=1, pady=5)
nupp3 = ttk.Button(raam, text="Me", command = replace_tweets_mina)
nupp3.grid(column=5, row=1, pady=5 )
nupp4 = ttk.Button(raam, text="Messages")
nupp4.grid(column=6, row=1, pady=5)
nupp5 = ttk.Button(raam, text="Säutsu", command = säutsumine)
nupp5.grid(column=1, row=6, pady=5, sticky = (E))

#säutsu sisestamine, uuri ttk.Text
twiidikast = Text(raam, width=30, height=1, wrap = 'word')
twiidikast.grid(column=1, row = 5)
twiidikast.insert('1.0','Sisesta siia oma tweet...')
twiidikast.bind('<1>', kustuta_tekst)
twiidikast.tag_add('hall tekst', '1.0', 'end')#algul tekst hall
twiidikast.tag_configure('hall tekst', foreground = 'gray')
Voldemar = ttk.Label(raam, text = 'Voldemar.py ©®', anchor = 'e')
Voldemar.grid(column = 1, row = 1)

#loob teksti
username = ttk.Label(raam, text = kasutajanimi)
username.grid(column = 2, row = 14, sticky = (W))
tweets = ttk.Label(raam, text = 'X tweets....')#sticky = (E) ei tööta siin ja anchor = 'w' ei muuda midagi
tweets.grid(column = 2, row = 15, sticky = (W))
following = ttk.Label(raam, text = 'Y following')
following.grid(column = 2, row = 16, sticky = (W))
followers = ttk.Label(raam, text = 'Z followers')
followers.grid(column = 2, row = 17, sticky = (W))
space = ttk.Label(raam, text = '')
space.grid(column = 1, row = 13, sticky = (E))

#logo osa, jpg ja png ei tööta miskipärast
logo = ttk.Label(raam)
logo.place(x=0, y=260)
logopilt = PhotoImage(file='logo.gif')
logo['image'] = logopilt
raam.mainloop()

