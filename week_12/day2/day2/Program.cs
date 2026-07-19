using System;
using System.Collections.Generic;

namespace TrackedPlatform
{
    abstract class Platform
    {
        private int _trackId;
        private double _speedKnots;
        private double _heading;

        public int TrackId 
        { 
            get => _trackId;
            private set { _trackId = value; }
        }

        public double SpeedKnots
        {
            get => _speedKnots;
            set
            {
                if (value < 0)
                {
                    throw new ArgumentException("The 'Speed' must be more than 0.");
                }
                _speedKnots = value;
            }
        }
        public double Heading
        {
            get => _heading;
            set
            {
                if (value < 0 || value > 359)
                {
                    throw new ArgumentException("The 'heading' must be between 0 and 359.");
                }
                _heading = value;
            }
        }

        protected Platform(int trackId, double speedKnots, double heading)
        {
            TrackId = trackId;
            SpeedKnots = speedKnots;
            Heading = heading;
        }

        public abstract string StatusLine();
        public abstract bool IsTrackable();
        public override string ToString()
        {
            return $"TrackId: #{TrackId}| SpeedKnots: {SpeedKnots} | Heading: {Heading}";
        }
    }

    class AirPlatform: Platform
    {
        private double _altitudeFeet;
        public double AltitudeFeet
        {
            get => _altitudeFeet;
            set
            {
                if (value < 0)
                {
                    throw new ArgumentException("The 'AltitudeFeet' must be more than 0.");
                }
                _altitudeFeet = value;
            }
        }
        

        public AirPlatform(int trackId, double speedKnots, double heading, double altitudeFeet)
            :base(trackId, speedKnots, heading)
        {
            AltitudeFeet = altitudeFeet;
        }

        public override string StatusLine()
        {
            return $"Platform: Air | TrackId: #{TrackId}| SpeedKnots: {SpeedKnots}\n" +
                $"Heading: {Heading} | AltitudeFeet: {AltitudeFeet} | IsTrackable:  {IsTrackable()}";
        }
        public override bool IsTrackable()
        {
            if (AltitudeFeet >= 100 && AltitudeFeet <= 60000
                && SpeedKnots > 0) { return true; }
            
            return false;          
        }
    }

    class SeaPlatform: Platform
    {
        private double _depthMeters;

        public double DepthMeters
        {
            get => _depthMeters;
            set
            {
                if (value < 0)
                {
                    throw new ArgumentException("The 'DepthMeters' must be more than 0.");
                }
                _depthMeters = value;
            }
        }

        public SeaPlatform(int trackId, double speedKnots, double heading, double depthMeters)
            :base(trackId, speedKnots, heading)
        {
            DepthMeters = depthMeters;
        }
        public override string StatusLine()
        {
            return $"Platform: Sea | TrackId: #{TrackId}| SpeedKnots: {SpeedKnots}\n" +
                $"Heading: {Heading} | DepthMeters: {DepthMeters} | IsTrackable:  {IsTrackable()}";
        }
        public override bool IsTrackable()
        {
            if (DepthMeters > 300)
            {
                return false;
            }
            return true;
        }
    }

    class GroundPlatform: Platform
    {
        private string _terrainType;

        public GroundPlatform(int trackId, double speedKnots, double heading, string terrainType)
            :base(trackId, speedKnots, heading)
        {
            _terrainType = terrainType;
        }
        public override string StatusLine()
        {
            return $"Platform: Ground | TrackId: #{TrackId}| SpeedKnots: {SpeedKnots}\nHeading: {Heading} | TerrainType: {_terrainType} | IsTrackable:  {IsTrackable()}";
        }

        public override bool IsTrackable()
        {
            if (_terrainType.ToLower().Trim() == "tunnel")
            {
                return false;
            }
            return true;
        }


    }
    class Test
    {
        static void Main()
        {

            AirPlatform a1 = new AirPlatform(1, 345.0, 67, 8900);          
            SeaPlatform s1 = new SeaPlatform(2, 45, 300, 34);
            GroundPlatform g1 = new GroundPlatform(6, 90, 123, "123");
            AirPlatform a2 = new AirPlatform(4, 34, 250, 50);
            SeaPlatform s2 = new SeaPlatform(5, 0, 45, 500);
            GroundPlatform g2 = new GroundPlatform(3, 587, 98, "tunnel");

            List<Platform> listPlms = [a1, s1, g1, a2, s2, g2];
            foreach (Platform pltm in listPlms)
            {
                Console.WriteLine(pltm.StatusLine());
                Console.WriteLine();

            }
        }
    }

}