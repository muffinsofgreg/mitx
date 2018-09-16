#include <stdio.h>

int number = 12345;

int exponent(int num, int pow)
{
    int new_num = 1;
    for (int i = 0; i < pow; i++)
    {
        new_num *= num;  
    }
    return new_num;
}

int digit_count(int number)
{
    static int count = 0;

    if (number > 0)
    {
        count++;
        digit_count(number/10);
    }
    else
    {
        return count;
    }
}

int digits_from_left(int number, int num_digits)
{
    int new_number = number / exponent(10, (digit_count(number) - num_digits));
    return new_number;
}

int main(void)
{
    printf("%i\n", digits_from_left(number, 3));  
}
