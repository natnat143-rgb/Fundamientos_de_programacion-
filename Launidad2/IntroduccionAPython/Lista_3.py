#Crear una lista vacia con su nombre y van a agregar 5 elemntos con input:
#(Nombre, Preparatoria, Lugar de residencia, Edad, Carrera)

#Se crea una lista llamada lista_datos
lista_datos = []
print(" Lista de Datos ")

#Colocar tu Nombre
Dato = input(" Nombre: ")
lista_datos.append(Dato)

#Agrega nombre de la prepa a la lista
Dato = input("Preparatoria: ")
lista_datos.append(Dato)

#Agrega tu lugar de residencia
Dato = input("Lugar de residencia: ")
lista_datos.append(Dato)

#Agrega tu edad
Dato = input("Edad: ")
lista_datos.append(Dato)

#Agrega tu carrera
Dato = input("Carrera: ")
lista_datos.append(Dato)

#Se imprime la lista de datos
print("\n📌 Tus datos son:")
for Dato in lista_datos:
    print(f"- {Dato}")
#Se crea la lista
print("\n✅ ¡Lista creada con éxito!")
#https://www.webfx.com/tools/emoji-cheat-sheet/