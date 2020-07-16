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

'''
return sirve para sacar informacion de una funcion, ya qie por defauk cualquier valor tratado dentro de la funcion se cada dentro
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

# Recordatorio para las <tuplas, Listas y Diccionarios>
'''
Aqui puede que esten un poco confundidos con respecto a las tuplas y listas ya que son muy parecidas pero  ojo 
las tuplas se encierran asi() mientras que las listas asi [] y la diferencia es que los datos en las tuplas no se modifican ni se 
pueden agregar nuevos datos mientras que en las listas si 😁, ahora si queremos poder eliminar un dato entonces lo ideal es hacer
un diccionario
'''
# Tuplas

'''medidas = ("28", "15", "32", "40")'''

# Listas
'''
Nombres = ["Ramon", "juan", "Lucas"]

# print("el nombre es: " + Nombres[0])

Nombres.append("nuevo dato")

print(Nombres)
'''

# Diccionarios
'''
Aqui podemos observar que los diccionarios son un poco diferentes ya que no se accede a una posicion solamente con el indice
si no que ahora podemos asignarle una palabra reservada y asignarle por consiguente un valor😱 y a diferencia de las tuplas y listas se 
puede eliminar un valor usando <<del>> 
'''
Mi_Diccionario = {'clave_1':1, 'clave_2':2, 'clave_3':3}


print(Mi_Diccionario['clave_2'])

del(Mi_Diccionario['clave_3'])

print(Mi_Diccionario)

Mi_Diccionario['clave_1'] = 'Nuevo valor'

print(Mi_Diccionario)
