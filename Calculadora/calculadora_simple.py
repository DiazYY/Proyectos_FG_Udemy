import tkinter as tk

#ruta_icono = 'C:\\Users\\the_d\OneDrive\Documentos\Programacion\Proyectos_FG_Udemy\Calculadora\calculator.ico'

# Create Main Window
windows = tk.Tk()
windows.title('Calculadora')

# Change Icon
#windows.iconbitmap(ruta_icono)

# variables
expresion = ''
resultado_mostrado = False

# Funcion para actualizar la expresion en el cuadrop de texto
def pulsar_tecla(tecla):
    global expresion

    expresion += str(tecla)
    texto_visor.set(expresion)


def limpiar_visor():
    global expresion, resultado_mostrado

    expresion = ''
    texto_visor.set(expresion)
    resultado_mostrado = False

# Funcion para calcular el resultado
def calcular():
    global expresion, resultado_mostrado

    try:
        # Evaluar la expresion ingresada
        resultado = eval(expresion, {"__builtins__":None}, {})
        # verificar si resultado es un numero entero
        if resultado == int(resultado):
            resultado = int(resultado)
        texto_visor.set(str(resultado))
        expresion = str(resultado)
        resultado_mostrado = True
    except Exception as e:
        texto_visor.set("Error")
        expresion = ''
        resultado_mostrado = False

# Configurar filas y columnas
for n in range(5):
    windows.grid_rowconfigure(n, weight=1)

for n in range(3):      # Ajustar a 4 columnas
    windows.grid_columnconfigure(n, weight=1)

texto_visor = tk.StringVar()
pantalla = tk.Entry(windows,
                    textvariable=texto_visor,
                    font=('Helvetica', 24),
                    bd=10,
                    insertwidth=4,
                    width=14,
                    borderwidth=4,
                    justify="right")

pantalla.grid(row=0,column=0, columnspan=4)

botones = [
    (7,1,0),(8,1,1),(9,1,2),('/',1,3),
    (4,2,0),(5,2,1),(6,2,2),('*',2,3),
    (1,3,0),(2,3,1),(3,3,2),('-',3,3),
    (0,4,0),(',',4,1),('C',4,2),('+',4,3),
    ]
# crear botones
for (texto, fila, columna) in botones:
    if texto == 'C':
        comando = limpiar_visor
    else:
        comando = lambda x=texto: pulsar_tecla(x)
    boton = tk.Button(windows,
                      text=texto,
                      padx=20,
                      pady=20,
                      font=('Helvetica', 20),
                      command=comando)


    boton.grid(row=fila, column=columna, sticky='nsew')

    # Configuración del color de fondo para números
    if isinstance(texto, int):  # Verificar si el texto es un número
        boton.config(bg='Cadetblue1')
    else:
        boton.config(bg='MediumPurple1')

# Crear boton igual
button_equal = tk.Button(windows, text='=',
                        padx=20,
                        pady=20,
                        font=('Helvetica', 40),
                        bg='lightgreen',
                        command=calcular)
button_equal.grid(row=5, column=0, columnspan=4, sticky='nsew')

windows.mainloop()
