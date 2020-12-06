# Bitwise Operators in 'C'

- __&__ : bitwise AND
- __|__ : bitwise OR
- __<<__ : bitwise Left Shift
- __>>__ : bitwise Right Shift
- __~__ : bitwise NOT (Negation)
- __^__ : bitwise XOR

## Difference between Logical operator and bitwise operator

- __&&__ is a __logical AND__ operator
- __&__ is a __bitwise AND__ operator

```c
char A = 40;
char B = 30;
char C;

C = A&&B; // A, B are True so C = 1

/* A : 0 0 1 0 1 0 0 0
   &
   B : 0 0 0 1 1 1 1 0
   ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
   C : 0 0 0 0 1 0 0 0 */
C = A&B; // C = 8
```

<br>

- __||__ is a __logical OR__ operator
- __|__ is a __bitwise OR__ operator

``` c
char A = 40;
char B = 30;
char C;

C = A||B; // C = 1;

/* A : 0 0 1 0 1 0 0 0
   &
   B : 0 0 0 1 1 1 1 0
   ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
   C : 0 0 1 1 1 1 1 0 */
C = A|B; // C = 62
```

<br>

- __!__ is a __logical NOT__ operator
- __~__ is a __bitwise NOT__ operator

``` c
char A = 40;
char B = 30;
char C;

C = !A; // C = 0;

/*   A : 0 0 1 0 1 0 0 0
C = ~A : 1 1 0 1 0 1 1 1 */
C = ~A; // C = -41
```

<br>

- Truth table for XOR Gate

  | INPUTS(1) | INPUTS(2) |  OUTPUTS  |
  | :-------: | :-------: | :-------: |
  |     A     |     B     | Y = A ^ B |
  |     0     |     0     |     0     |
  |     0     |     1     |     1     |
  |     1     |     0     |     1     |
  |     1     |     1     |     0     |

  

- __^__ is a __bitwise XOR__ operator

``` c
char A = 40;
char B = 30;
char C;

/* A : 0 0 1 0 1 0 0 0
   ^
   B : 0 0 0 1 1 1 1 0
   ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
   C = 0 0 1 1 0 1 1 0 */
C = A^B; // C = 54
```

## Example

```c
#include<stdint.h>
#include<stdio.h>

void wait_for_user_input(void);

int main(void){

  int32_t num1, num2;

  printf("Enter First number: ");
  scanf("%d", &num1);
  printf("Enter Second number: ");
  scanf("%d", &num2);

  printf("Bitwise AND(&) : %d\n", (num1&num2));
  printf("Bitwise OR(|) : %d\n", (num1|num2));
  printf("Bitwise XOR(^) : %d\n", (num1^num2));
  printf("Bitwise NOT(~) : %d\n", (~num1));

  wait_for_user_input();
}

void wait_for_user_input(void)
{
  printf("Press enter key to exit");
  while(getchar() != '\n')
  {
    // just read the input buffer and do nothing
  }
  getchar();
}
```

# Applicability of bitwise operations

- In an Embedded C program, most of the time you will be doing
  - Testing of bits (__&__)
  - Setting of bits (__|__)
  - Clearing of bits (__~__ and __&__)
  - Toggling of bits (__^__)

## Testing of bits ( & )

### Exercise

- Write a program to finfd out whether a user entered integer is __even__ or __odd__.
- Use testing of bits logic

### Bit-Masking

<img src="https://i.stack.imgur.com/jy0de.png" style="zoom:80%;" /> 

Source : https://i.stack.imgur.com/jy0de.png

- Bit-Masking is a technique in programming used to __test__ or __modify__ the states of the bits of a given data.
- Modify : if the state of the bit 0, make it 1 or if the state of the bit is 1 then make it 0
- Test : check whether the required bit position of a data is 0 or 1

### Code

```c
#include<stdint.h>
#include<stdio.h>

void wait_for_user_input(void);

int main(void)
{
  int32_t num1;
  printf("Enter a number:");
  scanf("%d", &num1);

  if(num1&1) // 1 is Mask value
  {
      printf("%d is odd number\n", num1);
  }
  else
  {
      printf("%d is even number\n", num1);
  }

  wait_for_user_input();
}

void wait_for_user_input(void)
{
  printf("Press enter key to exit");
  while(getchar() != '\n')
  {
    // just read the input buffer and do nothing
  }
  getchar();
}
```

## Setting of bits ( | )

### Exercise

- Write a program to set(make bit state to 1) 4th and 7th-bit position of a given number and print the result.

### Code

```c
#include<stdint.h>
#include<stdio.h>

void wait_for_user_input(void);

int main(void)
{
  int32_t num1, output;
  printf("Enter a number:");
  scanf("%d", &num1);

  output = num1 | 0x90;
  printf("[input] [output] : 0x%x 0x%x\n", num1, output);

  wait_for_user_input();
}

void wait_for_user_input(void)
{
  printf("Press enter key to exit");
  while(getchar() != '\n')
  {
    // just read the input buffer and do nothing
  }
  getchar();
}
```

## Clearing of bits (~ and &)

- Method 1 __&__ 
  	|      | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
   | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
   | Data | 1 | 0 | 1 | 1 | 1 |1|1|0|
   | Mask | 1 | 0 | 0 | 0 | 1 |1|1|1|
   | Output | 1 | 0 | 0 | 0 | 1 |1|1|0|

- Only __6 5 4__ are cleared out
- __7 3 2 1 0__ are __un-affected data__  

- Method 2 __~__
  	|      | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
   | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
   | Data | 1 | 0 | 1 | 1 | 1 |1|1|0|
   | Mask | 0 | 1 | 1 | 1 | 0 |0|0|0|
   | Output | 1 | 0 | 0 | 0 | 1 |1|1|0|

- Negate (Bitwise NOT) the mask value first and then perform bitwise AND (&)

## Toggling of bits (^)

| LED_state & Mask |        Bits         |
| :--------------: | :-----------------: |
|    LED_state     | 0 0 0 0 0 0 0 __1__ |
|       Mask       |   0 0 0 0 0 0 0 1   |
|    LED_state     | 0 0 0 0 0 0 0 __0__ |
|       Mask       |   0 0 0 0 0 0 0 1   |
|    LED_state     | 0 0 0 0 0 0 0 __1__ |

