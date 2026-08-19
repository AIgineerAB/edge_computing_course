# Exercise 2 - Raspberry Pi Pico fundamentals

In this exercise, you get to further explore APIs and IoT pipelines. This exercise cover 06-08.

> [!NOTE]
> whenever you modify your circuits on the microcontroller, make sure that it is connected

## 0. Joking

Use this [joke API](https://github.com/15dkatz/official_joke_api) and get a joke from pico and print it out on an LCD display. If you don't have enough characters on the actual display, you could just cut the remaining characters off.

## 1. Travel board

Use [trafiklabs API here](https://www.trafiklab.se/api/our-apis/resrobot-v21/) and make a displayboard for coming trains in Sweden. For example you could choose a station in Stockholm and find out the arriving trains/buses and show amount of minutes left. This should update of course so that the information is fresh and usable.

## 2. IoT pipeline with other sensors

Create an IoT pipeline similar to lecture 08_iot_pipeline, but choose other types of sensors, for example photosensor and visualize it live on Grafana dashboard.

## 3. Theory questions

&nbsp; a) Why do we need MQTT protocol?

&nbsp; b) What are the purposes of overcomplicating the pipeline when you could simply just do requests directly from pico into the computer?

&nbsp; c) Think of some useful projects where this types of IoT pipelines could play a central role.

&nbsp; d) What are publish-subscribe system and what are they used for?

## Glossary

Fill in this table either by copying this into your own markdown file or copy it into a spreadsheet if you feel that is easier to work with.

| terminology  | explanation |
| ------------ | ----------- |
| mqtt         |             |
| consumer     |             |
| producer     |             |
| IoT          |             |
| streaming    |             |
| polling      |             |
| containerize |             |
| broker       |             |
| mosquitto    |             |
| grafana      |             |
| timescaledb  |             |
| postgres     |             |
|              |             |
