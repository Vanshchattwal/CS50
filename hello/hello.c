#include <stdio.h>
#include <cs50.h>

int main(void)
{
    //Ask for Name
    string name = get_string("What is your Name? \n");

    //Print Name
    printf("Hello,%s\n", name);
}
