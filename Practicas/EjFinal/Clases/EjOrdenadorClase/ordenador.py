from dispositivos import Entrada, Procesador, Salida
from procesadores import ProcesadorUpper, ProcesadorRever
from salidas import EscribirFichero

# teclado = Entrada("Teclado Logitech")
# procesador = Procesador("AMD")
# pantalla = Salida("Pantalla Samsung")
#
# procesador.conectar_a(pantalla)
# teclado.conectar_a(procesador)
#
# teclado.procesar()

# teclado = Entrada("Teclado Logitech")
# procesador = ProcesadorRever("AMD Rever")
# pantalla = Salida("Pantalla Samsung")
#
# procesador.conectar_a(pantalla)
# teclado.conectar_a(procesador)
#
# teclado.procesar()

teclado = Entrada("Teclado Logitech")
procesador = ProcesadorRever("AMD Rever")
fichero = EscribirFichero("Fichero en disco")

procesador.conectar_a(fichero)
teclado.conectar_a(procesador)

teclado.procesar()
