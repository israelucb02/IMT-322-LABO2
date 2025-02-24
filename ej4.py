import RPi.GPIO as GPIO
import time

# Definir pines
LED_PINS = [5, 6, 13, 19]
BUTTON_NEXT_LED = 23
BUTTON_ADD_TIME = 24

# Configuración GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

# Configurar LEDs como salida
for pin in LED_PINS:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)

# Configurar botones como entrada con pull-up
GPIO.setup(BUTTON_NEXT_LED, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BUTTON_ADD_TIME, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Variables
led_state=False
selected_led = 0
led_on_time = 1
last_led_change_time = 0  # Momento en que el LED se encendió
last_button1_state = GPIO.input(BUTTON_NEXT_LED)
last_button2_state = GPIO.input(BUTTON_ADD_TIME)

try:
    while True:
        current_time = time.time()  # Simulación de millis() en Python
        
        # Leer estado de los botones (evitando rebotes manualmente)
        button1_state = GPIO.input(BUTTON_NEXT_LED)
        button2_state = GPIO.input(BUTTON_ADD_TIME)

        # Si el botón 1 se presionó (cambia LED)
        if button1_state == GPIO.LOW and last_button1_state == GPIO.HIGH:
            GPIO.output(LED_PINS[selected_led], GPIO.LOW)  # Apagar LED actual
            selected_led = (selected_led + 1) % len(LED_PINS)  # Cambia al siguiente LED
            led_on_time = 1  # Reinicia el tiempo
            last_led_change_time = current_time
            print(f"LED cambiado a {selected_led + 1}, tiempo reiniciado a {led_on_time}s")

        # Si el botón 2 se presionó (aumenta el tiempo de encendido)
        if button2_state == GPIO.LOW and last_button2_state == GPIO.HIGH:
            led_on_time += 1
            print(f"Tiempo de LED {selected_led + 1} aumentado a {led_on_time}s")

        # Guardar el estado actual de los botones para la próxima iteración
        last_button1_state = button1_state
        last_button2_state = button2_state

        # Control de encendido del LED (similar a millis en Arduino)
        if current_time - last_led_change_time >= led_on_time:
            led_state = not led_state  # Alternar estado del LED
            GPIO.output(LED_PINS[selected_led], GPIO.HIGH if led_state else GPIO.LOW)
            last_led_change_time = current_time  # Actualizar el tiempo de referencia
           # GPIO.output(LED_PINS[selected_led], GPIO.LOW)  # Apagar LED
           # last_led_change_time=time.time()
       # else:
        #    GPIO.output(LED_PINS[selected_led], GPIO.HIGH)  # Encender LED
#            last_led_change_time=time.time()


        time.sleep(0.1)  # Pequeña pausa para reducir carga del CPU

except KeyboardInterrupt:
    print("\nSaliendo y limpiando GPIO...")
    GPIO.cleanup()

