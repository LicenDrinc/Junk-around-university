using System;
using System.Collections.Generic;
using System.Text;
using System.Linq;
using System.Threading.Tasks;

public class Program
{
    public static int[,] mass = new int[15,15];
    
    public static void Main()
    {
        for (int i = 0; i < 15; i++)
        {
            for (int j = 0; j < 15; j++)
            {
                mass[i,j] = i == j ? 1 : 0;
                Console.Write($"{mass[i,j]} ");
            }
            Console.WriteLine("");
        }
        
        //Console.ReadKey();
    }
}