 <img src="https://cdn.pixabay.com/photo/2015/10/05/21/03/circuit-board-973311_960_720.jpg" style="zoom: 44%;" /><img src="https://cdn.pixabay.com/photo/2016/11/24/20/48/programming-1857236_960_720.jpg" style="zoom: 44%;" />

# Hardware and Software

## 0. Introduction

- IoT devices are a combination of hardware and software
- Hardware and software components must be designed together

<br>

## 1. Hardware Components

### 1.1. Datasheets

- __Datasheets__ give details of each hardware component
  - Physical size
  - Input/output pins
  - Electrical parameters (max current, etc)

<br>

### 1.2. Datasheet Example

- Size specifications for manufacturing

<img src="https://user-images.githubusercontent.com/61633137/103164080-f7139400-4849-11eb-89f9-86ad7c9d89f3.jpg" alt="8607885336_ac591857cf_z" style="zoom:67%;" /> 

- Electrical and thermal parameters

<img src="https://www.researchgate.net/publication/325991484/figure/tbl1/AS:670512476852254@1536874040802/Electrical-and-thermal-parameters-of-the-cooper-used-for-the-fuse.png" style="zoom:67%;" /> 

<br>

### 1.3. Integrated Circuits (ICs)

<img src="https://user-images.githubusercontent.com/61633137/103164164-f62f3200-484a-11eb-9642-aa1b1df676d0.jpg" alt="26947433653_2aac1c1795_c" style="zoom: 50%;" /> 

- A small electronic device made of a semiconductor material
  - Silicon, Gallium Arsenide, etc
- Chip is protected by a package
- Package has a set of pins to allow chip access

<br>

### 1.4. Micro-controller Properties

#### 1.4.1. Micro-controller Characteristics

- Data-path Bit-width
  - Number of bits in __each register__
  - Determines __accuracy__ and __data throughput__
- Input & Output Pins
  - Need __enough pins__ to support your application
- Performance 
  - __Clock rates are slower than desktop__

<br>

#### 1.4.2. Other Micro-controller Features

- __Timers__
  - Needed for __real-time applications__
- __Analog-to-Digital Converters__
  - Used to __read input from analog sensors__
- __Low-power modes__
  - __Power saving__ is key
- __Communication protocol support__
  - Interface with other __ICs__
  - __UART__, __I2C__, __SPI__, etc

<br>

## 2. Micro-controllers and Software

### 2.1 Micro-controller Components

#### 2.1.1. AVR ATmega2560

- 8-bit micro-controller
- Up to 16MHz
- 256KB of flash memory
- 4KB EEPROM, 8KB SRAM
- Peripherals

<br>

#### 2.1.2. Components

- Storage elements
  - Data stored in different components
  - Speed & Cost (area) trade off
- Register: stores a single value
  - Like a single memory location
  - Extremely fast & expensive
- Several special-purpose registers, used internally
- General-purpose registers, used by the program

<br>

#### 2.1.3. Storage Elements

- Register file: Stores many values
  - A set of registers; each has an address
  - Acts just like a memory
  - Extremely fast, expensive
- Instruction operands are here
  - add $r3, $r2, $r1
- Can only read one or two registers at a time
- May contain ~32 registers

<br>

#### 2.1.4. Memories

- __Cache__: Stores many values
  - Slower than a register file
  - Cheaper than register file
  - Still fairly fast and expensive
- Data cache holds data that the program operates on
- Instruction cache holds program instructions

<br>

#### 2.1.5. Main Memory

- Very big: Gigabytes (Gb)
- Not in the CPU
- Connected to the CPI via __system bus__
- Memory access is slow
- __Von Neumann Bottleneck__
  - Memory is much slower than the CPU
  - Memory access time slows program execution

<br>

### 2.2. Compilation & Interpretation

#### 2.2.1. Software Translation

- __Machine Language__: CPU instructions represented in binary
- __Assembly language__: CPI instruction with mnemonics
  - Easter to read
  - Like machine language
- __High-level language__: commonly used languages (C, C++, Java)
  - Easier to use
- All software must be translated into the machine language of the micro-controller

<br>

#### 2.2.2. Compilation and Interpretation

- __Compilation__: translate instructions once before running the code
  - C, C++, Java (partially)
  - Translation occurs only once, saves time
- __Interpretation__: translate instructions while code is executed
  - Basic, Java (partially)
  - Translation occurs every execution
  - Translation can adapt to runtime situation

<br>

### 2.3 Python vs C & C++

#### 2.3.1. Python

- Python is interpreted, a scripting language
- It is easier to work with, if speed is not primary

#### 2.3.2. C & C++

- C & C++ are compiled
- C & C++ are more common for performance

#### 2.3.3. Software Tool Chain

<img src="https://user-images.githubusercontent.com/61633137/103165496-0ef41380-485c-11eb-9be6-bcc69ad607e4.png" alt="1" style="zoom: 80%;" /> 

- Software written on a host
- Transferred to the flash memory in the micro-controller
- Tool chain is the set of tools needed to process the software

<br>

## 3. Operating Systems

### 3.1. Introduction

![Untitled Diagram](https://user-images.githubusercontent.com/61633137/103166815-0bb35480-4869-11eb-9c96-46963a7e5300.png) 

- Manages other programs
  - Windows, Linux, iOS, etc
- Allows many programs to be executed together
- Incorporates a nice user interface
- Needs processing power and memory
- Slows down the system, makes development easier

### 3.2. Operating System Example

- Web-controlled car with a camera
  - Car is controlled via the Internet
  - Car has its own web server
  - Web interface allows user to control car and see camera images
  - Car also has 'auto brake' feature to avoid collisions

<br>

### 3.3. Task Support

- Multiple Tasks
  - Assume that one micro-controller is being used
  - At least four different tasks must be performed
    1. __Send video data__ : continuous while a user is connected
    2. __Service motion buttons__ : whenever button is pressed, may last seconds
    3. __Detect obstacles__ : continuous at all times
    4. __Auto brake__ : whenever obstacle is detected, may last seconds
  - Detect and auto brake cannot occur together
  - 3 tasks may need to occur concurrently

<br>

#### 3.4. Process & Task Support

- Main job of an OS is to support the __Process (Task) Abstraction__
- A __process__ is an instantiation of a program, it must have access to
  - the CPU
  - memory
  - other resources
    - I/O
    - ADC
    - Timers
    - Network
    - more...
- OS must __manage resources__
  - Give processes fair access to the CPU
  - Give processes access to resources

<br>