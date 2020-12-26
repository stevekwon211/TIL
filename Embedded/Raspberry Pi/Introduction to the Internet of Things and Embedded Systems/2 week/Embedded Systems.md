![49323186646_8875a033ac_c](https://user-images.githubusercontent.com/61633137/103147296-6b412f80-4797-11eb-968e-a0152fcb809c.jpg)

# 1. Features and Constraints of Embedded Systems

## 1.1. What are Embedded Systems?

- __Computer-based systems__ that do not appear to be computers, complexity is hidden from the user
- Much more common than desktops or laptops
- They __interact with users__ via simple interface
  - Digital camera, TV, cellphone, etc
- They __interact with another device__, invisible to user
  - Disk drive, memory stick, anti-lock braking system

<br>

### 1.1.1. Efficiency Rules

- Most embedded products are in __cost-critical markets__ (e.g. consumer electronics)
- Other applications are in __performance or power critical markets__ (e.g. military, medical)

<br>

### 1.1.3. Tight Constraints

- Manufacturing cost
- Design cost
- Performance
- Power
- Time-to-market
- Very different from traditional software engineering
  - __Moore's law__ will save you eventually

<br>

## 1.2. More on Embedded Systems

### 1.2.1. Application Specificity

- Embedded systems tend to be __application-specific__
  - Perform __one task__ or __set of related tasks__
  - Some devices __blur the line__ (e.g. cell phones)
- Design is focused on __one application__, unlike general-purpose systems (e.g. laptops)
- __Higher design efficiency__ is possible
  - Special-purpose vs general purpose (e.g. video games)
- Hardware and software are often __designed together__
  - General-purpose systems use hardware and software developed by different companies

<br>

## 1.3. Generic Embedded Systems Structure

### 1.3.1. Intellectual Property (IP) Core

- An integrated circuit that performs __one function__
- Cheap in __high volume__
- Very useful for __common tasks__
  - Network controllers (Ethernet, CAN)
  - Audio & Video (audio codec, VGA controller)
- Must interact with the __micro-controller__
  - Consider communication protocol

<br>

### 1.3.2. Field Programmable Gate Array (FPGA)

- Hardware that can be reconfigured via __RAM__
  - Faster than SW, slower than ASIC
  - No fabrication needed

<br>

# 2. Components of Embedded Systems

## 2.1. Micro-controllers

-  Integrated circuit that executes a program
  - Micro-controller vs Micro-processor
  - Slower, 16MHz - 500MHz
  - Less memory, fewer features
- Connected to other hardware components
- Sends commands and receives data
- Needs to be programmed
  - Write a program in a language, such as C, Python, etc
  - Place the program in the mctrlr memory

<br>

### 2.1.2. Programming Micro-controllers

- Write code on a host machine - regular desktop or laptop
- Programming the micro-controller - transferring the program from host to micro-controller

<br>

### 2.1.3.  Using a Programmer

- Programming hardware can be used to place program in micro-controller memory

<br>

## 2.2. More on Components of Embedded Systems

### 2.2.1. Using a Development Board

- Includes hardware needed for programming

<br>

### 2.2.2 General Purpose Processors

- Used for any application
- Many features included

<br>

### 2.2.3. Digital Signal Processors

- Made to support DSP functions
- Vector instructions
- Cheaper but more limited

<br>

### 2.2.4. Sensors

- Provide simple information
  - Thermistor: reports temperature
  - Photo-resistor: reports light intensity

<br>

### 2.2.5. Complex Sensors

- More complicated data
  - CMOS camera: captures images
  - Ethernet controller: enables network communication

<br>

### 2.2.6.  Actuators

- Cause events to occur in the environment
- Simple actuators
  - Light-Emitting Diodes (LEDs) - small lights
  - LCD Display - simple display

<br>

### 2.2.7. Complex Actuators

- Servo motor: moves something
- Ethernet controller: enables network communication

<br>

# 3. Interacting with the Physical World

## 3.1. Analog & Digital Conversion

### 3.1.1. Analog to Digital Conversion

- Converts analog data to digital data
- Used to interface with analog sensors

<br>

### 3.1.2. Digital to Analog Conversion

- Converts digital signals to analog signals
- Used to interface with analog actuators

<br>

### 3.1.3. ADC Example

<img src="https://upload.wikimedia.org/wikipedia/commons/5/5a/Conversion_AD_DA.png" style="zoom:67%;" /> 

- Sound is a pressure wave over time
- A microphone converts pressure voltage
- Voltage is sampled over time
- Each voltage sample is represented as a digital number

<br>

## 3.2. Basic Equipment

### 3.2.1. Development board

- A development board with a micro-controller (Arduino, Raspberry Pi, STM, etc)
- The center of most projects

<br>

### 3.2.2. Connectors

- USB
- Ethernet cable
- Jumper wires
- more...

<br>

### 3.2.3. Inputs

- Potentiometer
- Photo-resistor
- Keypad
- Buttons
- more...

<br>

### 3.2.4. Outputs

- LEDs
- Resistor
- Breadboard
  <img src="https://cdn.pixabay.com/photo/2020/05/23/17/27/breadboard-5210635_960_720.jpg" style="zoom:67%;" />
  - All holes in a side column are connected (Each row of 5 holes is connected)
  - Used for fast, non-permanent wiring
  - Holes fit 24-gauge wire and, 0.1 inch spacing
    - Common prototyping sizes
- more...

