import os , time
os.system('cls')

# 3. El programa permite al usuario cambiar su contraseña e ingresar sus coordenadas actuales

right_user = 51612 # Usuario predefinido
right_password = 21615 # Contraseña predefinida

# Listas

datos_user = [right_user, right_password] # Se almacenan los datos del login en una lista
coordenadas=[[],[],[]] # Lista anidada vacía para registrar las coordenadas ingresadas por teclado

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

def menuopcion6(lista_menu): # Selección de una opción favorita
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
                time.sleep(2)
                funcion_reto2() # En caso de que ocurra algún error, el programa retorna al menú principal
        else:
            print("Error")
            time.sleep(2)
            funcion_reto2()
    else:
        print("Error")
        exit()

def cambio_password(datos_user):
    os.system('cls')
    passwordactual = int(input("Ingrese la contraseña actual: ")) # Se confirma la contraseña actual (21615)
    if datos_user[1] == passwordactual:
        passwordnueva = int(input("Ingrese la nueva contraseña: "))
        if passwordnueva == datos_user[1]: # Arroja un error si la contraseña nueva es igual a la actual (21615)
            print("La nueva contraseña no puede ser igual a la contraseña actual")
            time.sleep(2)
        else:
            datos_user[1] = passwordnueva # Si la contraseña es diferente a 21615, entonces se actualiza la contraseña en la lista datos_user
            time.sleep(1)
    else:
        print("Error")    
        exit() # Si la contraseña actual se ingresa de forma errónea, el programa finaliza su ejecución

def coordenadas_actuales(coordenadas):

    os.system('cls')
    time.sleep(2) 
    if len(coordenadas[0]) == 0: # Se usa para saber si el usuario ya ingresó los datos de ubicación
        print("Ingrese las coordenadas de los tres sitios que más frecuenta (trabajo, casa, parque): ")
        for x in range(3):
            lat = float(input(f"Ingrese latitud {x+1}: "))
            if lat < 6.077 or lat > 6.284: # Rango de latitud predeterminado (Betulia, Antioquia)
                print("Error coordenada")
                exit()
            else:
                lon = float(input(f"Ingrese longitud {x+1}: "))
                if lon < -76.049 or lon > -75.841: # Rango de longitud predeterminado (Betulia, Antioquia)
                    print("Error coordenada")
                    exit()
                else:    
                    coordenadas[x] = [lat,lon] # Las coordenadas ingresadas por el usuario se almacenan en la lista coordenadas
                    time.sleep(2) 
    else:
        for x in range(3):
            print(f"Coordenada [latitud,longitud] {x+1}: {coordenadas[x]}")
        # Esta parte se desarrolla cuando el usuario escoge nuevamente la opción 2 para actualizar sus coordenadas
        latitud  = [coordenadas[0][0],coordenadas[1][0],coordenadas[2][0]]
        longitud = [coordenadas[0][1],coordenadas[1][1],coordenadas[2][1]]
        norte, sur = latitud.index(max(latitud)), latitud.index(min(latitud))
        oriente, occidente = longitud.index(max(longitud)), longitud.index(min(longitud))
        print(f"La coordenada {norte+1} es la que esta más al norte")
        print(f"La coordenada {occidente+1} es la que esta más al occidente")
        print("Presione 1, 2 o 3 para actualizar la respectiva coordenada")
        print("Presione 0 para regresar al menú")
        nueva_coordenada=int(input())
        if (nueva_coordenada == 0 or nueva_coordenada ==""):
            return
        else:
            if nueva_coordenada == 1 or nueva_coordenada == 2 or nueva_coordenada == 3:
                lat = float(input("Ingrese latitud: "))
                lon = float(input("Ingrese longitud: "))
                if (lat < 6.077 or lat > 6.284) and (lon < (-76.049) or lon > (-75.841)):
                    print("Error coordenada")
                    exit()
                else: # Se ejecuta el cambio de las nuevas coordenadas en la lista anidada
                    coordenadas[nueva_coordenada-1][0] = lat
                    coordenadas[nueva_coordenada-1][1] = lon
                    time.sleep(2) 
            else:
                print("Error actualización")    
                exit()

def funcion_reto2(): # Función que incluye todas las opciones del programa
    
    lista_menu = ["Cambiar contraseña","Ingresar coordenadas actuales","Ubicar zona wifi más cercana","Guardar archivo con ubicación cercana","Actualizar registros de zonas wifi desde archivo","Elegir opción de menú favorita","Cerrar sesión"]
    contador_intentos = 0 # Cuenta el número de intentos fallidos y se sale del menú al ser igual a 3
    opcion_menu = 1 # Se inicializa en 1 para que entre por primera vez al while  
    ref = "" # Se genera vacía para que tome el valor de la opción en el menú
    
    while (opcion_menu != 7 and contador_intentos <=3):  # Si el usuario supera la cantidad de intentos fallidos (3), el programa termina su ejecución
        opcion_menu = menuppal(lista_menu)
        if (opcion_menu > 7) or (opcion_menu <= 0): # Condicional que controla que las opciones del menú esten entre 1 y 7
            contador_intentos+=1
            print("Error")
            time.sleep(1)

        else:
            ref = lista_menu[opcion_menu-1] # Se hace uso de las referencias para que cuando la posición de una opción cambie de lugar en el menú, esta mantenga la información correspondiente

        if ref == "Cambiar contraseña":
            cambio_password(datos_user) # Función para cambiar la contraseña
        
        if ref == "Ingresar coordenadas actuales":
            coordenadas_actuales(coordenadas) # Función donde el usuario ingresa sus coordenadas actuales o actualiza dichas coordenadas luego de haberlas ingresado por primera vez

        if ref == "Ubicar zona wifi más cercana":
            print(f"Usted ha elegido la opción {opcion_menu}") 
            exit()

        if ref == "Guardar archivo con ubicación cercana":
            print(f"Usted ha elegido la opción {opcion_menu}") 
            exit()
        
        if ref == "Actualizar registros de zonas wifi desde archivo":
            print(f"Usted ha elegido la opción {opcion_menu}") 
            exit()

        if opcion_menu == 6:
            opcion_menu = menuopcion6(lista_menu) 
            os.system('cls')

        if (opcion_menu == 7): # Funciona cuando el usuario digita la opción "cerrar sesión", una vez que ha elegido opción favorita
            print("Hasta pronto")
            exit()
        
    if (opcion_menu == 7): # El programa permite al usuario salir del menú.
        print("Hasta pronto") # Funciona cuando el usuario digita la opción "cerrar sesión" por primera vez (sin elegir opción favorita)
        exit() 

def login(): # Programa completo, incluye todas las funciones
    
    captcha1 = 612 # Captcha1 = últimos 3 valores del usuario (612)
    captcha2 = 5*1+2-6 # Captcha2 = penúltimo número del usuario (1) - se compone de 4 operaciones matemáticas
    right_captcha = 613 # Captcha correcto = captcha 1 (612) + captcha 2 (1)

    print("Bienvenido al sistema de ubicación para zonas públicas WIFI")
    user=int(input("Ingrese el usuario: "))
    if user==right_user:
        password=int(input("Ingrese la contraseña: "))
    else:
        print("Error")
        exit()
        
    if password==right_password:
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

login() # Se ejecuta el programa completo