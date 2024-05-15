from machine import Pin
from esp32_gpio_lcd import GpioLcd
from time import sleep_ms

def scroll_text(lcd, text, delay, line):
    lcd.move_to(0, line) 
    lcd.putstr(text)
    for i in range(len(text)):
        lcd.move_to(i, line)
        lcd.putstr(text[i:i+16])
        sleep_ms(delay)

def test_main():
    print("Corriendo Texto de prueba")
    lcd_line1 = GpioLcd(rs_pin=Pin(4), enable_pin=Pin(15),
                  d4_pin=Pin(5),
                  d5_pin=Pin(18),
                  d6_pin=Pin(21),
                  d7_pin=Pin(22),
                  num_lines=1,  num_columns=20)
    lcd_line1.blink_cursor_on()
    
    lcd_line2 = GpioLcd(rs_pin=Pin(4), enable_pin=Pin(15),
                  d4_pin=Pin(5),
                  d5_pin=Pin(18),
                  d6_pin=Pin(21),
                  d7_pin=Pin(22),
                  num_lines=1,  num_columns=20)
    lcd_line2.move_to(0, 1)
    
    message1 = input("Ingrese un texto para la línea 1: ")
    message2 = input("Ingrese un texto para la línea 2: ")
    
    while True:
        scroll_text(lcd_line1, message1, 200, 0)  # Ajusta el retraso según la velocidad de desplazamiento deseada
        scroll_text(lcd_line2, mes, 200, 0)
        sleep_ms(5000)

test_main()
