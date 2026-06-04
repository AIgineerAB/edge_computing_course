# Setup 

In this video we setup the toolchain needed 

<a href="https://www.youtube.com/watch?v=F82MrOkheSE&t=7s" target="_blank">
  <img src="https://github.com/kokchun/assets/blob/main/raspberry_pi/pico_vscode.png?raw=true" alt="setting up vscode for pico development" width="600">
</a>
 


## Setup micropython on Pico 2W

Connect pico 2W to your computer, you will see a flash drive with two files in it. If it doesn't show up shut remove the pico and click down BOOTSEL button and then connect the USB. Now you should see the flash drive. 

Install micropython on pico by dropping this file into the drive

- [micropython for Pico 2W](https://www.micropython.org/download/RPI_PICO2_W/)

it will eject itself after a few seconds and restarts itself in Python mode. 

> [!NOTE] 
> if you have another version of Raspberry pi Pico, you need to find the micropython firmware corresponding to that version


## Account on wokwi

Go into [wokwi](https://wokwi.com/) and create account and login there. This is a page for simulating hardware, and we'll work extensively with simulating different solutions before actually wiring things up on the board.

