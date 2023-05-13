from tkinter import *
from tkinter import ttk
import os


root = Tk()
root.title("texto")

personitas = []

notebook = ttk.Notebook(root)

pestaña1 = ttk.Frame(notebook)
pestaña2 = ttk.Frame(notebook)

notebook.add(pestaña1, text="Añadir")
notebook.add(pestaña2, text="Tabla")

notebook.pack(expand=True, fill=BOTH)

class Persona:
    def __init__(self, nombre: str, apellido_paterno: str, apellido_materno: str, correo: str, movil: str, ocupacion: str, leer: str, musica: str, videojuegos: str, estado: str):
        self.nombre = nombre
        self.apellido_paterno = apellido_paterno
        self.apellido_materno = apellido_materno
        self.correo = correo
        self.movil = movil
        self.ocupacion = ocupacion
        self.leer = leer
        self.musica = musica
        self.videojuegos = videojuegos
        self.estado = estado

if not os.path.isfile("archivo.csv"):
    with open("archivo.csv", "w") as file:
        file.write("Nombre:,Apellido Materno:,Apellido Paterno:,Correo:,Movil:,Ocupacion:,Leer:,Musica:,Videojuegos:,Estado:")

else:
    with open("archivo.csv", "r") as file:
        line = file.readline()
        line = file.readline()
        personitas = []
        while line:
            Datos = line.strip().split(",")
            personita = Persona(Datos[0], Datos[1], Datos[2], Datos[3], Datos[4], Datos[5], Datos[6], Datos[7], Datos[8], Datos[9])
            personitas.append(personita)
            line = file.readline()

        table = ttk.Treeview(pestaña2, columns=("Nombre", "Apellido Materno", "Apellido Paterno", "Correo", "Movil", "Ocupacion", "Leer", "Musica", "Videojuegos", "Estado"))
        table.heading("#0", text="ID")
        table.heading("Nombre", text="Nombre")
        table.heading("Apellido Materno", text="Apellido Materno")
        table.heading("Apellido Paterno", text="Apellido Paterno")
        table.heading("Correo", text="Correo")
        table.heading("Movil", text="Movil")
        table.heading("Ocupacion", text="Ocupacion")
        table.heading("Leer", text="Leer")
        table.heading("Musica", text="Musica")
        table.heading("Videojuegos", text="Videojuegos")
        table.heading("Estado", text="Estado")

        table.column("#0", width=50)
        table.column("Nombre", width=100)
        table.column("Apellido Materno", width=100)
        table.column("Apellido Paterno", width=100)
        table.column("Correo", width=100)
        table.column("Movil", width=100)
        table.column("Ocupacion", width=100)
        table.column("Leer", width=100)
        table.column("Musica", width=100)
        table.column("Videojuegos", width=100)
        table.column("Estado", width=100)

        for i, personita in enumerate(personitas):
            table.insert(parent="", index=i, iid=i, text=i+1, values=(personita.nombre, personita.apellido_materno, personita.apellido_paterno, personita.correo, personita.movil, personita.ocupacion, personita.leer, personita.musica, personita.videojuegos, personita.estado))

        table.pack(expand=True, fill=BOTH)

def GuardarDatos():
    personita = Persona(NombreEntry.get(), APaternoEntry.get(), AMaternoEntry.get(), CorreoEntry.get(), MovilEntry.get(), ocupacionradio.get(), Leercheck.get(), Musicheck.get(), Videocheck.get(), estados.get())
    personitas.append(personita)

    with open ("archivo.csv", "a") as file:
         file.write(f"{personita.nombre}, {personita.apellido_materno}, {personita.apellido_paterno}, {personita.correo}, {personita.movil}, {personita.ocupacion}, {personita.leer}, {personita.musica}, {personita.videojuegos}, {personita.estado}\n")
         table.insert(parent="", index="end", iid=len(personitas), text=len(personitas), values=(personita.nombre, personita.apellido_materno, personita.apellido_paterno, personita.correo, personita.movil, personita.ocupacion, personita.leer, personita.musica, personita.videojuegos, personita.estado))

         NombreEntry.delete(0, END)
         APaternoEntry.delete(0, END)
         AMaternoEntry.delete(0, END)
         CorreoEntry.delete(0, END)
         MovilEntry.delete(0, END)
         ocupacionradio.set(None)
         Leercheck.set(False)
         Musicheck.set(False)
         Videocheck.set(False)
         estados.set(False)

