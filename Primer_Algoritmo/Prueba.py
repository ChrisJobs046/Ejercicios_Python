# Recuerden siempre tabular bien en python para que este lea el codigo correctamente.👍
#print("soy el mejor")

'''
Nombre = "Salvador"

Apellido = "Ramon"

Edad = 15
'''


# [Entrada]

# f"{}" esto sirve para concatenar.
# el signo de +, tambien sirve para concatenar.
# str() Sirve para convertir un valor numerico en un string.

'''
print(f"{Nombre} - {Apellido} {str(Edad)}")

Pregunta = input("¿Cual es tu nombre?:")

print("El nombre del usuario es: "+ Pregunta)
'''

# [Condiciones]
''' el tema de las condiciones las hice en el programa de signo del zodiaco😂'''

# Funciones
'''Recuerden que las funciones sirven practicamente para reutilizar codigo'''
'''return sirve para sacar informacion de una funcion, ya qie por defauk cualquier valor tratado dentro de la funcion se cada dentro
   de esta.
'''

'''var_altura = int(input("¿Cual es tu altura?: "))

def MostrarAltura(altura):
    
    resultado = ""

    if altura >= 180:
        resultado = ("Eres una persona alta")
    else:
        resultado = ("Eres bajito!!! por lo tanto tu novia no te ama😭😭😭 ")

    return resultado

print (MostrarAltura(var_altura))
'''
# Recordatorio
'''
Aqui puede que esten un poco confundidos con respecto a las tuplas y listas ya que son muy parecidas pero  ojo 
las tuplas se encierran asi() mientras que las listas [] y la diferencia es que los datos en las tuplas no se puede modificar 
mientras que en las listas si 😁
'''
# Tuplas

medidas = ("28", "15", "32", "40")

# Listas

Nombres = ["Ramon", "juan", "Lucas"]

print("el nombre es: " + Nombres[0])



