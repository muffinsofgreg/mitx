#include <stdio.h>
#include <cs50.h>

//Credit Card Length Constants
#define AMEX_LENGTH 15
#define MASTER_LENGTH 16
#define VISA_LENGTH 13

//This should be main check loop at the end. Define validation function
//first and then use that function in the while loop.
//Then after all that, determine which company

int luhn(long long cc);
int good_length(long long number);
string cc_comp(long long cc_num);
int digit_place(long long number, int digit);
int digit_count(long long number);
int digits_from_left(long long number, int num_digits);
long long exponent(long long num, int raise);

int main(void)
{

    long long number = get_long_long("Number: ");

    if (good_length(number) == 0 || luhn(number) == 0)
    {
        printf("INVALID\n");
    }
    else
    {
        printf("%s\n", cc_comp(number));
    }

}

//Luhns Algorithm Check function
int luhn(long long cc_num)
{
    //Declare variables to be used
    int result = 0;

    //Step 1: Multiple every other digit by 2, starting with 2nd to last digit
    //Step 2: Add those products digits together
    for (int i = 2; i <= digit_count(cc_num); i += 2)
    {
        int each_two = digit_place(cc_num, i) * 2;
        for (int j = 1; j <= digit_count(each_two); j++)
        {
            result += digit_place(each_two, j);
        }
    }

    //Step 3: Add that sum to the sum of the digits not multiplied by 2
    for (int i = 1; i <= digit_count(cc_num); i += 2)
    {
        result += digit_place(cc_num, i);
    }

    //Step 4: If that total's last digit is 0 (%10 == 0) then it is valid
    if (result % 10 == 0)
    {
        return 1;
    }
    else
    {
        return 0;
    }

}

//Quick check if number passes the standard card number length
int good_length(long long number)
{
    switch (digit_count(number))
    {
        case AMEX_LENGTH:
        case MASTER_LENGTH:
        case VISA_LENGTH:
            return 1;
        default :
            return 0;
    }

}

//Which company check function
string cc_comp(long long cc_num)
{
    switch (digits_from_left(cc_num, 2))
    {
        case 34:
        case 37:
            return "AMEX";
        case 51:
        case 52:
        case 53:
        case 54:
        case 55:
            return "MASTERCARD";
        case 40:
        case 41:
        case 42:
        case 43:
        case 44:
        case 45:
        case 46:
        case 47:
        case 48:
        case 49:
            return "VISA";
        default:
            return "INVALID";
    }
}

//Determine which number exists at digit place in int
int digit_place(long long number, int digit)
{
    // Reduces number to that target digit is in first place
    number = number / exponent(10, (digit - 1));
    // Pops last "target" digit off end to number variable
    number = number % 10;
    return number;
}

//Count the number of digits in an integer
int digit_count(long long number)
{
    int count = 0;

    while (number > 0)
    {
        count++;
        number = number / 10;
    }
    return count;
}

//Return number of digits from the left
int digits_from_left(long long number, int num_digits)
{
    int new_number = number / exponent(10, (digit_count(number) - num_digits));
    return new_number;
}

//Return exponential expression bc math.h pow() function not working for me
long long exponent(long long num, int raise)
{
    long long new_num = 1;
    for (int i = 0; i < raise; i++)
    {
        new_num *= num;
    }
    return new_num;
}

