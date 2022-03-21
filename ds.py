import spidev

"""

The distance formula has been taken from sparkfun forum. A user named
jmatson11 used it from sharp distance sensor datasheet.

"""
 
spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz=1000000

def channel(num):
	value = spi.xfer2([1,(8+channel)<<4,0])
	signal = ((value[1]&3) << 8) + value[2]
	return signal

if __name__ == "__main__":
	voltage = (num(0)/1023)*3.3
	calculate_distance = 16.2537 * voltage**4 - 129.893 * voltage**3 + 382.268 * voltage**2 - 512.611 * voltage + 301.439
	print(f"Current distance to the trash is: {calculate_distance} cm.")
