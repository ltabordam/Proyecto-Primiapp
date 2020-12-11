from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import *
from io import *
import winsound
import os.path
import time as tm
import sqlite3
from bs4 import *
from urllib.request import urlopen
from datetime import *
from sys import exit

indices = ['0','1','2','3','4','5','6','7','8','9'] 
dias = ['1','2','3','4','5','6','7','8','9', '10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31'] 
meses = {'enero': '1','febrero': '2','marzo': '3','abril': '4','mayo': '5', 'junio': '6','julio': '7' ,'agosto': '8' ,'septiembre':'9','octubre':'10','noviembre': '11','diciembre': '12' }

frequency = 2500  # Set Frequency To 2500 Hertz
duration = 1000  # Set Duration To 1000 ms == 1 second

conn = sqlite3.connect('login2')

c = conn.cursor()

try:
    c.execute("""CREATE TABLE login (
                username text,
                password text
                ) """)
except:
    print('tabla ya exsiste')


# commit the changes to db
conn.commit()
# close the connection

def login():

    """ 
    Genera la interfaz visual relacionada con el login. Aloja las funciones registro(), submit(), validar()

    Función del tipo no recibe, no retorna (Sin parametros)

    return: None:

    """
    conn = sqlite3.connect('login2')

    c = conn.cursor()

    window = Tk()
    window.title("PrimiApp")
    window.geometry("415x340")
    window.config(background= "#B1B2B0")

    def registro():
        """ 

        Genera la interfaz visual de la parte de registros de usuario, del mismo modo llama 
        a la funcion definida .cursor(), originaria de la base de datos, para recorrer
        la base de datos, aloja la función. submit()

        Función no recibe, no retorna (Sin Parametros)

        return: None:

        """

        window = Tk()
        window.title("Registro")
        window.geometry("415x315")
        window.config(background= "#B1B2B0")
        conn = sqlite3.connect('login2')

        c = conn.cursor()

        def submit():
            """
            Genera la validación necesaria para el registro de nuevos usuarios en la aplicación
            mediante la obtencion de las entradas (Campos de tipo Entry, función registro ()) y 
            escribe un nuevo campo a modo de tupla en la base de datos.

            Función no recibe, no retorna (Sin parametros)

            :return :None

            """

            conn = sqlite3.connect('login2')

            c = conn.cursor()

            if entrada_password.get() == '' or entrada_usuario.get == '':
                return

            c.execute("INSERT INTO login VALUES(:username,:password)",
                      {'username': entrada_usuario.get(),
                       'password': entrada_password.get()})

            # commit the changes to db
            conn.commit()

            c.execute('SELECT *,oid FROM login')
            registro = c.fetchall()
            print(registro)

            conn.commit()


            entrada_usuario.delete(0, END)
            entrada_password.delete(0, END)
            messagebox.showinfo(message= 'PrimiAmigo registrado!!!', title='Registro Exitoso')
        conn.commit()

        Label(window, text= 'Sé un PrimiAmigo', bg = '#94B43B', fg='Black', width = '300', height= '3', font=("Bold", 20)).pack()

        Label(window, text='PrimiAmigo', bg= '#B1B2B0' ).pack()
        entrada_usuario = Entry(window)
        entrada_usuario.pack()
        Label(window, bg='#B1B2B0' ).pack()

        Label(window, text='Contraseña', bg= '#B1B2B0' ).pack()
        entrada_password = Entry(window)
        entrada_password.pack()
        Label(window, bg='#B1B2B0' ).pack()


        Button(window, text='Guarda info', bg='#94B43B', command=submit).pack()
        

    def validar():

        """

        Función encargada de la validación de los valores de Usuario y contraseña obtenidos de las entradas
        (Campos de tipo Entry, función login()), en la base de datos y del mismo modo permitir la entrada o no
        a la aplicación. Inicializa guardar(obtener_fechas()), definir_festivos() , init_window()

        Función no recibe, no retorna

        :return :None

        """

        conn = sqlite3.connect('login2')

        c = conn.cursor()

        c.execute('SELECT *,oid FROM login')
        registro = c.fetchall()
        print(registro)

        for elemento in registro:

            if entrada_user.get() in elemento[0] and contraseña.get() in elemento[1] and contraseña.get() != '':
                print('bienvenido')
                file_exists = os.path.isfile('festivos.txt')
                if file_exists:
                    init_window()
                else:
                    guardar(obtener_fechas())
                    definir_festivos()
                    init_window()
            
                

                    


        conn.commit()

    Label(window, text="Hola PrimiAmigo",bg = '#94B43B', fg='Black', width = '300', height= '3', font=("Bold", 20)).pack()
    Label(window,text ='', bg='#B1B2B0' ).pack()

    global entrada_user
    global contraseña
    
    Label(window, text='PrimiAmigo', bg= '#B1B2B0' ).pack()
    entrada_user = Entry(window)
    entrada_user.pack()
    Label(window, bg='#B1B2B0' ).pack()

    Label(window,text='Contraseña', bg= '#B1B2B0').pack()
    contraseña = Entry(window,show='*')
    contraseña.pack()
    Label(window, bg='#B1B2B0' ).pack()

    
    Button(window, text='Ingresar',bg='#94B43B',command= validar).pack()

    Label(window, bg='#B1B2B0' ).pack()
    
    Button(window, text='Registrate',bg='#94B43B', command= registro).pack()

    

    

# commit the changes to db
conn.commit()
# close the connection
conn.close()

