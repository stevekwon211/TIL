# Decision Making in 'C'

In 'C' there are 5 different ways to take decisions by making use of below decision taking statements.

- if Statement
- if-else Statement
- if-else-if ladder
- Conditional Operators
- Switch/case Statement

![](https://media.geeksforgeeks.org/wp-content/cdn-uploads/20191202113149/CPP-Decision-Making.png)

Source : https://www.geeksforgeeks.org/decision-making-c-c-else-nested-else/

<br>

# if statement

- Single statement execution

  ```c
  if(expression)
      statement;
  ```

  

- Multiple statement execution

  ```c
  if(expression){
      statement_1;
      statement_2;
      statement_3;
      statement_4;
      statement_n;
  }
  ```

  

- Example

  ```c
  #include<stdio.h>
  #include<stdint.h>
  
  int main(void)
  {
      int age = 0;
      printf("Enter your age: ");
      scanf("%d",&age);
  
      if (age < 18)
      {
          printf("You cannot vote\n");
      }
      if (age >= 18)
      {
          printf("You can vote\n");
      }
  
  }
  ```

  <br>

# if-else statement

- Single statement execution

  ```c
  if(expression)
      statement_1;
  else
      statement_2;
  ```

  

- Multiple statement execution

  ```c
  if(expression)
  {
      statement_1;
      statement_2;
  }
  else
  {
      statement_3;
      ststement_4;
  }
  ```

  

- Example

  ```c
  #include<stdio.h>
  #include<stdint.h>
  
  int main(void)
  {
      int age = 0;
      printf("Enter your age: ");
      scanf("%d",&age);
  
      if (age < 18)
      {
          printf("You cannot vote\n");
      }
      else
      {
          printf("You can vote\n");
      }
  
  }
  ```



## Return value of scanf

__scanf__ returns total number of inputs scanned successfully

```c
scanf("%f", &num1);
```

In this above case __scanf__ returns 1, if the scan is successful.  
If the scan is unsuccessful then __scanf__ returns 0.  

- Example

  ```c
  #include<stdio.h>
  #include<stdint.h>
  
  void wait_for_user_input(void);
  
  int main(void)
  {
      float num1, num2;
      printf("Enter the first number: ");
  
      if (scanf("%f", &num1) == 0){
        printf("invalid input! Exiting ..\n");
        wait_for_user_input();
        return 0;
      }
      
      printf("Enter the scond number: ");
      
      if (scanf("%f", &num2) == 0){
        printf("invalid input! Exiting ..\n");
        wait_for_user_input();
        return 0;
      }
      
      int32_t n1, n2;
      
      /* storing only integer partof the real numbers*/
      n1 = num1;
      n2 = num2;
      
      if ( (n1 != num1) || (n2 != num2) ){
        printf("Warning ! Comparing only integer part\n");
      }
      
      if (n1 == n2)
      {
          printf("both numbers are equal\n");
      }
      else{
        if (n1 < n2){
            printf("%d is bigger\n", n2);
        }else{
            printf("%d is bigger\n", n1);
        }
      }
  
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

<br>

# if-else-if ladder statement

```c
if (expression1) // First check this expression
{
    //statement(s)
}
else if (expression2) // Check this expression only if above expression is false
{
    //statement(s)
}
else if (expression3) // Check this expression only if above expression is false
{
    //statement(s)
}
else (expression1)
{
    //statement(s) // Execute these statements only if all the above expression checks are false
}
```



- Example

  ```c
  #include<stdio.h>
  #include<stdint.h>
  
  void wait_for_user_input(void);
  
  int main(void)
  {
      uint64_t income;
      uint64_t tax;
  
      double temp_income;
  
      printf("Enter your total income: $");
      scanf("%lf", &temp_income);
  
      if(temp_income < 0)
      {
        printf("Income can not be negative\n");
        wait_for_user_input();
        return 0;
      }
  
      income = (uint64_t) temp_income;
  
      if (income <= 9525)
      {
        tax = 0;
      }
      else if ( (income > 9525) && (income <= 38700) )
      {
        tax = income * 0.12;
      }
      else if ( (income > 38700) && (income <= 82500) )
      {
        tax = income * 0.22;
      }
      else if (income > 82500)
      {
        tax = income * 0.32;
        tax = tax + 1000;
      }
      else
      {
        ; //NOP
      }
  
      printf("Tax payable : $%llu\n", tax);
  
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

  <br>

# Conditional Operators

- Conditional operator is a ternary operator in C used for conditional evaluation.
- Operator symbol __? :__
- It is a ternary operator because it operates on three operands.

<br>

## Syntax of conditional operator

- expression 1 ? expression 2 : expression 3

  ```c
  uint32_t a = (5 + 4)?(9 - 4):99;
  // if (5 + 4) is True, (9 - 4) is executed
  // if (5 + 4) is False, 99 will be value of a
  // in this case, a = 5
  ```

- Example

  ```c
  #include<stdio.h>
  #include<stdint.h>
  
  int main(void)
  {
      int age = 0;
      printf("Enter your age: ");
      scanf("%d",&age);
  
      (age < 18) ? printf("You cannot vote\n") : printf("You can vote\n");
  	
      return 0;
  }
  ```

  <br>

# Switch / case statement

- Switch/Case statement is one of the decision making statement available in 'C'

- It may be used instead of several if-else statements.

- Syntax of Switch/case statement

  ```c
  switch(expression)
  {
      case value:
          Statement-1;
          Statement-n;
          break;
      case value:
          Statement-1;
          Statement-n;
          break;
      case value:
          Statement-1;
          Statement-n;
          break;
      default value:
          Statement-1;
          Statement-n;
  }
  ```

  
- Example 1 - LED Control

  ```c
  int main(void)
  {
    uint8_t keyu_read = read_keypad();
      
      switch(key_read)
      {
          case 1:
              all_leds_race();
              break;
          case 2:
              all_leds_on();
              break;
          case 3:
              all_leds_toggle();
              break;
          case 4:
              all_leds_blink();
              break;
          default:
              all_leds_off();
              printf("Invalid key! Please enter number between 1 to 4 only\n");
      }
  }
  ```
  
  

- Example 2 - Area Calculation Program

  ```c
  #include<stdio.h>
  #include<stdint.h>
  
  void wait_for_user_input(void);
  
  int main(void)
  {
    float area, a, b, h, l, w, r;
    char key_input;
  
    printf("Area calculation program\n");
    printf("Circle --> c\nTriangle --> t\nRectangle --> r\nSquare --> s\nTrapezoid --> z\n");
    printf("Enter the code here:");
    scanf("%c", &key_input);
  
    switch(key_input)
    {
      case 'c':
          printf("Circle Area Calculation\n");
          printf("Enter the Radius(r) value:");
          scanf("%f", &r);
            if (r < 0)
            {
              printf("Radus cannot be negative\n");
              wait_for_user_input();
              return 0;
            }
          area = r*r*3.14;
          printf("Area = %lf\n", area);
          break;
  
      case 't':
          printf("Triangle Area Calculation\n");
          printf("Enter the Base(b) value:");
          scanf("%f", &b);
          printf("Enter the Height(h) value:");
          scanf("%f", &h);
            if ( (b < 0) || (h < 0) )
            {
              printf("Base of Height cannot be negative\n");
              wait_for_user_input();
              return 0;
            }
          area = (b*h)/2;
          printf("Area = %lf\n", area);
          break;
  
      case 'r':
          printf("Rectangle Area Calculation\n");
          printf("Enter the Width(w) value:");
          scanf("%f", &w);
          printf("Enter the Length(l) value:");
          scanf("%f", &l);
            if ( (w < 0) || (l < 0) )
            {
              printf("Width or Length cannot be negative\n");
              wait_for_user_input();
              return 0;
            }
          area = w*l;
          printf("Area = %lf\n", area);
          break;
  
      case 's':
          printf("Square Area Calculation\n");
          printf("Enter the Side(a) value:");
          scanf("%f", &a);
            if (a < 0)
            {
              printf("Side cannot be negative\n");
              wait_for_user_input();
              return 0;
            }
          area = a*a;
          printf("Area = %lf\n", area);
          break;
  
      case 'z':
          printf("Trapezoid Area Calculation\n");
          printf("Enter the Base(a) value:");
          scanf("%f", &a);
          printf("Enter the Base(b) value:");
          scanf("%f", &b);
          printf("Enter the Height(h) value:");
          scanf("%f", &h);
            if ( (a < 0) || (b < 0) || (h < 0) )
            {
              printf("Base or Height cannot be negative\n");
              wait_for_user_input();
              return 0;
            }
          area = (a+b)/2*h;
          printf("Area = %lf\n", area);
          break;
  
        default:
          printf("Invalid input\n");
  
    }
  
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

  