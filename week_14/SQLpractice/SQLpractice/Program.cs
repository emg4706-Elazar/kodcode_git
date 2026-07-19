using System.Linq;
using System;
using System.Text.Json;

namespace SQLpractic
{
    class Report
    {
        public int Id { get; set; }
        public string Category { get; set; }
        public int Priority { get; set; }
        public string Zone { get; set; }
        public int SignalStrength { get; set; }
        public string Shift { get; set; }
    }


    class Program
    {
        public static void Main()
        {
            string filepath = "W4D2_reports.json";
            string file = LoadFile(filepath);
            List<Report> reports = JsonSerializer.Deserialize<List<Report>>(file);

            // 1. How many reports are there in total?
            int total = reports.Count();
            Console.WriteLine($"Q1 Total reports: {total}");

            // 2. List the ids of all SIGNAL reports.
            var signalIds = reports.Where(r => r.Category == "SIGNAL").Select(r => r.Id);
            Console.WriteLine($"Q2 SIGNAL ids: {string.Join(", ", signalIds)}");

            // 3. List the ids of all reports with Priority of 4 or higher.
            var q3 = reports.Where(r => r.Priority >= 4).Select(r => r.Id);
            Console.WriteLine($"Q3 ids with Priority 4 and higher: {string.Join(", ", signalIds)}");
        }

        public static string LoadFile(string path)
        {
            string file = String.Empty;

            if (!File.Exists(path))
            {
                return file;
            }
            file = File.ReadAllText(path);

            return file;
        }
    }
}