def init_window():
    """
    Abre la ventan inicial de la aplicación, encargado de llamar las funciones calendar(),temporizador() y window_notes()


    :return: None
    """
    conn = sqlite3.connect('login2')

    c = conn.cursor()

    t = 0

    primera_ventana = Tk()
    primera_ventana.geometry('400x350')
    primera_ventana.title('Menu Principal')
    primera_ventana.config(bg ='#B1B2B0' )

    # image = PhotoImage(file = "UNAL.gif" )
    # image = image.subsample(2,2)
    # label = Label(image = image)
    # label.pack()


    Label(primera_ventana, text = 'Primiapp', bg = '#94B43B', fg='Black', width = '300', height= '3', font= ("Tahoma", 20)).pack()

    Label(primera_ventana,text='',bg = '#B1B2B0').pack()
    

    Button(primera_ventana, text = 'Agenda',bg = '#94B43B', fg='Black', width = '20', height= '1' , command = calendar).pack()
    Label(primera_ventana,text='',bg = '#B1B2B0').pack()
    
    Button(primera_ventana, text = 'Notas',bg = '#94B43B', fg='Black', width = '20', height= '1' , command = window_notes).pack()
    Label(primera_ventana,text='',bg = '#B1B2B0').pack()
    
    Button(primera_ventana, text = 'Temporizador', bg = '#94B43B', fg='Black', width = '20', height= '1' , command = temporizador).pack()
    Label(primera_ventana,text='',bg = '#B1B2B0').pack()
    
    Button(primera_ventana, text = 'Recargar',bg = '#94B43B', fg='Black', width = '6', height= '1' , command = init_window).pack()
    Label(primera_ventana,text='',bg = '#B1B2B0').pack()

    Button(primera_ventana, text = 'Salir',bg = '#94B43B', fg='Black', width = '5', height= '1' , command = sys.exit).pack()

    messagebox.showinfo(message= 'Para una mejor experiencia una vez iniciada sesión minimice la pantalla de ingreso, muchas gracias')
    
    
    primera_ventana.mainloop()  

def calendar():

    """
    Abre una ventana nueva  y un widget clendario utilizando tkcalendar, define init_agendar() e init_agendado()

    Función no recibe no retorna
    
    :return:None
    
    """
    root = Tk()
    root.title("Calendar")
    root.geometry("600x600")
    root.config(background="#94B43B")

    cal = Calendar(root, selectmode="day", year=2020, month=10, day=29, font=("Arial", 20))
    cal.pack(pady=20, fill="both", expand=True)

    def init_agendar():
        """
           
        Inicia una nueva ventana con un widget de texto para registar la información a guardar en la fecha seleccionada, del mismo modo 
        cuenta con un widget de tipo Combobox que mediante etiquetas de importancia predefinidas, permitiendo así registrar bajo 
        bajo esta etiqueta y su nivel de  importancia, inicializa take_info()

        Función no recibe, no retorna
        
        
        :return: None
        """

        my_label.config(text=cal.get_date())

        def take_input():
            """
            Guarda la informacion en un archivo de texto definido como primiapp.txt, la informacion que toma es la alojada
            en el widget de texto, la obtencion del nombre de usuario que corre la aplicacion en ese momento, la etiqueta
            seleccionada en la lista predefinida (tkk.Comobobox()) y la fecha calendario sobre la cual se esta realizando 
            el registro.

            Función no recibe no retorna

            :return:None
            """

            INPUT = t.get("1.0", "end-1c")
            
            print(INPUT)
        
            archivo_texto = open('primiapp.txt', 'a', newline='')

            info = entrada_user.get()+combo_operadores.get()+cal.get_date() + INPUT 

            archivo_texto.write(info)
            archivo_texto.write('\n')
            archivo_texto.close()

            messagebox.showinfo(message= 'Evento guardado satifactoriamente', title='Agendado')
        
        root = Tk()
        root.title("AGENDAR")
        root.geometry("390x350")
        root.config(bg='#B1B2B0')
        labelA = Label(root, text="¿Qué deseas \n guardar?", font=("italic", 15),width=35, bg='#A61C31' )
        labelA.grid(row=0, column=0)

        label_2 = Label(root, text="", bg='#B1B2B0')
        label_2.grid(row=1, column=0)

        combo_operadores = ttk.Combobox(root)
        combo_operadores['values'] = ['Cuando se pueda','Poco urgente', 'Urgente', 'Muy Urgente']
        combo_operadores.current(0)
        combo_operadores.grid(row=2, column=0)

        label_4 = Label(root, text="", bg='#B1B2B0')
        label_4.grid(row=3, column=0)

        t = Text(root, width=30, height=10, font=("italic", 10))
        t.grid(row=4, column=0)

        label_3 = Label(root, text="", bg='#B1B2B0')
        label_3.grid(row=5, column=0)

        bE = Button(root, text="Guardar", font=("Italic", 10), command=lambda: take_input(), bg='#A61C31')
        bE.grid(row=6, column=0)


        
    def init_agendado():
        """   
        Inicia una nueva ventana con un widget de texto para mostrar la información a registar en la fecha seleccionada, del mismo modo 
        cuenta con un widget de tipo Combobox que mediante etiquetas de importancia predefinidas, mostrando así unicamente lo registrado 
        bajo esta etiqueta, inicializa show_info(), del mismo modo muestra si hay un festivo en esa fecha estas obtenidas gracias al 
        web scrapper

        Función no recibe, no retorna
        
        :return: None
        """

        my_label.config(text=cal.get_date())

        def show_info():
            """
            Abre el archivo donde se encuantra la informacion por fechas y la  inserta en el widget de texto

            Funcioón no recibe no retorna

            :return:None
            """

            archivo_texto = open('primiapp.txt', 'r')
            texto = archivo_texto.read()
            archivo_texto.close()
            texto = texto.split('\n')
            validar_registro = str(entrada_user.get())
            validar_etiqueta = str(combo_operadores_2.get())

            for recordatorio in texto:
                if validar_registro in recordatorio:
                    print(recordatorio)
                    recordatorio = recordatorio[len(validar_registro):]
                    if validar_etiqueta in recordatorio:
                        print(recordatorio)
                        recordatorio= recordatorio[len(validar_etiqueta):]
                        print(recordatorio)
                        if recordatorio[0:8] == str(cal.get_date()) or recordatorio[0:7] == str(cal.get_date()) or recordatorio[0:6] == str(cal.get_date()):
                            t2.insert(END, recordatorio)
                            t2.insert(END, '\n')

            archivo_festivo = open('festivos_calendar.txt', 'r')
            texto_festivos = archivo_festivo.read()
            archivo_festivo.close()
            texto_festivos = texto_festivos.split('\n')
            for festividad in texto_festivos:
                if festividad[0:8] == str(cal.get_date()) or festividad[0:7] == str(cal.get_date()) or festividad[0:6] == str(cal.get_date()):
                    t2.insert(END, festividad)
                    t2.insert(END,'\n')

        root = Tk()
        root.title("Agendado")
        root.geometry("390x350")
        root.config(bg='#B1B2B0')
        labelA = Label(root, text="Lo agendado!!", font=("italic", 15),width=35, bg='#94B43B' )
        labelA.grid(row=0, column=0)

        label_2 = Label(root, text="", bg='#B1B2B0')
        label_2.grid(row=1, column=0)

        combo_operadores_2 = ttk.Combobox(root)
        combo_operadores_2['values'] = ['Cuando se pueda','Poco urgente', 'Urgente', 'Muy Urgente']
        combo_operadores_2.current(0)
        combo_operadores_2.grid(row=2, column=0)

        label_3 = Label(root, text="", bg='#B1B2B0')
        label_3.grid(row=3, column=0)

        t2 = Text(root, width=30, height=10, font=("italic", 10))
        t2.grid(row=4, column=0)

        label_3 = Label(root, text="", bg='#B1B2B0')
        label_3.grid(row=5, column=0)

        bE = Button(root, text="Muestrame", font=("Italic", 10), command=lambda: show_info(), bg='#94B43B')
        bE.grid(row=6, column=0)

    # widget que llama a la funcion init_agendar()
    my_button = Button(root, text="Abrir agendar", command=lambda: init_agendar())
    my_button.pack(pady=20)

    # widget que llama a la funcion init_agendado()
    my_button = Button(root, text="Abrir agendado", command=lambda: init_agendado())
    my_button.pack(pady=20)

    my_label = Label(root, text="")
    my_label.pack(pady=20)


