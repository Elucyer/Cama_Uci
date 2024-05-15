from machine import Pin, PWM
import time

# Configurar los pines de los botones y los pines de los servomotores
boton_servo1_pin = Pin(12, Pin.IN, Pin.PULL_UP)  # Cambia el número de pin según tu configuración
boton_servo2_pin = Pin(13, Pin.IN, Pin.PULL_UP)  # Cambia el número de pin según tu configuración

servo1_pin = 15  # Cambia el número de pin según tu configuración
servo2_pin = 14  # Cambia el número de pin según tu configuración

# Configurar los pines de los servomotores como PWM
servo1_pwm = PWM(Pin(servo1_pin), freq=50)
servo2_pwm = PWM(Pin(servo2_pin), freq=50)

# Función para mover el servo a una posición específica
def move_servo(servo, angle):
    duty = (angle / 180) * 102 + 26
    servo.duty(duty)

# Bucle principal
while True:
    # Verificar el estado del botón para el primer servo
    if boton_servo1_pin.value() == 0:
        # Incrementar el ángulo en 10 grados
        angle1 += 10
        if angle1 > 180:
            angle1 = 0
        move_servo(servo1_pwm, angle1)
        time.sleep(0.2)  # Esperar para evitar rebotes del botón
    
    # Verificar el estado del botón para el segundo servo
    if boton_servo2_pin.value() == 0:
        # Incrementar el ángulo en 10 grados
        angle2 += 10
        if angle2 > 180:
            angle2 = 0
        move_servo(servo2_pwm, angle2)
        time.sleep(0.2)  # Esperar para evitar rebotes del botón
