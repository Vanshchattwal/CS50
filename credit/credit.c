#include <cs50.h>
#include <stdio.h>

int main(void)
{
    //get credit card number
    long ccnumber;
    do
    {
        ccnumber = get_long("Please enter your credit card number : ");
    }
    while(ccnumber < 1);

    //check length and pattern

    int card_length;
    {
        for (card_length = 0; ccnumber != 0; card_length++)
        {
            ccnumber = ccnumber / 10;
        }
        return card_length;

        if ( card_length == 13 ||card_length == 15 ||card_length == 16)
    {
        printf("VALID");
    }
    else{ printf("INVALID");}

    }


}

