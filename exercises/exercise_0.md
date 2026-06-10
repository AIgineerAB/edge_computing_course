# Exercise 0 - Raspberry Pi Pico fundamentals

In this exercise, you get to familiarize yourself with simulating, building and programming different circuits. This exercise cover 00-03.

> [!NOTE]
> whenever you modify your circuits on the microcontroller, make sure that it is connected

## 0. Morse code

In this exercise we will build a circuit for doing morse code.

&nbsp; a) Start with wokwi and build the circuit for an LED.

> [!IMPORTANT]
> don't forget resistor ≥ 330$\Omega$ between GPIO pin and the LED.

&nbsp; b) Now create a longer signal and a shorter signal with some time durations of your choices.

&nbsp; c) Recreate the alphabet with morse code and store in a dictionary.

&nbsp; d) Blink the word "COOL" with morse code signal.

&nbsp; e) Let the user type in a word or a message and let the LED blink accordingly.

&nbsp; f) Now wire this up on your Pico and upload the code to it to try it out.

&nbsp; g) Also add an emergency button that will trigger SOS signal in morse code. First do this in wokwi before adding it to your Pico.

## 1. Reaction game

For this exercise also create a simulation before building the circuits.

&nbsp; a) Make an LED turn on and then randomly turn off. When it is turned off, the player needs to press the button. Then it should output the reaction time of that player.

&nbsp; b) It is fun to train your reaction time like that, but can it be more fun? Yeah if you can beat your friend. Extend this into a two player game that tracks the winner and that persons time.

## 2. Traffic system

In the lectures, we have covered normal traffic light and a pedestrian puffin light. Can put them in a system with both these traffic lights working like a real traffic light and pedestrian light would work.

Make sure to get this working in wokwi simulation before moving on to the actual board. You might need two breadboards as it can be too crowded with just one.

## 3. Theory questions

&nbsp; a) You have a 3.3V GPIO pin and a 330Ω resistor. If you connect them directly to Ground (creating a short circuit through the resistor), what is the current flowing through that resistor?

Ohms law: $V = IR$

&nbsp; b) If you have an LED circuit and you disconnect the wire going to the GND pin on the Pico, the LED turns off. Why? Is it because the "power" stopped, or because the "path" was broken?

&nbsp; c) Can a GPIO pin on the Pico be used as both an Input and an Output? If so, what does that mean for your code?

&nbsp; d) When you use input() in MicroPython while connected to your PC, where is the text actually being processed? Is it happening inside the Pico's microcontroller chip, or is the Pico just receiving the result from your computer?

&nbsp; e) How many voltage comes from GPIO pins?

&nbsp; f) Why do you have to have a resistor between LED and GPIO pin?

&nbsp; g) What happens when an LED is connected backwards?

&nbsp; h) What is the purpose of using a breadboard?

## Glossary

Fill in this table either by copying this into your own markdown file or copy it into a spreadsheet if you feel that is easier to work with.

| terminology       | explanation |
| ----------------- | ----------- |
| REPL              |             |
| raspberry pi      |             |
| raspberry pi pico |             |
| sensor            |             |
| hardware          |             |
| firmware          |             |
| breadboard        |             |
| micropython       |             |
| thonny            |             |
| edge computing    |             |
| GPIO              |             |
| pins              |             |
| LED               |             |
| multimeter        |             |
| transistor        |             |
| capacitor         |             |
| anode             |             |
| cathode           |             |
|                   |             |
|                   |             |
