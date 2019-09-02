from tkinter import Tk,Label,Button,Frame
from datetime import datetime

# Define glboal variables.
proceso = 0
running = False
t_pause=0
#i and first are flag variablers for the splitter.
i = 0
first = True

def iniciar():  #Starts the timer.
    if running==True:
        resume()
        return 0
    global proceso
    global tini
    global running
    running = True
    # Save the starting time as reference.
    tini = datetime.now()

    # Calls the main function that will repeat recusively. Will work as a  clock.
    proceso=time.after(1, ejecutar)

def resume():
    global proceso
    global tini
    global t_pause
    
    
    proceso=time.after(1,ejecutar)
 
def ejecutar(): #Recursive function. Checks time difference between reference and now and updates it every ms on screen.
  global proceso
  global tini
  global time

  now = datetime.now()-tini
  
  # Formats the time and updates it
  date = strfdelta(now, "{hours}:{minutes}:{seconds}:{centiseconds}")
  time['text'] = str(date)
  
  #Function calls itself recursively every ms updating the time.
  proceso=time.after(1, ejecutar)

def split():    #Save an split time for a section or partial. Does not affect the global time.
  global proceso
  global i, first
  global lista
  global clock

  if (running==True):   #Checks if timer is running to avoid weird things (buffered variables). Just in case.
    if (i==0) and (first==True):    #First loop is different as its reference is global time.
      
      clock = datetime.now()
      partial = datetime.now()-tini
      timesplit = strfdelta(partial, "{hours}:{minutes}:{seconds}:{centiseconds}")
      lista[i]['text'] = str(timesplit)
      first = False
    else:   #Later loops reference is last split time instead of global time.
      partial = datetime.now()-clock
      timesplit = strfdelta(partial, "{hours}:{minutes}:{seconds}:{centiseconds}")
      lista[i]['text'] = str(timesplit)
      clock = datetime.now()
    i += 1
    if (i>=3):
      i = 0

def pausar():
    global proceso
    global t_pause
    
    t_pause = datetime.now()
    
    time.after_cancel(proceso)
    
def parar():    #Stops timer and resets it
    global proceso
    global running
    global first, i
    running = False
    first = True
    i = 0
    time.after_cancel(proceso)
   
def strfdelta(tdelta, fmt): #Formats time. Can be modified easily to show different formats.
    d = {"days": tdelta.days}
    d["hours"], rem = divmod(tdelta.seconds, 3600)
    d["minutes"], d["seconds"] = divmod(rem, 60)
    d["centiseconds"] = int(tdelta.microseconds/10000)
    return fmt.format(**d)

def salir():    #Quits the app and close the window.
    global root
    root.destroy()

root = Tk()
root.title('Cronometro')
root.geometry('225x400') # anchura x altura

time = Label(root, fg='red', width=20, font=("","18"))
time.pack()

# Place for the split times. I still have to make it dynamic.
split_one=Label(root, fg='red', width=20, font=("","14"))
split_one.pack()
split_two=Label(root, fg='red', width=20, font=("","14"))
split_two.pack()
split_tre=Label(root, fg='red', width=20, font=("","14"))
split_tre.pack()

lista = [split_one, split_two, split_tre]

# Generate a frame to place all the command buttons.
frame=Frame(root)
btnIniciar=Button(frame, fg='blue', text='Iniciar', command=iniciar)
btnIniciar.grid(row=1, column=1)
btnSplit=Button(frame, fg='blue', text='Split', command=split)
btnSplit.grid(row=1, column=2)
#btnPausa=Button(frame, fg='blue', text='Pausa', command=pausar)
#btnPausa.grid(row=1, column=3)
btnParar=Button(frame, fg='blue', text='Parar', command=parar)
btnParar.grid(row=1, column=4)
btnSalir=Button(frame, fg='blue', text='Salir', command=salir)
btnSalir.grid(row=1, column=5)

frame.pack(side="bottom")
 
root.mainloop()
