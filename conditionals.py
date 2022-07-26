# Declaramos una variable
calificacion = input("Introduce tu calificación del AZ-900: ")

calificacion = int(calificacion)

# Preguntamos si la calificación es menor a 700
if calificacion < 700 :
    print("Ves, por no estudiar") # Si es menor a 700 muestra esto
elif calificacion > 1000 :
    print("Mientes! No puedes sacar más de mil puntos")
else : # Si no cumple con el if anterior, pasa a la siguiente línea
    print("Felicidades, pasa por tu certificado") # Se ejecuta si ningún if se cumple

# Verificador de mayoría de edad
edad = input("Introduce tu edad: ")
edad = int(edad)

if edad >= 18 and edad <= 100 :
    print("Bienvenid@ al Mamitas")
elif edad > 100 :
    print("Si vienes acompañado de tus abuelos, si te podemos fiar")
elif edad < 0 :
    print("Ni que fueras viejer@ del tiempo")
else :
    print("No puedes llevarte esos cigarros")