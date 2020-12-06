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
