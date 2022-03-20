# packages to be imported
from luma.core.interface.serial import i2c, spi   # set the frames for sending and receiving data and commands over the serial channel
from luma.core.render import canvas   # sets the 2D-3D graphics
from luma.oled.device import sh1106    # select the device configurations
import time
# I2C bus settings
serial = i2c(port=1, address=0x3C)  # declaration of the device to the system


device = sh1106(serial) # device configuration 

while True:
    
    
    with canvas(device) as draw:   # graphics and data settings 
        
    
        draw.rectangle(device.bounding_box, outline="white", fill="black")
        draw.text((30, 40), "Comp EDP 2", fill="white")
        #time.sleep(2)