def window_notes():
    """
    Funcion llamada mediante la función init_window(), aloja a las funciones relacionadas con los aspectos de notas, estas son
    menu_notas(), entrada_datos(), buscar_notas() y calculo_rapido(), estas como funciones principales y con las que interactua el usuario
    pero también aloja las funciones buscar_registro(), almacenamiento_nota(), ponderado_de_notas(), busqueda_reporte(),
    promedio_reporte(), impresion(). Estas ultimas funciones relacionadas con las primeras

    Función no recibe, no retorna

    :return:None

    """
    
    def menu_notas():

        """
        Genera una interfaz gráfica que sirve de menu para la sección de notas, es la encargada de inicializar a las funciones
        entrada_datos(), buscar_notas() y calculo_rapido() 

        Funcion no recibe no retorna

        :return :None

        """
        notas = Tk()
        notas.geometry('400x250')
        notas.title('Sección de notas')
        notas.config(bg = '#595A5C')

        Label(notas, text= 'Bienvenido a la sección' +'\n'+ 'de Notas PrimiAmigo',bg= '#A61C31', width = '300', height= '3',font = ('Tahoma', 15)).pack()
        Label(notas,text='',bg = '#595A5C').pack()

        Button(notas, text= 'Registro de Notas',bg= '#A61C31', command= entrada_datos).pack()
        Label(notas,text='',bg = '#595A5C').pack()

        Button(notas, text= 'Buscar Registro de Notas', bg= '#A61C31',  command= buscar_notas).pack()
        Label(notas,text='',bg = '#595A5C').pack()

        Button(notas, text= 'Cálculo rápido',bg= '#A61C31', command= calculo_rapido).pack()
        Label(notas,text='',bg = '#595A5C').pack()

        notas.mainloop()

    def calculo_rapido():

        """
        Genera un interfaz gráfica para la funcion de ponderar notas sin guardar, dada por la inicializacion de ponderado_de_notas()

        Función no recibe, no retorna

        :return :None

        """
        calculo = Tk()
        calculo.geometry('400x250')
        calculo.title('Calculo Nota Rapido')
        calculo.config(bg='#595A5C' )

        Label(calculo, text= 'Bienvenido a la sección de' +'\n'+ 'Cálculo Rápido PrimiAmigo',bg= '#A61C31', width = '300', height= '3',font = ('Tahoma', 15)).pack()
        Label(text='',bg='#595A5C' )

        global notas_actuales
        global nota_minima

        notas_actuales = str()

        Label(calculo, text = 'Notas actuales', bg='#595A5C').pack()
        notas_actuales = Entry(calculo)      
        notas_actuales.pack()
        Label(calculo).pack

        

        Label(calculo, text = '\n'+'Nota mínima para pasar', bg='#595A5C' ).pack()
        nota_minima = Entry(calculo) 
        nota_minima.pack()
        Label(calculo).pack
        Label(calculo, text='',bg='#595A5C' ).pack()

        Button(calculo, text="Calcular", command= ponderado_de_notas, bg = '#A61C31').pack()

        messagebox.showinfo(message= 'Digita las notas unicamente separadas por coma (,)', title= 'Funcionamiento')

        calculo.mainloop()


    def entrada_datos():
        """
        Genera un interfaz gráfica para la funcion de registrar las notas de una materia dada por el usuario
        inicializa las función almacenamiento_nota()

        Función no recibe, no retorna

        :return :None

        """
        registro = Tk()
        registro.geometry('400x250')
        registro.title('Acumulador de notas')
        registro.config(bg='#595A5C' )

        Label(registro, text= 'Bienvenido PrimiAmigo',bg= '#A61C31', width = '300', height= '3',font = ('Tahoma', 15)).pack()
        Label(text='', bg= '#595A5C')
        
        global materia
        global notas
        
        Label(registro, text = 'Materia', bg= '#595A5C').pack()
        materia = Entry(registro)
        materia.pack()
        Label(registro).pack

        Label(registro, text = 'Notas', bg= '#595A5C').pack()
        notas = Entry(registro)
        notas.pack()
        Label(registro).pack

        Label(registro, text='',bg='#595A5C' ).pack()

        Button(registro, text="Registrar", bg= '#A61C31', command= almacenamiento_nota).pack()

        messagebox.showinfo(message= "Digita las notas unicamente separadas por coma (,). \n Guarda tu materia de una manera que la recuerdes facilmente", title= 'Funcionamiento')

        registro.mainloop()

    def buscar_notas():

        """
        Genera un interfaz gráfica para la funcion de buscar un registro de notas digitado anteriormente o la ponderacion de las notas
        de la misma dadas anteriormente por el usuario inicializa las funciones busqueda_reporte() y promedio_reporte()

        Función no recibe, no retorna

        :return :None

        """
        reporte = Tk()
        reporte.geometry('400x250')
        reporte.title('Ver Notas')
        reporte.config(bg='#595A5C')

        Label(reporte, text= 'Bienvenido PrimiAmigo', bg= '#A61C31', width = '300', height= '3',font = ('Tahoma', 15)).pack()
        Label(text='',bg='#595A5C')
        
        global materia_busqueda
        
        Label(reporte, text = 'Materia a Buscar',bg='#595A5C').pack()
        materia_busqueda = Entry(reporte)
        materia_busqueda.pack()
        Label(reporte).pack
        
        Label(reporte, text='',bg='#595A5C' ).pack()

        Button(reporte, text="Buscar", command= busqueda_reporte, bg= '#A61C31').pack()
        Label(reporte, text= '', bg='#595A5C').pack()
        Button(reporte, text="Ponderar", command= promedio_reporte, bg= '#A61C31').pack()

        messagebox.showinfo(message= "Digita el nombre de tu materia de la misma manera que la guardaste", title= 'Funcionamiento')

        reporte.mainloop()
        
    def buscar_registro():
        """
        Mediante la libreria os.path se encarga de verificar si el archivo necesario, en este caso notas.txt existe
        en caso de existir no ejecuta ninguna acción sobre la aplicación, en caso de no existir el archivo
        lo genera bajo el nombre predifinido y lo enruta con el codigo para su uso
        
        Función no recibe no retorna

        :return :None

        """
        file_exists = os.path.isfile('notas.txt')
        if file_exists:
            pass
        else:
            file = open("notas.txt", "w+")
            file.close()

    def almacenamiento_nota():
        """
        Función encargada del registro de notas para su posterior revisión o ponderacion,
        escribe en el documento notas.txt, bajo un orden de nombre de usuario, materia y notas,
        estas tres informaciones son obtenidas de entradas desde las interfaces gráficas de login
        y de entrada datos, inicializa la función buscar_registro()

        función no recibe no retorna

        return: None:

        """
        ind = str(materia.get())
        validar_registro = str(entrada_user.get())
        reporte = str(notas.get()).split(',')
        buscar_registro()
        archivo_notas = open('notas.txt', 'a', newline='') 
        registro = validar_registro + ind 
        for nota in reporte:
            registro += str(nota) + ','
        archivo_notas.write(registro) 
        archivo_notas.write('\n')
        archivo_notas.close()

        messagebox.showinfo(message ='Registro Exitoso', title= 'Almacenado de datos')
    
    def ponderado_de_notas():

        """

        Recibe las notas de los campos de entrada en la ventana calculo rapido y ejecuta una ponderación de notas
        y una respectiva comparación frente a una nota minima dada también por el usuario.

        Función no recibe no retorna

        retun: None:

        """
        notas = str(notas_actuales.get()).split(',')
        
        elementos = list(map(float, notas))

        nota_pasar = float(nota_minima.get())

        acumulado = 0
        contador = 0
        for elemento in elementos:
            elemento = float(elemento)
            acumulado = acumulado + elemento
            contador += 1
            ponderado_de_notas = acumulado / contador
        if ponderado_de_notas > nota_pasar and ponderado_de_notas >= 4.5:
            messagebox.showinfo(message = str(round(ponderado_de_notas, 2)) +' '+'Fresco pelao que va pasando', title='Melo')
        elif ponderado_de_notas > nota_pasar and 4.5 > ponderado_de_notas >= 4:
            messagebox.showinfo( message = str(round(ponderado_de_notas, 4)) +' '+'Vas pasando,pero se puede mejorar', title='Tu tranquilo')
        elif ponderado_de_notas >= nota_pasar and 4 > ponderado_de_notas >= 3:
            messagebox.showinfo( message = str(round(ponderado_de_notas, 4)) +' '+'Raspando raspando te puede ir afectando', title= 'Ojito')
        elif ponderado_de_notas < nota_pasar:
            messagebox.showinfo( message = str(round(ponderado_de_notas, 4)) +' '+ 'Llorelo papa ', title='A rezar')
    
    def busqueda_reporte():
        """
        Realiza una busqueda de las notas de una materia registrada por el usuario y almacenadas en el archivo notas.txt
        para evitar dar notas de otras personas obtiene el nombre de usuario mediante la funcion .get(), y realiza así un busqueda 
        precisa.

        Función no recibe no retorna

        :return:None

        """

        try:
            archivo_primera_vez = open('notas.txt', 'r')
            archivo_primera_vez.close()

        except:
            messagebox.showinfo(message='Aún no has registrado ninguna materia', title='Verificar Guardado')

        archivo_busqueda = open('notas.txt', 'r')
        reporte = archivo_busqueda.read()
        archivo_busqueda.close()
        reporte = reporte.split('\n')

        cod_materia = str(materia_busqueda.get())
        validar_registro = str(entrada_user.get())

        a_mostrar = []

        for linea in reporte:
            if validar_registro in linea:
                linea = linea[len(validar_registro):]
                if cod_materia in linea:
                    linea = linea[len(cod_materia):]
                    linea = linea.split(',')
            
                    for elemento in linea:
                        if elemento != '':
                            a_mostrar.append(float(elemento))

        messagebox.showinfo(message = a_mostrar)

    def promedio_reporte():

        """
        Realiza una busqueda de las notas de una materia registrada por el usuario y almacenadas en el archivo notas.txt
        para evitar dar notas de otras personas obtiene el nombre de usuario mediante la funcion .get(), y realiza así un busqueda 
        precisa, una vez determinada las notas por usuario y identificador de materia realiza un ponderado de las notas registradas
        y entrega esta información al usuario

        Función no recibe no retorna

        :return:None

        """
        archivo_busqueda = open('notas.txt', 'r')
        reporte = archivo_busqueda.read()
        archivo_busqueda.close()
        reporte = reporte.split('\n')

        cod_materia = str(materia_busqueda.get())
        validar_registro = str(entrada_user.get())

        a_mostrar = []
        cantidad_notas = 0
        sumatoria = 0

        for linea in reporte:
            if validar_registro in linea:
                linea= linea[len(validar_registro):]
                if cod_materia in linea:
                    linea = linea[len(cod_materia):]
                    linea = linea.split(',')
            
                    for elemento in linea:
                        if elemento != '':
                            a_mostrar.append(float(elemento))

        for digito in a_mostrar:
            sumatoria += digito
            cantidad_notas += 1

        ponderado = round(sumatoria / cantidad_notas, 2)

        messagebox.showinfo(message = 'El ponderado de esta materia es:' + '\n'+ str(ponderado), title= 'Ponderado' +' '+ str(cod_materia))
    
    def impresion():
        """
        llama a la funcion de ventana_notas()
        :return:none
        """
        menu_notas()

    impresion()


