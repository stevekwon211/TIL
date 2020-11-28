---
title: Importance of stdint.h
author: Hyukil (Steve) Kwon
date: 2020-11-22 22:30:00 +0900
categories: [C, Basic]
tags: [stdint.h, c]
comments: true
---
# Data type size and compiler

Data types may cause portability issues of code when compiler changes.  
One compiler may consider integer data type size as 2 bytes, another compiler may consider it as 4 bytes and some other compiler may consider it as 8 bytes.



# Portability Issues in C

In C programming language the most commonly used data types `int` and `long` cause portability issues.  

The reason is that the storage size for `int`, `long`  type variable is not defined within the __C standard (C90 or C99)__.  

The compiler vendors have the choice to define the storage size for the variable depending solely on hardware capabilities of the target platform, with respect to the minimum widths defined by the standard.  



# stdint.h

The standard library header file stdint.h defines fixed-width integers using alias data types for the standard data types available in C  

A fixed-width integer data type is an aliased data type that is based on the exact number of bits required to store the data  

| Exact Alias |       Description        |                          range                          |
| :---------: | :----------------------: | :-----------------------------------------------------: |
|   int8_t    |  exactly 8 bits signed   |                       -128 to 127                       |
|   uint8_t   | exactly 8 bits unsigned  |                        0 to 255                         |
|   int16_t   |  exactly 16 bits signed  |                    -32,768 to 32,767                    |
|  uint16_t   | exactly 16 bits unsigned |                       0 to 65535                        |
|   int32_t   |  exactly 32 bits signed  |            -21,147,483,648 to 2,147,483,647             |
|  uint32_t   | exactly 32 bits unsigned |                   0 to 4,294,967,295                    |
|   int64_t   |  exactly 64 bits signed  | -9,223,372,036,854,776,808 to 9,223,372,036,854,775,807 |
|  uint64_t   | exactly 64 bits unsigned |             0 to 18,446,744,073,709,551,615             |

  

# Some useful stdint.h aliases while programming

- __uintmax_t__: defines the largest fixed-width unsigned integer possible on the system
- __intmax_t__: defines the largest fixed-width signed integer possible on the system
- __uintptr_t__: defines a unsigned integer type that is wide enough to store the value of a pointer