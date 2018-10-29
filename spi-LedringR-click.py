import time
import spidev

print("Make the Click Led ring R board work!")

spi = spidev.SpiDev()
spi.open(0, 0)

# This Click board is just (4) 74HCP595 8-bit shift
# registers daisy chained to the SPI data bus.

n = 25  # How many steps around the loop
m = 100 # How many times 0xaa or 0x55

# All on
spi.xfer([0xff, 0xff, 0xff, 0xff])
time.sleep(.5)

data_to_send = 4 * [0x0]
for i in range(0,m):
    if i % 32 == 0:
        r = 0x1
    else:
        r = r << 1

    data_to_send[0] = r % 256
    data_to_send[1] = (r >> 8) % 256
    data_to_send[2] = (r >> 16) % 256
    data_to_send[3] = (r >> 24) % 256

    time.sleep(.01)

    spi.xfer(data_to_send)

for i in range(0,n):

    if i % 2 == 0:
        data_to_send = [0xaa, 0xaa, 0xaa, 0xaa]
    else:
        data_to_send = [0x55, 0x55, 0x55, 0x55]

    # You can send less than 1 byte at a time and a max of 4 bytes
    spi.xfer(data_to_send)

    # Slow it down so your eyes can see the blinking
    time.sleep(.07)

# Lights off
spi.xfer([0x00, 0x00, 0x00, 0x00])

print("End Test")

