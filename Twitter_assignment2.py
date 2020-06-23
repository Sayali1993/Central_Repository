from twitter import *
from tkinter import *


def showTweets(x, num):
    for i in range(0, num):
        line1 = (x[i]['user']['screen_name'])
        line2 = (x[i]['text'])
        w = Label(master, text=line1 + "\n"+line2 + "\n\n")
        w.pack()


def getTweets():

    x = t.statuses.home_timeline(screen_name="XYZ")
    return x


t = Twitter(
    auth=OAuth('Access token','Access token secret'))

numberOfTweets = 3
master = Tk()
showTweets(getTweets(), numberOfTweets)
master.title('Enter a new tweet')
master["padx"] = 40
master["pady"] = 20
textFrame = Frame(master)
entryLabel = Label(textFrame)
master.mainloop()


