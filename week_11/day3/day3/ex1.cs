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
            stil_unidentified
        }

        static List<int> ids = [];
        static List<Classification> lables = [];
        static List<int?> strengthes = [];

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
                        lables.Add(GetLable());
                        strengthes.Add(GetStrength());
                        Console.WriteLine("New source was created successfully\n");
                        break;
                    case 2:
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
            Console.WriteLine("  ======== Nenu ========");
            Console.WriteLine("1. Log new transmission");
            Console.WriteLine("2. Exit");
        }

        static int GetChoice()
        {
            bool isValid = false;
            while (!isValid)
            {
                Console.WriteLine("\nEnter your choice: ");
                string choice = Console.ReadLine();
                int validChoice;
                isValid = int.TryParse(choice, out validChoice);
                if (!isValid || (validChoice > 3 && validChoice <= 0))
                {
                    Console.WriteLine("Wrong number. Please try again...\n");
                }
                else
                {
                    return validChoice;
                }

            }
            // default int 
            return 1;
        

        }
    }
    
    
}