def temporizador():
    """
    Genera una nueva ventana con dos tipos de widget, 3 Button para iniciar la cuenta regresiva, paara establecer el tiempo y la asignatura
    y 3 de Entry para ingresar el tiempo en minutos , horas y la asignatura

    Función no recibe no retorna

    :return:None
    """
    crear_bd()
    conn2 = sqlite3.connect('tempo')

    c2 = conn2.cursor()
    global horas
    global minutos_iniciales
    global segundos
    global minutos
    global controlador
    controlador = 1
    horas = 0
    minutos_iniciales = 0
    segundos = 60
    minutos = 0

    def set_timer():
        """
        le asigna el valor int de los Entries referentes a Minutos y Horas a minutos_iniciales y a horas,
        por otro lado inicializa guardar_tempo()

        Función no recibe retorna

        :return: None
        """
        conn2 = sqlite3.connect('tempo')

        c2 = conn2.cursor()
        global horas
        global minutos_iniciales
        global segundos
        global minutos

        horas = (e1.get())

        if horas == '':
            horas = 0
        else:
            horas = int(horas)
        horas_r = horas * 60

        minutos_iniciales = int(e2.get())

        if minutos_iniciales == '':
            minutos_iniciales = 0
        else:
            minutos_iniciales = int(minutos_iniciales)
        minutos_r = minutos_iniciales

        segundos = 60
        minutos = 0
        materia = e3.get()
        tiempo_r = int(minutos_r) + int(horas_r)
        guardar_tempo(int(tiempo_r),materia)

        return

    def horas_f():

        """
        Inicialmente cuenta las horas determinadas por el Entry de horas, cuando horas son iguales a 0
        da la finalizacion del programa, esto se relaciona con los minutos para detrminar la fnalización
        una vez terminada su ejecucion presenta un mensaje y reproduce un sonido de alerta

        Función no recibe no retorna

        :return: None

        """
        global horas
        if horas > 0:
            horas = horas - 1
            Lh.config(text=horas)
            global minutos

            minutos = 59
            Lm.after(0, minutero)
        elif horas <= 0:
            winsound.Beep(261, duration)
            winsound.Beep(293, duration)
            winsound.Beep(329, duration * 2)
            winsound.Beep(392, duration * 2)
            winsound.Beep(329, duration)
            winsound.Beep(293, duration)
            winsound.Beep(261, duration)
            horas = horas - 1
            Lm.config(text='Ya puede tomar' + '\n' + 'un descanso')
            Ln.config(text='')
            Ln2.config(text='')
            Ls.config(text='')
            Lh.config(text='')

    def minutero():
        """
        por minuto va disminuyendo, y actualiza en pantalla
        el paso del tiempo, dependiendo de la condición, llama a segundero()

        Función no recibe no retorna

        :return:None
        """
        global minutos_iniciales
        global minutos
        global horas
        global segundos

        if minutos_iniciales > 0:

            minutos_iniciales = minutos_iniciales - 1
            Lm.config(text=minutos_iniciales)
            print(minutos_iniciales)
            Ln.config(text=':')
            Ln2.config(text=':')
            Lh.config(text=horas)
            Lm.after(0, segundero)

        elif minutos_iniciales <= 0 and minutos == 0:
            Ln.config(text=':')
            Ln2.config(text=':')
            horas_f()
            if horas <= 0:
                return


        elif minutos > 0:
            Lm.config(text=minutos)
            minutos = minutos - 1

            Ls.after(0, segundero)

    def segundero():
        """
        Funcion recursiva encargada de contar los segundos en un minuto

        Funcion no recibe no retorna

        :return :None

        """
        global segundos
        global horas
        global controlador

        if segundos < 0.5:
            controlador = controlador + 1
            segundos = 61
            minutero()

        if int(horas) <= -1 or segundos <= 0:
            return

        Ls.config(text=int(segundos))
        print(segundos)
        segundos = round((segundos - round((1 / controlador), 3)), 3)
        print(segundos)
        Ls.after(1000, segundero)

    root = Tk()
    root.title("Temporizador")

    root.geometry("550x350")
    root.config(background="#466B3F")

    Lh = Label(root, font=("Italic ", 30), fg='white',background="#466B3F")
    Lh.grid(column=3, row=1, padx=3)
    Ln = Label(root, font=("Italic ", 30), fg='white',background="#466B3F")
    Ln.grid(column=4, row=1,padx=3)
    Lm = Label(root, font=("Italic ", 30), fg='white',background="#466B3F")
    Lm.grid(column=5, row=1,padx=3)
    Ln2 = Label(root, font=("Italic ", 30), fg='white',background="#466B3F")
    Ln2.grid(column=6, row=1,padx=3)
    Ls = Label(root, font=("Italic ", 30), fg='white',background="#466B3F")
    Ls.grid(column=7, row=1,padx=3)




    time = IntVar()
    time2 = IntVar()
    time3 = IntVar()

    e1 = Entry(root, textvariable=time)
    e1.grid(row=2, column=2, padx=30)
    labele1 = Label(root, font=('Arial Bold', 15), fg='white', text='Ingrese Horas',background="#466B3F")
    labele1.grid(column=2, row=1,padx=20)
    e2 = Entry(root, textvariable=time2)
    e2.grid(row=5, column=2, padx=30)
    labele2 = Label(root, font=('Arial Bold', 15), fg='white',text='Ingrese Minutos',background="#466B3F")
    labele2.grid(column=2, row=4,padx=20)
    e3 = Entry(root, textvariable=time3)
    e3.grid(row=7, column=2, padx=30)
    labele3 = Label(root, font=('Arial Bold', 15), fg='white',text='Ingrese Asignatura',background="#466B3F")
    labele3.grid(column=2, row=6,padx=20)

    b1 = Button(root, text="Establecer", font=('Arial Bold', 10), width=5, command=set_timer,background='#595A5C')
    b1.grid(row=8, column=2, padx=30,ipadx=30,pady=10)

    b2 = Button(root, text="Empezar", font=('Arial Bold', 10), width=5, command=minutero,background='#595A5C')
    b2.grid(row=9, column=2, padx=30,ipadx=30,pady=10)

    b3 = Button(root, text="Ver Registro", font=('Arial Bold', 10), width=5, command=tempo_registro,background='#595A5C')
    b3.grid(row=10, column=2, padx=10,ipadx=30,pady=10)


