from tkinter import Tk,Label,Button,Frame
from datetime import datetime
proceso=0
 
def iniciar():
    global proceso
    global tini

    tini = datetime.now()

    time['text'] = contador
    proceso=time.after(1, ejecutar)
 
def ejecutar():
  global proceso
  global tini
def parar():
    global proceso
    time.after_cancel(proceso)
 
root = Tk()
root.title('Cronometro')
 
time = Label(root, fg='red', width=20, font=("","18"))
time.pack()
 
# si queremos que se autoejecuta al iniciar el programa hay que desomentar
# esta linea y comentar los botones
#iniciar()
 
# Generamos un frame para poner los botones de iniciar y parar
frame=Frame(root)
btnIniciar=Button(frame, fg='blue', text='Iniciar', command=iniciar)
btnIniciar.grid(row=1, column=1)
btnParar=Button(frame, fg='blue', text='Parar', command=parar)
btnParar.grid(row=1, column=2)
frame.pack()
 
root.mainloop()
