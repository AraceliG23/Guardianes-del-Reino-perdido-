"""
GUARDIANES DEL REINO PERDIDO
Desarrolladora: Astrid Araceli Giron Luna

ENTRADA: Opciones y decisiones del jugador.
PROCESO: Seleccionar personaje, superar niveles y recuperar cristales.
SALIDA: Victoria, derrota y recompensas.
"""

import time

PERSONAJES = {
    "1": ["AlÃ©n", "Guerrero"],
    "2": ["Luna", "Maga"],
    "3": ["Call", "Explorador"],
    "4": ["Luz", "Sanadora"]
}

CRISTALES = ["Verde", "Azul", "Morado", "Naranja", "Rojo"]
vidas = 3
cristales = []
jugador = ""
clase = ""
inicio = 0
TIEMPO_LIMITE = 600


def elegir(mensaje, opciones):
    while True:
        respuesta = input(mensaje).strip()
        if respuesta in opciones:
            return respuesta
        print("OpciÃ³n no vÃ¡lida. Intenta nuevamente.")


def estado():
    restante = TIEMPO_LIMITE - int(time.time() - inicio)
    print("\nVidas:", vidas)
    print("Cristales:", len(cristales), "/ 5")
    print("Tiempo restante:", max(0, restante), "segundos")
    return vidas > 0 and restante > 0


def perder_vida():
    global vidas
    vidas -= 1
    print("Â¡Perdiste una vida! Vidas restantes:", vidas)


def conseguir(nombre):
    if nombre not in cristales:
        cristales.append(nombre)
        print("Â¡Conseguiste el cristal", nombre + "!")


def combate(enemigo, energia):
    global vidas
    print("\nÂ¡ApareciÃ³", enemigo + "!")

    while energia > 0 and vidas > 0:
        print("\nEnergÃ­a del enemigo:", energia)
        print("1. Atacar")
        print("2. Defender")
        print("3. Habilidad especial")
        opcion = elegir("Â¿QuÃ© haces? ", ["1", "2", "3"])

        if opcion == "1":
            energia -= 1
            print("Â¡Atacaste al enemigo!")
            perder_vida()
        elif opcion == "2":
            print("Te defendiste y evitaste el daÃ±o.")
        else:
            energia -= 2
            print("Â¡", jugador, "usÃ³ su habilidad especial!")

        if energia > 0 and opcion != "2" and vidas > 0:
            print(enemigo, "contraataca.")
    if energia <= 0:
        print("Â¡Derrotaste a", enemigo + "!")


def seleccionar_personaje():
    global jugador, clase
    print("\n===== SELECCIÃ“N DE PERSONAJES =====")
    for numero, datos in PERSONAJES.items():
        print(numero + ".", datos[0], "-", datos[1])
    opcion = elegir("Selecciona tu personaje (1-4): ",
                    ["1", "2", "3", "4"])
    jugador, clase = PERSONAJES[opcion]
    print("\nElegiste a", jugador, "- Clase:", clase)
    print("Â¡PrepÃ¡rate para salvar el reino!")


def nivel_bosque():
    print("\n===== NIVEL 1: BOSQUE ENCANTADO =====")
    print("1. Camino de Ã¡rboles")
    print("2. Camino de flores")
    print("3. Camino oscuro")
    opcion = elegir("Elige un camino: ", ["1", "2", "3"])
    if opcion == "3":
        combate("Monstruo del bosque", 2)
    else:
        print("Encontraste el camino correcto.")
    if vidas > 0:
        conseguir("Verde")


def nivel_cueva():
    print("\n===== NIVEL 2: CUEVA DE CRISTAL =====")
    print("Resuelve el acertijo: Tengo agujas y no sÃ© coser. Â¿QuÃ© soy?")
    print("1. Ãrbol   2. Reloj   3. Espada")
    respuesta = elegir("Tu respuesta: ", ["1", "2", "3"])
    if respuesta == "2":
        print("Â¡Respuesta correcta! Se abre la cueva.")
    else:
        print("Respuesta incorrecta. La respuesta era reloj.")
        perder_vida()
    if vidas > 0:
        conseguir("Azul")


