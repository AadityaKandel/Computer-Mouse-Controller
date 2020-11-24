import os
import keyboard
import time
from tkinter import *
import tkinter.messagebox as tmsg
from PIL import ImageTk, Image
import pyautogui
# Import Success

try:
	f = open('liscence.dll')
	for words in f:
		pass
	if '78kfsid93859nfas' in words:
		f.close()
		w = open('How To Use.txt','w+')
		w.write('1: Mouse Up == Up Arrow Key\n2: Mouse Down == Down Arrow Key\n3: 0 Key == Click The Mouse')
		w.close()
		# Root Starting..
		root = Tk()

		root.title('( Registered ) Automatic Mouse Controller')

		# Setting Variables
		checking = StringVar()
		checking.set('Welcome To Laptop Mouse Controller')
		activate = StringVar()
		activate.set('Hey There, Press F1 To Activate Me')
		exit = StringVar()

		# Defining
		def nowdoit():
			exit.set('''To Close Me Don't Press X But Press F6''')
			for i in range(0,9999999999999):
				root.update()
				a = pyautogui.position()
				if keyboard.is_pressed('up'):
					aa = a[0]
					bb = a[1]-10
					pyautogui.mouseUp(x=aa, y=bb)
				elif keyboard.is_pressed('down'):
					aa = a[0]
					bb = a[1]+10
					pyautogui.mouseUp(x=aa, y=bb)
				elif keyboard.is_pressed('left'):
					aa = a[0]-10
					bb = a[1]
					pyautogui.mouseUp(x=aa, y=bb)
				elif keyboard.is_pressed('right'):
					aa = a[0]+10
					bb = a[1]
					pyautogui.mouseUp(x=aa, y=bb)
				elif keyboard.is_pressed('end'):
					pyautogui.click()
					pyautogui.hotkey('ctrl','a')
					pyautogui.press('backspace')
				elif keyboard.is_pressed('0'):
					pyautogui.click()
				elif keyboard.is_pressed('esc'):
					activate.set('Hey There, Press F1 To Activate Me')
					break
				elif keyboard.is_pressed('f6'):
					os.system('taskkill /PID python.exe')
					os.system('cls')
					quit()

		Label(textvariable = checking,font = "impact 20 italic",bg = "black",fg = "white").pack()
		try:
			# Importing Images
			img = ImageTk.PhotoImage(Image.open("main.automatic"))
			panel = Label(image = img,bg = "black")
			panel.pack()
		except:
			tmsg.showinfo('Error','main.automatic Not Found')
			os.system('taskkill /PID python.exe')
			os.system('cls')
			quit()

		Label(textvariable = activate,font = "impact 20",bg = "black",fg = "white").pack()
		Label(textvariable = exit,font = "impact 20 italic",bg = "black",fg = "white",pady = 10).pack()		
		root.config(bg = "black")

		# Making For I Range
		for i in range(0,9999999999999999):
			root.update()
			if keyboard.is_pressed('f1'):
				activate.set('Activated Successfully')
				nowdoit()
		root.mainloop()
	else:
		print('Liscence Key Is Wrong..')
		f.close()
except:
	root = Tk()

	# Showing Error Message
	tmsg.showinfo('File Not Found','Error, liscence.dll is not Found')
	quit()

	root.mainloop()