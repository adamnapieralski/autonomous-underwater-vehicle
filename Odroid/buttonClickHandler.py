#skrypt odpalany po zbootowaniu się odroida, odroid czeka na przycisk żeby odpalić odpowiedni skrypt a ten 
#zamknąć 
import wiringpi
import subprocess
PIN_TO_SENSE = 6        #numer pinu 

def gpioCallback():
<<<<<<< HEAD
    #print ("GPIO CALLBACK - called by buttonclick!")
    subprocess.call('sudo python3 /home/odroid/MainOdroid.py ', shell=True)
=======
    print("GPIO CALLBACK - called by buttonclick!")
    subprocess.call('python3 /home/odroid/MainOdroid.py ', shell=True)
>>>>>>> 383f4892900b360f0d43a815283f9ee99e016ebb

wiringpi.wiringPiSetup()
wiringpi.pinMode(PIN_TO_SENSE, 0)
wiringpi.pullUpDnControl(PIN_TO_SENSE, wiringpi.PUD_UP) #podciaganie rezystorem do 3.3V

#wiringpi.wiringPiISR(PIN_TO_SENSE, wiringpi.GPIO.INT_EDGE_FALLING, gpioCallback) #wersja na przerwaniu

while True:
    if wiringpi.digitalRead(PIN_TO_SENSE) == 0:
        gpioCallback()
        break
    wiringpi.delay(100) #ms