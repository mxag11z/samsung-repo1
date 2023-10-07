from gpiozero import LED
from time import sleep

# Configura los pines GPIO para los LEDs
led_verde = LED(17)  # Cambia el número de pin según tu configuración
led_ambar = LED(18)  # Cambia el número de pin según tu configuración
led_rojo = LED(19)   # Cambia el número de pin según tu configuración

# Función para controlar el semáforo
def controlar_semaforo(estado):
    if estado == "verde":
        led_verde.on()
        led_ambar.off()
        led_rojo.off()
    elif estado == "ambar":
        led_verde.off()
        led_ambar.on()
        led_rojo.off()
    elif estado == "rojo":
        led_verde.off()
        led_ambar.off()
        led_rojo.on()
    else:
        print("Estado desconocido")

try:
    while True:
        opcion = input("Escribe 'verde', 'ambar' o 'rojo' para controlar el semáforo (o 'salir' para salir): ")
        if opcion == "salir":
            break
        controlar_semaforo(opcion)
except KeyboardInterrupt:
    pass
finally:
    # Apaga todos los LEDs antes de salir
    led_verde.off()
    led_ambar.off()
    led_rojo.off()

