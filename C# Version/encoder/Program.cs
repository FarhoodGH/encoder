using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using encoderDLL;

namespace encoder
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.Clear();
            Console.Title = "Encoder ~ Choose Options";
            Console.ForegroundColor = ConsoleColor.DarkYellow;
            Console.WriteLine("             \r\n _____            _____                                 _ \r\n|  __ \\          / ____|                               | |\r\n| |  | |  ___   | (___    ___   ___  _   _  _ __  ___  | |\r\n| |  | | / _ \\   \\___ \\  / _ \\ / __|| | | || '__|/ _ \\ | |\r\n| |__| || (_) |  ____) ||  __/| (__ | |_| || |  |  __/ |_|\r\n|_____/  \\___/  |_____/  \\___| \\___| \\__,_||_|   \\___| (_)\r\n\r\n     Coded By @javadimoghadam & @FarhoodGH (C# Version)\r\n                                                          \r\n                                                          \r\n");
            Console.ResetColor();
            while (true)
            {
                Console.WriteLine("Please enter your Method( [D]ecode ,  [E]ncode , [e]xit ) -> ");
                var data = Console.ReadLine();
                if (data != null && data == "E" || data == "D" || data == "e")
                {
                    var tools = new encode();
                    if (data == "e")
                    {
                        Console.Clear();
                        Console.ForegroundColor = ConsoleColor.Green;
                        Console.WriteLine("Exit SuccessFully !");
                        Console.ResetColor();
                        Environment.Exit(0);
                    }
                    else if (data == "E")
                    {
                        Console.WriteLine("Please enter your code -> ");
                        var d = Console.ReadLine();
                        Console.WriteLine(tools.Encode(d));
                    }
                    else if (data == "D")
                    {
                        Console.WriteLine("Please enter your text -> ");
                        var d = Console.ReadLine();
                        Console.WriteLine(tools.Decode(d));
                    }
                    else
                    {
                        Console.ForegroundColor = ConsoleColor.Red;
                        Console.WriteLine("Wrong argument !");
                        Console.ResetColor();
                    }
                }
            }
        }
    }
}
