from tkinter import *
from tkinter import messagebox
lista = []

def iniciarArchivo():
	archivo=open("ag.txt", "a")
	archivo.close()


def cargar():
	archivo=open("ag.txt", "r")
	linea= archivo.readline()
	if linea:
		while linea:
			if linea [-1] == '\n':
				linea=linea[:-1]
			lista.append(linea)
			linea=archivo.readline()
		archivo.close()

def escribirContacto():
	archivo=open("ag.txt", "w")
	lista.sort()
	for elemento in lista:
		archivo.write(elemento + "\n")
	archivo.close()

def consultar():
	r = Text(ventana,width=93 ,height=13)
	lista.sort()
	valores=[]
	r.insert(INSERT, "Nombre\t\tApellido P\t\tApellido M\t\tTelefono\t\tCorreo\n")
	for elemento in lista:
		arreglo=elemento.split("$")
		#com $ guardamos contacto
		valores.append(arreglo[3])
		r.insert(INSERT, arreglo[0] + "\t\t" + arreglo[1] + "\t\t" + arreglo[2] + "\t\t" + arreglo[3] + "\t\t" + arreglo[4] + "\t\n")
	r.place(x=20, y=290)
	spinTelefono=Spinbox(ventana, value=(valores), textvariable=eliminarcontacto).place(x=450, y=50)
	if lista == []:
		spinTelefono=Spinbox(ventana, value=(valores)).place(x=450, y=50)
	r.config(state=DISABLED)

ventana = Tk()
eliminarcontacto = StringVar()
iniciarArchivo()
cargar()
consultar()

colorFondo = "#006"
colorLetra = "#FFF"
ventana.title("Agenda con archivos")
ventana.geometry("800x650")
ventana.configure(background=colorFondo)
etiquetaTitulo=Label(ventana, text="Agenda con archivos", bg=colorFondo, fg= colorLetra, font=("Helvetica", 16)).place(x=250, y=10)
etiquetaNombre=Label(ventana, text="Nombre: ", bg=colorFondo, fg= colorLetra).place(x=50, y=50)
nombre = StringVar()
cajaNombre=Entry(ventana, textvariable=nombre).place(x=150, y=50)
etiquetaApellidoP=Label(ventana, text="Apellido Paterno: ", bg=colorFondo, fg= colorLetra).place(x=50, y=90)
apellidoP = StringVar()
cajaApellidoP=Entry(ventana, textvariable=apellidoP).place(x=150, y=90)
etiquetaApellidoM=Label(ventana, text="Apellido Materno: ", bg=colorFondo, fg= colorLetra).place(x=50, y=130)
apellidoM = StringVar()
cajaApellidoM=Entry(ventana, textvariable=apellidoM).place(x=150, y=130)
etiquetaTelefono=Label(ventana, text="Tel: ", bg=colorFondo, fg= colorLetra).place(x=50, y=170)
telefono = StringVar()
cajaTelefono=Entry(ventana, textvariable=telefono).place(x=150, y=170)
etiquetaCorreo=Label(ventana, text="Correo: ", bg=colorFondo, fg= colorLetra).place(x=50, y=210)
correo = StringVar()
cajaTelefono=Entry(ventana, textvariable=correo).place(x=150, y=210)
def guardar():
	n=nombre.get()
	ap=apellidoP.get()
	am=apellidoM.get()
	t=telefono.get()
	c=correo.get()
	lista.append(n+"$"+ap+"$"+am+"$"+t+"$"+c)
	escribirContacto()
	messagebox.showinfo("Guardado", "El contacto ha sido guardado en la agenda")
	#Una vez que uno lo guarda quiero que las cajas de texto queden vacías, hago lo siguiente:
	nombre.set("")
	apellidoP.set("")
	apellidoM.set("")
	telefono.set("")
	correo.set("")
	consultar() #Por ultimo le mando el metodo consultar para que se actualice
botonGuardar=Button(ventana, text="Guardar", command=guardar, bg="#009", fg=colorLetra).place(x=180, y=250)
etiquetaEliminar=Label(ventana, text="Teléfono: ", bg=colorFondo, fg= colorLetra).place(x=370, y=50)
spinTelefono=Spinbox(ventana, textvariable=eliminarcontacto).place(x=450, y=50)
def eliminar():
	eliminado=eliminarcontacto.get()
	removido=False #Esto es solo una bandera para ver que se eliminó correctamente el contacto
	for elemento in lista:
		arreglo=elemento.split("$")
		if eliminarcontacto.get() == arreglo[3]:
			lista.remove(elemento) #Que remueva ese elemento
			removido=True
	escribirContacto()
	consultar() #Para que se actualice nuestra tabla
	if removido:
		messagebox.showinfo("Eliminar", "Elemento eliminado: "+ eliminado)
botonEliminar=Button(ventana, text="Eliminar",command=eliminar, bg="#009", fg=colorLetra).place(x=450, y=100)

mainloop()