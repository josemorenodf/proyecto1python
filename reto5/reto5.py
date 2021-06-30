import os, time, math
os.system('cls')

# 5. El programa le muestra al usuario los datos que ha almacenado en el sistema. Igualmente, le permite exportar un archivo .csv con esa información

global right_password 
right_user = 51612 # Usuario predefinido
right_password = 21615 # Contraseña predefinida
bandera = 0 # Esta variable permite al programa saber si el usuario ya ha ingresado sus coordenadas al sistema, ya que esto es necesario para ingresar a varias opciones del menú

# Listas

lista_menu = ["Cambiar contraseña","Ingresar coordenadas actuales","Ubicar zona wifi más cercana","Guardar archivo con ubicación cercana","Actualizar registros de zonas wifi desde archivo","Elegir opción de menú favorita","Cerrar sesión"] # Lista con las opciones del menú
coordenadas = [[],[],[]] # Lista anidada vacía para registrar las coordenadas ingresadas por teclado
zonas_wifi = [[6.124,-75.946,1035],[6.125,-75.966,109],[6.135,-75.976,31],[6.144,-75.836,151]] # [lat], [lon], [promedio de usuarios]
# La lista anterior almacena las coordenadas de las zonas wifi que se encuentran cerca de la ubicación que usa el programa
zonas_wifi_distancia = [[],[],[],[]] # Lista anidada vacía para almacenar los datos recolectados en la función de ubicar zonas wifi más cercanas
informacion = {} # Este diccionario almacena los diferentes datos que el usuario ingresa durante la ejecución del programa
opcubic = None # La opción de ubicación se registra varias veces durante la ejecución del programa

# Bloque de funciones

def actualizar_registros_zonas_wifi(informacion): # Muestra a usuario los datos que se han almacenado en el sistema
    os.system('cls')
    print("Diccionario Informacion")
    print("Actualizar registros de zonas wifi desde archivo")
    print()
    print(informacion) # Muestra el diccionario con todos los datos almacenados
    print()
    print("Datos de coordenadas para zonas wifi actualizados, presione 0 para regresar al menú principal")
    
    confirmacion = int(input()) 

    if confirmacion == 0:
        return
    else:
        exit()

def guardar_archivo_ubicacion_cercana(informacion,opcubic): # Esta función permite al usuario descargar un archivo con la información que se encuentra en el sistema
    os.system('cls')
    print("Guardar archivo con ubicacion cercana") 
    if len(coordenadas[0]) == 0: # Verifica que el usuario ya haya ingresado sus coordenadas al sistema, de otra forma no podrá ingresar a esta opción del menú
        print("Error de alistamiento")
        exit()
    else:
        if opcubic not in (1,2,3):
            print("Error de alistamiento")
            exit()
        else:
            print("Diccionario Informacion")
            print()
            print(informacion) # Muestra el diccionario con todos los datos almacenados
            print()
            print("¿Está de acuerdo con la información a exportar? Presione 1 para confirmar, 0 para regresar al menú principal")
            
            confirmacion = int(input())
            if confirmacion == 0:
               return     
            else:
                 if confirmacion == 1:
                    print("Exportando archivo")
                    exit()

def printcoordenadas(coordenadas): # Muestra al usuario las coordenadas registradas en el sistema
   os.system('cls') 
   for x in range(3):
        print(f"Coordenada [latitud,longitud] {x+1} : {coordenadas[x]}") 

def distancia(opcubic,coordenadas,zonas_wifi,zonas_wifi_distancia): # Calcula la distancia entre la ubicación actual del usuario y la zona wifi más cercana a su ubicación

    radio = 6371 # radio de la tierra en km
    lat2 = coordenadas[opcubic-1][0]
    lon2 = coordenadas[opcubic-1][1]
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

def distancias_ordenadas(zonas_wifi_distancia, zonas_wifi): # Calcula cuál es la zona wifi más cercana a la ubicación del usuario
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

