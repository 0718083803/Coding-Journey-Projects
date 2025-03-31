from tkinter import *
from tkinter import DISABLED, NORMAL, messagebox
import customtkinter

customtkinter.set_appearance_mode('Dark')
customtkinter.set_default_color_theme('dark-blue')

root = customtkinter.CTk()
root.title("Tic Tac Toe")
root.geometry('450x475')
root.iconbitmap('icon.ico')

#Declaration Of All Variables
h=150#Height
w=150#Width
win_colour='green'
x_turn=True
x_score = 0
y_score = 0
#Checking Win Or Lose
#Clearing The whole Game
def clear():
    btn_1.configure(text='',state=NORMAL,fg_color='White')
    btn_2.configure(text='',state=NORMAL,fg_color='White')
    btn_3.configure(text='',state=NORMAL,fg_color='White')
    btn_4.configure(text='',state=NORMAL,fg_color='White')
    btn_5.configure(text='',state=NORMAL,fg_color='White')
    btn_6.configure(text='',state=NORMAL,fg_color='White')
    btn_7.configure(text='',state=NORMAL,fg_color='White')
    btn_8.configure(text='',state=NORMAL,fg_color='White')
    btn_9.configure(text='',state=NORMAL,fg_color='White')
#Replaying
def replay():
  answer = messagebox.askyesno(message="Do You Want To Replay?")
  if answer == True:
      clear()
  elif answer == False:
      root.quit()
#Disabling
def disable():
    btn_1.configure(state=DISABLED)
    btn_2.configure(state=DISABLED)   
    btn_3.configure(state=DISABLED)
    btn_4.configure(state=DISABLED)
    btn_5.configure(state=DISABLED)
    btn_6.configure(state=DISABLED)
    btn_7.configure(state=DISABLED)
    btn_8.configure(state=DISABLED)
    btn_9.configure(state=DISABLED)
