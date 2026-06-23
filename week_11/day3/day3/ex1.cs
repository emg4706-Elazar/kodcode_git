using System;
using System.Reflection.Emit;


namespace SourcesManagement
{
    class SourceManager
    {
        enum Classification
        {
            freindly,
            hostile,
            still_unidentified
        }

        static List<int> ids = [];
        static List<Classification> labels = [];
        static List<int?> strengths = [];

        static void Main()
        {
            bool isRun = true;
            while (isRun)
            {
                PrinterMenu();
                int choice = GetChoice();

                switch (choice)
                {
                    case 1:
                        ids.Add(GetId());
                        labels.Add(GetLable());
                        strengths.Add(GetStrength());
                        Console.WriteLine("New source was created successfully\n");
                        break;
                    case 3:
                        DisplayAllSources(ids, labels, strengths);
                        break;

                    case 4:
                        isRun = false;
                        Console.WriteLine("\nEnd");
                        break;
                }
            }
        }


        static int GetId()
        {
            bool isValid = false;

            while (!isValid)
            {
                Console.WriteLine("Enter id: ");
                string id = Console.ReadLine();

                int validId;
                isValid = int.TryParse(id, out validId);
                if (!isValid)
                {
                    Console.WriteLine("Wrong input. Please try again...\n");
                }
                else
                {
                    return validId;
                }
            }
            // default int 
            return 1;
        }
        

        static Classification GetLable()
        {
            Classification validLable;
            bool isValid = false;

            while (!isValid)
            {
                Console.WriteLine("Enter Classification: ");
                string lable = Console.ReadLine();
                isValid = Enum.TryParse(lable, true, out validLable);
                if (!isValid)
                {
                    Console.WriteLine("Wrong classification. Please try again...\n");
                }
                else
                {
                    return validLable;
                }
            }
            return default(Classification);

        }
        static int GetStrength()
        {
            bool isValid = false;

            while (!isValid)
            {
                Console.WriteLine("Enter strength: ");
                string strength = Console.ReadLine();

                int validStrength;
                isValid = int.TryParse(strength, out validStrength);
                if (!isValid)
                {
                    Console.WriteLine("Wrong input. Please try again...\n");
                }
                else
                {
                    return validStrength;
                }
            }
            // default int 
            return 1;
        }


        static void PrinterMenu()
        {
            Console.WriteLine("\n  ======== Menu ========");
            Console.WriteLine("1. Log a new transmission");
            Console.WriteLine("2. Calibrate the strength");
            Console.WriteLine("3. Desplay all sources");
            Console.WriteLine("4. Exit");
        }


        static int GetChoice()
        {
            while (true)
            {
                Console.WriteLine("\nEnter your choice: ");
                string choice = Console.ReadLine();
                int validChoice;
                bool isValid = int.TryParse(choice, out validChoice);
                // Its behavior not clear
                if (!isValid || (validChoice > 4 || validChoice <= 0))
                {
                    Console.WriteLine("Wrong number. Please try again...\n");
                    continue;
                }
                return validChoice;
            }
        
        }

        static void DisplayAllSources(List<int> ids,
            List<Classification> labels, List<int?>strengths)
        {
            int length = ids.Count;
            for (int i = 0; i < length; i++)
            {
                Console.WriteLine($"\nID: {ids[i]} |" +
                    $" Classification: {labels[i]} | Strength: {strengths[i]}");
            }
        }
    }
}


