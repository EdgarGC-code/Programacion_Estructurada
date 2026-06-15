from paquete1 import modulos,modulo_paquete
modulos.borrarPantalla()

nom="Juan"
ape="Polainas"


nombre,apellidos=modulos.funcion4(nom,ape)
edad=modulo_paquete.solicitar_edad
print(f"Nombre:{nombre}\n Apellidos{apellidos}\n Edad: {edad}")

modulos.funcion4()
