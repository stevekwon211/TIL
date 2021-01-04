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
