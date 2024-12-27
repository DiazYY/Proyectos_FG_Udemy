import tkinter as tk

ruta_icono = 'C:\\Users\\the_d\OneDrive\Documentos\Programacion\Proyectos_FG_Udemy\Calculadora\calculator.ico'

# Create Main Window
windows = tk.Tk()
windows.title('Calculadora')

# Change Icon
windows.iconbitmap(ruta_icono)

# Variables
expresion = ''
resultado_mostrado = False

# Función para actualizar la expresión en el cuadro de texto
def pulsar_tecla(tecla):
    global expresion, resultado_mostrado

    if resultado_mostrado:
        if tecla in ['+', '-', '*', '/']:  # Si presiona un operador, continuar
            resultado_mostrado = False
        else:  # Si presiona un número o ".", comenzar una nueva expresión
            expresion = ''
            resultado_mostrado = False

    expresion += str(tecla)
    texto_visor.set(expresion)

# Función para limpiar el visor
def limpiar(event=None):
    global expresion, resultado_mostrado

    expresion = ''
    texto_visor.set(expresion)
    resultado_mostrado = False

# Función para calcular el resultado
def calcular(event=None):
    global expresion, resultado_mostrado

    try:
        # Evaluar la expresión ingresada
        resultado = eval(expresion, {"__builtins__": None}, {})
        # Verificar si el resultado es un número entero
        if resultado == int(resultado):
            resultado = int(resultado)
        texto_visor.set(str(resultado))
        expresion = str(resultado)
        resultado_mostrado = True

    except Exception as e:
        texto_visor.set("Error")
        expresion = ''
        resultado_mostrado = False

# Función para manejar la entrada desde el teclado
def entrada_teclado(event):
    tecla = event.char
    if tecla.isdigit() or tecla in ['+', '-', '*', '/', '.']:
        pulsar_tecla(tecla)
    elif tecla == '\r':  # Enter para calcular
        calcular()
    elif tecla == '\x08':  # Backspace para borrar el último carácter
        borrar_ultimo()
    return "break"

# Función para borrar el último carácter ingresado
def borrar_ultimo(event=None):
    global expresion
    expresion = expresion[:-1]  # Elimina el último carácter
    texto_visor.set(expresion)

# Configurar filas y columnas
for n in range(5):
    windows.grid_rowconfigure(n, weight=1)

for n in range(4):  # Ajustar a 4 columnas
    windows.grid_columnconfigure(n, weight=1)

# Visor de texto
texto_visor = tk.StringVar()
pantalla = tk.Entry(windows,
                    textvariable=texto_visor,
                    font=('Helvetica', 30, 'bold'),
                    bd=10,
                    insertwidth=4,
                    width=16,
                    borderwidth=2,
                    justify="right",
                    relief='sunken',
                    bg='#e8f0fe',
                    fg='#333333')
pantalla.grid(row=0, column=0, columnspan=4,sticky="ew",padx=10,pady=10)

# Vincular el teclado al visor
pantalla.bind('<Key>', entrada_teclado)  # Captura teclas presionadas
pantalla.bind('<Return>', calcular)  # Enter para calcular
pantalla.bind('<BackSpace>', borrar_ultimo)  # Backspace para borrar

# Botones
botones = [
    (7, 1, 0), (8, 1, 1), (9, 1, 2), ('/', 1, 3),
    (4, 2, 0), (5, 2, 1), (6, 2, 2), ('*', 2, 3),
    (1, 3, 0), (2, 3, 1), (3, 3, 2), ('-', 3, 3),
    (0, 4, 0), ('.', 4, 1), ('C', 4, 2), ('+', 4, 3),
]

# Colores almacenados en variables
color_fondo_numero = '#b3cde0'
color_fondo_operacion = '#7A869A'
color_fondo_especial = '#9B90B6'
color_fondo_calcular = '#b0e57c'
color_fondo_presionado = '#6a51a3'
color_fondo_calcular_presionado = '#76c7c0'
color_texto_numero = '#333333'
color_texto_especial = '#ffffff'

# Crear botones
for (texto, fila, columna) in botones:
    if texto in ['+','-','*','/']:
        comando = lambda x=texto: pulsar_tecla(x)
        color_fondo = color_fondo_operacion
        color_texto = color_texto_especial
    elif texto == 'C':
        comando = limpiar
        color_fondo = color_fondo_especial
        color_texto = color_texto_especial
    elif texto == '.':
        comando = lambda x=texto: pulsar_tecla(x)
        color_fondo = color_fondo_especial
        color_texto = color_texto_especial
    else:
        comando = lambda x=texto: pulsar_tecla(x)
        color_fondo = color_fondo_numero
        color_texto = color_texto_numero

    boton = tk.Button(windows,
                      text=texto,
                      padx=20,
                      pady=20,
                      font=('Helvetica', 20, 'bold'),
                      command=comando,
                      bd=1,
                      relief="raised",
                      bg=color_fondo,
                      fg=color_texto,
                      activeforeground=color_fondo_especial,
                      activebackground=color_fondo_presionado)
    boton.grid(row=fila, column=columna, sticky='nsew', padx=2, pady=2)


# Botón igual
button_equal = tk.Button(windows,
                         text='=',
                         padx=20,
                         pady=20,
                         font=('Helvetica', 40, 'bold'),
                         bg=color_fondo_calcular,
                         fg=color_texto_numero,
                         bd=1,
                         relief="raised",
                         activeforeground=color_fondo_calcular_presionado,
                         activebackground=color_texto_especial,
                         command=calcular)
button_equal.grid(row=5, column=0, columnspan=4, sticky='ew',padx=2,pady=2)

# Iniciar loop principal
windows.mainloop()