mainFrame=ttk.Frame(pestaña1, padding="10 10 10 10",)
mainFrame.grid(column=0, row=0)

usuarioFrame=ttk.Frame(mainFrame,padding="10 10 10 10", relief="raised")
usuarioFrame.grid(column=0, row=0, columnspan=2, rowspan=3)

NombreEntry=ttk.Entry(usuarioFrame)
NombreEntry.grid(column=1, row=1, columnspan=2)

APaternoEntry=ttk.Entry(usuarioFrame)
APaternoEntry.grid(column=1, row=2, columnspan=2)

AMaternoEntry=ttk.Entry(usuarioFrame)
AMaternoEntry.grid(column=1, row=3, columnspan=2)

CorreoEntry=ttk.Entry(usuarioFrame)
CorreoEntry.grid(column=1, row=4, columnspan=2)

MovilEntry=ttk.Entry(usuarioFrame)
MovilEntry.grid(column=1, row=5, columnspan=2)

ttk.Label(usuarioFrame, text="Nombre: \n").grid(column=0, row=1)
ttk.Label(usuarioFrame, text="A. Paterno: \n").grid(column=0, row=2)
ttk.Label(usuarioFrame, text="A. Materno: \n").grid(column=0, row=3)
ttk.Label(usuarioFrame, text="Correo: \n").grid(column=0, row=4)
ttk.Label(usuarioFrame, text="Movil: \n").grid(column=0, row=5)
        
aficionesFrame=ttk.Frame(mainFrame, padding="10 10 10 10", relief="raised")
aficionesFrame.grid(column=0, row=4, columnspan=2)

ttk.Label(aficionesFrame, text="Aficiones: \n").grid(column=0, row=0)

Leercheck= BooleanVar()
Leerch = ttk.Checkbutton(aficionesFrame, text='Leer',variable=Leercheck).grid(column=0, row=1)
Musicheck= BooleanVar()
Musich = ttk.Checkbutton(aficionesFrame, text= 'Musica',variable=Musicheck).grid(column=1, row=1)
Videocheck= BooleanVar()
Videoch = ttk.Checkbutton(aficionesFrame, text= 'Videojuegos',variable=Videocheck).grid(column=2, row=1)

personaFrame=ttk.Frame(mainFrame, padding="10 10 10 10")
personaFrame.grid(column=2, row=0, rowspan=3)

ocupacionradio=StringVar()
estudiante= ttk.Radiobutton(personaFrame, text='Estudiante',variable=ocupacionradio, value='estudiante').grid(column=0,sticky=W)
empleado= ttk.Radiobutton(personaFrame, text='Empleado',variable=ocupacionradio, value='empleado').grid(column=0,sticky=W)
desempleado= ttk.Radiobutton(personaFrame, text='Desempleado',variable=ocupacionradio, value='desempleado').grid(column=0, sticky=W)

comboFrame=ttk.Frame(mainFrame, padding="10 10 10 10")
comboFrame.grid(column=2,row=4)

estados = StringVar()

comboEstados = ttk.Combobox(comboFrame, textvariable= estados)
comboEstados.grid()
comboEstados['values']=("Jalisco","Nayarit", "Colima", "Michoacan","Estados(32)")

ttk.Button(mainFrame, text="Guardar", command=GuardarDatos).grid(column=0,row=5)
ttk.Button(mainFrame, text="Cancelar").grid(column=1,row=5)

root.mainloop()