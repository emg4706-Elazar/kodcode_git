using System;
using System.Threading.Channels;

class FleetManager
{ 

    
    // Main
    static void Main()
    {
        List<int[]> tracks = [];

        bool isrun = true;

        while (isrun)
        {
            PrinterMenu();
            int choice = GetInput();

            switch (choice)
            {
                case 1:
                    int[] track = AddTrack();
                    tracks.Add(track);
                    break;

                case 2:
                    tracks.Remove(RemoveTrack(tracks));
                    break;

                case 3:
                    Console.WriteLine("\nEnd");
                    isrun = false;
                    break;
            }
        }
        
    }



    // Printer Menu
    static void PrinterMenu()
    {
        Console.WriteLine("========= Menu =========");
        Console.WriteLine("1. Add new track");
        Console.WriteLine("2. Remove track");
        Console.WriteLine("3. Exit");
        Console.WriteLine("\nEnter your choice:");

    }



    // Get input
    static int GetInput()
    {
        string choice = Console.ReadLine();
        int ConvInt = int.Parse(choice);

        return ConvInt;
    }


    // Add new Track
    static int[] AddTrack()
    {
        Console.WriteLine("Enter the detailes: ");
        string id = Console.ReadLine();
        string speed = Console.ReadLine();
        string heading = Console.ReadLine();
        int[] track = [0, 0, 0];
        track[0] = int.Parse(id);
        track[1] = int.Parse(speed);
        track[2] = int.Parse(heading);
       
        return track;
    }

    // Remove a Track
    static int[] RemoveTrack(List<int[]> tracks)
    {
        Console.WriteLine("Enter ID: ");
        string existid = Console.ReadLine();
        int ConvId = int.Parse(existid);
        int[] track = [];

        foreach (int[] t in tracks)
        {
            if (t[0] == ConvId)
            {
                track = t;
            }
            
        }
        if (track.Length == 0)
        {
            Console.WriteLine($"ID: {existid} not found");
        }

        return track;
    }
    



}