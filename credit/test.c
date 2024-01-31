#include <stdio.h>
#include <cs50.h>

long card_length(long ccnumber);
int main(void)
{
    long ccnumber = get_long("enter number");
    int length = card_length(ccnumber);
    if(card_length == 13.0 || card_length == 15.0 || card_length == 16.0)
    {
        printf("V");
    }
    else{
        printf("I");
    }
}
int card_length(void)
    {
        for (card_length = 0; ccnumber != 0; card_length++)
        {
            ccnumber = ccnumber / 10;
        }
        return card_length;
    }