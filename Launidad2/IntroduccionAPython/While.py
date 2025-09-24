#Usamos la primera función para mostrar el menu
def mostrar_menu() -> None:
    print("\n===== MENÚ PRINCIPAL =====")
    print("1) Saludar")
    print("2) Calcular la suma de dos números")
    print("3) Mostrar la tabla de multiplicar del 5")
    print("0) Salir")
    
#La segunda función es para solicitar el nombre y saludar
def opcion_saludar() -> None:
    nombre = input("¿Cómo te llamas? ").strip()
    print(f"¡Hola, {nombre}! Bienvenido/a.")

#Tercera funcion solicita dos números y realiza la suma
def opcion_suma() -> None:
    try:
        a = float(input("Primer número: "))
        b = float(input("Segundo número: "))
        print(f"La suma es: {a + b}")
    except ValueError:
        print(" Debes introducir valores numéricos.")

#Cuarta función se muestra la tabla
def opcion_tabla() -> None:
    numero = 5
    print(f"\nTabla del {numero}:")
    for i in range(1, 11):
        print(f"{numero} × {i} = {numero * i}")


# ---------- Bucle principal ----------
#Evalúa la condición como verdadera
continuar = True
              
while continuar:
    mostrar_menu()
    #Usamos el input para elegir una opción             
    eleccion = input("Elige una opción: ").strip()
#Usamos las condiciones if y elif para que cada una cumpla su condición especifica
    if eleccion == "1":
        opcion_saludar()
    elif eleccion == "2":
        opcion_suma()
    elif eleccion == "3":
        opcion_tabla()
    elif eleccion == "0":
        print("\n ¡Hasta luego!")
        continuar = False#Evalúa la condición como falsa
    else:
        print(" Opción no válida, intenta de nuevo.")

print("Programa terminado.")