from tkinter import Tk,Label,Button,Frame
from datetime import datetime
proceso=0
i = 0
running = False
first = 0
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
  date = strfdelta(now, "{hours}:{minutes}:{seconds}")
  cs = int(now.microseconds/10000)
  time['text'] = str(date)+":"+str(cs)
  
  #Calls itself recursively every ms updating the time on the timer
  proceso=time.after(1, ejecutar)

def split():
  global proceso
  global i, first
  global lista
  global partial

  if (running==True):
    if (i==0) and (first==0):
      print(first)
      partial = datetime.now()
      lista[i]['text'] = datetime.now()-tini
      first = 1
    else:
      lista[i]['text'] = datetime.now()-partial
      partial = datetime.now()
    i += 1
    if (i>=3):
      i =0

def parar():
    global proceso
    global running
    running = False
    time.after_cancel(proceso)
   
def strfdelta(tdelta, fmt):
    d = {"days": tdelta.days}
    d["hours"], rem = divmod(tdelta.seconds, 3600)
    d["minutes"], d["seconds"] = divmod(rem, 60)
    return fmt.format(**d)
 
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
btnSalir=Button(frame, fg='blue', text='Salir', command=quit)
btnSalir.grid(row=2, column=4)

frame.pack()
 
root.mainloop()
