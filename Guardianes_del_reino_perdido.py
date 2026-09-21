
print("========================================")
print("   GUARDIANES DEL REINO PERDIDO")
print("========================================")
print()
print("¡Bienvenido, Guardián!")
print("El reino necesita tu ayuda.")
print("Prepárate para vivir una gran aventura.")
print()

input("Presiona ENTER para continuar...")

while True:
    print("\n========== MENÚ PRINCIPAL ==========")
    print("1. Nueva partida")
    print("2. Continuar")
    print("3. Créditos")
    print("4. Opciones")
    print("5. Salir")
    print("====================================")
    opcion = input("Selecciona una opción: ")
    if opcion == "1":
        print("\nHas seleccionado NUEVA PARTIDA.")
        print("¡Comencemos la aventura!")

    elif opcion == "2":
        print("\nHas seleccionado CONTINUAR.")
        print("Buscando partida guardada...")

    elif opcion == "3":
        print("\n========== CRÉDITOS ==========")
        print("Juego: Guardianes del Reino Perdido")
        print("Desarrollado por: Astrid Araceli Giron Luna")

    elif opcion == "4":
        print("\n========== OPCIONES ==========")
        print("1. Sonido")
        print("2. Gráficos")
        print("3. Controles")

    elif opcion == "5":
        print("\nGracias por jugar, Guardián.")
        print("¡Hasta la próxima aventura!")
        break
    else:
        print("\nOpción no válida. Intenta nuevamente.")


        