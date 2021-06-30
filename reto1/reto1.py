# 1. Etapa de Login

print("Bienvenido al sistema de ubicación para zonas públicas WIFI")

right_user = 51612 # Usuario predefinido
right_password = 21615 # Contraseña predefinida

user=int(input("Ingrese el usuario: "))
if right_user==user:
    password=int(input("Ingrese la contraseña: "))
else:
    print("Error")
    exit()

captcha1 = 612 # Captcha1 = últimos 3 valores del usuario (612)
captcha2 = 5*1+2-6 # Captcha2 = penúltimo número del usuario (1) - se compone de 4 operaciones matemáticas
right_captcha = 613 # Captcha correcto = captcha 1 (612) + captcha 2 (1)
if right_password==password:
    captcha = int(input(f"Ingrese la suma del captcha: {captcha1}+{captcha2}= "))
    if right_captcha == captcha:
        print("Sesión iniciada")
    else:
        print("Error")
        exit()
else:
    print("Error")
    exit()