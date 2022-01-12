import tkinter as tk
import random
import math
from fractions import Fraction

tipo = 0
pregunta = ''
respuesta = 0

def click_return(event):
    responder_pregunta()
# Para que para en vez de oprimir "responder" puedas oprimir enter o return 

def check_float(usuario):
    try:
        numero = float(usuario)
    except ValueError:
        if respuesta == 0:
            return 1
        else:
            return 0
    return usuario
# 

def iniciar_sumar_restar():
    global tipo
    tipo = 0
    cambiar_solucionador()

def iniciar_multi_divi():
    global tipo
    tipo = 1
    cambiar_solucionador()

def iniciar_expon():
    global tipo
    tipo = 2
    cambiar_solucionador()

def iniciar_pitagoras():
    global tipo
    tipo = 3
    cambiar_solucionador()

def iniciar_pemdas():
    global tipo
    tipo = 4
    cambiar_solucionador()

def iniciar_pendiente():
    global tipo
    tipo = 5
    cambiar_solucionador()
# Las siguientes funciones son para que el codigo sepa que opción fue 
# elegida (suma y resta, multiplicacion y división, PEMDAS, ect..) 
# las variables de tipo, son las que determina cual area fue escogida


def preguntar_sumar_restar():
    global pregunta
    global respuesta
    numero1 = random.randint(-1000,1000)
    numero2 = random.randint(0,1000)
    
    plus_or_minus = random.randint(1,2)
    
    if plus_or_minus == 1:
        signo = '+'
        respuesta = numero1 + numero2
    else:
        signo = '-'
        respuesta = numero1 - numero2
    
    pregunta = str(numero1) + ' ' + str(signo) + ' ' + str(numero2) + ' ='
# En esta función le damos al usuario problemas de sumar y restar, 
# cada problema despliega numeros de forma aleatoria 
# los margenes en las preguntas llegam desde -1000 a 1000. 

def preguntar_multi_divi():
    global pregunta
    global respuesta
    a = random.randint(-1000,1000)
    b = random.randint(-1000,1000)
    c = random.randint(1,2)
    
    signo = ''
    if c==1:
        signo = '*'
        respuesta = a*b
    else:
        signo = '÷'
        respuesta = round(a/b,3)

    pregunta = str(a) + ' ' + str(signo) + ' ' + str(b) + ' ='
# En esta función le damos al usuario problemas de multiplicar y dividir, 
# cada problema despliega numeros de forma aleatoria 
# los margenes en las preguntas llegam desde -1000 a 1000. 

def preguntar_exponenciales():
    global pregunta
    global respuesta
    numero1 = random.randint(0,12)
    if numero1 <= 3:
        numero2 = random.randint(0,5)
    else:
        numero2 = random.randint(0,3)
        
    pregunta = str(numero1) + '^' + str(numero2) + ' ='
    respuesta = numero1**numero2
# En esta función le damos al usuario problemas de exponenciales, 
# cada problema despliega numeros de forma aleatoria 
# los margenes en las preguntas llegam desde 0 a 5 en exponencial y 0 a 12 los numeros abajo del exponencial. 

def preguntar_pitagoras():
    global pregunta
    global respuesta
    a = random.randint(1,10)
    b = random.randint(1,10)
    pregunta = 'Lado A es igual a ' + str(a) + ' y lado B es igual a ' + str(b) + '.\n¿Cual es lado C?'
    respuesta = round(math.sqrt(a**2 + b**2),3)
# En esta función le damos al usuario problemas de pitagoras, 
# cada problema despliega numeros de forma aleatoria 
# los margenes en las preguntas llegam desde 1 a 10. 
    
def preguntar_pemdas():
    global pregunta
    global respuesta
    preguntas = ['14*18/2*18-7','15*18+12*3+9','15*5/4*2','(5-2)*(5-2*15)/20','(7*7)/(7*7)',
    '(10^2*5)/3*3/6','20/5*3(7*8)','5-5*10*6','(6+3)^2+(9-10/5)','(19-8)*(10+4)+8^2']
    respuestas = [2261,315,37.5,-3.75,1,83.33,672,-295,86,218]
    num = random.randint(0,9)
    pregunta = 'Responde esta pregunta usando PEMDAS,\nrondea a dos decimales: \n' + preguntas[num]
    respuesta = respuestas[num]
# En esta función le damos al usuario problemas de pemdas, para que los problemas no sean tan similares
# creamos una lista con varios diferentes problemas.

def preguntar_pendiente():
    global pregunta
    global respuesta
    x1 = random.randint(-50,0)
    y1 = random.randint(-50,50)
    x2 = random.randint(0,50)
    y2 = random.randint(-50,50)
    a = y2 - y1
    b = x2 - x1

    pregunta = "Cual es el pendiente de los puntos:\n(" + str(x1) + ", " + str(y1) + ") y (" + str(x2) + ", " + str(y2) + ")"
    respuesta = round(a/b,3)
# En esta función le damos al usuario problemas de la pendiente, dado que el problema requiere 4 numeros iniciales
# creamos randoms que van entre -50 a 0, -50 a 50, 0 a 50 y -50 a 50.

def preguntar_pregunta():
    if tipo == 0:
        preguntar_sumar_restar()
    elif tipo == 1:
        preguntar_multi_divi()
    elif tipo == 2:
        preguntar_exponenciales()
    elif tipo == 3:
        preguntar_pitagoras()
    elif tipo == 4:
        preguntar_pemdas()
    elif tipo == 5:
        preguntar_pendiente()
        
    texto['text'] = texto['text'] + '\n\n' + pregunta
# Esta funcion esta encargada en decirle al codigo que area escogimos para trabajar 

