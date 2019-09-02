from tkinter import Tk,Label,Button,Frame
from datetime import datetime

proceso=0
i = 0
running = False
first = True

def iniciar():
    global proceso
    global tini
    global running
    running = True
    # Save the starting time of our timer as a time reference
    tini = datetime.now()

    # Calls the main function that will repeat recusively to work as a precise clock
    proceso=time.after(1, ejecutar)
 
def ejecutar():
  global proceso
  global tini
  global time

  now = datetime.now()-tini
  
  # Write the time
  date = strfdelta(now, "{hours}:{minutes}:{seconds}:{centiseconds}")
  time['text'] = str(date)
  
  #Calls itself recursively every ms updating the time on the timer
  proceso=time.after(1, ejecutar)

def split():
  global proceso
  global i, first
  global lista
  global clock

  if (running==True):
    if (i==0) and (first==True):
      
      clock = datetime.now()
      partial = datetime.now()-tini
      timesplit = strfdelta(partial, "{hours}:{minutes}:{seconds}:{centiseconds}")
      lista[i]['text'] = str(timesplit)
      first = False
    else:
      partial = datetime.now()-clock
      timesplit = strfdelta(partial, "{hours}:{minutes}:{seconds}:{centiseconds}")
      lista[i]['text'] = str(timesplit)
      clock = datetime.now()
    i += 1
    if (i>=3):
      i = 0

def parar():
    global proceso
    global running
    global first, i
    running = False
    first = True
    i = 0
    time.after_cancel(proceso)
   
def strfdelta(tdelta, fmt):
    d = {"days": tdelta.days}
    d["hours"], rem = divmod(tdelta.seconds, 3600)
    d["minutes"], d["seconds"] = divmod(rem, 60)
    d["centiseconds"] = int(tdelta.microseconds/10000)
    return fmt.format(**d)

def salir():
    global root
    root.destroy()

root = Tk()
root.title('Cronometro')
root.geometry('225x400') # anchura x altura

time = Label(root, fg='red', width=20, font=("","18"))
time.pack()

split_one=Label(root, fg='red', width=20, font=("","14"))
split_one.pack()
split_two=Label(root, fg='red', width=20, font=("","14"))
split_two.pack()
split_tre=Label(root, fg='red', width=20, font=("","14"))
split_tre.pack()

lista = [split_one, split_two, split_tre]

# Generamos un frame para poner los botones de iniciar y parar
frame=Frame(root)
btnIniciar=Button(frame, fg='blue', text='Iniciar', command=iniciar)
btnIniciar.grid(row=2, column=1)
btnSplit=Button(frame, fg='blue', text='Split', command=split)
btnSplit.grid(row=2, column=2)
btnParar=Button(frame, fg='blue', text='Parar', command=parar)
btnParar.grid(row=2, column=3)
btnSalir=Button(frame, fg='blue', text='Salir', command=salir)
btnSalir.grid(row=2, column=4)

frame.pack(side="bottom")
 
root.mainloop()
