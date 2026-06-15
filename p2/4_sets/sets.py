# """

 
#  Sets.- 
#   Es un tipo de datos para tener una coleccion de valores pero no tiene ni indice ni orden

#   Set es una colección desordenada, inmutable* y no indexada. No hay miembros duplicados.
# """
# print("\033c")
# set1 = {"Python", "SQL", "Estructurado"}
# print(set1)

# for i in set1:
#     print(i)

# set2 = {"Hola", True, 33, 3.1416}
# print(set2)

# set2_respaldo = set2.copy()
# set2.clear()

# set3 = {""}
# print(set3)

# set3.add("Hola")
# print(set3)

# set3.add(3)
# print(set3)

# set3.add("3")
# print(set3)

# set3.add(10.0)
# print(set3)

# set3.add(3)
# print(set3)

# set3.pop()
# set3.pop()
# print(set3)


# set3.clear()
# print(set3)

# set3.add("33")


# lista=[10,9,8.5,3,3.4,8.5,10]
# print(lista)
# conjunto = set(lista)
# lista=list(conjunto)
# print(lista)


# ejemplo Crear un programa que solicite los email de los alumnos de la UTD almacenar en una lista y posteriormente mostrar en pantalla los email sin duplicados

# Solucion 1
# emails_final = []
# opc = "S"

# while opc == "S":
#     email = input("Ingrese el 'email' del alumno de la UTD: ")
#     emails_final.append(email)
#     opc = input("Deseas agregar otro email?: ").upper().strip()

# conjunto = set(emails_final)
# email_final=list(conjunto)
# print(email_final)


lista_emails = []
set_email = {""}

opc = "S"

while opc == "S":
  lista_emails.append(input("Ingrese un email: ").lower().strip())
  set_email.add(input("Ingrese un email: ").lower().strip())
  ocp = input("Deseas agregar otro e mail?: ")

set_emails = set(lista_emails)
lista_emails = list(set_emails)
print(lista_emails)



#Solucion 2
lista_emails = []
set_email = {""}

resp = True

while resp:
  lista_emails.append(input("Ingrese un email: ").lower().strip())
  resp = input("Deseas agregar otro e mail? (SI/NO): ").upper().strip()
  if resp == "NO":
    resp = False
email_set = (set(lista_emails))
lista_emails = list(lista_emails)
print(lista_emails)


#EJERCICIOS

## Lista de numeros de telefono

emails = []
resp = True

while resp:
  emails.insert(0, str(input("Ingrese un email: ").upper().strip()))

  resp = input("Deseas agregar otro e mail? (S/N): ").upper().strip()
  if resp == "N":
    resp = False

set_emails = set(emails)
emails = list(set_emails)
print(lista_emails)

