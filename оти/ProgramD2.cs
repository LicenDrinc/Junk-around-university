using System;
using System.Collections.Generic;
using System.Text;
using System.Linq;
using System.Threading.Tasks;

public class Program
{
    public static int[,] mass = new int[50, 50];

    public static void Main()
    {
        for (int i = 0; i < 50; i++)
        {
            for (int j = 0; j < 50; j++)
            {
                Scheme2(i, j);

                if (mass[i, j] < 1000)
                    Console.Write("0");
                if (mass[i, j] < 100)
                    Console.Write("0");
                if (mass[i, j] < 10)
                    Console.Write("0");

                Console.Write($"{mass[i, j]} ");
            }
            Console.WriteLine("");
        }

        //Console.ReadKey();
    }

    public static void Scheme2(int i, int j)
    {
        mass[i, j] = i * 50 + 50 - j;
    }
}
