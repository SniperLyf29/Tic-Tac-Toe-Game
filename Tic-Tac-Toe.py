import tkinter.messagebox
from tkinter import *

root=Tk()
root.geometry("1350x750+0+0")
root.title("Tic Tac Toe")
root.configure(background="Cadet Blue")

'''###################################Frames and Labels Start#############################################'''

Topf=Frame(root,bg="Cadet Blue",pady=2,
	width=1350,height=100,relief=RIDGE)
Topf.grid(row=0,column=0)

lblTitle=Label(Topf,font=('arial',50,'bold'),
	text="Welcome to Tic Tac Toe",bd=21,
	bg="Cadet Blue",fg="Cornsilk",justify=CENTER)
lblTitle.grid(row=0,column=0)

MainFrame=Frame(root,bg="Powder Blue",bd=10,
	width=1350,height=600,relief=RIDGE)
MainFrame.grid(row=1,column=0)

LeftFrame=Frame(MainFrame,bg="Cadet Blue",pady=2,
	bd=10,padx=10,width=750,height=500,relief=RIDGE)
LeftFrame.pack(side=LEFT)

RightFrame=Frame(MainFrame,bg="Cadet Blue",pady=2,
	bd=10,padx=10,width=560,height=500,relief=RIDGE)
RightFrame.pack(side=RIGHT)

RightFrame1=Frame(RightFrame,bg="Cadet Blue",pady=2,
	bd=10,padx=10,width=560,height=200,relief=RIDGE)
RightFrame1.grid(row=0,column=0)

RightFrame2=Frame(RightFrame,bg="Cadet Blue",pady=2,
	bd=10,padx=10,width=560,height=200,relief=RIDGE)
RightFrame2.grid(row=1,column=0)

'''###################################Buttons and Entries#############################################'''

PlayerX=IntVar()
PlayerO=IntVar()

PlayerX.set(0)
PlayerO.set(0)

button = StringVar()
click=True

def checker(buttons):
	global click
	if buttons["text"]=="" and click == True:

		buttons["text"] = "X"
		click = False
		scorekeeper()

	elif buttons["text"]=="" and click == False:

		buttons["text"] = "O"
		click = True
		scorekeeper()

