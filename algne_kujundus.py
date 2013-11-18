#compose tweet halliks(lebo), kastile vajutades kaob see ära ja kiri muutub mustaks,
#username ja muud asjad paika, kasti sisse twiitidele eraldi kastid äkki? modi akna suurust
#siisselogimise kontroll
#voldemari enda font
#twiitide pikkus
from tkinter import *
from tkinter import ttk
from twitter import *
from os.path import isfile

def säutsumine():
    twitter.statuses.update(status=twiidikast.get('1.0',END))
    twiidikast.delete('1.0', END)
    twiidikast.insert('1.0', 'Sisesta siia oma twiit...')
    twiidikast.tag_add('vajutus', '1.0', 'end')

def kustuta_tekst(n):
    twiidikast.delete('1.0', END)

def twiit(a,b,c):
    twiit = ttk.Label(raam, wraplength = 290,text = a)
    twiit.place(x = b, y = c)

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
        
def delete_tweets():
    c = 50
    for a in range(0,5):
        b= 320
        twiit("\n"+" "+140*" "+"\n"+140*" "+'\n',b, c)
        c += 60
        
def replace_tweets():
    delete_tweets()
    get_tweets()
    
#loob akna
raam = Tk()
raam.title("Voldemar")
raam.geometry("620x420")


CONSUMER_KEY = "OyremhLVargLoqBAG2PZwQ" #voldemari consumer key
CONSUMER_SECRET = "25GrCT1ItNRnHmMQc4QRD1qUpm8jvY1HTzsaYHqLCBE" #voldemari consumer secret
kasutajanimi = "E_R_K_I" #kasutajanimi
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
nupp2 = ttk.Button(raam, text="Friends")
nupp2.grid(column=4, row=1, pady=5)
nupp3 = ttk.Button(raam, text="Trending")
nupp3.grid(column=5, row=1, pady=5 )
nupp4 = ttk.Button(raam, text="Messages")
nupp4.grid(column=6, row=1, pady=5)
nupp5 = ttk.Button(raam, text="Säutsu", command = säutsumine)
nupp5.grid(column=1, row=6, pady=5, sticky = (E))

#säutsu sisestamine, uuri ttk.Text
twiidikast = Text(raam, width=30, height=5, wrap = 'word')
twiidikast.grid(column=1, row = 5)
twiidikast.insert('1.0','Sisesta siia oma tweet...')
twiidikast.tag_add('vajutus', '1.0', 'end')#muudame vajutusel teksti mustaks
twiidikast.tag_configure('vajutus', foreground = 'gray')
twiidikast.tag_bind('vajutus', '<ButtonPress-1>', kustuta_tekst)
Voldemar = ttk.Label(raam, text = 'Voldemar.py ©®', anchor = 'e')
Voldemar.grid(column = 1, row = 1)

#loob teksti
username = ttk.Label(raam, text = 'User name')
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




