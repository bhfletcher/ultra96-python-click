## This stuff is for tinkering with the Mickroe Click boards from the Avnet/Xilinx Ultra96 Python  environment (also works with Ultra96 PYNQ)

**Pre-requisites:**
  - Existing /dev/spidevx.x devices
  - User permission of devices! ("sudo chmod a+rwx /dev/spidev?.?", chown or the right way with adduser to existing group spi or sudo)
  - Python with pip installed
  - Relevant Click boards

**How to install and use PYNQ:**
  - How-to video and instructions: https://ultra96-pynq.readthedocs.io/en/latest/getting_started.html
  - Ultra96 PYNQ distribution found here: http://avnet.me/ultra96_pynq_sd_image

**Github for Python with Mikro Click boards:**
  - Boot up, ssh into your PYNQ/PetaLinux distribution for Ultra96
  - Using Ultra96 PYNQ or equivalent install, git "sudo apt install git"
  - git clone https://github.com/focalplane/Ultra96-click.git

**Attaching the click boards:**
  - To attach click board, POWER DOWN ULTRA96 BOARD: "sudo shutdown -h now", then UNPLUG power!
  - Attach Click mezzanine board with Click board installed in appropriate slot
  - Power on and boot up, ssh with user: xilinx, password: xilinx then use the boards

**For SPI bus Mikro Click boards:**
  - "sudo pip3 install spidev"
  - "cd python-click" into git folder, then run "sudo python3 spitest.py" for sanity check of spi device driver
  -  If you have an LED Ring R Click board to test in slot 1 "sudo python3 spi-LedringR-click.py"
  -  Click board slot 1 -> /dev/spidev0.1 , slot 2 -> /dev/spidev1.1

**For I2C bus Mikro Click boards:**
  - "sudo apt install python3-smbus"
  - /dev/i2c-1 is the Ultra96 I2C mux
  - If PetaLinux is setup to take care of the I2C Mux then Click slot 1 -> /dev/i2c-3, slot 2 -> /dev/i2c-4
  - To verify things are working and you have an LPS22HB Click board: "sudo python3 i2c-lps22hb-click.py"

**Good Luck!**
