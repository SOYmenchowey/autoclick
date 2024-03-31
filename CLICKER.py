import time
import pyautogui
import keyboard
import tkinter as tk
import threading
from tkinter import simpledialog
from tkinter import messagebox

root = tk.Tk()
root.title("AUTOLCICKER")
root.geometry("400x600")
root.resizable(False,False)
root.config(background="black")


letra = None
escuchando = True

def cerrar_programa():
    global escuchando
    escuchando = False  # Detener la ejecución del autoclicker
    root.destroy()  # Cerrar la ventana principal

def cerrar_con_esc(event):
    if event.keysym == "Escape":
        cerrar_programa()
        
        
            
def LogicaAutoCliker():
  global escuchando
  print("AutoCliker Acitvado")  
  
  
  time.sleep(1)
  try:
    while escuchando:
      keyboard.wait(letra_1)
      labelSALIR.config(text="PULSE LA TECLA 'ESC' PARA SALIR")
      labelSTATUS.config(text="STATUS DEL SCRIPT : ACTIVO")
      labelDETENER.config(text=f'Para detener el script, pulsa la tecla :\n "{letra}" ')   
      while True:
         if keyboard.is_pressed(letra):
          #print("Saliendo del script...")
          labelSTATUS.config(text="STATUS DEL SCRIPT : DESACTIVADO")
          labelDETENER.config(text='')
          labelSTATUS.place(x=45,y=380)
          BotonEmepzar.config(state="normal")
          break
         else:
          pyautogui.click()
          time.sleep(0.5) 
      time.sleep(0.02)  # Evita consumir demasiado       
  except Exception as e:
      messagebox("ERROR AL DIGITAR LETRAS")
       
      
      
def hilo_clicker():
   hilo = threading.Thread(target=LogicaAutoCliker)
   hilo.start()  
   
   
def PedirLetra():
    global letra
    global letra_1
    
    labelDETENER.config(text=f'')
    labelINICIAR.config(text=f'')
    letra = simpledialog.askstring("WARNING","DIGITE TECLA PARA DETENER AUTOCLICKER")
    time.sleep(0.5)
    letra_1=simpledialog.askstring("WARNING","DIGITE TECLA PARA INICIAR AUTOCLICKER")
    
    if letra is not None:
        print("La tecla escrita fue : ", letra)
        BotonEmepzar.config(state="disabled")  
        contador()
    else:
        messagebox.showinfo("ATENCION","NO SE DETECTO NINGUNA LETRA")
             
     
def contador():
    global letra
    j = 5
    labelSTATUS.config(text="")
    for i in range (5,-1,-1):
        labelCUENTA_rEGRESIVA.config(text=str(i))
        j-=1
        print(j)
        time.sleep(0.5)
        
        root.update()
        
        
    if j == -1:
     labelCUENTA_rEGRESIVA.config(text="")  
     
     labelDETENER.config(text=f'Para detener el script, manten pulsado \n"{letra}" ')
     labelINICIAR.config(text=f'Para iniciar el script, pulsa la tecla \n "{letra_1}" ')
     root.update() 
     hilo_clicker()     
                      



BotonEmepzar = tk.Button(root,text="INICIAR",command=PedirLetra)
BotonEmepzar.place(x=151,y=100)
BotonEmepzar.config(height=5,width=10,font=("Arial",12))

labelEMPEZAR = tk.Label(root,text="Auto-Clicker")
labelEMPEZAR.place(x=60,y=10)
labelEMPEZAR.config(font=("Courier",30),fg="#DC7633",background="black")


labelCUENTA_rEGRESIVA = tk.Label(root)
labelCUENTA_rEGRESIVA.place(x=180,y=380)
labelCUENTA_rEGRESIVA.config(fg="red",bg="black",font=("Arial",30))

labelSTATUS = tk.Label(root)
labelSTATUS.place(x=61,y=380)
labelSTATUS.config(fg="green",bg="black",font=("Terminal",22,"underline"))

labelDETENER = tk.Label(root)
labelDETENER.place(x=10,y=420)
labelDETENER.config(fg="#52BE80",bg="black",font=("Terminal",22))

labelINICIAR = tk.Label(root)
labelINICIAR.place(x=10,y=498)
labelINICIAR.config(fg="#52BE80",bg="black",font=("Terminal",22))

labelSALIR = tk.Label(root)
labelSALIR.place(x=35,y=550)
labelSALIR.config(fg="#F1948A",bg="black",font=("Terminal",22))


root.bind("<Escape>", cerrar_con_esc)

root.protocol("WM_DELETE_WINDOW", cerrar_programa)

root.mainloop()