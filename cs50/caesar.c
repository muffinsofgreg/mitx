#include <stdio.h>
#include <cs50.h>
#include <ctype.h>
#include <string.h>

int main(int argc, string argv[])
{
    // Turns 1st CLA into int
    int key = atoi(argv[1]);

    string plaintext = getString("Enter your text: \n");
    
}

// Shift function, takes text and shift key
string shift(string input, key)
{
    for (int i = 0; i < strlen(input); i++)
    {
        if (isalpha(input[i]) == true) 
        {
            input[i] = input[i] + key;
        }
        else
        {
            continue;
        }
    }
}
