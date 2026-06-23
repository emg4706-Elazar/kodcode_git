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
            
            ids.Add(GetId());
            lables.Add(GetLable());
            strengthes.Add(GetStrength());



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
            Console.WriteLine("===== Nenu =====");
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
            }

        }
    }
    
    
}


