using System;
using System.Collections.Generic;
using System.Text;
using System.Linq;
using System.Threading.Tasks;

public class Program
{
    public static int[,] mass = new int[25,30];
    
    public static Random random = new Random();
    
    public static void Main()
    {
        for (int i = 0; i < 25; i++)
        {
            for (int j = 0; j < 30; j++)
            {
                mass[i,j] = random.Next(100);
                if (mass[i,j] < 10)
                {
                    Console.Write("0");
                }
                Console.Write($"{mass[i,j]} ");
            }
            Console.WriteLine("");
        }
        
        //Console.ReadKey();
    }
}