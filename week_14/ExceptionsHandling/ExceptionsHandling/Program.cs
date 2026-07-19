using System;
using System.IO;
using System.Collections.Generic;
using HxceptionsHandling;


namespace ExceptionsHandling
{
    

    class Program
    {
        public static void Main()
        {
            string filepath = "w4d1_field_reports_input.txt";
            List<Report> reports = new List<Report>();

            List<string> lines = LoadTxtFile(filepath);

            
            if (lines.Count != 0)
            {
                ParseLines(lines, reports);
            }
        }




        public static void ParseLines(List<string> lines, List<Report> reports)
        {
            int validLinesCounter = 0;
            int invalidLinesCounter = 0;
            foreach (string line in lines)
            {
                string[] fields = line.Split();
                try
                {
                    int id = int.Parse(fields[0]);
                    string catrgory = fields[1];
                    int priority = int.Parse(fields[2]);
                    if (priority < 0)
                    {
                        throw new NegativePriorityException();
                    }
                    reports.Add(new Report(id, catrgory, priority));
                    validLinesCounter++;
                }
                catch (NegativePriorityException)
                {
                    Console.WriteLine("Error: Negative priority");
                    invalidLinesCounter++;
                }
                catch (FormatException e)
                {
                    invalidLinesCounter++;
                    Console.WriteLine(e.Message);
                }
            }
            Console.WriteLine($"Valid lines: {validLinesCounter}.");
            Console.WriteLine($"Invald lines: {invalidLinesCounter}.");
 
        }

        public static List<string> LoadTxtFile(string path)
        {
            if (!File.Exists(path))
            {
                Console.WriteLine("No reports yet.");
                return new List<string>();
            }
            try
            {
                List<string> lines = new List<string>();

                using (StreamReader reader = new StreamReader(path))
                {
                    string? line;

                    while ((line = reader.ReadLine()) != null)
                    {
                        lines.Add(line);
                    }
                }
                if (lines.Count == 0)
                {
                    Console.WriteLine("The file is empty.");
                }

                return lines;
            }
            catch (IOException e)
            {
                Console.WriteLine($"Could not read the file: {e.Message}");
                return new List<string>();
            }

        }
        
    }
}
    
    


