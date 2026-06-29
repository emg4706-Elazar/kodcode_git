using System;
using System.Security.Cryptography.X509Certificates;
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
                if (value >= 0)
                {
                    _speedKnots = value;
                }
            }
        }
        public double Heading
        {
            get => _heading;
            set
            {
                if (value >= 0 && value <= 359)
                {
                    _heading = value;
                }
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
            return $"Platform: Air | TrackId: #{TrackId}| SpeedKnots: {SpeedKnots} | Heading: {Heading}";
        }
    }

    class AirPlatform: Platform
    {
        private double _altitudeFeet;

        public AirPlatform(int trackId, double speedKnots, double heading, double altitudeFeet)
            :base(trackId, speedKnots, heading)
        {
            _altitudeFeet = altitudeFeet;
        }

        public override string StatusLine()
        {
            return $"Platform: Air | TrackId: #{TrackId}| SpeedKnots: {SpeedKnots}\nHeading: {Heading} | AltitudeFeet: {_altitudeFeet} | IsTrackable:  {IsTrackable()}";
        }
        public override bool IsTrackable()
        {
            if (_altitudeFeet < 100 || _altitudeFeet > 60000) { return false; }
            if (SpeedKnots < 0) { return false; }

            return true;
        }
    }

    class SeaPlatform: Platform
    {
        private double _depthMeters;

        public SeaPlatform(int trackId, double speedKnots, double heading, double depthMeters)
            :base(trackId, speedKnots, heading)
        {
            _depthMeters = depthMeters;
        }
        public override string StatusLine()
        {
            return $"Platform: Sea | TrackId: #{TrackId}| SpeedKnots: {SpeedKnots}\nHeading: {Heading} | DepthMeters: {_depthMeters} | IsTrackable:  {IsTrackable()}";
        }
        public override bool IsTrackable()
        {
            if (_depthMeters < 0 || _depthMeters > 300)
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
            if (_terrainType == "tunnel")
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
            SeaPlatform s1 = new SeaPlatform(2, 45, 8600, 34);
            GroundPlatform g1 = new GroundPlatform(3, 587, 98, "234");
            AirPlatform a2 = new AirPlatform(4, -8, 900, 788);
            SeaPlatform s2 = new SeaPlatform(5, -4, 492, 500);
            GroundPlatform g2 = new GroundPlatform(6, 90, 123, "tunnel");


            List<Platform> listPlms = [ a1, s1, g1, a2, s2, g2 ];
            foreach (Platform pltm in listPlms)
            {
                Console.WriteLine(pltm.StatusLine());
                Console.WriteLine(pltm.IsTrackable());
                Console.WriteLine();
            }
        }
    }

}