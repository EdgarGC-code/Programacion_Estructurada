trabajadores=[]
sueldo_total = (0)
while True:
    nombre = input("Nombre: ")
    horas = int(input("Horas Trabajadas: "))
    sueldo_hora = float(input("sueldo pagado por hora:"))

    sueldo_base = sueldo_hora * horas

    #aumentos
    if horas >= 10 and horas < 15:
        aumento = sueldo_base * 0.20  #20%
    elif horas >=15 and horas <20:
        aumento = sueldo_base * 0.30 
    elif horas >=20 and horas <25:
        aumento = sueldo_base * 0.15
    elif horas >25:
        aumento = sueldo_base * 0.08
    else:
        aumento = 0

    sueldo_neto = sueldo_base + aumento
    
    trabajador = {f"Nombre": nombre,
                   "horas": horas,
                    "sueldo por hora": sueldo_hora}
    trabajadores.append(trabajador)
    sueldo_total += sueldo_neto

    print("Trabajador agregado...")

    pregunta = input("deseas agregar otro trabajador? (s/n): ")
    if pregunta != "s":
        break

print("----------------------")
print(f"Total de trabajadores: ", len(trabajadores))
for trabajador in trabajadores:
    for clave, valor in trabajador.items():
        print(f"{clave}: {valor}")
    print("-"*25)
print(f"Sueldo total pagado: ", sueldo_total)