def tempo_registro():

    """
    Crea la interfaz gráfica para observar los registros de temporizador e incializa ver_minutos()

    Función no recibe no retorna

    :return :None

    """

    root2 = Tk()
    root2.title('Registro Temporizador')
    root2.geometry('850x200')
    root2.config(background="#76232F")
    messagebox.showinfo(message="""Al ingresar un periodo de tiempo hacerlo bajo un formato de dia_menor - dia_mayor, Gracias por su colaboracion""")

    ltitulo = Label(root2, font=('Arial Bold', 10), fg='white',text='Ingrese Año',background="#76232F")
    ltitulo.grid(row=0,column=0,padx=10)
    ltitulo2 = Label(root2, font=('Arial Bold', 10), fg='white',text='Ingrese Mes',background="#76232F")
    ltitulo2.grid(row=0,column=1,padx=10)
    ltitulo3 = Label(root2, font=('Arial Bold', 8), fg='white',text='Ingrese Dia o Periodo de tiempo',background="#76232F")
    ltitulo3.grid(row=0,column=2,padx=10)
    ltitulom = Label(root2, font=('Arial Bold', 8), fg='white',text='Ingrese Asignatura',background="#76232F")
    ltitulom.grid(row=0,column=3,padx=30)
    global entrada_fecha
    global entrada_fecha2
    global entrada_fecha3
    global entrada_materia

    entrada_fecha = Entry(root2,width=30)
    entrada_fecha.grid(row=2,column=0)
    entrada_fecha2 = Entry(root2,width=30)
    entrada_fecha2.grid(row=2,column=1)
    entrada_fecha3 = Entry(root2,width=30)
    entrada_fecha3.grid(row=2,column=2)
    entrada_materia = Entry(root2,width=30)
    entrada_materia.grid(row=2,column=3,padx=30)

    print('si estoy aca')
    bb = Button(root2, text='Ver Registro', background='#595A5C', width='20', height='1',
           command=lambda: lmindeestudio.config(text=ver_minutos()))
    bb.grid(row=3,column=1,pady=5)

    lentrada = Label(root2, font=('Arial Bold', 20), text='Tiempo de estudio:', fg='white',background="#76232F")
    lentrada.grid(row=4,column=1,pady=5)


    lmindeestudio = Label(root2, font=('Arial Bold', 20), text=':', fg='white',background="#76232F")
    lmindeestudio.grid(row=5,column=1,pady=5)