#Checking if there is a win after every move
def checkwin():
    #Checking Winning of X
    global y_score
    global x_score
    if btn_1.cget('text') == 'X' and btn_2.cget('text') == 'X' and btn_3.cget('text')=='X':
          btn_1.configure(fg_color=win_colour)
          btn_2.configure(fg_color=win_colour)
          btn_3.configure(fg_color=win_colour)
          messagebox.showinfo(message="Player X WINS!!!")
          x_score+=1
          x_score_lbl.configure(text=f"X Score: {x_score}")
          disable()
          replay()
    elif btn_4.cget('text') == 'X' and btn_5.cget('text') == 'X' and btn_6.cget('text')=='X':
          btn_4.configure(fg_color=win_colour)
          btn_5.configure(fg_color=win_colour)
          btn_6.configure(fg_color=win_colour)
          messagebox.showinfo(message="Player X WINS!!!")
          x_score+=1
          x_score_lbl.configure(text=f"X Score: {x_score}")
          disable()
          replay()
    elif btn_7.cget('text') == 'X' and btn_8.cget('text') == 'X' and btn_9.cget('text') =='X':
          btn_7.configure(fg_color=win_colour)
          btn_8.configure(fg_color=win_colour)
          btn_9.configure(fg_color=win_colour)
          messagebox.showinfo(message="Player X WINS!!!")
          x_score+=1
          x_score_lbl.configure(text=f"X Score: {x_score}")
          disable()
          replay()
    elif btn_1.cget('text') == 'X' and btn_4.cget('text') == 'X' and btn_7.cget('text') =='X':
          btn_1.configure(fg_color=win_colour)
          btn_4.configure(fg_color=win_colour)
          btn_7.configure(fg_color=win_colour)
          messagebox.showinfo(message="Player X WINS!!!")
          x_score+=1
          x_score_lbl.configure(text=f"X Score: {x_score}")
          disable()
          replay()
    elif btn_2.cget('text') == 'X' and btn_5.cget('text') == 'X' and btn_8.cget('text') =='X':
          btn_2.configure(fg_color=win_colour)
          btn_5.configure(fg_color=win_colour)
          btn_8.configure(fg_color=win_colour)
          messagebox.showinfo(message="Player X WINS!!!")
          x_score+=1
          x_score_lbl.configure(text=f"X Score: {x_score}")
          disable()
          replay()
    elif btn_3.cget('text') == 'X' and btn_6.cget('text') == 'X' and btn_9.cget('text')=='X':
          btn_3.configure(fg_color=win_colour)
          btn_6.configure(fg_color=win_colour)
          btn_9.configure(fg_color=win_colour)
          messagebox.showinfo(message="Player X WINS!!!")
          x_score+=1
          x_score_lbl.configure(text=f"X Score: {x_score}")
          disable()
          replay()
    elif btn_3.cget('text')== 'X' and btn_5.cget('text') == 'X' and btn_7.cget('text')=='X':
          btn_3.configure(fg_color=win_colour)
          btn_5.configure(fg_color=win_colour)
          btn_7.configure(fg_color=win_colour)
          messagebox.showinfo(message="Player X WINS!!!")
          x_score+=1
          x_score_lbl.configure(text=f"X Score: {x_score}")
          disable()
          replay()
    elif btn_1.cget('text') == 'X' and btn_5.cget('text') == 'X' and btn_9.cget('text') =='X':
          btn_1.configure(fg_color=win_colour)
          btn_5.configure(fg_color=win_colour)
          btn_9.configure(fg_color=win_colour)
          messagebox.showinfo(message="Player X WINS!!!")
          x_score+=1
          x_score_lbl.configure(text=f"X Score: {x_score}")
          disable()
          replay()
   #Checking Y winning
    elif btn_1.cget('text') == 'Y' and btn_2.cget('text') == 'Y' and btn_3.cget('text')=='Y':
        btn_1.configure(fg_color=win_colour)
        btn_2.configure(fg_color=win_colour)
        btn_3.configure(fg_color=win_colour)
        messagebox.showinfo(message="Player Y WINS!!!")
        y_score+=1
        y_score_lbl.configure(text=f"Y Score: {y_score}")
        disable()
        replay()
    elif btn_4.cget('text') == 'Y' and btn_5.cget('text') == 'Y' and btn_6.cget('text')=='Y':
          btn_4.configure(fg_color=win_colour)
          btn_5.configure(fg_color=win_colour)
          btn_6.configure(fg_color=win_colour)
          messagebox.showinfo(message="Player Y WINS!!!")
          y_score+=1
          y_score_lbl.configure(text=f"Y Score: {y_score}")
          disable()
          replay()
    elif btn_7.cget('text') == 'Y' and btn_8.cget('text') == 'Y' and btn_9.cget('text') =='Y':
      btn_7.configure(fg_color=win_colour)
      btn_8.configure(fg_color=win_colour)
      btn_9.configure(fg_color=win_colour)
      messagebox.showinfo(message="Player Y WINS!!!")
      y_score+=1
      y_score_lbl.configure(text=f"Y Score: {y_score}")
      disable()
      replay()
    elif btn_1.cget('text') == 'Y' and btn_3.cget('text') == 'Y' and btn_7.cget('text')=='Y':
      btn_1.configure(fg_color=win_colour)
      btn_5.configure(fg_color=win_colour)
      btn_7.configure(fg_color=win_colour)
      messagebox.showinfo(message="Player Y WINS!!!")
      y_score+=1
      y_score_lbl.configure(text=f"Y Score: {y_score}")
      disable()
      replay()
    elif btn_2.cget('text') == 'Y' and btn_5.cget('text') == 'Y' and btn_8.cget('text')=='Y':
      btn_2.configure(fg_color=win_colour)
      btn_5.configure(fg_color=win_colour)
      btn_8.configure(fg_color=win_colour)
      messagebox.showinfo(message="Player Y WINS!!!")
      y_score+=1
      y_score_lbl.configure(text=f"Y Score: {y_score}")
      disable()
      replay()
    elif btn_3.cget('text') == 'Y' and btn_6.cget('text') == 'Y' and btn_9.cget('text')=='Y':
      btn_3.configure(fg_color=win_colour)
      btn_6.configure(fg_color=win_colour)
      btn_9.configure(fg_color=win_colour)
      messagebox.showinfo(message="Player Y WINS!!!")
      y_score+=1
      y_score_lbl.configure(text=f"Y Score: {y_score}")
      disable()
      replay()
    elif btn_3.cget('text') == 'Y' and btn_5.cget('text') == 'Y' and btn_7.cget('text')=='Y':
      btn_3.configure(fg_color=win_colour)
      btn_5.configure(fg_color=win_colour)
      btn_7.configure(fg_color=win_colour)
      messagebox.showinfo(message="Player Y WINS!!!")
      y_score+=1
      y_score_lbl.configure(text=f"Y Score: {y_score}")
      disable()
      replay()
    elif btn_1.cget('text') == 'Y' and btn_5.cget('text') == 'Y' and btn_9.cget('text')=='Y':
      btn_1.configure(fg_color=win_colour)
      btn_5.configure(fg_color=win_colour)
      btn_9.configure(fg_color=win_colour)
      messagebox.showinfo(message="Player Y WINS!!!")
      y_score+=1
      y_score_lbl.configure(text=f"Y Score: {y_score}")
      disable()
      replay()
    elif btn_1.cget('text') != '' and btn_2.cget('text') != '' and btn_3.cget('text') != '' and btn_4.cget('text') != '' and btn_5.cget('text') != '' and btn_6.cget('text') != '' and btn_7.cget('text') != '' and btn_8.cget('text') != '' and btn_9.cget('text') != '' :
        messagebox.showinfo(message="Draw!!!")
        replay()
#Putting The Moves
def xy1(): 

  global x_turn  
  if x_turn == True and btn_1.cget('text')=='':
      btn_1.configure(text="X",font=('Helvetia',80),text_color='Black')
      x_turn=False 
  elif x_turn == False and btn_1.cget('text')=='':
      btn_1.configure(text="Y",font=('Helvetia',90),text_color='Black')
      x_turn=True
  checkwin()  
