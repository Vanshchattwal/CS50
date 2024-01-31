#include "helpers.h"
#include <math.h>
#include<stdio.h>
#include<string.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            float red = image[i][j].rgbtRed;
            float green = image[i][j].rgbtGreen;
            float blue = image[i][j].rgbtBlue;

            int average = round((red + green + blue) / 3) ;

            image[i][j].rgbtRed = image[i][j].rgbtGreen = image[i][j].rgbtBlue = average;
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int originalRed = image[i][j].rgbtRed;
            int originalGreen = image[i][j].rgbtGreen;
            int originalBlue = image[i][j].rgbtBlue;

            int sepiared = round(.393 * originalRed + .769 * originalGreen + .189 * originalBlue);
            int sepiagreen = round(.349 * originalRed + .686 * originalGreen + .168 * originalBlue);
            int sepiablue = round(.272 * originalRed + .534 * originalGreen + .131 * originalBlue);

            if (sepiared > 255)
            {
                sepiared = 255;
            }
            if (sepiagreen > 255)
            {
                sepiagreen = 255;
            }
            if (sepiablue > 255)
            {
                sepiablue = 255;
            }

            image[i][j].rgbtRed = sepiared;
            image[i][j].rgbtGreen = sepiagreen;
            image[i][j].rgbtBlue = sepiablue;

        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width / 2; j++)
        {
            RGBTRIPLE new = image[i][j];
            image[i][j] = image[i][width - (j + 1)];
            image[i][width - (j + 1)] = new;
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE temp[height][width];
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            temp[i][j] = image[i][j];
        }
    }

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            float totalred, totalgreen, totalblue;
            totalred = totalgreen = totalblue = 0;
            int counter = 0.00;

            for (int x = -1; x < 2; x++)
            {
                for (int y = -1; y < 2; y++)
                {
                    int currentx = i + x;
                    int currenty = j + y;

                    if (currentx >= 0 && currenty >= 0 && currentx <= (height - 1) && currenty <= (width - 1))
                    {
                        totalred += image[currentx][currenty].rgbtRed;
                        totalgreen += image[currentx][currenty].rgbtGreen;
                        totalblue += image[currentx][currenty].rgbtBlue;

                        counter++;
                    }
                }

                temp[i][j].rgbtRed = round(totalred / counter);
                temp[i][j].rgbtGreen = round(totalgreen / counter);
                temp[i][j].rgbtBlue = round(totalblue / counter);
            }
        }
    }
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            image[i][j] = temp[i][j];
        }
    }
    return;
}
