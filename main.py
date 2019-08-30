from tkinter import Tk,Label,Button,Frame
from datetime import datetime
proceso=0
i = 0

def iniciar():
    global proceso
    global tini
   
    # Save the starting time of our timer as a time reference
    tini = datetime.now()

    # Calls the main function that will repeat recusively to work as a precise clock
    proceso=time.after(1, ejecutar)
 
def ejecutar():
  global proceso
  global tini
  
  # Write the time
  time['text'] = datetime.now()-tini
  
  #Calls itself recursively every ms updating the time on the timer
  proceso=time.after(1, ejecutar)

def split():
  global proceso
  global i
  i += 1
  timesplit = time
  timesplit = Label(root, fg='red', width=20, font=("","14"))
  timesplit.pack()

def parar():
    global proceso
    time.after_cancel(proceso)
 
root = Tk()
root.title('Cronometro')
 
time = Label(root, fg='red', width=20, font=("","18"))
time.pack()
 
# Generamos un frame para poner los botones de iniciar y parar
frame=Frame(root)
btnIniciar=Button(frame, fg='blue', text='Iniciar', command=iniciar)
btnIniciar.grid(row=1, column=1)
btnSplit=Button(frame, fg='blue', text='Split', command=split)
btnSplit.grid(row=1, column=2)
btnParar=Button(frame, fg='blue', text='Parar', command=parar)
btnParar.grid(row=1, column=3)
btnSalir=Button(frame, fg='blue', text='Salir', command=quit)
btnSalir.grid(row=1, column=4)
frame.pack()
 
root.mainloop()
