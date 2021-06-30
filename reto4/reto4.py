import os, time, math
os.system('cls')

# 4. El programa permite ubicar una zona wifi cercana, además de calcular la distancia entre la ubicación actual del usuario y la de la zona wifi más cercana. De igual forma, el programa da indicaciones específicas al usuario para que se dirija a la zona wifi

right_user = 51612 # Usuario predefinido
right_password = 21615 # Contraseña predefinida

# Listas

lista_menu = ["Cambiar contraseña","Ingresar coordenadas actuales","Ubicar zona wifi más cercana","Guardar archivo con ubicación cercana","Actualizar registros de zonas wifi desde archivo","Elegir opción de menú favorita","Cerrar sesión"] # Lista con las opciones del menú
datos_user = [right_user, right_password] # Se almacenan los datos del login en una lista
coordenadas=[[],[],[]] # Lista anidada vacía para registrar las coordenadas ingresadas por teclado
zonas_wifi = [[6.124,-75.946,1035],[6.125,-75.966,109],[6.135,-75.976,31],[6.144,-75.836,151]] # [lat], [lon], [promedio de usuarios]
# La lista anterior almacena las coordenadas de las zonas wifi que se encuentran cerca de la ubicación que usa el programa (Betulia, Antioquia)
zonas_wifi_distancia = [[],[],[],[]] # Lista anidada vacía para almacenar los datos recolectados en la función de ubicar zonas wifi más cercanas

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
    if (opcion_favorita >= 1 and opcion_favorita <=5): # # El usuario debe responder correctamente a 2 adivinanzas para elegir una opción favorita
        adivinanza1 = int(input("Para confirmar por favor responda:\nCuando te pones a contar por mí tienes que empezar. La respuesta es: "))
        if (adivinanza1 == 1):
            adivinanza2 = int(input("Para confirmar por favor responda:\nCuenta las manos o cuenta los pies y sabrás cual número es. La respuesta es: "))
            if (adivinanza2 == 2):
                os.system('cls')
                aux = lista_menu[0] # La variable aux permite hacer el intercambio de las opciones del menú
                lista_menu[0] = lista_menu[(opcion_favorita-1)]
                lista_menu[(opcion_favorita-1)] = aux
            else:
                print("Error")
                time.sleep(2)
                funciones_menu() # Ejecuta nuevamente todas las funcionalidades del menú si ocurre un error
        else:
            print("Error")
            time.sleep(2)
            funciones_menu()
    else:
        print("Error")
        exit()

def cambio_password(datos_user): # Función para cambiar la contraseña
    os.system('cls')
    passwordactual = int(input("Ingrese la contraseña actual: "))
    if datos_user[1] == passwordactual: # Se confirma la contraseña actual (21615)
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

def coordenadas_actuales(coordenadas): # Función donde el usuario ingresa sus coordenadas actuales o actualiza dichas coordenadas luego de haberlas ingresado por primera vez

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
                    coordenadas[x] = [lat,lon]  # Las coordenadas ingresadas por el usuario se almacenan en la lista coordenadas
                    time.sleep(2) 
    else:
        printcoordenadas(coordenadas)
        # Esta parte permite conocer cuál de las coordenadas almacenadas están más al norte, sur, oriente y occidente 
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
        else: # Esta parte se desarrolla cuando el usuario escoge nuevamente la opción para actualizar coordenadas
            if nueva_coordenada == 1 or nueva_coordenada == 2 or nueva_coordenada == 3:
                lat = float(input("Ingrese latitud: "))
                lon = float(input("Ingrese longitud: "))
                if (lat < (6.077) or lat > (6.284)): # Valida el rango de la latitud actualizada
                    print("Error coordenada")
                    exit()
                if (lon < (-76.049) or lon > (-75.841)): # Valida el rango de la longitud actualizada
                    print("Error coordenada")
                    exit()
                else:
                    coordenadas[nueva_coordenada-1][0] = lat # Actualiza la latitud ingresada en su respectiva coordenada
                    coordenadas[nueva_coordenada-1][1] = lon # Actualiza la longitud ingresada en su respectiva coordenada
                    time.sleep(2) 
            else:
                print("Error actualización")    
                exit()

            return norte, sur, oriente, occidente

    len(coordenadas[0]) == 1 # Cuando se hayan ingresado las coordenadas, esto actúa como un contador para hacer uso de la opción 3 del menú
    return coordenadas

def printcoordenadas(coordenadas): # Muestra al usuario las coordenadas registradas en el sistema
   os.system('cls') 
   for x in range(3): 
        print(f"Coordenada [latitud,longitud] {x+1} : {coordenadas[x]}") 

def distancia (opcion_ubicacion, coordenadas, zonas_wifi_distancia): # Calcula la distancia entre la ubicación actual del usuario y la zona wifi más cercana a su ubicación

    radio = 6371 # radio de la tierra en km
    lat2 = coordenadas[opcion_ubicacion-1][0]
    lon2 = coordenadas[opcion_ubicacion-1][1]
    for i in range(4):
        lat1 = zonas_wifi[i][0]
        lon1 = zonas_wifi[i][1]
        # Cálculo de deltas:
        distancia_lat = math.radians((lat2-lat1))
        distancia_lon = math.radians((lon2-lon1))
        # Cálculo de variables para la fórmula
        a = math.sin(distancia_lat/2) * math.sin(distancia_lat/2) + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(distancia_lon/2) * math.sin(distancia_lon/2)
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
        # Cálculo de la distancia
        d = (radio * c)*1000 # Los km del radio se pasan a metros / 1km = 1000m
        zonas_wifi_distancia[i] = [lat1,lon1,round(d),zonas_wifi[i][2],i]

