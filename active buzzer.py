import RPi.GPIO as GPIO
from time import sleep
#active buzzer pin
buzPin = 27
#button pin
btnPin = 18
GPIO.setmode(GPIO.BCM) # use BCM numbers
GPIO.setup(buzPin,GPIO.OUT) #set buzPin OUTPUT mode
GPIO.setup(btnPin,GPIO.IN,GPIO.PUD_UP) #set btnPin input mode
while True:
    val =GPIO.input(btnPin)
    print(val);
    if(val == 1):# Judge wether the button is pressed
        GPIO.output(buzPin,GPIO.HIGH) # Buzzer Ring
    else:
        GPIO.output(buzPin,GPIO.LOW) #buzzer off
GPIO.cleanup() #release all GPIO