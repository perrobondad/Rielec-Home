#importamos la libreria GPIO y Time
import RPi.GPIO as GPIO
import time
#Definimos el modo BCM 
GPIO.setmode(GPIO.BCM) 
#Ahora definimos el pin GPIO 22 como salida
GPIO.setup(22, GPIO.OUT)
#Y le damos un valor logico alto para encender el LED
GPIO.output(22, 1)
#Le damos un retardo y lo apagamos
time.sleep(0.1)
GPIO.output(22, 0)
GPIO.cleanup()