#include <stdio.h>
#include <cs50.c>
#include <cs50.h>

int main(void)
{
	printf("X is: ");
	int x = get_int();

	printf("Y is: ");
	int y = get_int();

	printf("%i plus %i is %i", x, y, x + y);
	printf("%i minus %i is %i", x, y, x - y);
	printf("%i times %i is %i", x, y, x*y);
	printf("%i divided by %i is %i", x, y, x/y);
	printf("remainder of %i divided by %i is %i", x, y, x%y);
}
