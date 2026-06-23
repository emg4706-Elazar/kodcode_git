using System;
using System.ComponentModel.Design;


namespace SourcesManagement
{
    class SourceManager
    {
        enum Classification
        {
            friendly,
            hostile,
            stil_unidentified
        }

        static List<int> ids;
        static List<Classification> lables;
        static List<int> strength = new List<int>();


        static void Main()
        {
            ids.Add(GetId());



        }


        static int GetId()
        {
            Console.WriteLine("Enter id: ");
            string id = Console.ReadLine();
            int ConvId = int.Parse(id);
            return ConvId;
        }

        static Classification GetLable()
        {
            bool isValid = false;
            Classification validLable;
            while (!isValid)
            {
                Console.WriteLine("Enter Classification: ");
                string lable = Console.ReadLine();


                isValid = Enum.TryParse(lable, true, out validLable);
                if (!isValid)
                {
                    Console.WriteLine("Wrong classification. Please try again...\n");
                }

            }
            return validLable;
        }

    }
}


