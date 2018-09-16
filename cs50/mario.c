#include <stdio.h>
#include <cs50.h>

// Prototype two functions called in main()
void print_space(int x);
void print_hash(int x);

int main(void)
{

    int height;

    // Loop to get height, an integer between 0 and 23
    do
    {
        height = get_int("What is the pyramid height?: ");
    }
    while (height < 0 || height > 23);

    // Declare formatting variables, width starts at 1 for topmost block
    int width = 1;
    int spaces = height - 1;
    int gap = 2;

    // Main format loop
    for (int i = 0; i < height; i++)
    {
        print_space(spaces);
        print_hash(width);
        print_space(gap);
        print_hash(width);
        printf("\n");
        spaces--;
        width++;
    }
}

// Prints number of hash characters
void print_hash(int x)
{
    for (int i = 0; i < x; i++)
    {
        printf("#");
    }
}

// Prints number of space characters
void print_space(int x)
{
    for (int i = 0; i < x; i++)
    {
        printf(" ");
    }
}

