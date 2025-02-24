import RPi.GPIO as GPIO
import time
import random  

heater_pin = 5  
fan_pin = 13     

def setup():
    
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    
    GPIO.setup(heater_pin, GPIO.OUT)
    GPIO.setup(fan_pin, GPIO.OUT)
    
    GPIO.output(heater_pin, GPIO.LOW)
    GPIO.output(fan_pin, GPIO.LOW)

def get_temperature():
    return random.uniform(5, 25)  

def control_temperature():
    
    while True:
        temperature = get_temperature()  
        print(f"Temperatura actual: {temperature:.2f} °C")

        if temperature < 12:
            GPIO.output(heater_pin, GPIO.HIGH)  
            GPIO.output(fan_pin, GPIO.LOW)      
            print("🔥 Calefactor ENCENDIDO")
        
        elif temperature > 20:
            GPIO.output(heater_pin, GPIO.LOW)  
            GPIO.output(fan_pin, GPIO.HIGH)    
            print("❄ Ventilador ENCENDIDO")
        
        else:
            GPIO.output(heater_pin, GPIO.LOW)  
            GPIO.output(fan_pin, GPIO.LOW)     
            print("✅ Temperatura ÓPTIMA - Ambos dispositivos APAGADOS")

        time.sleep(2)  

try:
    setup()
    control_temperature()
except KeyboardInterrupt:
    print("\nSaliendo del programa...")
    GPIO.cleanup()  
