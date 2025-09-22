Edades = {
#La coma es como un "ENTER" para agregar otro campo
    "Brayan": 25,
    "Luis": 30,
    "José": 22
}
#Añadimos otro integrante
print("Edad de Luis:", Edades["Luis"])    
Edades["Brayan"] = 28
print("\nDespués de añadir a Brayan:")
print(Edades)                               
#Imprimir la actualizacion de la edad
Edades["Luis"] = 26
print("\nDespués de actualizar la edad de Luis:")
print(Edades)                              
#Eliminamos a Jose
del Edades["José"]
print("\nDespués de eliminar a José:")
print(Edades)                               
#Listoo
print("\nRecorriendo el diccionario:")
for Nombre, Edad in Edades.items():         
    print(f"{Nombre} tiene {Edad} años")