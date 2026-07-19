using System;

namespace ExceptionsHandling
{
    class Report
    {
        public int Id { get; }
        public string Category { get; set; }
        public int Priority { get; set; }

        public Report(int id, string category, int priority)
        {
            Id = id;
            Category = category;
            Priority = priority;
        }

    }
}