def scorekeeper():
	if button1['text']=='X' and button2['text']=='X' and button3['text']=='X':
		
		button1.configure(background="powder blue")
		button2.configure(background="powder blue")
		button3.configure(background="powder blue")

		n=float(PlayerX.get())
		score=n+1
		PlayerX.set(score)
		tkinter.messagebox.showinfo("Winner X","You have just won a game!")

	elif button4['text']=='X' and button5['text']=='X' and button6['text']=='X':
		
		button4.configure(background="#bf171f")
		button5.configure(background="#bf171f")
		button6.configure(background="#bf171f")

		n=float(PlayerX.get())
		score=n+1
		PlayerX.set(score)
		tkinter.messagebox.showinfo("Winner X","You have just won a game!")

	elif button7['text']=='X' and button8['text']=='X' and button9['text']=='X':
		
		button7.configure(background="#17bf87")
		button8.configure(background="#17bf87")
		button9.configure(background="#17bf87")

		n=float(PlayerX.get())
		score=n+1
		PlayerX.set(score)
		tkinter.messagebox.showinfo("Winner X","You have just won a game!")


	elif button1['text']=='X' and button5['text']=='X' and button9['text']=='X':
		
		button1.configure(background="#a3e300")
		button5.configure(background="#a3e300")
		button9.configure(background="#a3e300")

		n=float(PlayerX.get())
		score=n+1
		PlayerX.set(score)
		tkinter.messagebox.showinfo("Winner X","You have just won a game!")

	elif button3['text']=='X' and button5['text']=='X' and button7['text']=='X':
		
		button3.configure(background="#f2870c")
		button5.configure(background="#f2870c")
		button7.configure(background="#f2870c")

		n=float(PlayerX.get())
		score=n+1
		PlayerX.set(score)
		tkinter.messagebox.showinfo("Winner X","You have just won a game!")

	elif button1['text']=='X' and button4['text']=='X' and button7['text']=='X':
		
		button1.configure(background="#ab05ab")
		button4.configure(background="#ab05ab")
		button7.configure(background="#ab05ab")

		n=float(PlayerX.get())
		score=n+1
		PlayerX.set(score)
		tkinter.messagebox.showinfo("Winner X","You have just won a game!")

	elif button2['text']=='X' and button5['text']=='X' and button8['text']=='X':
		
		button2.configure(background="#f2bbd5")
		button5.configure(background="#f2bbd5")
		button8.configure(background="#f2bbd5")

		n=float(PlayerX.get())
		score=n+1
		PlayerX.set(score)
		tkinter.messagebox.showinfo("Winner X","You have just won a game!")

	elif button3['text']=='X' and button6['text']=='X' and button9['text']=='X':
		
		button3.configure(background="#857aa1")
		button6.configure(background="#857aa1")
		button9.configure(background="#857aa1")

		n=float(PlayerX.get())
		score=n+1
		PlayerX.set(score)
		tkinter.messagebox.showinfo("Winner X","You have just won a game!")





	if button1['text']=='O' and button2['text']=='O' and button3['text']=='O':
		
		button1.configure(background="powder blue")
		button2.configure(background="powder blue")
		button3.configure(background="powder blue")

		n=float(PlayerO.get())
		score=n+1
		PlayerO.set(score)
		tkinter.messagebox.showinfo("Winner O","You have just won a game!")

	elif button4['text']=='O' and button5['text']=='O' and button6['text']=='O':
		
		button4.configure(background="#bf171f")
		button5.configure(background="#bf171f")
		button6.configure(background="#bf171f")

		n=float(PlayerO.get())
		score=n+1
		PlayerO.set(score)
		tkinter.messagebox.showinfo("Winner O","You have just won a game!")

	elif button7['text']=='O' and button8['text']=='O' and button9['text']=='O':
		
		button7.configure(background="#17bf87")
		button8.configure(background="#17bf87")
		button9.configure(background="#17bf87")

		n=float(PlayerO.get())
		score=n+1
		PlayerO.set(score)
		tkinter.messagebox.showinfo("Winner O","You have just won a game!")


	elif button1['text']=='O' and button5['text']=='O' and button9['text']=='O':
		
		button1.configure(background="#a3e300")
		button5.configure(background="#a3e300")
		button9.configure(background="#a3e300")

		n=float(PlayerO.get())
		score=n+1
		PlayerO.set(score)
		tkinter.messagebox.showinfo("Winner O","You have just won a game!")

	elif button3['text']=='O' and button5['text']=='O' and button7['text']=='O':
		
		button3.configure(background="#f2870c")
		button5.configure(background="#f2870c")
		button7.configure(background="#f2870c")

		n=float(PlayerO.get())
		score=n+1
		PlayerO.set(score)
		tkinter.messagebox.showinfo("Winner O","You have just won a game!")

	elif button1['text']=='O' and button4['text']=='O' and button7['text']=='O':
		
		button1.configure(background="#47993c")
		button4.configure(background="#47993c")
		button7.configure(background="#47993c")

		n=float(PlayerO.get())
		score=n+1
		PlayerO.set(score)
		tkinter.messagebox.showinfo("Winner O","You have just won a game!")

	elif button2['text']=='O' and button5['text']=='O' and button8['text']=='O':
		
		button2.configure(background="#0fbda6")
		button5.configure(background="#0fbda6")
		button8.configure(background="#0fbda6")

		n=float(PlayerO.get())
		score=n+1
		PlayerO.set(score)
		tkinter.messagebox.showinfo("Winner O","You have just won a game!")

	elif button3['text']=='O' and button6['text']=='O' and button9['text']=='O':
		
		button3.configure(background="#def207")
		button6.configure(background="#def207")
		button9.configure(background="#def207")

		n=float(PlayerO.get())
		score=n+1
		PlayerO.set(score)
		tkinter.messagebox.showinfo("Winner O","You have just won a game!")


