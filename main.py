import threading
from tkinter import *  # This line means to import all the classes and method present in tkinter.
import random
from tkinter import ttk
import string
import time
import threading





from ttkthemes import *

#functionality part

def reset():
    global wrongwords
    wrongwords=0
    remaining_time_labelcount.config(text='0')
    elapse_time_countlabel.config(text='0')
    totalwords_countlabel.config(text='0')
    wpm_countlabel.config(text='0')
    accuracy_countlabel.config(text='0')
    wrong_countlabel.config(text='0')
    textArea.config(state=NORMAL)
    textArea.delete(0.0, END)
    textArea.config(state=DISABLED)
    startButton.config(state=NORMAL)
    resetButton.config(state=DISABLED)

t=0
totaltime=60
wrongwords=0
accuracy=0
def timer():
    global wrongwords
    textArea.config(state=NORMAL)
    startButton.config(state=DISABLED)
    textArea.focus_set()
    for t in range(1,60):
        elapse_time_countlabel.config(text=t)
        remainingtime=totaltime-t
        remaining_time_labelcount.config(text=remainingtime)
        root.update()
        time.sleep(1)

    textArea.config(state=DISABLED)
    resetButton.config(state=NORMAL)
    totalword=len(textArea.get(0.0,END).split())
    totalwords_countlabel.config(text=totalword)

    textArea_words=textArea.get(0.0,END).split()
    label_paragraph_words=paragraphLabel['text'].split()

    for pair in list(zip(textArea_words,label_paragraph_words)):
        if pair[0] !=pair[1]:
            wrongwords+=1
    wrong_countlabel.config(text=wrongwords)

    wpm=totalword-wrongwords
    wpm_countlabel.config(text=wpm)
    try:
        accuracy=round(((wpm/totalword)*100))
        accu = str(round(accuracy))
        accuracy_countlabel.config(text=accu + "%")
    except:
        pass


def start():
    t1= threading.Thread(target=timer)
    t1.setDaemon(True)
    t1.start()


def colorchange(widget):
    widget.config(bg='blue')
    widget.after(200,lambda : widget.config(bg='black'))



#GUI part

root = ThemedTk()
root.get_themes()
root.set_theme('radiance')

root.geometry('940x735+200+10')

root.resizable(False, False)
root.overrideredirect(True)

titleFrame=Frame(root, bg='orange', bd=4)
titleFrame.grid()

titleLAbel = Label(titleFrame, text='MASTER TYPING', font=('algerian', 28, 'bold'),bg='blue',fg='white',width=38,bd=10)
titleLAbel.grid()

paragraphFrame = Frame(root)
paragraphFrame.grid(row=1,column=0)
paragraph_list=[' I failed the first quarter of a class in middle school, so I made a fake report card. I did this every quarter that year. I forgot that they mail home the end-of-year cards, and my mom got it before I could intercept with my fake. She was PISSED—at the school for their error. The teacher also retired that year and had already thrown out his records, so they had to take my mother’s “proof” (the fake ones I made throughout the year) and “correct” the “mistake.” ',

                    ' In my junior year of high school, this guy asked me on a date. He rented a Redbox movie and made a pizza. We were watching the movie and the oven beeped so the pizza was done. He looked me dead in the eye and said, “This is the worst part.” I then watched this boy open the oven and pull the pizza out with his bare hands, rack and all, screaming at the top of his lungs. We never had a second date.Ok so then what is i cannot tell you because that didnt happen.',

                    'I went to this girl’s party the week after she beat the shit out of my friend. While everyone was getting trashed, I went around putting tuna inside all the curtain rods and so like weeks went by and they couldn’t figure out why the house smelled like festering death. They caught me through this video where these guys at the party were singing Beyonce while I was in the background with a can of tuna.This is what happened in this short funny story if you like.',

                    'One time way back in sixth grade math class I had to fart really bad. Me being the idiot that I am decided that it would be silent. Big surprise it wasn’t. The only person talking was the teacher and she was interrupted by freaking cannon fire farts. She said she was disappointed I couldn’t hold it in and proceeded to tell a story of how she taught a famous athlete who did nearly the same thing.I felt ashamed then everyone laughed and at the end I also laughed.',

                    'So a couple weeks ago, me and my friends were sitting on this cement kind of pedestal (as we called it) It’s basically the steps up to the portable. (classroom that no one uses) and this weird supply French teacher comes up to us and says: you shouldn’t be sitting on this ground, it’s too cold and it’s bad for your ovaries. I asked her how or why and she said that if children sit on cold ground their ovaries will freeze and that we won’t be able to have kids.',
                    'One of the most valuable possession of human life is its health. With good health, one can attain everything in life. In order to perform an important work effectively, one has to be in sound health. Nowadays, everyone is suffering from some sort of mental, health, chronic or physical illness, which however deprives them. Often bad habits such as smoking have brought upon diseases and weakness upon a person which he is not aware of and are of no value to their family and society.',
                    'Alcohol is taken in almost all cool and cold climates, and to a very much less extent in hot ones. It is taken by people who live in the Himalaya Mountains, but not nearly so much by those who live in the plains of India. Alcohol is not necessary in any way to anybody. The regular use of alcohol, even in small quantities, tends to cause mischief in many ways to various organs of the body. It affects the liver, it weakens the mental powers, and lessens the energy of the body.',

                    'The Computer is an automatic device that performs mathematical calculations and logical operations. They are being put to use in widely divergent fields such as book-keeping, spaceflight controls, passanger reservation service, language translation etc. There are two categories: analog and digital. The former represents numbers by some physical quantity such as length, angular relation or electric current whereas the latter represent numbers by seperate devices for each digit.']