def xy2():
  global x_turn  
  if x_turn == True and btn_2.cget('text')=='':
      btn_2.configure(text="X",font=('Helvetia',80),text_color='Black')
      x_turn=False
  elif x_turn == False and btn_2.cget('text')=='':
      btn_2.configure(text="Y",font=('Helvetia',90),text_color='Black')
      x_turn=True
  checkwin()
def xy3():
  global x_turn  
  if x_turn == True and btn_3.cget('text')=='' :
      btn_3.configure(text="X",font=('Helvetia',80),text_color='Black')
      x_turn=False
  elif x_turn == False and btn_3.cget('text')=='':
      btn_3.configure(text="Y",font=('Helvetia',90),text_color='Black')
      x_turn=True
  checkwin()
def xy4():
  global x_turn  
  if x_turn == True and btn_4.cget('text')=='':
      btn_4.configure(text="X",font=('Helvetia',80),text_color='Black')
      x_turn=False
  elif x_turn == False and btn_4.cget('text')=='':
      btn_4.configure(text="Y",font=('Helvetia',90),text_color='Black')
      x_turn=True
  checkwin()
def xy5():
  global x_turn  
  if x_turn == True and btn_5.cget('text')=='':
      btn_5.configure(text="X",font=('Helvetia',80),text_color='Black')
      x_turn=False
  elif x_turn == False and btn_5.cget('text')=='':
      btn_5.configure(text="Y",font=('Helvetia',90),text_color='Black')
      x_turn=True
  checkwin()
def xy6():
  global x_turn  
  if x_turn == True and btn_6.cget('text')=='':
      btn_6.configure(text="X",font=('Helvetia',80),text_color='Black')
      x_turn=False
  elif x_turn == False and btn_6.cget('text')=='':
      btn_6.configure(text="Y",font=('Helvetia',90),text_color='Black')
      x_turn=True
  checkwin()
def xy7():
  global x_turn  
  if x_turn == True and btn_7.cget('text')=='':
      btn_7.configure(text="X",font=('Helvetia',80),text_color='Black')
      x_turn=False
  elif x_turn == False and btn_7.cget('text')=='':
      btn_7.configure(text="Y",font=('Helvetia',90),text_color='Black')
      x_turn=True
  checkwin()
def xy8():
  global x_turn  
  if x_turn == True and btn_8.cget('text')=='' :
      btn_8.configure(text="X",font=('Helvetia',80),text_color='Black')
      x_turn=False
  elif x_turn == False and btn_8.cget('text')=='':
      btn_8.configure(text="Y",font=('Helvetia',90),text_color='Black')
      x_turn=True
  checkwin()
def xy9():
  global x_turn  
  if x_turn == True and btn_9.cget('text')=='':
      btn_9.configure(text="X",font=('Helvetia',80),text_color='Black')
      x_turn=False
  elif x_turn == False and btn_9.cget('text')=='':
      btn_9.configure(text="Y",font=('Helvetia',90),text_color='Black')
      x_turn=True
  checkwin()


#Score Keeper
x_score_lbl = customtkinter.CTkLabel(root,text=f'X Score: {x_score}',font=('Helvetica',20))        
x_score_lbl.grid(row=0,column=0)
y_score_lbl = customtkinter.CTkLabel(root,text=f'Y Score: {y_score}',font=("Helvetica",20))
y_score_lbl.grid(row=0,column=2)
#Buttons1-9
btn_1 = customtkinter.CTkButton(root,text='',height=h,width=w,command=xy1,corner_radius=0,fg_color='White')
btn_1.grid(row=1,column=0)
btn_2 = customtkinter.CTkButton(root,text='',height=h,width=w,command=xy2,corner_radius=0,fg_color='White')
btn_2.grid(row=1,column=1)
btn_3 = customtkinter.CTkButton(root,text='',height=h,width=w,command=xy3,corner_radius=0,fg_color='White')
btn_3.grid(row=1,column=2)
btn_4 = customtkinter.CTkButton(root,text='',height=h,width=w,command=xy4,corner_radius=0,fg_color='White')
btn_4.grid(row=2,column=0)
btn_5 = customtkinter.CTkButton(root,text='',height=h,width=w,command=xy5,corner_radius=0,fg_color='White')
btn_5.grid(row=2,column=1)
btn_6 = customtkinter.CTkButton(root,text='',height=h,width=w,command=xy6,corner_radius=0,fg_color='White')
btn_6.grid(row=2,column=2)
btn_7 = customtkinter.CTkButton(root,text='',height=h,width=w,command=xy7,corner_radius=0,fg_color='White')
btn_7.grid(row=3,column=0)
btn_8 = customtkinter.CTkButton(root,text='',height=h,width=w,command=xy8,corner_radius=0,fg_color='White')
btn_8.grid(row=3,column=1)
btn_9 = customtkinter.CTkButton(root,text='',height=h,width=w,command=xy9,corner_radius=0,fg_color='White')
btn_9.grid(row=3,column=2)

root.mainloop()