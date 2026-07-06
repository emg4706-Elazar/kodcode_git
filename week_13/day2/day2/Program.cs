using System.IO;
namespace ImageMetadataManagement
{
    class ImageMetadataManager
    {
        public int Id { get; set; }
        public double CloudCover { get; set; }
        public string Sensor { get; set; }

        public ImageMetadataManager(int id, double cloudCover, string sensor)
        {
            Id = id;
            CloudCover = cloudCover;
            Sensor = sensor;
        }

        public bool IsValid()
        {
            if (CloudCover < 0 || CloudCover > 100)
            {
                return false;
            }

            return true;
        }
        
        public string Format()
        {
            return $"Image {Id} {CloudCover}% cloud [{Sensor}]";
        }
        public void SaveToFile(string path)
        {
            File.WriteAllText(path, Format());
        }

        public int Score()
        {
            switch (Sensor)
            {
                case "SAR":
                    return 100 - (int)(CloudCover);

                case "EO":
                    return 60 - (int)(CloudCover);

                case "IR":
                    return 40 - (int)(CloudCover);

                default:
                    return 0;
            }
        }

        public static void Main()
        {
            ImageMetadataManager manager1 = new ImageMetadataManager(1, 20, "SAR");
            ImageMetadataManager manager2 = new ImageMetadataManager(2, 34, "EO");
            ImageMetadataManager manager3 = new ImageMetadataManager(3, 10, "IR");

            manager1.SaveToFile("image.txt");
            manager2.SaveToFile("image.txt");
            manager3.SaveToFile("image.txt");

            Console.WriteLine(manager1.Score());
            Console.WriteLine(manager2.Score());
            Console.WriteLine(manager3.Score());



        }
    }
}