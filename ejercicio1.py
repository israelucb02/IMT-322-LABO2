import RPi.GPIO as GPIO
import time


led_pins = [19, 13]  
button_pin = 23  
state = 1  

def setup():
    GPIO.setwarnings(False) 
    GPIO.setmode(GPIO.BCM)   
    
    
    for pin in led_pins:
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.LOW) 
    
    GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def state_1():
    GPIO.output(led_pins[0], GPIO.HIGH)
    GPIO.output(led_pins[1], GPIO.LOW)
    time.sleep(1)
    GPIO.output(led_pins[0], GPIO.LOW)
    GPIO.output(led_pins[1], GPIO.HIGH)
    time.sleep(1)

def state_2():
    GPIO.output(led_pins[0], GPIO.HIGH)
    GPIO.output(led_pins[1], GPIO.HIGH)
    time.sleep(2)
    GPIO.output(led_pins[0], GPIO.LOW)
    GPIO.output(led_pins[1], GPIO.LOW)
    time.sleep(2)

def state_3():

    GPIO.output(led_pins[0], GPIO.HIGH)
    GPIO.output(led_pins[1], GPIO.HIGH)

def state_4():
    """State 4: This state turn
    GPIO.output(led_pins[0], GPIO.LOW)
    GPIO.output(led_pins[1], GPIO.LOW)

def change_state():
    
    global state
    state = (state % 4) + 1  # de 1 a 4

def run():
    global state
    try:
        while True:
            if GPIO.input(button_pin) == GPIO.LOW:  # presionado el boton
                change_state()
                time.sleep(0.3)  
            
            if state == 1:
                state_1()
            elif state == 2:
                state_2()
            elif state == 3:
                state_3()
            elif state == 4:
                state_4()
            
            time.sleep(0.1)  # delay
    except KeyboardInterrupt:
        print("\nSaliendo del programa...")
        GPIO.cleanup()

setup()
run()




