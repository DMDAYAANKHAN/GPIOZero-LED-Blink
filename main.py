#code by Ayaan khan
#support me https://www.buymeacoffee.com/ayaancode2t

from gpiozero import LED
from time import sleep

led = LED(21) # make sure to change the pin according to your requirements

while true:
  led.on()
  sleep(1) # you can change the delay/time here
  led.off()
  sleep(1) # you can change the delay/time here
  
 
