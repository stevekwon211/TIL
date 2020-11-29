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
