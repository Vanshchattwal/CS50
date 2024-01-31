#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int height, row, column, space, trow;


    do
    {
        height = get_int("Height :");
    }
    while (height < 1 || height > 8);


    for (row = 0; row < height; row++)
    {
        for (space = 0; height - row - 1 > space; space++)
        {
            printf(" ");
        }
        for (column = 0; column <= row; column++)
        {
            printf("#");
        }
        printf("  ");
        for (trow = 0; trow < column; trow++)
        {
            printf("#");
        }
        printf("\n");
    }


}