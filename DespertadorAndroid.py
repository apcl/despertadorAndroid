from android import Android
import time

droid = Android()

defH = int (input ('Hora (0-23): '))
defM = int (input ('Minuto (0-59): '))
texto = input ('Texto ("despierta"): ')

while True:
    h = int (time.strftime ('%H'))
    m = int (time.strftime ('%M'))
    if (h == defH and m >= defM):
        droid.ttsSpeak (texto)
        print (texto)
    time.sleep(10)