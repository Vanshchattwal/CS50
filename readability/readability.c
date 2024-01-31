#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <math.h>

int letter_len(string entry);
int words(string ent);
int s_len(string entr);

int main(void)
{
    string input = get_string("Text : ");

    double llength = letter_len(input);

    double wcount = words(input);

    double slength = s_len(input);

    double L = llength / wcount * 100 ;

    double S = slength / wcount * 100 ;

    int index = round(0.0588 * L - 0.296 * S - 15.8);

    if(index > 16)
    {
        printf("Grade 16+\n");
    }
    else if(index < 1)
    {
        printf("Before Grade 1\n");
    }
    else
    {
        printf("Grade %i\n", index);
    }


    //printf("%s" result);

}

int letter_len(string entry)
{
    int letter_count = 0;
    int ll;
    for(ll = 0; ll < strlen(entry); ll++)
    {
        if(isupper(entry[ll]))
        {
            letter_count = letter_count + 1;
        }
        else if(islower(entry[ll]))
        {
            letter_count = letter_count + 1;
        }
        else
        {
            letter_count = letter_count + 0;
        }
    }
    return letter_count;
}

int words(string ent)
{
    int word_len_count = 1;
    int wl;
    for(wl =0; wl <= strlen(ent); wl++)
    {
        if(ent[wl] == ' ')
        {
            word_len_count++;
        }
        else
        {
            word_len_count = word_len_count + 0;
        }
    }
    return word_len_count;
}

int s_len(string entr)
{
    int sent_coun = 0;
    int sl;
    for(sl = 0; sl < strlen(entr); sl++)
    {
        if(entr[sl] == '!')
        {
            sent_coun = sent_coun + 1;
        }
        else if(entr[sl] == '?')
        {
            sent_coun = sent_coun + 1;
        }
        else if(entr[sl] == '.')
        {
            sent_coun = sent_coun + 1;
        }
        else
        {
            sent_coun = sent_coun + 0;
        }
    }
    return sent_coun;
}