def distancias_ordenadas(zonas_wifi_distancia): # Calcula cuál es la zona wifi más cercana a la ubicación del usuario
    for x in range(4):
        for y in range(4): # Haciendo uso de la matriz zonas_wifi_distancia, el programa organiza por cercanía cada zona wifi, dependiendo de las coordenadas que el usuario haya ingresado por teclado y que se almacenan en el sistema
            if zonas_wifi_distancia[x][2]<zonas_wifi_distancia[y][2]:
                aux1 = zonas_wifi_distancia[x]
                zonas_wifi_distancia[x]=zonas_wifi_distancia[y]
                zonas_wifi_distancia[y]=aux1
    print()
    print("Zonas wifi cercanas con menos usuarios") # Da información al usuario sobre las zonas wifi cercanas
    for x in range(2):
        print(f"La zona wifi {x+1}: ubicada en [{zonas_wifi_distancia[x][0]},{zonas_wifi_distancia[x][1]}] a {zonas_wifi_distancia[x][2]} metros, tiene en promedio {zonas_wifi_distancia[x][3]} usuarios")

def ubicar_wifi(coordenadas): # Permite ubicar una zona wifi cercana y da indicaciones precisas para llegar a la zona wifi seleccionada
    if len(coordenadas[0]) == 0: # Si el usuario no ha registrado sus coordenadas, el programa no permite ingresar a esta opción del menú y finaliza la ejecución
        print("Error sin registro de coordenadas")
        exit()
    else:
        os.system('cls')
        printcoordenadas(coordenadas) # Muestra las coordenadas registradas en el sistema para que el usuario elija su ubicación actual
        print("Por favor elija su ubicación actual (1,2 ó 3) para calcular la distancia a los puntos de conexión")
        opcion_ubicacion = int(input())
        if opcion_ubicacion not in (1,2,3):
            print("Error ubicación")
            exit()
        else:
            os.system('cls')
            print(f"Coordenadas [latitud,longitud] {opcion_ubicacion}: {coordenadas[opcion_ubicacion-1]}")
            distancia(opcion_ubicacion, coordenadas, zonas_wifi_distancia) # Hace uso de la ecuación matemática para calcular la distancia entre los puntos
            distancias_ordenadas(zonas_wifi_distancia) # Determina las zonas wifi más cercanas según lo anterior
            print("Elija 1 o 2 para recibir indicaciones de llegada") # El usuario selecciona la zona wifi a la que quiere dirigirse
            opcion_llegada = int(input())
            if opcion_llegada not in (1,2):
                print("Error zona wifi")
                exit()
            else: # El programa da indicaciones al usuario para llegar a la zona wifi seleccionada
                print()
                velocidad_bus = 16.67 # mts/seg
                velocidad_auto = 20.83 # mts/seg
                print("Para llegar a la zona wifi dirigirse primero al sur y luego hacia el occidente")
                tiempo_bus = ((zonas_wifi_distancia[opcion_llegada-1][2])/velocidad_bus)/60
                tiempo_auto = ((zonas_wifi_distancia[opcion_llegada-1][2])/velocidad_auto)/60
                print(f"Tiempo promedio en bus: {round(tiempo_bus)} minutos")
                print(f"Tiempo promedio en auto: {round(tiempo_auto)} minutos")

            backtomenu = int(input("Presione 0 para salir: "))
            if (backtomenu == 0):
                return
            else:
                exit()  

def funciones_menu(): # Función que incluye todas las opciones del programa
    
    contador_intentos = 0 # Cuenta el número de intentos fallidos y se sale del menú al ser igual a 3
    opcion_menu = 1 # Se inicializa en 1 para que entre por primera vez al while  
    ref = "" # Se genera vacía para que tome el valor de la opción en el menú
    
    while (opcion_menu != 7 and contador_intentos <=3): # Si el usuario supera la cantidad de intentos fallidos (3), el programa termina su ejecución
        opcion_menu = menuppal(lista_menu)
        if (opcion_menu > 7) or (opcion_menu <= 0): # Condicional que controla que las opciones del menú esten entre 1 y 7
            contador_intentos+=1
            print("Error")
            time.sleep(1)

        else:
            ref = lista_menu[opcion_menu-1]  # Se hace uso de las referencias para que cuando la posición de una opción cambie de lugar en el menú, esta mantenga la información correspondiente

        if ref == "Cambiar contraseña":
            cambio_password(datos_user) # Función para cambiar la contraseña
        
        if ref == "Ingresar coordenadas actuales":
            coordenadas_actuales(coordenadas) # Función donde el usuario ingresa sus coordenadas actuales o actualiza dichas coordenadas luego de haberlas ingresado por primera vez

        if ref == "Ubicar zona wifi más cercana":
            ubicar_wifi(coordenadas)  # Permite ubicar una zona wifi cercana y da indicaciones precisas para llegar a la zona wifi seleccionada

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

def programa(): # Programa completo, incluye todas las funciones
    
    captcha1 = 612 # Captcha1 = últimos 3 valores del usuario (612)
    captcha2 = 5*1+2-6  # Captcha2 = penúltimo número del usuario (1) - se compone de 4 operaciones matemáticas
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
            funciones_menu() # Ejecuta el menú principal al iniciar sesión
        else:
            print("Error")
            exit()
    else:
        print("Error")
        exit()

programa() # Se ejecuta el programa completo