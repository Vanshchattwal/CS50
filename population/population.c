#include <stdio.h>
#include <cs50.h>

int main(void)
{
    //starting count
    int start;
    do
    {
        start = get_int("total number of llamas ? \n");
    }
    while (start < 9);

    //count wanted

    int end;
    do
    {
        end = get_int("How many you want ? \n");
    }
    while (end < start);

    //calculate years

    int years = 0;
    while (start < end)
    {
        start = start + (start / 3) - (start / 4);
        years = years + 1;
    }

    printf("Years: %i\n", years);

}