from machine import Pin, PWM
import time

# Definir los pines de los servomotores
servo1_pin = Pin(25, Pin.OUT)
servo2_pin = Pin(26, Pin.OUT)
servo3_pin = Pin(27, Pin.OUT)

# Configurar PWM para los servomotores
servo1 = PWM(servo1_pin, freq=50)
servo2 = PWM(servo2_pin, freq=50)
servo3 = PWM(servo3_pin, freq=50)

# Definir los pines de los botones
button1_pin = Pin(18, Pin.IN, Pin.PULL_DOWN)
button2_pin = Pin(19, Pin.IN, Pin.PULL_DOWN)
button3_pin = Pin(21, Pin.IN, Pin.PULL_DOWN)

# Función para mover el servomotor a un ángulo específico
def set_servo_angle(servo, angle):
    # El ángulo se mapea a un ciclo de trabajo entre 40 y 115 (para un rango de 0 a 180 grados)
    duty = int((angle / 180.0 * 75) + 40)
    servo.duty(duty)

# Ángulos definidos para cada botón
angle1 = 45  # Ángulo para el servomotor 1 cuando se presiona el botón 1
angle1_2 = 90  # Segundo ángulo para el servomotor 1
angle2 = 45  # Ángulo para el servomotor 2 cuando se presiona el botón 2
angle3 = 45  # Ángulo para el servomotor 3 cuando se presiona el botón 3

# Estados anteriores de los botones para detectar cambios
prev_button1_state = button1_pin.value()
prev_button2_state = button2_pin.value()
prev_button3_state = button3_pin.value()

# Estado de los servomotores
servo1_angle = angle1

while True:
    # Leer el estado actual de los botones
    current_button1_state = button1_pin.value()
    current_button2_state = button2_pin.value()
    current_button3_state = button3_pin.value()
    
    # Detectar cambios en el estado del botón 1
    if current_button1_state != prev_button1_state:
        if current_button1_state == 0:  # Botón 1 presionado
            if servo1_angle == angle1:
                servo1_angle = angle1_2
            else:
                servo1_angle = angle1
            set_servo_angle(servo1, servo1_angle)
            print("Botón 1 presionado, moviendo servo 1 a", servo1_angle, "grados")
        prev_button1_state = current_button1_state

    
    # Detectar cambios en el estado del botón 2
    if current_button2_state != prev_button2_state:
        if current_button2_state == 0:  # Botón 2 presionado
            set_servo_angle(servo2, angle2)
            print("Botón 2 presionado, moviendo servo 2 a", angle2, "grados")
        prev_button2_state = current_button2_state
    
    # Detectar cambios en el estado del botón 3
    if current_button3_state != prev_button3_state:
        if current_button3_state == 0:  # Botón 3 presionado
            set_servo_angle(servo3, angle3)
            print("Botón 3 presionado, moviendo servo 3 a", angle3, "grados")
        prev_button3_state = current_button3_state
    
    time.sleep(0.1)  # Pequeño retraso para evitar el rebote del botón