def nivel_castillo():
    print("\n===== NIVEL 3: CASTILLO ABANDONADO =====")
    print("1. Puerta dorada")
    print("2. Puerta de piedra")
    print("3. Puerta de madera")
    opcion = elegir("Â¿QuÃ© puerta eliges? ", ["1", "2", "3"])
    if opcion == "2":
        print("Â¡Encontraste la llave secreta!")
    else:
        print("Â¡CaÃ­ste en una trampa!")
        perder_vida()
    if vidas > 0:
        conseguir("Morado")


def nivel_volcan():
    print("\n===== NIVEL 4: VOLCÃN DE FUEGO =====")
    print("1. Saltar entre rocas")
    print("2. Buscar un puente")
    print("3. Caminar sobre la lava")
    opcion = elegir("Â¿CÃ³mo cruzas? ", ["1", "2", "3"])
    if opcion == "3":
        print("Â¡La lava te quema!")
        perder_vida()
    else:
        print("Â¡Lograste cruzar el volcÃ¡n!")
    if vidas > 0:
        conseguir("Naranja")


def nivel_final():
    print("\n===== NIVEL 5: FORTALEZA DEL REY OSCURO =====")
    print("Â¡El Rey Oscuro aparece ante ti!")
    combate("Rey Oscuro", 5)
    if vidas > 0:
        conseguir("Rojo")


def nueva_partida():
    global vidas, cristales, inicio

    vidas = 3
    cristales = []
    seleccionar_personaje()
    input("\nPresiona ENTER para comenzar la aventura...")
    inicio = time.time()

    niveles = [nivel_bosque, nivel_cueva, nivel_castillo,
               nivel_volcan, nivel_final]

    for nivel in niveles:
        if not estado():
            break
        nivel()
        if not estado():
            break

    if len(cristales) == 5 and vidas > 0 and estado():
        print("\n===== Â¡VICTORIA! =====")
        print("Â¡Derrotaste al Rey Oscuro y salvaste el reino!")
        print("Cristales recuperados:", ", ".join(cristales))
        print("\nRECOMPENSAS")
        print("- Medalla de GuardiÃ¡n")
        print("- Trofeo del Reino")
        print("- Habilidad especial desbloqueada")
        print("Â¡Felicidades,", jugador + "!")
    else:
        print("\n===== DERROTA =====")
        print("No lograste salvar el reino.")
        print("Cristales obtenidos:", len(cristales))
        print("Vidas restantes:", vidas)

    input("\nPresiona ENTER para regresar al menÃº...")


def continuar():
    print("\nNo hay partidas guardadas.")
    print("Selecciona Nueva partida para comenzar.")
    input("Presiona ENTER para volver al menÃº...")


def creditos():
    print("\n===== CRÃ‰DITOS =====")
    print("Juego: Guardianes del Reino Perdido")
    print("Desarrolladora: Astrid Araceli Giron Luna")
    print("Programado en Python")
    input("\nPresiona ENTER para volver al menÃº...")


def opciones():
    print("\n===== OPCIONES =====")
    print("Sonido: Activado")
    print("GrÃ¡ficos: Alto")
    print("Controles: Teclado")
    input("\nPresiona ENTER para volver al menÃº...")


def menu_principal():
    while True:
        print("\n==============================")
        print("       MENÃš PRINCIPAL")
        print("==============================")
        print("1. Nueva partida")
        print("2. Continuar")
        print("3. CrÃ©ditos")
        print("4. Opciones")
        print("5. Salir")
        print("==============================")
        opcion = elegir("Selecciona una opciÃ³n: ",
                        ["1", "2", "3", "4", "5"])

        if opcion == "1":
            nueva_partida()
        elif opcion == "2":
            continuar()
        elif opcion == "3":
            creditos()
        elif opcion == "4":
            opciones()
        else:
            print("\nÂ¡Gracias por jugar!")
            print("Fin de Guardianes del Reino Perdido.")
            break


def main():
    print("=" * 45)
    print("Â¡BIENVENIDO A GUARDIANES DEL REINO PERDIDO!")
    print("Recupera los cinco cristales y salva el reino.")
    print("=" * 45)
    input("Presiona ENTER para continuar...")
    menu_principal()


if __name__ == "__main__":
    main()