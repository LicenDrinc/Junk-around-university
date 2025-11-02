using System;
using System.Collections.Generic;
using System.Text;
using System.Linq;
using System.Threading.Tasks;

public class Program
{
    public static int[,] mass = new int[50, 50];

    public static int k1;
    public static int k2;
    public static int k3;
    public static int k4;

    public static void Main()
    {
        for (int k = 0; k < 25; k++)
        {
            for (int i = 49 - k; i >= 0 + k; i--)
                mass[49 - k, i] = i == 49 ? 1 : mass[49 - k, i + 1] + 1;

            for (int i = 49 - k - 1; i >= 0 + k + 1; i--)
                mass[i, k] = mass[i + 1, k] + 1;

            for (int i = 0 + k; i < 50 - k; i++)
                mass[k, i] = i == 0 + k ? mass[k + 1, i] + 1 : mass[k, i - 1] + 1;

            for (int i = 0 + k + 1; i < 50 - k - 1; i++)
                mass[i, 49 - k] = mass[i - 1, 49 - k] + 1;
        }

        for (int i = 0; i < 50; i++)
        {
            for (int j = 0; j < 50; j++)
            {
                if (mass[i, j] < 1000)
                    Console.Write(" ");
                if (mass[i, j] < 100)
                    Console.Write(" ");
                if (mass[i, j] < 10)
                    Console.Write(" ");

                Console.Write($"{mass[i, j]} ");
            }
            Console.WriteLine("");
        }
    }
}
