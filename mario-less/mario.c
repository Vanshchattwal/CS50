#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int x, row, column, space;

    //take input for height

    do
    {
        x = get_int("Height:");

    }
    while
    (x < 1 || x > 8);

    //printing columns, rows and space

    for (row = 0; x > row; row++)
    {
        for (space = 0; x - row - 1 > space; space++)
        {
            printf(" ");
        }
        for (column = 0; row >= column; column++)
        {
            printf("#");
        }
        printf("\n");
    }

}