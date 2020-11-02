
from tkinter import *
from tkinter import messagebox
from tkcalendar import *
from io import *


root = Tk()
root.title("PRIMIAPP")
root.geometry("415x850")
root.config(background="blue")
t = 0
# se crea y se abre el archivo
primiapp =open('primiapp.txt','r')
primiapp.close()


def init_window():
    """
    Abre la ventan inicial de la aplicacion define a calendar(),temporizador() y notas()


    :return: None
    """
    label1 = Label(root,text="PRIMIAPP",font=("Italic",50))
    label1.grid(column=0,row=0)

    def calendar():
        """
        Abre una ventana nueva  y un widget clendario utilizando tkcalendar, define inita_agenda()
        :return:None
        """
        root = Tk()
        root.title("Calendar")
        root.geometry("600x600")
        root.config(background="orange")

        cal = Calendar(root, selectmode="day", year=2020, month=10, day=29,font=("Arial",20))
        cal.pack(pady=20, fill="both", expand=True)

        def init_agenda():
            """
             abre una nueva ventana con dos widget de texto para insertar la informacion, inicializa Take_input() y Show_info()
            :return: None
            """
            my_label.config(text=cal.get_date())
            def take_input():
                """
                Guarda la informacion  de T en un archivo tambien la inserts en T2

                :return:None
                """
                INPUT = t.get("1.0", "end-1c")
                t2.insert(END,INPUT)
                print(INPUT)
                archivo_texto =open('primiapp.txt','a',newline='')

                info = cal.get_date()+INPUT

                archivo_texto.write(info)
                archivo_texto.write('\n')
                archivo_texto.close()


            def show_info():
                """
                abre el archivo donde se encuantra la informacion por fechas y la  inserta en T2
                :return:None
                """

                archivo_texto = open('primiapp.txt', 'r')
                texto = archivo_texto.read()
                archivo_texto.close()
                texto = texto.split('\n')

                for recordatorio in texto:
                    if recordatorio[0:8] == str(cal.get_date()):
                        t2.insert(END, recordatorio)
                        t2.insert(END,'\n')



            root = Tk()
            root.title("Agendar")
            root.geometry("500x300")
            root.config(background="yellow")
            labelA = Label(root,text="AGENDAR",font=("italic",20))
            labelA.grid(row=0,column=0)
            labelD = Label(root,text="AGENDADO",font=("italic",20))
            labelD.grid(row=0,column=2)
            labelAD = Label(root,text=cal.get_date(),font=("italic",20))
            labelAD.grid(row=1,column=2)
            labele = Label(root,text="",font=("italic",30))
            labele.config(background="yellow")
            labele.grid(row=1,column=0)
            t = Text(root,width=20,height=5,font=("italic",10))
            t.grid(row=2,column=0)
            labele2 = Label(root, text="",font=("italic", 30),width=2)
            labele2.config(background="yellow")
            labele2.grid(row=2,column=1)
            t2 = Text(root,width=20,height=5,bg="light cyan",font=("italic",10))
            t2.grid(row=2,column=2)
            # widget Button que llama a la funcion Take_inpput()
            bE = Button(root, text="Guardar", font=("Italic", 10), command=lambda: take_input())
            bE.grid(row=3,column=0)
            # widget Button que llama a la funcion show_info()
            ba = Button(root, text="Guardado", font=("Italic", 10), command=lambda: show_info())
            ba.grid(row=3,column=2)
            #cal.get_date()
            #T2.get("1.0", "end-1c")

        # widget que llama a la funcion init_agenda()
        my_button = Button(root, text="Abrir agenda", command= lambda:init_agenda())
        my_button.pack(pady=20)

        my_label = Label(root, text="")
        my_label.pack(pady=20)

    def notas():
        """
        define las funciones ventana_notas(),click_dame_la_nota(),ponderado_de_notas() e impresion()
        :return:None
        """
        def ventana_notas():
            """
            abre una ventna nueva con dos widget Entry para ingresar la nota limite y las notas obtenidas
            :return:None
            """
            window = Tk()
            window.title('Promedio de notas')
            window.geometry('600x250')
            window.config(background="red")

            label = Label(window, text='Calculo de notas', font=('', 15))
            label.grid(column=0, row=0)
            label.config(background='red')

            entrada_notas = Entry(window, width=20)
            entrada_notas.grid(column=1, row=1)
            entrada_nota_limite = Entry(window, width=20)
            entrada_nota_limite.grid(column=1, row=2)

            label_entrada_notas = Label(window, text='Ingrese sus notas: ', font=('Arial Bold', 15))
            label_entrada_notas.grid(column=0, row=1)
            label_entrada_notas.config(background='red')
            label_entrada_nota_limite = Label(window, text="""Ingrese la nota minima
             para pasar: """, font=('Arial Bold', 15))
            label_entrada_nota_limite.grid(column=0, row=2)
            label_entrada_nota_limite.config(background='red')
            label_nota_actual = Label(window, text='Tu nota es:', font=('Arial Bold', 15))
            label_nota_actual.grid(column=0, row=6)
            label_nota_actual.config(background='red')

            boton = Button(window,
                           command=lambda: click_dame_la_nota(
                               label_nota_actual,
                               entrada_notas.get(),
                               entrada_nota_limite.get()),
                           text='Calcular',
                           bg="purple",
                           fg="white")
            boton.grid(column=1, row=4)

            messagebox.showinfo('Entrada de datos', """Para el campo de notas escribirlas sin espacios unicamente  separadas por una coma (,). Para el campo de nota limite ingresar una sola nota con un decimal """)

        def click_dame_la_nota(label, notas, nota_pasar):
            """
            configura el texto de label para que muestre el resultado ponderado final
            :param string label: "tu nota es"
            :param string notas: notas ingresadas
            :param float nota_pasar: nota limite para pasar
            :return:None
            """
            entrada_notas = notas
            entrada_nota_limite = float(nota_pasar)
            res = ponderado_de_notas(entrada_notas, entrada_nota_limite)
            label.config(text='Resultado: ' + str(res))

        def ponderado_de_notas(notas=0, nota_pasar=3, porcentaje_seccion=0):
            """
            pondera las notas  y determina que mensaje alentador se debe mostrar

            :param string notas: notas separads por comas
            :param float nota_pasar: notas
            :param int porcentaje_seccion: porcentaje se seccion
            :return: string con nota ponderada y mensaje alentador
            """

            notas = notas.split(',')
            elementos = list(map(float, notas))

            if porcentaje_seccion == 0:


                acumulado = 0
                contador = 0
                for elemento in elementos:
                    elemento = float(elemento)
                    acumulado = acumulado + elemento
                    contador += 1
                ponderado_de_notas = acumulado / contador
                if ponderado_de_notas > nota_pasar and ponderado_de_notas >= 4.5:
                    return round(ponderado_de_notas, 4), 'Fresco pelao que va pasando'
                elif ponderado_de_notas > nota_pasar and 4.5 > ponderado_de_notas >= 4:
                    return round(ponderado_de_notas, 4), 'Vas pasando,pero se puede mejorar'
                elif ponderado_de_notas >= nota_pasar and 4 > ponderado_de_notas >= 3:
                    return round(ponderado_de_notas, 4), 'Raspando raspando te puede ir afectando'
                elif ponderado_de_notas < nota_pasar:
                    return round(ponderado_de_notas, 4), 'Llorelo papa '

        def impresion():
            """
            llama a la funcion de ventana_notas()
            :return:none
            """
            ventana_notas()

        impresion()




    def temporizador():
        """
        abre una nueva ventana con dos widget de Button para iniciar la cuenta regresiva  y uno de Entry para ingresar el tiempo,
        :return:None
        """
        global t
        t = 0
        def set_timer():
            """
            le asigna el valor int del Entry e1 a t
            :return: int t
            """
            global t
            t = t + int(e1.get())
            return t

        def countdown():
            """
            cada segundo le resta 1 a el valor de t y configura el texto en t para reflejar el cambio
            :return:None
            """
            global t
            if t > 0:
                L1.config(text=t)
                t = t - 1
                L1.after(1000, countdown)
            elif t == 0:
                print("end")
                L1.config(text="Ya puede tomar un descanso", font=("arial", 20))


        root = Tk()
        root.title("Temporizador")

        root.geometry("600x200")
        root.config(background="green")
        L1 = Label(root, font=("Italic ", 30))
        L1.grid(column=3, row=0)


        time = StringVar()
        e1 = Entry(root, textvariable=time)
        e1.grid(row=1, column=2,padx=30)

        b1 = Button(root, text="SET", font=("Italic", 10), width=5, command=set_timer)
        b1.grid(row=4, column=2, padx=30)

        b2 = Button(root, text="START", font=("Italic", 10), width=5, command=countdown)
        b2.grid(row=6, column=2, padx=30)





    # botones que  llaman a las funciones principales de la applicacion
    labeln = Label(root, text="", font=("Italic", 50),bg="blue")
    labeln.grid(column=0, row=1)
    boton_r = Button(root,command = lambda:calendar(), text="Calendario",font=("Italic",20))
    boton_r.grid(column = 0, row= 2)
    labeln2 = Label(root, text="", font=("Italic", 30),bg="blue")
    labeln2.grid(column=0, row=3)
    boton_r = Button(root,command = lambda:notas(), text="Notas",font=("Italic",20))
    boton_r.grid(column = 0, row= 4)
    labeln3 = Label(root, text="", font=("Italic", 30),bg="blue")
    labeln3.grid(column=0, row=5)
    boton_r = Button(root,command = lambda:temporizador(), text="Temporizador",font=("Italic",20))
    boton_r.grid(column = 0, row= 6)
    labeln4 = Label(root, text="", font=("Italic", 30),bg="blue")
    labeln4.grid(column=0, row=7)
    boton_r = Button(root,command = lambda:init_window(), text="restart")
    boton_r.grid(column = 0, row= 8)

def main():
    """
    llama a la funcion  init_window()
    :return:None
    """
    init_window()

main()

mainloop()