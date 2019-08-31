from tkinter import Tk,Label,Button,Frame
from datetime import datetime
proceso=0
 
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
  
  now = datetime.now()-tini
  # Write the time
  date = strfdelta(now, "{hours}:{minutes}:{seconds}")
  cs = int(now.microseconds/10000)
  time['text'] = str(date)+":"+str(cs)
  
  #Calls itself recursively every ms updating the time on the timer
  proceso=time.after(1, ejecutar)
  
def parar():
    global proceso
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
 
# Generamos un frame para poner los botones de iniciar y parar
frame=Frame(root)
btnIniciar=Button(frame, fg='blue', text='Iniciar', command=iniciar)
btnIniciar.grid(row=1, column=1)
btnParar=Button(frame, fg='blue', text='Parar', command=parar)
btnParar.grid(row=1, column=2)
btnSalir=Button(frame, fg='blue', text='Salir', command=quit)
btnSalir.grid(row=1, column=3)
frame.pack()
 
root.mainloop()
