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
		w.write('1: Up Arrow Key == Mouse Up\n2: Down Arrow Key == Mouse Down\n3: 0 Key == Click The Mouse\n4: - Key == Close Any Program Or If Needed Can Be Used To Shutdown Computer\n + Key == Clear All The Written Characters')
		w.close()
		# Root Starting..
		root = Tk()
		root.geometry('700x700')
		root.minsize(700,700)
		root.maxsize(700,700)
		root.title('( Registered ) Automatic Mouse Controller')

		# Setting Variables
		checking = StringVar()
		checking.set('Welcome To Laptop Mouse Controller')
		activate = StringVar()
		activate.set('Hey There, Press ctrl+1 To Activate Me')
		exit = StringVar()
		mouse = StringVar()
		mouse.set('Mouse Sensetivity [1,100]')
		en = IntVar()
		en.set(10)

		# Defining
		def nowdoit():
			exit.set('''To Close Me Don't Press X But Press ctrl+2''')

			# left.open('left.config','w+')
			# right.open('right.config','w+')
			# up.open('up.config','w+')
			# down.open('down.config','w+')
			for i in range(0,9999999999999):
				root.update()
				a = pyautogui.position()
				if ((en.get()) < 101):
					if keyboard.is_pressed('up'):
						aa = a[0]
						bb = a[1]-(en.get())
						pyautogui.mouseUp(x=aa, y=bb)
					elif keyboard.is_pressed('down'):
						aa = a[0]
						bb = a[1]+(en.get())
						pyautogui.mouseUp(x=aa, y=bb)
					elif keyboard.is_pressed('left'):
						aa = a[0]-(en.get())
						bb = a[1]
						pyautogui.mouseUp(x=aa, y=bb)
					elif keyboard.is_pressed('right'):
						aa = a[0]+(en.get())
						bb = a[1]
						pyautogui.mouseUp(x=aa, y=bb)
					elif keyboard.is_pressed('+'):
						pyautogui.click()
						pyautogui.hotkey('ctrl','a')
						pyautogui.press('backspace')
					elif keyboard.is_pressed('0'):
						pyautogui.click()
					elif keyboard.is_pressed('esc'):
						activate.set('Hey There, Press ctrl+1 To Activate Me')
						break
					elif keyboard.is_pressed('ctrl+2'):
						os.system('taskkill /PID python.exe')
						os.system('cls')
						quit()
					elif keyboard.is_pressed('-'):
						pyautogui.hotkey('alt','f4')
				else:
					pass
					

		Label(textvariable = checking,font = "impact 20 italic",bg = "black",fg = "white").pack()
		Label(textvariable = mouse,font = "impact 20 italic",bg = "black",fg = "white").pack()
		Entry(textvariable = en,font = "comicsansms 14 italic",bg = "white",fg = "black").pack()
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
			if keyboard.is_pressed('ctrl+1'):
				activate.set('Activated Successfully')
				nowdoit()
		root.mainloop()
	else:
		print('Liscence Key Is Wrong..')
		f.close()
except:
	root = Tk()

	# Showing Error Message
	tmsg.showinfo('File Not Found','UnExpected Error Occured')
	quit()

	root.mainloop()
