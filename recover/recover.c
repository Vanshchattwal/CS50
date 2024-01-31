#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
typedef uint8_t BYTE;

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./recover IMAGE");
        return 1;
    }

    unsigned char buffer[512];

    int image_number = 0;

    FILE *input = fopen(argv[1], "r");

    FILE *output = NULL;

    char *filename = malloc(8 * sizeof(char));

    if (input == NULL)
    {
        printf("ERROR, File Does not contain anything");
        return 2;
    }

    while (fread(buffer, sizeof(char), 512, input))
    {
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            if (image_number > 0)
            {
                fclose(output);
            }
            sprintf(filename, "%03i.jpg", image_number);

            output = fopen(filename, "w");

            image_number++;
        }

        if (output != NULL)
        {
            fwrite(buffer, sizeof(char), 512, output);
        }
    }
    free(filename);
    fclose(output);
    fclose(input);

    return 0;
}