def crear_bd():

    """
    Función encargada de revisar la existencia de la base de datos para el temporizador, en caso de no existir
    la crea. Del mismo modo crea una tabla y revisa su existencia, y la crea en caso de no existir.

    Función no recibe no retorna

    :retun:None

    """

    try:
        conn2 = sqlite3.connect('tempo')

        c2 = conn2.cursor()

        c2.execute("""CREATE TABLE tempo_info(
                     usuario text,
                     pass text,
                     fecha text,
                     tiempo text,
                     materia text)""")


        conn2.commit()

        conn2.close
    except: return

def guardar_tempo(tempo,materia ,fecha  = str(date.today())):
    """
    Aloja la información obtenido por el boton Establecer, referente a tiempo de estudio, usuario y asignatura
    
    Función Recibe no retorna

    :return:None

    """

    global entrada_user
    print(entrada_user)

    conn2 = sqlite3.connect('tempo')

    c2 = conn2.cursor()

    c2.execute("INSERT INTO tempo_info VALUES (:usuario,:pass,:fecha,:tiempo,:materia)",

               {'usuario': entrada_user.get(),
                'pass': contraseña.get(),
                'fecha': fecha,
                'tiempo': tempo,
                'materia': materia})

    conn2.commit()

    conn2.close()


def ver_minutos():
    """
    Permite ver el tiempo de estudio mediante los parametros de fecha, usuario y materia, 
    muestra tiempo de estudio no unicamente en fechas sino también en periodos de tiempo

    Función no recibe retorna
    
    :return:None

    """
    global  entrada_fecha
    global entrada_fecha2
    global entrada_fecha3
    global entrada_user
    global entrada_materia
    usuario = str(entrada_user.get())
    fecha = str(entrada_fecha.get())+'-'+str(entrada_fecha2.get())+'-'+str(entrada_fecha3.get())
    conn2 = sqlite3.connect('tempo')

    c2 = conn2.cursor()

    c2.execute("SELECT *,oid FROM tempo_info")
    info = c2.fetchall()
    print(info)
    print(fecha)
    tiempo_de_estudio = 0
    valor_final = 0
    if len(str(entrada_fecha.get())+'-'+str(entrada_fecha2.get())+'-'+str(entrada_fecha3.get())) == 10:
        for elemento in info:
            if usuario in elemento[0] and (str(entrada_fecha.get())+'-'+str(entrada_fecha2.get())+'-'+str(entrada_fecha3.get())) in elemento[2]and contraseña.get() in elemento[1] and elemento[4] in str(entrada_materia.get()):
                tiempo_de_estudio = tiempo_de_estudio + int(elemento[3])
        valor_final = 'Horas: '+ str(tiempo_de_estudio // 60) + '  Minutos: ' + str(tiempo_de_estudio % 60)
    if len((str(entrada_fecha.get())+'-'+str(entrada_fecha2.get())+'-'+str(entrada_fecha3.get()))) == 13:
        for elemento in info:
            if usuario in elemento[0] and int((str(entrada_fecha.get())+'-'+str(entrada_fecha2.get())+'-'+str(entrada_fecha3.get()))[11:12])>= int(elemento[2][8:9])and int((str(entrada_fecha.get())+'-'+str(entrada_fecha2.get())+'-'+str(entrada_fecha3.get()))[8:9])<= int(elemento[2][8:9]) and contraseña.get() in elemento[1]and elemento[4] in str(entrada_materia.get()):
                tiempo_de_estudio = tiempo_de_estudio + int(elemento[3])
        valor_final = 'Horas: '+ str(tiempo_de_estudio // 60) + '  Minutos: ' + str(tiempo_de_estudio % 60)




    print(valor_final)
    return valor_final



    conn2.commit()
    conn2.close()

      

def obtener_fechas():

    """
    Web scrapper encargado de recibir mediante la URL determianda las fechas y la razon de los festivos del años 2020
    y 2021 en Colombia, posterior a la busqueda, filtrado y almacenado de los datos reuqeridos, los acomoda por año
    y posteriormente los aloja en una lista utilizada en funciones posteriores, la cual contiene las lineas de texto con
    datos de dia, mes y razón del dia festivo.

    Función no recibe, retorna

    :return: festivos_txt
    type(festivos_txt) = list

    """

    url = "https://www.municipio.com.co/dias-festivos-2020-2021.html"
    page = urlopen(url)
    html = page.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")

    texto = soup.get_text()

    festivos =[linea for linea in texto.split('\n') if linea !='']

    contador_2020 = 0

    festivos_text = []

    for elemento in range(0, len(festivos)):
        if festivos[elemento][0] in indices and contador_2020 <= 18:
            fecha = festivos[elemento] +' '+ festivos[elemento+1] + ' ' + festivos[elemento+2]
            # print(fecha)
            festivos_text.append(fecha)
            elemento = festivos[elemento + 3]
            contador_2020 += 1

        elif festivos[elemento][0] in indices and contador_2020 == 19:
            fecha = festivos[elemento] +' '+ festivos[elemento+1] + ' ' + festivos[elemento+2]           
            festivos_text.append(fecha)
            elemento = festivos[elemento + 3]
            contador_2020 += 1

        elif festivos[elemento][0] in indices and contador_2020 > 19:
            fecha = festivos[elemento] +' '+ festivos[elemento+1] + ' ' + festivos[elemento+2]
            # print(fecha)
            festivos_text.append(fecha)
            elemento = festivos[elemento + 3]
            contador_2020 += 1
    
    return (festivos_text)


def verificar_guardado():

    """
    Mediante la libreria os.path se encarga de verificar si el archivo necesario, en este caso festivos.txt existe
    en caso de existir no ejecuta ninguna acción sobre la aplicación, en caso de no existir el archivo
    lo genera bajo el nombre predifinido y lo enruta con el codigo para su uso
    
    Función no recibe no retorna

    :return :None

    """
    file_exists = os.path.isfile('festivos.txt')
    if file_exists:
        pass
    else:
        file = open("festivos.txt", "w+")
        file.close()

def verificar_festivos_calendar():
    """
    Mediante la libreria os.path se encarga de verificar si el archivo necesario, en este caso festivos_calendar.txt existe
    en caso de existir no ejecuta ninguna acción sobre la aplicación, en caso de no existir el archivo
    lo genera bajo el nombre predifinido y lo enruta con el codigo para su uso
    
    Función no recibe no retorna

    :return :None

    """
    file_exists = os.path.isfile('festivos_calendar.txt')
    if file_exists:
        pass
    else:
        file = open("festivos_calendar.txt", "w+")
        file.close()


def guardar(festivos):
    """
    Se encarga de tomar la lista de dias festivos obtenidos en el Webscrapper y registrarlos de manera ordenada
    en un archivo.txt, en este caso festivos.txt, esta función es un paso intermedio para la muestra de los datos en
    la aplicación. Inicializa verificar_guardado()

    Función recibe no retorna

    :return :None
    """
    verificar_guardado()
    archivo_festivos = open('festivos.txt', 'a', newline='')
    
    for elemento in festivos:
        archivo_festivos.write(elemento)
        archivo_festivos.write('\n')
            
      
    archivo_festivos.close

def definir_festivos():

    """
    Se encarga de tomar los datos de dias festivos en el archivo festivos.txt, y convertirlos a un formato de tipo
    dia/mes/año y registrarlos en un archivo de nombre festivos_calendar.txt para la posterior lectura y presentación
    en la interfaz gráfica, incializa verificar_festivos_calendar()

    Función no recibe no retorna

    :return:None

    """
    verificar_festivos_calendar()

    archivo_base = open("festivos.txt", 'r')
    texto = archivo_base.read()
    archivo_base.close()
    texto = texto.split('\n')

    archivo_añadir = open("festivos_calendar.txt", 'a', newline='')

    # print(texto)
    contador_año = 0
    global añadir_calendar
    añadir_calendar = {}


    for elemento in texto:
        if elemento ==  'Festivos del 2020' or elemento == 'Festivos del 2021' or elemento =='':
            continue
        else:
            elemento = elemento.split(' ')
            # print(elemento)
            d = elemento[0]
            m = elemento[2]
            
            (dia, mes) = (d,m)
            if dia in dias:
                if mes in meses:
                    if contador_año <= 18:
                        evento = dia+'/'+meses.get(mes)+'/'+'20'
                        mensaje = ' '.join(elemento[4:])
                        añadir_calendar[evento] = mensaje
                        archivo_añadir.write(evento)
                        archivo_añadir.write(' ')
                        archivo_añadir.write(mensaje)
                        archivo_añadir.write('\n')
                        # print(evento)
                        contador_año += 1
                    elif contador_año > 18:
                        evento = dia+'/'+meses.get(mes)+'/'+'21'
                        mensaje = ' '.join(elemento[4:])
                        añadir_calendar[evento] = mensaje
                        archivo_añadir.write(evento)
                        archivo_añadir.write(' ')
                        archivo_añadir.write(mensaje)
                        archivo_añadir.write('\n')
                        
                        # print(evento)
                        contador_año += 1

    print(añadir_calendar)
    archivo_añadir.close()

def main():
    """
    llama a la funcion  login()
    :return:None
    """
    login()



main()

mainloop()