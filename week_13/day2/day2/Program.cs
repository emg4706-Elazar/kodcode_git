using GoodExample;

namespace GoodExample
{
    interface IImageOps { int CalculateScore(); }
    interface IRetaskable { void Retask() { } }
    interface ICalibtated { void CalibrateThermal() { } }

    abstract class SatelliteImage
    {
        public int Id { get; }
        public double CloudCover { get; }
        public double Score;

        protected SatelliteImage(int id, double cloudCover)
        {
            if (cloudCover < 0 || cloudCover > 100)
                throw new ArgumentOutOfRangeException(nameof(CloudCover), "Must be between 0 and 100.");
            Id = id;
            CloudCover = cloudCover;
            //Score = CalculateScore();
        }

        public abstract int CalculateScore();
        public abstract string Sensor { get; }
    }

    class SarImage : SatelliteImage, IImageOps
    {
        public SarImage(int id, double cloudCover) : base(id, cloudCover) { }
        public override string Sensor => "SAR";
        public override int CalculateScore() { return (int)(100 - CloudCover); }
    }

    class EoImage : SatelliteImage
    {
        public EoImage(int id, double cloudCover) : base(id, cloudCover) { }
        public override string Sensor => "EO";
        public override int CalculateScore() { return (int)(60 - CloudCover); }
    }

    class IrImage : SatelliteImage
    {
        public IrImage(int id, double cloudCover) : base(id, cloudCover) { }
        public override string Sensor => "IR";
        public override int CalculateScore()
        {
            return (int)(40 - CloudCover);
        }
    }

    class MultispectralImage : SatelliteImage
    {
        public MultispectralImage(int id, double cloudCover) : base(id, cloudCover) { }
        public override string Sensor => "MULTISPECTRAL";
        public override int CalculateScore() { return (int)(80 - CloudCover); }
    }

    class ImageFormatter
    {
        public string Format(SatelliteImage image)
        {
            return $"Image {image.Id}: {image.CloudCover}% cloud [{image.Sensor}]";
        }
    }

    class ImageFileSaver
    {
        private readonly ImageFormatter formatter = new ImageFormatter();
        public void Save(string path, SatelliteImage image)
        {
            File.WriteAllText(path, formatter.Format(image));
        }
    }

    class Repository<T> where T : SatelliteImage
    {
        private readonly List<T> images = new List<T>();
        public void Add(T image)
        {
            images.Add(image);
        }
        public IEnumerable<T> GetAll() { return images; }
    }

    class QuickLookImage : SatelliteImage
    {
        public QuickLookImage(int id, double cloudCover) : base(id, cloudCover) { }
        public override string Sensor => "QuickLook";
        public override int CalculateScore() { return (int)(0); }
    }

    class Program
    {
        static void Main()
        {
            ImagePipeline pipeline = new ImagePipeline(new MemoryStore());
            List<SatelliteImage> images = new List<SatelliteImage>
            {
                new SarImage(1, 12.5),
                new EoImage(2, 35.6),
                new SarImage(3, 78.2),
                new MultispectralImage(4, 20),
                new QuickLookImage(5, 22.1)
            };      

            int storedCount = pipeline.ProcessImages(images);
            Console.WriteLine($"Stored {storedCount} images.");
        }
    }
    class ImagePipeline
    {
        public readonly IStore Repo;

        public ImagePipeline(IStore repo)
        {
            Repo = repo;
        }
        public void Save(SatelliteImage image)
        {
            
            Repo.Save(image);
        }
        public int ProcessImages(List<SatelliteImage> images)
        {
            int Count = 0;
            foreach(SatelliteImage img in images)
            {
                img.Score = img.CalculateScore();
                Save(img);
                Count++;
            }
            return Count;
        }
        
    }

    class DiskStore { }

    class MemoryStore : IStore
    {
        private List<SatelliteImage> _store = new List<SatelliteImage>();
        public void Save(SatelliteImage img)
        {
            _store.Add(img);
        }
    }


    interface IStore
    {
        public void Save(SatelliteImage image) { }
    }


}


































//Repository<SatelliteImage> repository = new Repository<SatelliteImage>();

//repository.Add(new SarImage(1, 12.5));
//repository.Add(new EoImage(2, 35.6));
//repository.Add(new IrImage(3, 78.2));
//repository.Add(new MultispectralImage(4, 20));
//repository.Add(new QuickLookImage(5, 22.1));

//ImageFormatter formatter = new ImageFormatter();
//int total = 0;
//int unproccesed = 0;
//foreach (SatelliteImage image in repository.GetAll())
//{
//    try
//    {
//        Console.WriteLine(formatter.Format(image));
//        int score = image.CalculateScore();
//        Console.WriteLine($"Score: {score}");
//        total += score;
//    }
//    catch (ArgumentOutOfRangeException er)
//    {
//        unproccesed++;
//        Console.WriteLine($"Error: {er.Message}");
//    }
//    finally { Console.WriteLine("scanned."); }
//}
//Console.WriteLine($"Total unproccesed: {unproccesed}");
//Console.WriteLine($"Total Score: {total}");









//using System.IO;
//namespace ImageMetadataManagement
//{
//    class ImageMetadataManager
//    {
//        public int Id { get; set; }
//        public double CloudCover { get; set; }
//        public string Sensor { get; set; }

//        public ImageMetadataManager(int id, double cloudCover, string sensor)
//        {
//            Id = id;
//            CloudCover = cloudCover;
//            Sensor = sensor;
//        }

//        public bool IsValid()
//        {
//            if (CloudCover < 0 || CloudCover > 100)
//            {
//                return false;
//            }

//            return true;
//        }

//        public string Format()
//        {
//            return $"Image {Id} {CloudCover}% cloud [{Sensor}]";
//        }
//        public void SaveToFile(string path)
//        {
//            File.WriteAllText(path, Format());
//        }

//        public int Score()
//        {
//            switch (Sensor)
//            {
//                case "SAR":
//                    return 100 - (int)(CloudCover);

//                case "EO":
//                    return 60 - (int)(CloudCover);

//                case "IR":
//                    return 40 - (int)(CloudCover);

//                default:
//                    return 0;
//            }
//        }

//        public static void Main()
//        {
//            ImageMetadataManager manager1 = new ImageMetadataManager(1, 20, "SAR");
//            ImageMetadataManager manager2 = new ImageMetadataManager(2, 34, "EO");
//            ImageMetadataManager manager3 = new ImageMetadataManager(3, 10, "IR");

//            manager1.SaveToFile("image.txt");
//            manager2.SaveToFile("image.txt");
//            manager3.SaveToFile("image.txt");

//            Console.WriteLine(manager1.Score());
//            Console.WriteLine(manager2.Score());
//            Console.WriteLine(manager3.Score());



//        }
//    }

//    abstract class Sensor
//    {
//        public int Id { get; set; }
//        public double CloudCover { get; set; }

//        public Sensor(int id, double cloudCover)
//        {
//            Id = id;
//            CloudCover = cloudCover;
//        }
//        public bool IsValid()
//        {
//            if (CloudCover < 0 || CloudCover > 100)
//            {
//                return false;
//            }

//            return true;
//        }

//        public void SaveToFile(string path)
//        {
//            File.WriteAllText(path, Format());
//        }

//        public int Score()
//        {
//            return 100 - (int)(CloudCover);
//        }
//    }

//    class SensorSar :Sensor
//    {

//    }
//    public string Format()
//    {
//        return $"Image {Id} {CloudCover}% cloud [{Sensor}]";

//    }