def reset():
	button1['text']=''
	button2['text']=''
	button3['text']=''
	button4['text']=''
	button5['text']=''
	button6['text']=''
	button7['text']=''
	button8['text']=''
	button9['text']=''

	button1.configure(background="gainsboro")
	button2.configure(background="gainsboro")
	button3.configure(background="gainsboro")
	button4.configure(background="gainsboro")
	button5.configure(background="gainsboro")
	button6.configure(background="gainsboro")
	button7.configure(background="gainsboro")
	button8.configure(background="gainsboro")
	button9.configure(background="gainsboro")

def NewGame():
	reset()
	PlayerX.set(0)
	PlayerO.set(0)	


lblPlayerX=Label(RightFrame1,text="PlayerX:",font=('arial',50,'bold'),		
	padx=2,pady=2,bg="Cadet Blue")
lblPlayerX.grid(row=0,column=0,sticky=W)

txtPlayerX=Entry(RightFrame1,font=('arial',40,'bold'),bd=2,
	fg="black",textvariable=PlayerX,width=14,justify=LEFT).grid(row=0, column=1)

lblPlayerO=Label(RightFrame1,text="PlayerO:",font=('arial',50,'bold'),		
	padx=2,pady=2,bg="Cadet Blue")
lblPlayerO.grid(row=1,column=0,sticky=W)

txtPlayerO=Entry(RightFrame1,font=('arial',40,'bold'),bd=2,
	fg="black",textvariable=PlayerO,width=14,justify=LEFT).grid(row=1, column=1)




btnReset=Button(RightFrame2,text="Reset",font=('Time 26 bold'),
	height=3,width=20,bg="gainsboro",command=reset)
btnReset.grid(row=0,column=0)

btnNew=Button(RightFrame2,text="New Game",font=('Time 26 bold'),
	height=3,width=20,bg="gainsboro",command=NewGame)
btnNew.grid(row=1,column=0)




button1=Button(LeftFrame,text="",font=('Time 26 bold'),
	height=3,width=8,bg="gainsboro",command=lambda:checker(button1))
button1.grid(row=1,column=0,sticky=S+N+E+W)

button2=Button(LeftFrame,text="",font=('Time 26 bold'),
	height=3,width=8,bg="gainsboro",command=lambda:checker(button2))
button2.grid(row=1,column=1,sticky=S+N+E+W)

button3=Button(LeftFrame,text="",font=('Time 26 bold'),
	height=3,width=8,bg="gainsboro",command=lambda:checker(button3))
button3.grid(row=1,column=2,sticky=S+N+E+W)

button4=Button(LeftFrame,text="",font=('Time 26 bold'),
	height=3,width=8,bg="gainsboro",command=lambda:checker(button4))
button4.grid(row=2,column=0,sticky=S+N+E+W)

button5=Button(LeftFrame,text="",font=('Time 26 bold'),
	height=3,width=8,bg="gainsboro",command=lambda:checker(button5))
button5.grid(row=2,column=1,sticky=S+N+E+W)

button6=Button(LeftFrame,text="",font=('Time 26 bold'),
	height=3,width=8,bg="gainsboro",command=lambda:checker(button6))
button6.grid(row=2,column=2,sticky=S+N+E+W)

button7=Button(LeftFrame,text="",font=('Time 26 bold'),
	height=3,width=8,bg="gainsboro",command=lambda:checker(button7))
button7.grid(row=3,column=0,sticky=S+N+E+W)

button8=Button(LeftFrame,text="",font=('Time 26 bold'),
	height=3,width=8,bg="gainsboro",command=lambda:checker(button8))
button8.grid(row=3,column=1,sticky=S+N+E+W)

button9=Button(LeftFrame,text="",font=('Time 26 bold'),
	height=3,width=8,bg="gainsboro",command=lambda:checker(button9))
button9.grid(row=3,column=2,sticky=S+N+E+W)


root.mainloop()
