#Se crea una lista llamada lista_compras
lista_compras = []
print("🛒 Lista de Compras 🛒")
#Agrega producto1 a la lista
producto1 = input(" Agrega el primer producto: ")
lista_compras.append(producto1)
#Agrega producto2 a la lista
producto2 = input("Agrega el segundo producto: ")
lista_compras.append(producto2)
#Agrega producto3 a la lista
producto3 = input("Agrega el tercer producto: ")
lista_compras.append(producto3)
#Se imprime la lista
print("\n📌 Tu lista de compras es:")
for producto in lista_compras:
    print(f"- {producto}")
#Se crea la lista
print("\n✅ ¡Lista creada con éxito!")
#https://www.webfx.com/tools/emoji-cheat-sheet/