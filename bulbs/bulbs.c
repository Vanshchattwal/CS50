#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

const int BITS_IN_BYTE = 8;

void print_bulb(int bit);

int main(void)
{
    string input = get_string("Message : ");

    int l = strlen(input);
    int j, i, bit[8];
    for (j = 0; j < l; j++)
    {
        char decibal;
        decibal = input[j];
        //printf("%i", decibal);

        //decibal to binary
        for (int k = 0; k < 8; k++)
        {
            bit[k] = decibal % 2;
            decibal = decibal / 2;
        }

        for (int y = 7; y >= 0; y--)
        {
            print_bulb(bit[y]);
        }

        printf("\n");
    }
}

void print_bulb(int bit)
{
    if (bit == 0)
    {
        // Dark emoji
        printf("\U000026AB");
    }
    else if (bit == 1)
    {
        // Light emoji
        printf("\U0001F7E1");
    }
}