random.shuffle(paragraph_list)
paragraphLabel = Label(paragraphFrame, text=paragraph_list[0], wraplength=912, justify='left',font=('arial',13, 'bold'))
paragraphLabel.grid()

textFrame = Frame(root)
textFrame.grid(row=2, column=0)
textArea = Text(textFrame,font=('Arial',12,'bold'),width=101,height=7, wrap='word', bd=4, relief=GROOVE,
                state=DISABLED)
textArea.grid()


outputFrame = Frame(root)
outputFrame.grid(row=3, column=0)

elapse_time_label = Label(outputFrame, text='ELapsed time', fg='red', font=('Tahoma',12,'bold'))
elapse_time_label.grid(row=0,column=0,padx=5)

elapse_time_countlabel = Label(outputFrame, text='0', font=('Tahoma',12,'bold'))
elapse_time_countlabel.grid(row=0,column=1,padx=5)

remaining_time_label = Label(outputFrame, text='Remaining Time',fg='red', font=('Tahoma',12,'bold'))
remaining_time_label.grid(row=0,column=2,padx=5)

remaining_time_labelcount = Label(outputFrame, text='60', font=('Tahoma',12,'bold'))
remaining_time_labelcount.grid(row=0,column=3,padx=5)

wpm_label = Label(outputFrame, text='wpm',fg='red', font=('Tahoma',12,'bold'))
wpm_label.grid(row=0,column=4,padx=5)

wpm_countlabel = Label(outputFrame, text='0', font=('Tahoma',12,'bold'))
wpm_countlabel.grid(row=0,column=5,padx=5)

accuracy_label = Label(outputFrame, text='Accuracy',fg='red', font=('Tahoma',12,'bold'))
accuracy_label.grid(row=0,column=6,padx=5)

accuracy_countlabel = Label(outputFrame, text='0%', font=('Tahoma',12,'bold'))
accuracy_countlabel.grid(row=0,column=7,padx=5)

totalwords_label = Label(outputFrame, text='Total_Words',fg='red', font=('Tahoma',12,'bold'))
totalwords_label.grid(row=0,column=8,padx=5)

totalwords_countlabel = Label(outputFrame, text='0', font=('Tahoma',12,'bold'))
totalwords_countlabel.grid(row=0,column=9,padx=5)

wrong_label = Label(outputFrame, text='Wrong_Words',fg='red', font=('Tahoma',12,'bold'))
wrong_label.grid(row=0,column=10,padx=5)

wrong_countlabel = Label(outputFrame, text='0', font=('Tahoma',12,'bold'))
wrong_countlabel.grid(row=0,column=11,padx=5)

buttonFrame = Frame(root, pady=10)
buttonFrame.grid(row=4, column=0)

startButton= ttk.Button(buttonFrame, text='Start', command=start)
startButton.grid(row=0, column=0, padx=50)

