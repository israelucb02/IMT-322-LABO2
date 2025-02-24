import RPi.GPIO as GPIO
import time

leds = [19, 13, 6, 5]  
button_up = 23 
button_down = 24  
x = 0  

def setup():
    GPIO.setwarnings(False)  
    GPIO.setmode(GPIO.BCM)   
    
    for pin in leds:
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.LOW)  
    
    GPIO.setup(button_up, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(button_down, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def update_leds():
    valorb = format(x, '04b')  
    print(f"Decimal: {x}, Binario: {valorb}, Hex: {hex(x).upper()}")

    for i in range(4):
        GPIO.output(leds[i], GPIO.HIGH if valorb[i] == '1' else GPIO.LOW)

def increment():
    global x
    x = (x + 1) if x < 15 else 0
    update_leds()

def decrement():
    global x
    if x > 0:
        x -= 1
    update_leds()

def run():
    try:
        while True:
            if GPIO.input(button_up) == GPIO.LOW:  #
                increment()
                time.sleep(0.3)  

            if GPIO.input(button_down) == GPIO.LOW:  
                decrement()
                time.sleep(0.3) 
            
            time.sleep(0.1)  
    except KeyboardInterrupt:
        print("\nSaliendo del programa...")
        GPIO.cleanup()

# Configurar y ejecutar el programa
setup()
run()
