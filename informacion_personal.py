

informacion_personal = {"Nombre": "Jordan", "Edad": 24, "Ciudad": "Otavalo", }
print("\ninformacion personal original:",  informacion_personal) #INFORMACION ORIGINAL

# MODIFICAR EL VALOR CIUDAD
del informacion_personal ["Ciudad"] # ELIMINO LA CLAVE SINO SOLO LA MODIFICO CON LA LINEA DE ABAJO
informacion_personal ["Ciudad"] = "Quito"
print("informacion personal :", informacion_personal)

# AGREGAR UN NUEVO VALOR
informacion_personal["Profesion"] = "Mecanico"
print("informacion personal :", informacion_personal)

# VERIFICAR SI HAY UN NUMERO DE TELEFONO Y AGREGAR UNO
if "Telefono" in informacion_personal:
    print("Telefono esta en el conjunto")
else:
    print("Telefono no esta en el conjunto")
    # print("añada un numero de telefono")
    informacion_personal["Telefono"] = "0987654321"
    #informacion_personal["Telefono"] = input ()
print("informacion personal :", informacion_personal)

# ELIMINA LA CLAVE EDAD
del informacion_personal["Edad"]
print("informacion personal final :", informacion_personal)