def ubicar_wifi(coordenadas,opcubic,zonas_wifi,zonas_wifi_distancia,informacion): # Permite ubicar una zona wifi cercana y da indicaciones precisas para llegar a la zona wifi seleccionada
    if len(coordenadas[0]) == 0: # Si el usuario no ha registrado sus coordenadas, el programa no permite ingresar a esta opción del menú y finaliza la ejecución
        print("Error sin registro de coordenadas")
        exit()
    else:
        os.system('cls')
        printcoordenadas(coordenadas) # Muestra las coordenadas registradas en el sistema para que el usuario elija su ubicación actual
        print("Por favor elija su ubicación actual (1,2 ó 3) para calcular la distancia a los puntos de conexión")
        opcubic = int(input())
        if opcubic not in (1,2,3):
            print("Error ubicación")
            exit()
        else:
            os.system('cls')
            print(f"Coordenadas [latitud,longitud] {opcubic}: {coordenadas[opcubic-1]}")
            distancia(opcubic,coordenadas,zonas_wifi,zonas_wifi_distancia) # Hace uso de la ecuación matemática para calcular la distancia entre los puntos
            distancias_ordenadas(zonas_wifi_distancia, zonas_wifi) # Determina las zonas wifi más cercanas según lo anterior
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
                tiempo_bus = (zonas_wifi_distancia[opcion_llegada-1][2])/velocidad_bus
                tiempo_auto = (zonas_wifi_distancia[opcion_llegada-1][2])/velocidad_auto
                print(f"Tiempo promedio en bus: {round(tiempo_bus)} segundos")
                print(f"Tiempo promedio en auto: {round(tiempo_auto)} segundos")
                informacion = {"actual":coordenadas[opcubic-1],
                               "zonawifi1":[zonas_wifi_distancia[opcion_llegada-1][0],zonas_wifi_distancia[opcion_llegada-1][1],zonas_wifi_distancia[opcion_llegada-1][3]],
                               "recorrido":[zonas_wifi_distancia[opcion_llegada-1][2],"bus",tiempo_bus]}

            backtomenu = int(input("Presione 0 para salir: "))
            if (backtomenu == 0):
                return informacion,opcubic
            else:
                exit()

def definicion_coordenadas(coordenadas): # Esta parte permite conocer cuál de las coordenadas almacenadas están más al norte, sur, oriente y occidente 
        latitud  = [coordenadas[0][0],coordenadas[1][0],coordenadas[2][0]]
        longitud = [coordenadas[0][1],coordenadas[1][1],coordenadas[2][1]]
        norte, sur = latitud.index(max(latitud)), latitud.index(min(latitud))
        oriente, occidente = longitud.index(max(longitud)), longitud.index(min(longitud))
        return norte, sur, oriente, occidente

def cambio_password(right_password): # Función para cambiar la contraseña
    os.system('cls')
    passwordactual = int(input("Ingrese la contraseña actual: "))
    if right_password == passwordactual: # Se confirma la contraseña actual (21615)
        passwordnueva = int(input("Ingrese la nueva contraseña: "))
        if passwordnueva == right_password: # Arroja un error si la contraseña nueva es igual a la actual (21615)
            print("La nueva contraseña no puede ser igual a la contraseña actual")
            time.sleep(2)
        else:
            right_password = passwordnueva # Si la contraseña es diferente a 21615, entonces esta se actualiza
            return right_password
    else:
        print("Error")    
        exit()

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

def coordenadas_actuales(coordenadas,bandera): # Función donde el usuario ingresa sus coordenadas actuales o actualiza dichas coordenadas luego de haberlas ingresado por primera vez
    os.system('cls')
    if bandera == 0: # Se usa para saber si el usuario ya ingresó los datos de ubicación
        print("Ingrese las coordenadas de los tres sitios que más frecuenta (trabajo, casa, parque): ")
        for x in range(3):
            lat = float(input(f"Ingrese latitud {x+1}: "))
            if (lat != 0) or (lat !=""):
                if (lat < 6.077 or lat > 6.284): # Rango de latitud predeterminado (Betulia, Antioquia)
                    print("Error coordenada")
                    exit()
                else:
                    lon = float(input(f"Ingrese longitud {x+1}: "))
                    if (lat != 0) or (lat !=""):
                        if lon < (-76.049) or lon > (-75.841): # Rango de longitud predeterminado (Betulia, Antioquia)ingresada
                            print("Error coordenada")
                            exit()
                        else:    
                            coordenadas[x] = [lat,lon] # Envía los datos a la lista anidada de coordenadas, que antes estaba vacía
                            time.sleep(2) 
                    else:
                        print("Error")
                        exit()
            else:
                print("Error")
                exit()
    else:
        printcoordenadas(coordenadas)
         # Esta parte permite conocer cuál de las coordenadas almacenadas están más al norte, sur, oriente y occidente 
        norte,sur,oriente,occidente = definicion_coordenadas(coordenadas)
        print(f"La coordenada {norte+1} es la que esta más al norte")
        print(f"La coordenada {occidente+1} es la que esta más al occidente")
        print("Presione 1,2 o 3 para actualizar la respectiva coordenada")
        print("Presione 0 para regresar al menú")

        opcion_actualizacion=int(input()) 
        if opcion_actualizacion not in (0,1,2,3):
            print("Error actualización")
            exit()
        else: 
            if opcion_actualizacion == 0:
                return # Esta parte se desarrolla cuando el usuario escoge nuevamente la opción para actualizar coordenadas
            else:
                lat = float(input(f"Ingrese latitud {opcion_actualizacion}: "))
                if (lat != 0) or (lat !=""):  
                    if (lat < 6.077 or lat > 6.284): # Valida el rango de la latitud actualizada
                        print("Error coordenada")
                        exit()
                    else:
                        lon = float(input("Ingrese longitud: "))
                        if (lat != 0) or (lat !=""):
                            if lon < (-76.049) or lon > (-75.841): # Valida el rango de la longitud actualizada
                                print("Error coordenada")
                                exit()
                            else:
                                coordenadas[opcion_actualizacion-1] = [lat,lon] # Actualiza la coordenada ingresada, en su respectiva posición
                                time.sleep(2)
                        else:
                            print("Error")
                            exit()
                else:
                    print("Error")
                    exit()

    bandera = 1 # Cuando se hayan ingresado las coordenadas, esto actúa como un contador para hacer uso de la opción 3, 4 y 5 del menú
    return bandera

