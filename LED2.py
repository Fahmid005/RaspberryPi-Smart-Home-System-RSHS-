from gpiozero import LED
from gpiozero import Button

led1 = LED(4)
button1 = Button(17)

led2 = LED(6)
button2 = Button(13)

while True:
    button1.wait_for_press()
    led1.on()
    button1.wait_for_release()
    led1.off()
    
    button2.wait_for_press()
    led2.on()
    button2.wait_for_release()
    led2.off()
    
    
