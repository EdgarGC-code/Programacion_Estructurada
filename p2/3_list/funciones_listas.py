"""  
 List (Array)
 son colleciones o conjunto de datos/valores bajo un mismo nombre, para acceder a los valores se hace con un indice numerico 

 Nota: sus valores si son modificables

 La lista es una colección ordenada y modificable. Permite miembros duplicados.

"""

print("\033c")
#Funciones más comunes en las listas
paises = ["Mexico", "canada", "EUA", "Mexico", "Brasil"]

numeros = [23, 45, 8, 24]

varios = ["hola", 3.1416, 33, True]

vacia=[]

#Imprimir el contenido de una lista
print(paises)
print(numeros)
print(varios)
print(vacia)
print(paises[1])

#Recorrer la lista 

#1er forma 
for i in paises:
    print(i)

# #2do forma 
for i in range(0,len(paises)):
    print(paises[i])


#ordenar elementos de una lista
paises = ["Mexico", "canada", "EUA", "Mexico", "Brasil"]
print(paises)
paises.sort()
print(paises)

#dar la vuelta a una lista
paises.reverse()
print(paises)



#Agregar, insertar, Añadir un elemento a una lista
#1er forma 
paises.append("Hondura")
print(paises)
#2da forma
paises.insert(1,"colombia")
print(paises)

paises.insert(8,"Australia")
print(paises)


#Eliminar, borrar, suprimir, un elemento de una lista
#1er forma
paises.pop(4)
print(paises)

#2da forma 
paises.remove("Mexico")
print(paises)

#Buscar un elemento dentro de la lista
if "Brasil" in paises:
    print(f"La respuesta es True")
else:
    print("La respuesta es False")
    

#Contar el numeros de veces que aparece un elemento dentro de una lista
numeros = [23, 45, 8, 24, 100, 0, -1, -10, 23, 24, 8, 23, 50]
print(numeros)
numeros.sort()
print(numeros)
num=int(input("Dme un numero: "))
cuantos=numeros.count(num)
print(f"El numero de veces que aparece el {num} es {cuantos}")

#Conocer la posicion o indice en el que se encuentra un elemento de la lista
posicion = numeros.index(100)
print(f"la posicion del numero es: {posicion}")


#Unir el contenido de una lista dentro de otra lista
numeros = [23, 45, 8, 24, 100, 0, -1, -10, 23, 24, 8, 23, 50]
print(numeros)
numeros2=[500,1000]
print(numeros2)
numeros.extend(numeros2)
print(numeros)

#Crear a partir de las listas de numeros 1 y 2 un resultante y mostar el contenid ordenado descendentemente
numeros.sort()
numeros.reverse()
print(numeros)



