#sisselogimise kontroll
#twiitide pikkus
#hyperlinkide avamine
#s = ttk.Separator(parent, orient=HORIZONTAL)
from tkinter import *
from tkinter import ttk
from twitter import *
from os.path import isfile
from tkinter import font
from textwrap import * 

def validateTextInputSize(event):#Loendur toodab mingit jama counteri järgi, kui see läheb alla 10, võiks kohe ilmuda
     arv = (140-(len(twiidikast.get('1.0',END))-1))
     loendur = ttk.Label(raam, text = ' '+str(arv), anchor = 'e')
     if arv > 99:
         loendur.configure(background = color1, foreground = "white")
         loendur.grid(column = 1, row = 6)
     elif arv < 100:
         if arv > -1:
             loendur.configure(background = color1, foreground = "white")
             loendur.grid(column = 1, row = 6)
         elif arv < 0:
             loendur.configure(background = color1, foreground = "red")
             loendur.grid(column = 1, row = 6)

     
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

def twiit(a,b,c):
    #twiit = ttk.Label(raam, wraplength = 310,text = a)
    #twiit.configure(background = color1, foreground = "white")
    #twiit.place(x = b, y = c)
    b = c

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
        twiidiala.create_text(0,yasukoht, text = (name+'   '+"@"+user+"\n"+tweet+'\n'), anchor = 'w', font =("Segoe UI", 8), fill = "white")

def get_tweets_mina():
    c = 40
    twiidiala.delete(ALL)
    statuses = twitter.statuses.user_timeline()
    for a in range(0,11):
        x = statuses[a]
        tweet = x['text']
        user = (x['user'])['screen_name']
        name = (x['user'])['name']
        parem_twiit(name, user, tweet, c)
        c += 70

def get_tweets():
    c = 30
##    twiidiala.delete(ALL)
##    statuses = twitter.statuses.home_timeline()
##    for a in range(0,11):
##        x = statuses[a]
##        tweet = x['text'] #krabame dictist teksti
##        user = (x['user'])['screen_name'] #krabame dicti subdictist username
##        name = (x['user'])['name'] #lisaks usernamele võtaks silmale meeldivama nime ka
##        parem_twiit(name, user, tweet, c)
##        c += 70

def get_mentions():
    c = 30
    twiidiala.delete(ALL)#teeme tahvli puhtaks
    statuses = twitter.statuses.mentions_timeline()
    for a in range(0,11):
        x = statuses[a]
        tweet = x['text']
        user = (x['user'])['screen_name']
        name = (x['user'])['name']
        parem_twiit(name, user, tweet, c)
        c += 70
                
        
def delete_tweets():
    c = 25
    for a in range(0,5):
        b= 320
        twiit("\n"+" "+140*" "+"\n"+140*" "+'\n',b, c)
        c += 70
        
def replace_tweets():
    delete_tweets()
    get_tweets()

def replace_mentions():
    delete_tweets()
    get_mentions()

def replace_tweets_mina():
    delete_tweets()
    get_tweets_mina()

color1 = '#0B3A58'
#loob akna
raam = Tk()
raam.title("Skyglow")
raam.geometry("630x400")
raam.configure(background = color1)
raam.option_add("*Font", ("Segoe UI", 10))#font
paksFont = ("Times", 20, "bold")
#raam.resizable(width=FALSE, height=FALSE)

###loome scrollbari ja twiidiala
twiidiala = Canvas(raam, width = 302, height = 370)
scrollbar = ttk.Scrollbar(twiidiala)
twiidiala.configure(yscrollcommand = scrollbar.set, scrollregion = (0,0,320,800), highlightthickness = 0)
twiidiala.configure(bg = color1)
twiidiala.place(x = 316, y = 30)
scrollbar.place(x = 283, y = 0, height = 370)
scrollbar.configure(command=twiidiala.yview)


CONSUMER_KEY = "OyremhLVargLoqBAG2PZwQ" #voldemari consumer key
CONSUMER_SECRET = "25GrCT1ItNRnHmMQc4QRD1qUpm8jvY1HTzsaYHqLCBE" #voldemari consumer secret
kasutajanimi = "MadisKarli" #kasutajanimi
if not isfile(kasutajanimi+'.txt'): #kui vastavat faili veel pole siis loob selle
    oauth_dance('voldemar', 'OyremhLVargLoqBAG2PZwQ', '25GrCT1ItNRnHmMQc4QRD1qUpm8jvY1HTzsaYHqLCBE',kasutajanimi+'.txt')
f=open(kasutajanimi+'.txt') #avab faili ja võtab sealt oauth info
oauth_token = f.readline().strip()
oauth_secret = f.readline().strip()
f.close()
twitter = Twitter(auth=OAuth(oauth_token, oauth_secret, CONSUMER_KEY, CONSUMER_SECRET)) #logib twitterisse

get_tweets()

#loob nupud
nupp0 = ttk.Label(raam, text = '                        ')
nupp0.configure(background = color1, foreground = "white")
nupp0.grid (column = 2, row=1)
nupp1 = ttk.Button(raam, text="Home", command = replace_tweets)
nupp1.grid(column=3, row=1)
nupp2 = ttk.Button(raam, text="@", command = replace_mentions)
nupp2.grid(column=4, row=1)
nupp3 = ttk.Button(raam, text="Me", command = replace_tweets_mina)
nupp3.grid(column=5, row=1)
nupp4 = ttk.Button(raam, text="    ")
nupp4.grid(column=6, row=1)
nupp5 = ttk.Button(raam, text="Säutsu", command = säutsumine)
nupp5.grid(column=1, row=6, pady=5, sticky = (E))


#säutsu sisestamine, uuri ttk.Text
twiidikast = Text(raam, width=30, height=1, wrap = 'word')
twiidikast.grid(column=1, row = 5)
twiidikast.insert('1.0','Sisesta siia oma tweet...')
twiidikast.bind('<1>', kustuta_tekst)
twiidikast.bind("<KeyRelease>", validateTextInputSize)
twiidikast.tag_add('hall tekst', '1.0', 'end')#algul tekst hall
twiidikast.tag_configure('hall tekst', foreground = 'gray')
Skyglow = ttk.Label(raam, text = 'Skyglow ©®', anchor = 'e')
Skyglow.configure(background = color1, foreground = "white")
Skyglow.grid(column = 1, row = 1)

#tervitab kasutajat
username = ttk.Label(raam, text = 'Tere, '+kasutajanimi+ '!')
username.configure(background = color1, foreground = "white")
username.place(x = 0, y = 220)



##space = ttk.Label(raam, text = '')
##Voldemar.configure(background = color1, foreground = "white")
##space.grid(column = 1, row = 13, sticky = (E))

#logo osa, jpg ja png ei tööta miskipärast
logo = ttk.Label(raam)
logo.place(x=0, y=240)
logopilt = PhotoImage(file='logo.gif')
logo['image'] = logopilt
raam.mainloop()