def menuopcion6(lista_menu): # Selección de una opción favorita
    opcion_favorita = int(input("Seleccione opción favorita: "))
    if (opcion_favorita >= 1 and opcion_favorita <=5): # El usuario debe responder correctamente a 2 adivinanzas para elegir una opción favorita
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
        else:
            print("Error")
    else:
        print("Error")
        exit()

def funciones_menu(right_password,coordenadas,bandera,informacion,opcubic): # Función que incluye todas las opciones del programa
    
    contador_intentos = 0 # Cuenta el número de intentos fallidos y se sale del menú al ser igual a 3
    ref = None # Se genera vacía para que tome el valor de la opción en el menú
    
    while contador_intentos < 3: # Si el usuario supera la cantidad de intentos fallidos (3), el programa termina su ejecución
        opcion_menu = menuppal(lista_menu)
        if (opcion_menu > 7) or (opcion_menu <= 0): # Condicional que controla que las opciones del menú esten entre 1 y 7
            contador_intentos+=1
            print("Error")
            time.sleep(1)

        else:
            ref = lista_menu[opcion_menu-1] # Se hace uso de las referencias para que cuando la posición de una opción cambie de lugar en el menú, esta mantenga la información correspondiente

        if ref == "Cambiar contraseña":
            right_password = cambio_password(right_password) # Función para cambiar la contraseña
        
        if ref == "Ingresar coordenadas actuales":
            coordenadas_actuales(coordenadas,bandera) # Función donde el usuario ingresa sus coordenadas actuales o actualiza dichas coordenadas luego de haberlas ingresado por primera vez

        if ref == "Ubicar zona wifi más cercana":
            informacion,opcubic = ubicar_wifi(coordenadas,opcubic,zonas_wifi,zonas_wifi_distancia,informacion)  # Permite ubicar una zona wifi cercana y da indicaciones precisas para llegar a la zona wifi seleccionada

        if ref == "Guardar archivo con ubicación cercana":
            guardar_archivo_ubicacion_cercana(informacion,opcubic) # Permite al usuario descargar un archivo con la información que se encuentra en el sistema
        
        if ref == "Actualizar registros de zonas wifi desde archivo":
            actualizar_registros_zonas_wifi(informacion) # Muestra a usuario los datos que se han almacenado en el sistema

        if opcion_menu == 6:
            menuopcion6(lista_menu) 
            os.system('cls')

        if (opcion_menu == 7): # Funciona cuando el usuario digita la opción salir, una vez que ha elegido opción favorita
            print("Hasta pronto")
            exit()

def programa(right_password,coordenadas,bandera,informacion,opcubic): # Programa completo, incluye todas las funciones

    print("Bienvenido al sistema de ubicación para zonas públicas WIFI")
    user=int(input("Ingrese el usuario: "))
    if right_user != user:
        print("Error")
        exit()
    else:
        password=int(input("Ingrese la contraseña: "))
        if right_password == password:
            captcha1 = 612 # Captcha1 = últimos 3 valores del usuario (612)
            captcha2 = 5*1+2-6 # Captcha2 = penúltimo número del usuario (1) - se compone de 4 operaciones matemáticas
            right_captcha = captcha1 + captcha2 # Captcha correcto = captcha 1 (612) + captcha 2 (1)
            captcha = int(input(f"Ingrese la suma del captcha: {captcha1}+{captcha2}= "))
            if captcha == right_captcha:
                print("Sesión iniciada")
                time.sleep(2)
                funciones_menu(right_password,coordenadas,bandera,informacion,opcubic) # Ejecuta el menú principal al iniciar sesión
            else:
                print("Error")
                exit()
        else:
            print("Error")
            exit()

programa(right_password,coordenadas,bandera,informacion,opcubic) # # Se ejecuta el programa completo