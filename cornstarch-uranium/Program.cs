using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Console_Setup_CSharp
{
    class Program
    {
        static List<int> list = new List<int>() { 2, 5, 7, 10, 11, 15, 18 };
        static void Main(string[] args)
        {
            switch (args[0])
            {
                case "find":
                    Console.WriteLine("Searching for " + args[1]);
                    bool output = binarySearch(int.Parse(args[1]));
                    Console.WriteLine(output);
                    Console.ReadKey();
                    break;
                case "sort":
                    Console.WriteLine("Sorting list: " + list);
                    slow_sort();
                    Console.WriteLine("Sorted list: " + list);
                    Console.ReadKey();
                    break;
                default:
                    Console.WriteLine("Please enter a command.");
                    Console.ReadKey();
                    break;
            }

        }

        static bool binarySearch(int num)
        {
            int right_pointer = list.Count - 1;
            int left_pointer = 0;
            while (left_pointer + 1 != right_pointer)
            {
                int halfwayInd = left_pointer + (right_pointer - left_pointer) / 2;
                if (list.ElementAt(halfwayInd) > num)
                {
                    right_pointer = halfwayInd;
                }
                else if (list.ElementAt(halfwayInd) < num)
                {
                    left_pointer = halfwayInd;
                }
                else
                {
                    return true;
                }
            }
            if (list.ElementAt(left_pointer) == num || list.ElementAt(right_pointer) == num)
            {
                return true;
            }
            return false;
        }

        static void slow_sort()
        {
            for (int i = 0; i < list.Count(); i++)
            {
                int minimum = int.MaxValue;
                int min_index = i;
                for (int j = i + 1; j < list.Count(); j++)
                {
                    if (list.ElementAt(j) < minimum)
                    {
                        minimum = list.ElementAt(j);
                        min_index = j;
                    }
                }
                if (minimum < list.ElementAt(i))
                {
                    int temp_val = list[i];
                    list[i] = minimum;
                    list[min_index] = temp_val;
                }
            }
        }

        //static String list_as_string(List list)
        //{
        //
        //}
    }
}
