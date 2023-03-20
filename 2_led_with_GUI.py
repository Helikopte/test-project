from guizero import App, Box, PushButton, Text
import RPi.GPIO as GPIO
#setup GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
LED1=20
LED2=21
GPIO.setup(LED1, GPIO.OUT)
GPIO.setup(LED2, GPIO.OUT)
#function to turn on LED1
def led1_on():
    GPIO.output(LED1, GPIO.HIGH)
    status1.value ="ON"
#function to turn off LED1
def led1_off():
    GPIO.output(LED1, GPIO.LOW)
    status1.value ="OFF"
#function to turn ON LED2
def led2_on():
    GPIO.output(LED2, GPIO.HIGH)
    status2.value ="ON"
#function to turn off LED2
def led2_off():
    GPIO.output(LED2, GPIO.LOW)
    status2.value ="OFF"
#create GUI window
app = App(title = "LED Control")

#create box for Led1 controls
led1_box = Box(app, layout="grid")
led1_text = Text(led1_box, text="LED1", grid=[0,0])
led1_on_button = PushButton(led1_box, command = led1_on, text="ON", grid=[1,0])
led1_off_button = PushButton(led1_box, command = led1_off, text="OFF", grid=[2,0])
status1 = Text(led1_box, text = "OFF", grid=[3,0])

#create box for Led2 controls
led2_box = Box(app, layout="grid")
led2_text = Text(led2_box, text="LED2", grid=[0,0])
led2_on_button = PushButton(led2_box, command = led2_on, text="ON", grid=[1,0])
led2_off_button = PushButton(led2_box, command = led2_off, text="OFF", grid=[2,0])
status2 = Text(led2_box, text = "OFF", grid=[3,0])

# run the GUI window
app.display()
