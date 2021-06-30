import os , time
os.system('cls')

# 2. Creación de un menú principal y desarrollo de la opción 6 que permite elegir una opción favorita en el menú

# Bloque de funciones

def menuppal(lista_menu): # Menú principal
    os.system('cls')
    print("")
    print("",str("1."),lista_menu[0],"\n", 
    str("2."),lista_menu[1],"\n",
    str("3."),lista_menu[2],"\n",
    str("4."),lista_menu[3],"\n",
    str("5."),lista_menu[4],"\n",
    str("6."),lista_menu[5],"\n",
    str("7."),lista_menu[6],"\n")
    opcion_menu = int(input("Elija una opción: "))
    return opcion_menu

def menuop6(lista_menu): # Selección de una opción favorita
    opcion_favorita = int(input("Seleccione opción favorita: "))
    if (opcion_favorita >= 1 and opcion_favorita <=5): # El usuario debe responder correctamente a 2 adivinanzas para elegir una opción favorita
        adivinanza1 = int(input("Para confirmar por favor responda:\nCuando te pones a contar por mí tienes que empezar. La respuesta es: "))
        if (adivinanza1 == 1):
            adivinanza2 = int(input("Para confirmar por favor responda:\nCuenta las manos o cuenta los pies y sabrás cual número es. La respuesta es: "))
            if (adivinanza2 == 2):
                os.system('cls')
                aux = lista_menu[0] # Se hace el intercambio de las opciones del menú
                lista_menu[0] = lista_menu[(opcion_favorita-1)]
                lista_menu[(opcion_favorita-1)] = aux
            else:
                print("Error")
                menuppal(lista_menu) # En caso de que ocurra algún error, el programa retorna al menú principal
        else:
            print("Error")
            menuppal(lista_menu)
    else:
        print("Error")
        exit()

def funcion_reto2(): # Función que incluye todas las opciones del programa
    lista_menu = ["Cambiar contraseña","Ingresar coordenadas actuales","Ubicar zona wifi más cercana","Guardar archivo con ubicación cercana","Actualizar registros de zonas wifi desde archivo","Elegir opción de menú favorita","Cerrar sesión"]
    contadortotal = 0 # Cuenta el número de intentos fallidos y se sale del menú al ser igual a 3
    contador = 0
    opcion_menu = 1 # Se inicializa en 1 para que entre por primera vez al while
   
    while (opcion_menu != 7 and contadortotal !=3):  # Ciclo repetitivo para controlar el menu
        opcion_menu = menuppal(lista_menu)
        if (opcion_menu > 7) or (opcion_menu <= 0): # Condicional que controla que las opciones del menú esten entre 1 y 7
            contadortotal = contador + 1
            print("Error")

    # El programa permite acceder a las opciones del menú

        if opcion_menu == 1:
            print(f"Usted ha elegido la opción {opcion_menu}") 
            exit()
        
        if opcion_menu == 2:
            print(f"Usted ha elegido la opción {opcion_menu}") 
            exit()

        if opcion_menu == 3:
            print(f"Usted ha elegido la opción {opcion_menu}") 
            exit()

        if opcion_menu == 4:
            print(f"Usted ha elegido la opción {opcion_menu}") 
            exit()
        
        if opcion_menu == 5:
            print(f"Usted ha elegido la opción {opcion_menu}") 
            exit()

        if opcion_menu == 6:
            opcion_menu = menuop6(lista_menu) 
            os.system('cls')

        if (opcion_menu == 7): # Funciona cuando el usuario digita la opción "cerrar sesión", una vez que ha elegido opción favorita
            print("Hasta pronto")
            exit()
        
    if (opcion_menu == 7): # El programa permite al usuario salir del menú al elegir la opción 7
        print("Hasta pronto") # Funciona cuando el usuario digita la opción salir por primera vez (sin elegir opción favorita)
        exit() 

    if (contadortotal>=3): # Si el usuario supera la cantidad de intentos fallidos (3), el programa termina su ejecución
        print("Error")
        exit()               

def login(): # Programa completo, incluye todas las funciones
    
    right_user = 51612 # Usuario predefinido
    right_password = 21615 # Contraseña predefinida
    datos_user=[right_user, right_password] # Se almacenan los datos del login en una lista
    captcha1 = 612 # Captcha1 = últimos 3 valores del usuario (612)
    captcha2 = 5*1+2-6  # Captcha2 = penúltimo número del usuario (1) - se compone de 4 operaciones matemáticas
    right_captcha = 613 # Captcha correcto = captcha 1 (612) + captcha 2 (1)

    print("Bienvenido al sistema de ubicación para zonas públicas WIFI")
    user=int(input("Ingrese el usuario: "))
    if right_user==datos_user[0]:
        password=int(input("Ingrese la contraseña: "))
    else:
        print("Error")
        exit()
        
    if right_password==datos_user[1]:
        captcha = int(input(f"Ingrese la suma del captcha: {captcha1}+{captcha2}= "))
        if right_captcha == captcha:
            print("Sesión iniciada")
            time.sleep(2)
            funcion_reto2() # Ejecuta el menú principal al iniciar sesión
        else:
            print("Error")
            exit()
    else:
        print("Error")
        exit()

login() # Programa completo (llama a la función)