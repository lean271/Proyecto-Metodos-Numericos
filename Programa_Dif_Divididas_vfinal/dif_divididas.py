import tkinter as tk
from tkinter import ttk,Label,PhotoImage
import sympy as sp

# Aqui creo un objeto usando la clase Tk
#Se instancia la clase Tk() para crear una nueva ventana
ventana = tk.Tk()

ventana.title("Método de Diferencias Divididas hacia adelante por Elbin Puga")

#Esto es para modificar la ventana en pixeles ("ancho x largo")

ventana.geometry("900x600")

#Asigno una variable para cargar el logo
#Colocar el nombre del archivo en comillas " nombre foto"
imagen_fisc = PhotoImage(file = "fisc.png")

#Creo el widget Label para mostrar la imagen
etiqueta_logo = Label(ventana, image = imagen_fisc, background="gray19",width=200,height=200)
etiqueta_logo.place(anchor = "nw") #nw es noroeste

#Etiqueta autor

autor = Label(ventana,text="Autor: Elbin Puga",font=("Segoe Script",28,"bold"),fg="#fff",background="gray19")
autor.place(x=310,y=100)


#Creo la etiqueta para el titulo del metodo

titulo_metodo = Label(ventana, text="Método de diferencias divididas",font=("Segoe Script", 28),fg="#fff",background="gray19")
#Le doy la posicion mediante coordenadas (tanteo en base a las dimensiones de la ventana)
titulo_metodo.place(x=190 , y=180)

#Etiqueta para decirle al usuario que ingrese los puntos (3 puntos por defecto)
etiqueta_ingrese_puntos = Label(ventana, text = "Ingrese los puntos:",font=("Segoe Script",28),fg="#fff",background="gray19")
etiqueta_ingrese_puntos.place(x=320,y=300)

#Entradas que por el usuario 
etiqueta_p1 = Label(ventana,text="P1(",font=("Arial",24),background="gray19",fg="#fff")
etiqueta_p1.place(x=180,y=363)


#Entradas para que el usuario ingrese las coordenadas
#El metodo. Entry es esencial para que el usuario introduzca los datos
#El metodo .place me sirvio para darle una posicion en la ventana (tanteo)
x0 = tk.Entry(ventana,width=10,justify="center")
x0.place(x=240,y=370,relheight=0.05)
etiqueta_p1_coma = Label(ventana,text=",",font=("Arial",24),background="gray19",fg="#fff")
etiqueta_p1_coma.place(x=305,y=363)

y0 = tk.Entry(ventana,width=10,justify="center")
y0.place(x=320,y=370,relheight=0.05)
etiqueta_p1_parentesis = Label(ventana,text=")",font=("Arial",24),background="gray19",fg="#fff")
etiqueta_p1_parentesis.place(x=390,y=363)

etiqueta_p2 = Label(ventana,text="P2(",font=("Arial",24),background="gray19",fg="#fff")
etiqueta_p2.place(x=500,y=363)

x1 = tk.Entry(ventana,width=10,justify="center")
x1.place(x=560,y=370,relheight=0.05)
etiqueta_p2_coma = Label(ventana,text=",",font=("Arial",24),background="gray19",fg="#fff")
etiqueta_p2_coma.place(x=620,y=363)

y1 = tk.Entry(ventana,width=10,justify="center")
y1.place(x=635,y=370,relheight=0.05)
etiqueta_p2_parentesis = Label(ventana,text=")",font=("Arial",24),background="gray19",fg="#fff")
etiqueta_p2_parentesis.place(x=700,y=363)

etiqueta_p3 = Label(ventana,text="P3(",font=("Arial",24),background="gray19",fg="#fff")
etiqueta_p3.place(x=320,y=450)

x2 = tk.Entry(ventana,width=10,justify="center")
x2.place(x=380,y=458,relheight=0.05)
etiqueta_p3_coma = Label(ventana,text=",",font=("Arial",24),background="gray19",fg="#fff")
etiqueta_p3_coma.place(x=440,y=450)

y2 = tk.Entry(ventana,width=10,justify="center")
y2.place(x=460,y=458,relheight=0.05)
etiqueta_p3_parentesis = Label(ventana,text=")",font=("Arial",24),background="gray19",fg="#fff")
etiqueta_p3_parentesis.place(x=520,y=450)