resetButton= ttk.Button(buttonFrame, text='Reset', state=DISABLED, command=reset)
resetButton.grid(row=0, column=1, padx=50)

exitButton= ttk.Button(buttonFrame, text='Exit', command=root.destroy)
exitButton.grid(row=0, column=2, padx=50)

keyFrame = Frame(root, pady=15, bg='black')
keyFrame.grid(row=5, column=0,)

frame1to0 = Frame(keyFrame, bg='black', pady=3)
frame1to0.grid(row=0, column=0)

Label1 = Label(frame1to0, text='1', bg='black', fg='white', width=5, height=2, bd=4, font=('Arial',10,'bold'), relief=GROOVE)
Label1.grid(row=0, column=0, padx= 8)

Label2 = Label(frame1to0, text='2', bg='black', fg='white', width=5, height=2, bd=4, font=('Arial',10,'bold'), relief=GROOVE)
Label2.grid(row=0, column=1, padx= 8)

Label3 = Label(frame1to0, text='3', bg='black', fg='white', width=5, height=2, bd=4, font=('Arial',10,'bold'), relief=GROOVE)
Label3.grid(row=0, column=2, padx= 8)

Label4 = Label(frame1to0, text='4', bg='black', fg='white', width=5, height=2, bd=4, font=('Arial',10,'bold'), relief=GROOVE)
Label4.grid(row=0, column=3, padx=8)

Label5 = Label(frame1to0, text='5', bg='black', fg='white', width=5, height=2, bd=4, font=('Arial',10,'bold'), relief=GROOVE)
Label5.grid(row=0, column=4, padx=8)

Label6 = Label(frame1to0, text='6', bg='black', fg='white', width=5, height=2, bd=4, font=('Arial',10,'bold'), relief=GROOVE)
Label6.grid(row=0, column=5, padx=8)

Label7 = Label(frame1to0, text='7', bg='black', fg='white', width=5, height=2, bd=4, font=('Arial',10,'bold'), relief=GROOVE)
Label7.grid(row=0, column=6, padx=8)

Label8 = Label(frame1to0, text='8', bg='black', fg='white', width=5, height=2, bd=4, font=('Arial',10,'bold'), relief=GROOVE)
Label8.grid(row=0, column=7, padx=8)

Label9 = Label(frame1to0, text='9', bg='black', fg='white', width=5, height=2, bd=4, font=('Arial',10,'bold'), relief=GROOVE)
Label9.grid(row=0, column=8, padx=8)

Label0 = Label(frame1to0, text='0', bg='black', fg='white', width=5, height=2, bd=4, font=('Arial',10,'bold'), relief=GROOVE)
Label0.grid(row=0, column=9, padx=8)

Label10 = Label(frame1to0, text='-', bg='black', fg='white', width=5, height=2, bd=4, font=('Arial',10,'bold'), relief=GROOVE)
Label10.grid(row=0, column=10, padx=8)

Label11 = Label(frame1to0, text='=', bg='black', fg='white', width=5, height=2, bd=4, font=('Arial',10,'bold'), relief=GROOVE)
Label11.grid(row=0, column=11, padx=8)


frameqtop=Frame(keyFrame, bg='black', pady=3)
frameqtop.grid(row=1,column=0)

Labelq = Label(frameqtop, text='Q', bg='black', fg='white', width=5, height=2, bd=4, font=('Arial',10,'bold'), relief=GROOVE)
Labelq.grid(row=1, column=0, padx=8)

Labelw = Label(frameqtop, text='W', bg='black', fg='white', width=5, height=2, bd=4, font=('Arial',10,'bold'), relief=GROOVE)
Labelw.grid(row=1, column=1, padx=8)

Labele = Label(frameqtop, text='E', bg='black', fg='white', width=5, height=2, bd=4, font=('Arial',10,'bold'), relief=GROOVE)
Labele.grid(row=1, column=2, padx=8)

Labelr = Label(frameqtop, text='R', bg='black', fg='white', width=5, height=2, bd=4, font=('Arial',10,'bold'), relief=GROOVE)
Labelr.grid(row=1, column=3, padx=8)

Labelt = Label(frameqtop, text='T', bg='black', fg='white', width=5, height=2, bd=4, font=('Arial',10,'bold'), relief=GROOVE)
Labelt.grid(row=1, column=4, padx=8)

