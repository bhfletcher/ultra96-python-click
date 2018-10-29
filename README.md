## This stuff is for tinkering with the Mickroe Click boards from the Avnet/Xilinx Ultra96 Python  environment (also for Ultra96 PYNQ)

**Pre-requisites:**
  - Existing /dev/spidevx.x devices
  - User permission of devices! ("sudo chmod a+rwx /dev/spidev?.?", chown or the right way with adduser to existing group spi)
  - Python with pip installed
  - Relevant Click boards

**How to install and use PYNQ:**
  - How-to video and instructions: https://ultra96-pynq.readthedocs.io/en/latest/getting_started.html
  - Ultra96 PYNQ distribution found here: http://avnet.me/ultra96_pynq_sd_image

**Github for Python with Mikro Click boards:**
  - Boot up, ssh into your PYNQ/PetaLinux distribution for Ultra96
  - Using Ultra96 PYNQ or equivalent install, git "sudo apt install git"
  - git clone https://github.com/focalplane/Ultra96-click.git

**For SPI bus Mikro LED ring R Click board with PYNQ:**
  - To attach click board, POWER DOWN ULTRA96 BOARD: "sudo shutdown -h now", then UNPLUG power!
  - Attach LED ring R Click board in slot that is assocated with /dev/spidev0.1
  - Boot up, ssh with user: xilinx, password: xilinx
  - Install Python library spidev with "pip3 install spidev"
  - "cd Ultra96-click" into git folder, then run "python3 spitest.py" for sanity check of spi device
  - "python3 spi-LedringR-click.py" and watch the lights blink

**Good Luck!**
