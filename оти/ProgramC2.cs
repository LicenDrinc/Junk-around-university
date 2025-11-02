using System;
using System.Collections.Generic;
using System.Text;
using System.Linq;
using System.Threading.Tasks;

public class Program
{
    public static int[,] mass = new int[20,20];
    
    public static void Main()
    {
        for (int i = 0; i < 20; i++)
        {
            for (int j = 0; j < 20; j++)
            {
                if (i >= j + 1 && i <= 9 && j <= 9 || (j >= i && i > 9 && j > 9))
                    mass[i,j] = 1;
                else if (j >= i && i <= 9 && j <= 9 || (i + 1 >= j && i > 9 && j > 9))
                    mass[i,j] = 2;
                else
                    mass[i,j] = 3;
                Console.Write($"{mass[i,j]} ");
            }
            Console.WriteLine("");
        }
        
        //Console.ReadKey();
    }
}