Labely = Label(frameqtop, text='Y', bg='black', fg='white', width=5, height=2, bd=4, font=('Arial',10,'bold'), relief=GROOVE)
Labely.grid(row=1, column=5, padx=8)

Labelu = Label(frameqtop, text='U', bg='black', fg='white', width=5, height=2, bd=4, font=('Arial',10,'bold'), relief=GROOVE)
Labelu.grid(row=1, column=6, padx=8)

Labeli = Label(frameqtop, text='I', bg='black', fg='white', width=5, height=2, bd=4, font=('Arial',10,'bold'), relief=GROOVE)
Labeli.grid(row=1, column=7, padx=8)

Labelo = Label(frameqtop, text='O', bg='black', fg='white', width=5, height=2, bd=4, font=('Arial',10,'bold'), relief=GROOVE)
Labelo.grid(row=1, column=8, padx=8)

Labelp = Label(frameqtop, text='P', bg='black', fg='white', width=5, height=2, bd=4, font=('Arial',10,'bold'), relief=GROOVE)
Labelp.grid(row=1, column=9, padx=8)

Labelop = Label(frameqtop, text='[', bg='black', fg='white', width=5, height=2, bd=4, font=('Arial',10,'bold'), relief=GROOVE)
Labelop.grid(row=1, column=10, padx=8)

Labelpp = Label(frameqtop, text=']', bg='black', fg='white', width=5, height=2, bd=4, font=('Arial',10,'bold'), relief=GROOVE)
Labelpp.grid(row=1, column=11, padx=8)

frameatol = Frame(keyFrame, bg='black', pady=3)
frameatol.grid(row=2, column=0)

Labela = Label(frameatol, text='A', bg='black', fg='white', width=5, height=2, bd=4, font=('Arial',10,'bold'), relief=GROOVE)
Labela.grid(row=2, column=0, padx=8)

Labels = Label(frameatol, text='S', bg='black', fg='white', width=5, height=2, bd=4, font=('Arial',10,'bold'), relief=GROOVE)
Labels.grid(row=2, column=1, padx=8)

Labeld = Label(frameatol, text='D', bg='black', fg='white', width=5, height=2, bd=4, font=('Arial',10,'bold'), relief=GROOVE)
Labeld.grid(row=2, column=2, padx=8)

Labelf = Label(frameatol, text='F', bg='black', fg='white', width=5, height=2, bd=4, font=('Arial',10,'bold'), relief=GROOVE)
Labelf.grid(row=2, column=3, padx=8)

Labelg = Label(frameatol, text='G', bg='black', fg='white', width=5, height=2, bd=4, font=('Arial',10,'bold'), relief=GROOVE)
Labelg.grid(row=2, column=4, padx=8)

Labelh = Label(frameatol, text='H', bg='black', fg='white', width=5, height=2, bd=4, font=('Arial',10,'bold'), relief=GROOVE)
Labelh.grid(row=2, column=5, padx=8)

Labelj = Label(frameatol, text='J', bg='black', fg='white', width=5, height=2, bd=4, font=('Arial',10,'bold'), relief=GROOVE)
Labelj.grid(row=2, column=6, padx=8)

Labelk = Label(frameatol, text='K', bg='black', fg='white', width=5, height=2, bd=4, font=('Arial',10,'bold'), relief=GROOVE)
Labelk.grid(row=2, column=7, padx=8)

Labell = Label(frameatol, text='L', bg='black', fg='white', width=5, height=2, bd=4, font=('Arial',10,'bold'), relief=GROOVE)
Labell.grid(row=2, column=8, padx=8)

Labelkl = Label(frameatol, text=';', bg='black', fg='white', width=5, height=2, bd=4, font=('Arial',10,'bold'), relief=GROOVE)
Labelkl.grid(row=2, column=9, padx=8)

Labelll = Label(frameatol, text='"', bg='black', fg='white', width=5, height=2, bd=4, font=('Arial',10,'bold'), relief=GROOVE)
Labelll.grid(row=2, column=10, padx=8)

frameztom = Frame(keyFrame, bg='black', pady=3)
frameztom.grid(row=3, column=0)

labelz = Label(frameztom, text='Z', bg='black', fg='white', width=5, height=2, bd=4, font=('Arial',10,'bold'), relief=GROOVE)
labelz.grid(row=3, column=0, padx=8)

