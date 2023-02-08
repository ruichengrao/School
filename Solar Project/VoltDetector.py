import RPi.GPIO as GPIO
import csv
import schedule
#csv header/stated file
header = ["Volt"]
filename = 'Volt_Tracking.csv'
a = True

AO_pin = 0 #flame sensor AO connected to ADC chanannel 0
# change these as desired - they're the pins connected from the
# SPI port on the ADC to the Cobbler
SPICLK = 11
SPIMISO = 9
SPIMOSI = 10
SPICS = 8

#port init
def init():
          GPIO.setwarnings(False)
          GPIO.setmode(GPIO.BCM)
          # set up the SPI interface pins
          GPIO.setup(SPIMOSI, GPIO.OUT)
          GPIO.setup(SPIMISO, GPIO.IN)
          GPIO.setup(SPICLK, GPIO.OUT)
          GPIO.setup(SPICS, GPIO.OUT)
          pass

#read SPI data from MCP3008(or MCP3204) chip,8 possible adc's (0 thru 7)
def readadc(adcnum, clockpin, mosipin, misopin, cspin):
        if ((adcnum > 7) or (adcnum < 0)):
                return -1
        GPIO.output(cspin, True)  

        GPIO.output(clockpin, False)  # start clock low
        GPIO.output(cspin, False)     # bring CS low

        commandout = adcnum
        commandout |= 0x18  # start bit + single-ended bit
        commandout <<= 3    # we only need to send 5 bits here
        for i in range(5):
                if (commandout & 0x80):
                        GPIO.output(mosipin, True)
                else:
                        GPIO.output(mosipin, False)
                commandout <<= 1
                GPIO.output(clockpin, True)
                GPIO.output(clockpin, False)

        adcout = 0
        # read in one empty bit, one null bit and 10 ADC bits
        for i in range(12):
                GPIO.output(clockpin, True)
                GPIO.output(clockpin, False)
                adcout <<= 1
                if (GPIO.input(misopin)):
                        adcout |= 0x1

        GPIO.output(cspin, True)
        
        adcout >>= 1       # first bit is 'null' so drop it
        return adcout

def main():
        init()
        while True:
                ad_value = readadc(AO_pin, SPICLK, SPIMOSI, SPIMISO, SPICS)
                global voltage
                voltage = ad_value*(3.3/1024)*5
                global volts
                volts = [str(voltage)]
                with open(filename, 'a', newline="\n") as file:
                        csvwriter = csv.writer(file)
                        #skips header line after the first run
                        if a:
                         csvwriter.writerow(header)
                         a = False
                         csvwriter.writerow(volts)
                                
                GPIO.cleanup() 
          

schedule.every(2).minutes.do(main)
