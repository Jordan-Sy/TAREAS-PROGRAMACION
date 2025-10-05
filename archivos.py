
# Escritura y lectura de un archivo en Python

# Paso 1: Escritura en el archivo
# Abrimos  un archivo llamado "my_notes.txt"
# El modo "w" indica escritura (write), sobrescribe el contenido si ya existe.
archivo = open("my_notes.txt","w")

# Escribimos al menos tres líneas de notas personales
archivo.write("Primera nota: Hoy estoy aprendiendo a trabajar con archivos en Python.\n")
archivo.write("Segunda nota: Los archivos de texto se pueden leer y escribir fácilmente.\n")
archivo.write("Tercera nota: Es importante cerrar los archivos después de usarlos.\n")

# Cerramos el archivo para guardar los cambios
archivo.close()

# Paso 2: Lectura del archivo
# Abrimos el archivo en modo lectura ("r")
archivo = open("my_notes.txt", "r")

# Usamos un bucle para leer línea por línea con readline()
print("Contenido del archivo:\n")
contenido = archivo.readline()  # Leemos la primera línea
while contenido:  # Mientras haya contenido
    print(contenido)
    contenido = archivo.readline()  # Leemos la siguiente línea

# Paso 3: Cierre del archivo
archivo.close()