labelx = Label(frameztom, text='X', bg='black', fg='white', width=5, height=2, bd=4, font=('Arial',10,'bold'), relief=GROOVE)
labelx.grid(row=3, column=1, padx=8)

labelc = Label(frameztom, text='C', bg='black', fg='white', width=5, height=2, bd=4, font=('Arial',10,'bold'), relief=GROOVE)
labelc.grid(row=3, column=2, padx=8)

labelv = Label(frameztom, text='V', bg='black', fg='white', width=5, height=2, bd=4, font=('Arial',10,'bold'), relief=GROOVE)
labelv.grid(row=3, column=3, padx=8)

labelb = Label(frameztom, text='B', bg='black', fg='white', width=5, height=2, bd=4, font=('Arial',10,'bold'), relief=GROOVE)
labelb.grid(row=3, column=4, padx=8)

labeln = Label(frameztom, text='N', bg='black', fg='white', width=5, height=2, bd=4, font=('Arial',10,'bold'), relief=GROOVE)
labeln.grid(row=3, column=5, padx=8)

labelm = Label(frameztom, text='M', bg='black', fg='white', width=5, height=2, bd=4, font=('Arial',10,'bold'), relief=GROOVE)
labelm.grid(row=3, column=6, padx=8)

labelmm = Label(frameztom, text=',', bg='black', fg='white', width=5, height=2, bd=4, font=('Arial',10,'bold'), relief=GROOVE)
labelmm.grid(row=3, column=7, padx=8)

labelnm = Label(frameztom, text='.', bg='black', fg='white', width=5, height=2, bd=4, font=('Arial',10,'bold'), relief=GROOVE)
labelnm.grid(row=3, column=8, padx=8)

labelnn = Label(frameztom, text='/', bg='black', fg='white', width=5, height=2, bd=4, font=('Arial',10,'bold'), relief=GROOVE)
labelnn.grid(row=3, column=9, padx=8)

framespace = Frame(keyFrame, bg='black', pady=3)
framespace.grid(row=4, column=0)

labelspace= Label(framespace,  bg='black', fg='white', width=35, height=2, bd=4, relief=GROOVE)
labelspace.grid(row=4, column=0)



root.bind(r'-',lambda event : colorchange(Label10))
root.bind(r'_',lambda event : colorchange(Label10))
root.bind(r'=',lambda event : colorchange(Label11))
root.bind(r'+',lambda event : colorchange(Label11))
root.bind(r'[',lambda event : colorchange(Labelop))
root.bind(r']',lambda event : colorchange(Labelpp))
root.bind(r'{',lambda event : colorchange(Labelop))
root.bind(r'}',lambda event : colorchange(Labelpp))
root.bind(r';',lambda event : colorchange(Labelkl))
root.bind(r':',lambda event : colorchange(Labelkl))
#root.bind(r'',lambda event : colorchange(Labelll))
root.bind(r'"',lambda event : colorchange(Labelll))
root.bind(r',',lambda event : colorchange(labelmm))
#root.bind(r"<",lambda event : colorchange(labelmm))
root.bind(r'.',lambda event : colorchange(labelnm))
root.bind(r'>',lambda event : colorchange(labelnm))
root.bind(r'/',lambda event : colorchange(labelnn))
root.bind(r'?',lambda event : colorchange(labelnn))
root.bind('<space>',lambda event : colorchange(labelspace))


numbers_list=['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
numbers_label=[ Label0, Label1, Label2, Label3, Label4, Label5, Label6, Label7, Label8, Label9,]

for i in range(10):
    root.bind(i, lambda event , x= numbers_label[i] : colorchange(x))

small_alphabet_list=list(string.ascii_lowercase)
capital_alphabet_list=list(string.ascii_uppercase)

label_alphabet = [Labela,labelb, labelc, Labeld, Labele, Labelf, Labelg, Labelh, Labeli,Labelj, Labelk,Labell, labelm,labeln,Labelo,Labelp,Labelq, Labelr,Labels,
                  Labelt,Labelu,labelv,Labelw, labelx, Labely,labelz]

for i in range(26):
    root.bind(small_alphabet_list[i], lambda event, x=label_alphabet[i]: colorchange(x))
    root.bind(capital_alphabet_list[i], lambda event, x=label_alphabet[i]: colorchange(x))





root.mainloop()