#Funcion para obtener (get) los datos de entrada
def diferencias_divididas():
    #Darle otro color al fondo de la ventana
    ventana.configure(bg="gray8")
    #Conversion en tipo float para los puntos P1, P2 Y P3
    #Para el punto 1
    x_0 = float(x0.get())
    y_0 = float(y0.get())

    #Para el punto 2

    x_1 = float(x1.get())
    y_1 = float(y1.get())

    #Para el punto 3

    x_2 = float(x2.get())
    y_2 = float(y2.get())

    #Eliminar los widgets después de tocar el boton calcular
    etiqueta_logo.destroy()
    autor.destroy()
    titulo_metodo.destroy()
    etiqueta_ingrese_puntos.destroy()
    etiqueta_p1.destroy()    
    x0.destroy()
    y0.destroy()
    etiqueta_p1_coma.destroy()
    etiqueta_p1_parentesis.destroy()
    etiqueta_p2.destroy()
    x1.destroy()
    y1.destroy()
    etiqueta_p2_coma.destroy()
    etiqueta_p2_parentesis.destroy()
    etiqueta_p3.destroy()
    x2.destroy()
    y2.destroy()
    etiqueta_p3_coma.destroy()
    etiqueta_p3_parentesis.destroy()
    calcular.destroy()

    #Calculos: 
    dif_div1 = round((y_1-y_0)/(x_1-x_0),2)

    dif_div2 = round((y_2-y_1)/(x_2-x_1),2)
    
    dif_div3 = round((dif_div2-dif_div1)/(x_2-x_0),2)
    
    #Creacion de una lista para guardar los datos
    datos = [("j","x_j","y_j","f(x_j , y_j+1)",""),
            (0,x_0,y_0,"",""),
            (1,x_1,y_1,dif_div1,""),
            (2,x_2,y_2,dif_div2,dif_div3)]

    #Establezco la tabla

    for i in range(4):
        for j in range(5):
            tabla = tk.Entry(ventana,width=15,font=("Arial",16,"bold"))
            tabla.grid(row=i,column=j)
            tabla.insert(0,datos[i][j])

    mostrar_coeficientes = tk.Label(ventana, text="Los coeficientes son:",font=("Segoe Script",28,"bold"),background="gray8",fg="#fff")
    mostrar_coeficientes.place(x=250,y=150)
    #Aqui muestro el primer coeficiente
    a_0 = tk.Entry(ventana,width=10,justify="center",font=("Arial",20,"bold"),background="gray8",fg="#fff")
    a_0.place(x=180,y=250)
    a_0.insert(0,f"a_0 = {y_0}")

    #Aqui muestro el segundo coeficiente
    a_1 = tk.Entry(ventana,width=10,justify="center",font=("Arial",20,"bold"),background="gray8",fg="#fff")
    a_1.place(x=380,y=250)
    a_1.insert(0,f"a_1 = {dif_div1}")

    #Aqui muestro el tercer coeficiente
    a_2 = tk.Entry(ventana,width=10,justify="center",font=("Arial",20,"bold"),background="gray8",fg="#fff")
    a_2.place(x=580,y=250)
    a_2.insert(0,f"a_2 = {dif_div3}")

    #Calculo del polinomio
    x = sp.Symbol("x")
    p_n = round(y_0,2) + round(dif_div1,2)*(x-x_0)+round(dif_div3,2)*(x-x_0)*(x-x_1)
    expandir_pn = sp.expand(p_n)

    etiqueta_polinomio = tk.Label(ventana,text="El polinomio que aproxima los puntos dados es :",font=("Segoe Script",24,"bold"),background="gray8",fg="#fff")
    etiqueta_polinomio.place(x=40,y=300)
    polinomio = tk.Entry(ventana,width=30,justify="center",font=("Helvetica",28,"bold"),background="gray8",fg="#fff")
    polinomio.place(x=140, y=350)
    #Respuesta
    polinomio.insert(0,f"p_3(x) = {expandir_pn}")

#Boton para calcular
calcular = ttk.Button(ventana,text="Buscar Polinomio Interpolador",command=diferencias_divididas,)
calcular.place(x=370,y=520,relheight=0.10)

#Asignar un color de fondo y posteriormente iniciar la ventana
ventana.configure(bg = "gray19" )
ventana.mainloop()