def responder_pregunta():
    global correctas
    global incorrectas
    global contador
    
    input_usuario = entry_box.get()
    texto['text'] = texto['text'] + '\n' + input_usuario
    if float(check_float(input_usuario)) == respuesta:
        texto['text'] = texto['text'] + '\n' + 'Eso es correcto!'
        correctas += 1
        contador += 1
    else:
        texto['text'] = texto['text'] + '\n' + 'Incorrecto... La respuesta correcta era ' + str(respuesta)
        incorrectas += 1
        contador += 1
    entry_box.delete(0,20)
    preguntar_pregunta()
# Esta función es la que se encarga de ver si la respuesta del usuario es correcta o incorrecta.
# Utiliza la variable global de respuesta para verificar con las otras funciones. 

def cambiar_menu():
    global correctas
    global incorrectas
    global contador
    
    correctas = 0
    incorrectas = 0
    contador = 0
    
    frame = tk.Frame(root, bg='white')
    frame.place(relx= 0, rely = 0, relwidth = 1, relheight = 1)
    
    title = tk.Label(frame, text= "Escoge el tipo de matematicas que practicar", fg = 'black', bg = 'white', height = 3)
    title.pack()
    
    suma_resta = tk.Button(frame, text = 'Sumar y Restar', fg = 'black', command = iniciar_sumar_restar)
    suma_resta.place(relx = 0.05, rely = 0.1, relheight = 0.1, relwidth = 0.9)
    
    multi_divi = tk.Button(frame, text = 'Multiplicar y Dividir', fg = 'black', command = iniciar_multi_divi)
    multi_divi.place(relx = 0.05, rely = 0.225, relheight = 0.1, relwidth = 0.9)
    
    exponencial = tk.Button(frame, text = 'Exponencial', fg= 'black', command = iniciar_expon)
    exponencial.place(relx = 0.05, rely = 0.35, relheight = 0.1, relwidth = 0.9)
    
    pitagoras = tk.Button(frame, text = 'Encontrar la Hipotenusa Utilizando Pitagoras', \
                          fg = 'black', command = iniciar_pitagoras)
    pitagoras.place(relx = 0.05, rely = 0.475, relheight = 0.1, relwidth = 0.9)
    
    pemdas = tk.Button(frame, text = 'PEMDAS', fg = 'black', command = iniciar_pemdas)
    pemdas.place(relx = 0.05, rely = 0.6, relheight = 0.1, relwidth = 0.9)
    
    pendiente = tk.Button(frame, text = 'Encontrar la pendiente de dos puntos', fg = 'black', command = iniciar_pendiente)
    pendiente.place(relx = 0.05, rely = 0.725, relheight = 0.1, relwidth = 0.9)
# Aqui en esta función ponemos el codigo para agregar todos los botones de las areas que se deben de escoger
# al ponerle RUN al codigo. Cada area tiene su propio button que se representa con tk.button() y dentro de las
# parentesis corremos el "command" de cada area. 

def cambiar_solucionador():
    global entry_box
    global texto
    
    frame = tk.Frame(root, bg = '#e8e8e8')
    frame.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)
    
    entry_box = tk.Entry(frame, bg = 'white', fg = 'black', bd = 3)
    entry_box.place(relx = 0.05, rely = 0.885, relheight = 0.045, relwidth = 0.9)
    
    terminar = tk.Button(frame, text = 'Terminar', bg = 'white', command = cambiar_resultados)
    terminar.place(relx = 0.05, rely = 0.94, relheight = 0.045, relwidth = 0.425)
    
    responder = tk.Button(frame, text = 'Responder', bg = 'white', command = responder_pregunta)
    responder.place(relx = 0.525, rely = 0.94, relheight = 0.045, relwidth = 0.425)
    
    root.bind('<Return>', click_return)
    
    frame_preguntas = tk.Frame(frame, bg = 'white')
    frame_preguntas.place(relx = 0.05, rely = 0.025, relheight = 0.85, relwidth = 0.9)
    
    texto = tk.Label(frame_preguntas, fg = 'black', bg = 'white', anchor = 'sw',justify = 'left')
    texto.place(relheight = 1, relwidth = 1)
    
    preguntar_pregunta()
# En esta función ponemos la caja donde respondes las preguntas de cualquier area que escogiste, la información
# puesta en esta "entry" trabajara con otras partes del codigo para evaluar la respuesta.
    
def cambiar_resultados():
    global correctas
    global incorrectas
    global contador
    
    frame = tk.Frame(root, bg = '#e8e8e8')
    frame.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)
    
    title_res = tk.Label(frame, text = 'Resultados:', fg = 'black', bg = '#e8e8e8')
    title_res.place(relx = 0.375, rely = 0.3, relheight = 0.15, relwidth = 0.25)
    
    display_res = tk.Label(frame, text = 'Preguntas Correctas: ' + str(correctas) \
                           + '\nPreguntas Incorrectas: ' + str(incorrectas) + '\nTotal: ' + \
                           str(contador), fg = 'black')
    display_res.place(relx = 0.25, rely = 0.4, relheight = 0.15, relwidth = 0.5)
    
    OK = tk.Button(frame, text = 'Ok', bg = 'white', command = cambiar_menu)
    OK.place(relx = 0.3, rely = 0.6, relheight = 0.045, relwidth = 0.4)
# En esta funcion ponemos la informacion de las preguntas desplegadas al usuario. Sus preguntas correctas, 
# incorrectas y un contador para ver cuantas respondio.

root = tk.Tk()

canvas = tk.Canvas(root, height = 1136, width = 640)
canvas.pack()
# Creacion de la window de la applicacion

correctas = 0
incorrectas = 0
contador = 0
entry_box = 0
texto = 0

cambiar_menu()

root.mainloop()
# Con este mantienes que el codigo siga corriendo pero no pida nada mas afuera de lo escrito.