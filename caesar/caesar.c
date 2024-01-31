#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>

char encrypt(char words);

int main(int argc, string argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./caesar key \n");
        return 1;
    }
    for (int i = 0; i < strlen(argv[1]); i++)
    {
        if (!isdigit(argv[1][i]))
        {
            printf("Usage: ./caesar key \n");
            return 1;
        }
    }

    int k = atoi(argv[1]);
    char word;

    string input = get_string("plaintext: ");
    printf("ciphertext: ");


    for (int j = 0; j < strlen(input); j++)
    {
        if (isupper(input[j]))
        {
            printf("%c", (input[j] - 65 + k) % 26 + 65);
        }
        else if (islower(input[j]))
        {
            printf("%c", (input[j] - 97 + k) % 26 + 97);
        }
        else
        {
            printf("%c", input[j]);
        }
    }

    printf("\n");


}
